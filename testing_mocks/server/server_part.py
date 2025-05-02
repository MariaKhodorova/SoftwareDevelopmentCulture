from fastapi import FastAPI, HTTPException, UploadFile, File, Form
import os
import shutil
import csv

app = FastAPI()

users = {}
users_info = {}

# Регистрация пользователей
@app.post("/registration/")
def user_registration(username: str = Form(...)):
    if username in users.values():
        raise HTTPException(status_code=400, detail="Пользователь уже существует!")
    user_id = len(users) + 1
    users[user_id] = username
    users_info[user_id] = []
    return {"message": "Пользователь зарегистрирован", "user_id": user_id}

# Отдавать данные в формате json
def parse_csv(csv_string):
    data = []
    lines = csv_string.strip().split("\n")
    if not lines:
        return data

    reader = csv.reader(lines)
    header = next(reader)

    for row in reader:
        row_dict = {}
        for col_name, value in zip(header, row):
            row_dict[col_name] = value.strip()
        data.append(row_dict)

    return data

# Принимать данные в формате csv
@app.post("/upload/{user_id}")
def upload_file(user_id: int, file: UploadFile = File(...)):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден!")
    
    file_location = f"uploads/{user_id}_{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    with open(file_location, "r", encoding="utf-8") as f:
        csv_content = f.read()
    parsed_data = parse_csv(csv_content)
    
    users_info[user_id].extend(parsed_data)
    
    return {"message": "Файлы успешно загружены!"}

# Отдавать список пользователей
@app.get("/users/")
def get_users():
    return users

# Отдавать данные конкретного пользователя
@app.get("/data/{user_id}")
def get_user_data(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users_info[user_id]