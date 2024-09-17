import sqlite3
import os

# ../Sushka/Sushka_bot/development/database.db
# ALTER TABLE users ADD COLUMN paid_free BOOLEAN DEFAULT False

print('Hello!')

# Получаем относительный путь от пользователя
relative_path = input("Введите относительный путь к файлу (например, '../bla/1.db' or return): ")
while relative_path != '':
    try:
        # Преобразуем относительный путь в абсолютный
        absolute_path = os.path.abspath(relative_path)

        # Проверяем наличие файла
        if os.path.isfile(absolute_path):
            print(f"Файл существует: {absolute_path}")
            print('Подключаюсь к базе данных..')
            with sqlite3.connect(absolute_path) as db:
                print('Успешно подключён')
                post = input(f'Введите ваш запрос к базе данных:{absolute_path}\nВвод: ')
                while post != '':
                    try:
                        cursor = db.cursor()
                        cursor.execute(post)
                        db.commit()
                        print(f'{"-"*50}\nЗапрос: "{post}"\nк базе данных: "{absolute_path}"\nУспешно применён!\n{"-"*50}')
                    except Exception as e:
                        print(f'ERROR: {e}')
                    post = input(f'Введите ваш запрос к базе данных:{absolute_path}\nВвод(return для выхода): ')
            print('Отключение от базы данных')
        else:
            print(f"Файл не найден: {absolute_path}")
    except Exception as e:
        print(f'ERROR: {e}')
    relative_path = input("Введите относительный путь к файлу (например, '../bla/1.txt' or return): ")

print('EXIT')