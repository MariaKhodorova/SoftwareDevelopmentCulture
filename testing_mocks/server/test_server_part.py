import pytest
from unittest import mock
from fastapi.testclient import TestClient
from server_part import app, users, users_info

client = TestClient(app)

# Очистка пользователей перед каждым тестом
@pytest.fixture(autouse=True)
def reset_users():
    users.clear()
    users_info.clear()

# Проверка за зарегистрированного пользователя
def test_user_registration():
    response = client.post("/registration/", data={"username": "testuser"})
    assert response.status_code == 200
    assert "user_id" in response.json()

# Проверка загрузки файла в формате csv
def test_upload_file():
    with mock.patch("builtins.open", mock.mock_open(read_data="name,age\nJohn,30\nDoe,25")):
        response = client.post("/registration/", data={"username": "testuser"})
        user_id = response.json()["user_id"]

        file_mock = mock.Mock()
        file_mock.filename = "test.csv"
        file_mock.file = mock.MagicMock()

        response = client.post(f"/upload/{user_id}", files={"file": ("test.csv", "name,age\nJohn,30\nDoe,25")})
        assert response.status_code == 200
        assert response.json()["message"] == "Файлы успешно загружены!"

        response = client.get(f"/data/{user_id}")
        assert response.status_code == 200
        assert len(response.json()) == 2
        assert response.json()[0]["name"] == "John"
        assert response.json()[1]["name"] == "Doe"

# Проверка на получение списка пользователей
def test_get_users():
    with mock.patch("server_part.users", {1: "user1", 2: "user2"}):
        response = client.get("/users/")
        assert response.status_code == 200
        assert len(response.json()) == 2
        assert "user1" in response.json().values()
        assert "user2" in response.json().values()

# Проверка на получение конкретного пользователей
def test_get_user_data():
    with mock.patch("server_part.users", {1: "testuser"}), mock.patch("server_part.users_info", {1: [{"name": "Alice", "age": "22"}, {"name": "Bob", "age": "27"}]}):
        response = client.get("/data/1")
        assert response.status_code == 200
        assert len(response.json()) == 2
        assert response.json()[0]["name"] == "Alice"
        assert response.json()[1]["name"] == "Bob"

# Корректная обработка ошибок
def test_user_not_found():
    with mock.patch("server_part.users", {1: "testuser"}):
        response = client.get("/data/999")
        assert response.status_code == 404
        assert response.json()["detail"] == "User not found"
        
        test_csv = "name,age\nAlice,22\nBob,27"
        response = client.post("/upload/999", files={"file": ("data.csv", test_csv)})
        assert response.status_code == 404
        assert response.json()["detail"] == "Пользователь не найден!"