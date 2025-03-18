import logging
import json
import smtplib
from email.message import EmailMessage
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from tempfile import gettempdir


class CriticalEmailHandler(logging.Handler):
    def __init__(self, smtp_server, smtp_port, sender_email, receiver_email, smtp_user, smtp_password):
        super().__init__(level=logging.CRITICAL)
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password
    
    def emit(self, record):
        try:
            msg = EmailMessage()
            msg.set_content(self.format(record))
            msg["Subject"] = "Critical Alert from Device Registration Service"
            msg["From"] = self.sender_email
            msg["To"] = self.receiver_email
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)
        except Exception as e:
            print(f"Failed to send critical alert email: {e}")


SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SENDER_EMAIL = "noreply@example.com"
RECEIVER_EMAIL = "admin@example.com"
SMTP_USER = "noreply@example.com"
SMTP_PASSWORD = "yourpassword"

email_handler = CriticalEmailHandler(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, RECEIVER_EMAIL, SMTP_USER, SMTP_PASSWORD)
email_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
logging.getLogger().addHandler(email_handler)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

DATA_FILE = Path(gettempdir()) / "devices.json"

app = FastAPI()

devices = {}

def load_devices():
    global devices
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r") as f:
                devices = json.load(f)
            logging.info(f"Loaded {len(devices)} devices from disk.")
        except (json.JSONDecodeError, IOError) as e:
            logging.critical(f"Failed to load devices from disk: {e}")
            devices = {}
    else:
        logging.warning("No existing device data found, starting fresh.")

def save_devices():
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(devices, f, indent=4)
        logging.debug("Devices successfully saved to disk.")
    except IOError as e:
        logging.critical(f"Failed to save devices to disk: {e}")

load_devices()

class Device(BaseModel):
    device_id: str = Field("00:00:00:00:00:00")
    location: str = Field("Bratsk")
    owner: str = Field("Lyceum")
    measurement_type: str = Field("temperature")
    sensor_model: str = Field(..., description="Put particular sensor model name here")

@app.post("/register")
async def register_device(device: Device):
    logging.debug(f"Received registration request for device_id: {device.device_id}")

    if device.device_id in devices:
        logging.warning(f"Device {device.device_id} is already registered.")
        raise HTTPException(status_code=400, detail="Device already registered")

    devices[device.device_id] = device.model_dump()
    save_devices()
    logging.info(f"Device {device.device_id} registered successfully.")

    return {"message": "Device registered successfully"}

@app.get("/devices")
async def list_devices():
    logging.debug("Fetching list of all registered devices.")
    
    if not devices:
        logging.warning("Device list requested but no devices are registered.")
    
    return devices

@app.get("/device/{device_id}")
async def get_device(device_id: str):
    logging.debug(f"Fetching details for device_id: {device_id}")

    if device_id not in devices:
        logging.error(f"Device {device_id} not found.")
        raise HTTPException(status_code=404, detail="Device not found")

    logging.info(f"Device {device_id} details retrieved.")
    return devices[device_id]
