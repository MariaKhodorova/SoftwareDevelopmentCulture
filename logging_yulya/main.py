import logging
import json
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from tempfile import gettempdir
import requests

HTTP_ALERT_URL = "http://localhost:8000/alert"

class CriticalHTTPHandler(logging.Handler):
    def emit(self, record):
        if record.levelno == logging.CRITICAL:
            try:
                log_message = super().format(record)
                response = requests.post(HTTP_ALERT_URL, json={"alert": log_message})
                response.raise_for_status()
            except Exception as e:
                print(f"Failed to send HTTP alert: {e}")

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_message = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName
        }
        return json.dumps(log_message)

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)

http_handler = CriticalHTTPHandler()
http_handler.setFormatter(JSONFormatter())
logger.addHandler(http_handler)

DATA_FILE = Path(gettempdir()) / "devices.json"

app = FastAPI()
devices = {}

def load_devices():
    global devices
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r") as f:
                devices = json.load(f)
            logger.info(f"Loaded {len(devices)} devices from disk.")
        except (json.JSONDecodeError, IOError) as e:
            logger.critical(f"Failed to load devices from disk: {e}")
            devices = {}
    else:
        logger.warning("No existing device data found, starting fresh.")

def save_devices():
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(devices, f, indent=4)
        logger.debug("Devices successfully saved to disk.")
    except IOError as e:
        logger.critical(f"Failed to save devices to disk: {e}")

load_devices()

class Device(BaseModel):
    device_id: str = Field("00:00:00:00:00:00")
    location: str = Field("Bratsk")
    owner: str = Field("Lyceum")
    measurement_type: str = Field("temperature")
    sensor_model: str = Field(..., description="Put particular sensor model name here")

@app.post("/register")
async def register_device(device: Device):
    logger.debug(f"Received registration request for device_id: {device.device_id}")

    if device.device_id in devices:
        logger.warning(f"Device {device.device_id} is already registered.")
        raise HTTPException(status_code=400, detail="Device already registered")

    devices[device.device_id] = device.model_dump()
    save_devices()
    logger.info(f"Device {device.device_id} registered successfully.")
    return {"message": "Device registered successfully"}

@app.get("/devices")
async def list_devices():
    logger.debug("Fetching list of all registered devices.")
    if not devices:
        logger.warning("Device list requested but no devices are registered.")
    return devices

@app.get("/device/{device_id}")
async def get_device(device_id: str):
    logger.debug(f"Fetching details for device_id: {device_id}")
    if device_id not in devices:
        logger.error(f"Device {device_id} not found.")
        raise HTTPException(status_code=404, detail="Device not found")
    logger.info(f"Device {device_id} details retrieved.")
    return devices[device_id]

@app.post("/alert")
async def receive_alert(alert: dict):
    logger.critical(f"Received critical alert: {alert['alert']}")
    return {"message": "Alert received"}
