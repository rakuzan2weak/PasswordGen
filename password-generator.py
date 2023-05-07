import random
import string

def generate_password(length):
    # Создаем список символов, из которых будет генерироваться пароль
    characters = string.ascii_letters + string.digits + string.punctuation

    # Генерируем пароль заданной длины
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Пример использования
password = generate_password(8) # Генерируем пароль длиной 8 символов
print("Ваш пароль: " + password) # Выводим пароль на экран