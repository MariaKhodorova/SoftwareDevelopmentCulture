import questionary
import requests
import sys

class APIClient:
    """Класс для взаимодействия с API сервера"""
    def __init__(self, base_url="http://localhost:8000"):
        # Базовый URL сервера, по умолчанию локальный хост
        self.base_url = base_url

    def register_user(self):
        """Метод для регистрации нового пользователя"""
        # Запрашиваем имя пользователя через интерактивный ввод
        username = questionary.text("Введите имя пользователя:").ask()
        try:
            # Отправляем POST запрос на регистрацию
            response = requests.post(f"{self.base_url}/registration/", params={"username": username})
            if response.status_code == 200:
                data = response.json()
                print(f"Пользователь успешно зарегистрирован! ID пользователя: {data['user_id']}")
            else:
                print(f"Ошибка: {response.json()['detail']}")
        except requests.RequestException as e:
            print(f"Ошибка при подключении к серверу: {e}")

    def upload_file(self):
        """Метод для загрузки CSV файла на сервер"""
        # Запрашиваем ID пользователя и путь к файлу
        user_id = questionary.text("Введите ID пользователя:").ask()
        file_path = questionary.path("Выберите CSV файл для загрузки:").ask()
        
        try:
            # Открываем файл и отправляем его на сервер
            with open(file_path, 'rb') as file:
                files = {'file': (file_path.split('/')[-1], file, 'text/csv')}
                response = requests.post(f"{self.base_url}/upload/{user_id}", files=files)
                
            if response.status_code == 200:
                print("Файл успешно загружен!")
            else:
                print(f"Ошибка: {response.json()['detail']}")
        except FileNotFoundError:
            print("Файл не найден!")
        except requests.RequestException as e:
            print(f"Ошибка при подключении к серверу: {e}")

    def list_users(self):
        """Метод для получения списка всех пользователей"""
        try:
            # Отправляем GET запрос для получения списка пользователей
            response = requests.get(f"{self.base_url}/users/")
            if response.status_code == 200:
                users = response.json()
                print("\nСписок пользователей:")
                for user_id, username in users.items():
                    print(f"ID: {user_id}, Имя: {username}")
            else:
                print(f"Ошибка: {response.json()['detail']}")
        except requests.RequestException as e:
            print(f"Ошибка при подключении к серверу: {e}")

    def get_user_data(self):
        """Метод для получения данных конкретного пользователя"""
        # Запрашиваем ID пользователя
        user_id = questionary.text("Введите ID пользователя:").ask()
        try:
            # Отправляем GET запрос для получения данных пользователя
            response = requests.get(f"{self.base_url}/data/{user_id}")
            if response.status_code == 200:
                data = response.json()
                if data:
                    print("\nДанные пользователя:")
                    for item in data:
                        print(item)
                else:
                    print("У пользователя нет данных")
            else:
                print(f"Ошибка: {response.json()['detail']}")
        except requests.RequestException as e:
            print(f"Ошибка при подключении к серверу: {e}")

def main():
    """Основная функция программы"""
    # Создаем экземпляр клиента API
    client = APIClient()
    
    # Основной цикл программы
    while True:
        # Показываем меню выбора действий
        action = questionary.select(
            "Выберите действие:",
            choices=[
                "Регистрация пользователя",
                "Загрузить CSV файл",
                "Показать список пользователей",
                "Получить данные пользователя",
                "Выход"
            ]
        ).ask()

        # Обработка выбранного действия
        if action == "Регистрация пользователя":
            client.register_user()
        elif action == "Загрузить CSV файл":
            client.upload_file()
        elif action == "Показать список пользователей":
            client.list_users()
        elif action == "Получить данные пользователя":
            client.get_user_data()
        elif action == "Выход":
            print("До свидания!")
            sys.exit(0)


if __name__ == "__main__":
    main()

    