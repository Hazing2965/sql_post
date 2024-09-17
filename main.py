import sqlite3
import os

print('Hello!')
while True:
    try:
        # Получаем относительный путь от пользователя
        relative_path = input("Введите относительный путь к файлу (например, '../bla/1.txt'): ")

        # Преобразуем относительный путь в абсолютный
        absolute_path = os.path.abspath(relative_path)

        # Проверяем наличие файла
        if os.path.isfile(absolute_path):
            print(f"Файл существует: {absolute_path}")
            print('Подключаюсь к базе данных..')
            with sqlite3.connect(absolute_path) as db:
                print('Успешно подключён')
                post = input('Введите ваш запрос: ')
                cursor = db.cursor()
                cursor.execute(post)
                db.commit()
                print(f'Запрос: "{post}"\nк базе данных: "{absolute_path}"\nУспешно применён!')
            print('Отключение от базы данных') # paid_free
        else:
            print(f"Файл не найден: {absolute_path}")
    except Exception as e:
        print(f'ERROR: {e}')

