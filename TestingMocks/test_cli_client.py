import pytest
from unittest.mock import patch
import requests_mock
import json
from cli_client import APIClient

@pytest.fixture
def api_client():
    return APIClient()

# Тест регистрации пользователя
def test_register_user(api_client):
    with requests_mock.Mocker() as m:
        # Мокаем успешный ответ
        m.post('http://localhost:8000/registration/?username=TestUser',
               json={'message': 'Пользователь зарегистрирован', 'user_id': 1})
        
        # Мокаем ввод пользователя
        with patch('questionary.text', return_value=type('obj', (object,), {'ask': lambda: 'TestUser'})):
            api_client.register_user()

        # Проверяем, что запрос был сделан
        assert m.called
        assert m.call_count == 1

# Тест получения списка пользователей
def test_list_users(api_client):
    with requests_mock.Mocker() as m:
        # Мокаем ответ с списком пользователей
        mock_users = {
            "1": "User1",
            "2": "User2"
        }
        m.get('http://localhost:8000/users/', json=mock_users)
        
        with patch('builtins.print') as mock_print:
            api_client.list_users()
            
        # Проверяем, что запрос был сделан
        assert m.called
        assert m.call_count == 1

# Тест получения данных пользователя
def test_get_user_data(api_client):
    with requests_mock.Mocker() as m:
        # Мокаем ответ с данными пользователя
        mock_data = [
            {"name": "John", "age": "25"},
            {"name": "Anna", "age": "30"}
        ]
        m.get('http://localhost:8000/data/1', json=mock_data)
        
        # Мокаем ввод ID пользователя
        with patch('questionary.text', return_value=type('obj', (object,), {'ask': lambda: '1'})):
            with patch('builtins.print') as mock_print:
                api_client.get_user_data()
                
        # Проверяем, что запрос был сделан
        assert m.called
        assert m.call_count == 1

# Тест загрузки файла
def test_upload_file(api_client):
    with requests_mock.Mocker() as m:
        # Мокаем успешный ответ при загрузке файла
        m.post('http://localhost:8000/upload/1', 
               json={'message': 'Файлы успешно загружены!'})
        
        # Мокаем ввод пользователя и открытие файла
        with patch('questionary.text', return_value=type('obj', (object,), {'ask': lambda: '1'})):
            with patch('questionary.path', return_value=type('obj', (object,), {'ask': lambda: 'test.csv'})):
                with patch('builtins.open', create=True) as mock_open:
                    mock_open.return_value.__enter__.return_value = "mock_file"
                    api_client.upload_file()
                    
        # Проверяем, что запрос был сделан
        assert m.called
        assert m.call_count == 1

# Тест обработки ошибок
def test_error_handling(api_client):
    with requests_mock.Mocker() as m:
        # Мокаем ответ с ошибкой
        m.post('http://localhost:8000/registration/?username=TestUser',
               status_code=400,
               json={'detail': 'Пользователь уже существует!'})
        
        # Мокаем ввод пользователя
        with patch('questionary.text', return_value=type('obj', (object,), {'ask': lambda: 'TestUser'})):
            with patch('builtins.print') as mock_print:
                api_client.register_user()
                
        # Проверяем, что ошибка была обработана
        mock_print.assert_called_with('Ошибка: Пользователь уже существует!')


        