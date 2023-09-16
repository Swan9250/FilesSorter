#!/usr/bin/python3.11

import Database  # Класс для подключения к базе
import argparse  # Модуль для работы с аргументами консоли


class Migration01:  # Тренирую в питоне технологии yii2

    def __init__(self):
        db = Database.Mysql()  # Создаëм объект Mysql
        self.connect = db.connection  # Подключаемся к базе
        self.cursor = db.cursor  # Инициализируем объект для операций с базой
        self.args = self.parse_args()  # Получаем аргументы из консоли

    def up(self):  # Видоизменяем базу
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sorted_files(
            file_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            name VARCHAR(255),
            size INT,
            file_type VARCHAR(30),
            created DATETIME,
            last_modified DATETIME,
            added DATETIME,
            path TEXT,
            comment TEXT)
            """
        )  # Создание таблицы sorted_files

    def down(self):  # Возвращаем, как было до up
        self.cursor.execute(
            """
                DROP TABLE IF EXISTS sorted_files
            """
        )  # Удаление person_info

    @staticmethod
    def parse_args():
        parser_obj = argparse.ArgumentParser()  # Создаëм объект парсера
        group = parser_obj.add_mutually_exclusive_group(required=True)  # Группа взаимоисключаемых аргументов
        group.add_argument('up',
                           nargs='?')  # Добавляем аргумент up в группу. Второй параметр показывает, что количество аргументов для up не определено (а то бы ожидался хотя бы один)
        group.add_argument('down', nargs='?')  # Добавляем аргумент down в группу
        return parser_obj.parse_args()  # Парсим аргументы, согласно заданным выше правилам


connection = Migration01()  # Создаëм объект миграции
operation = ''
try:
    if connection.args.up:
        operation = 'up'
        connection.up()
        print("Up query execution succeeded")
    elif connection.args.down:  # elif здесь потому, что мало ли что я там ввëл, и как argparse на это отреагировал
        operation = 'down'
        connection.down()
        print("Down query execution succeeded")
except Exception as e:
    print(f"Query error execution: {e}\n")
    rollback = input("Need rollback?")
    if rollback in ('Y', 'y'):
        if operation == 'up':
            connection.down()
        else:
            connection.up()
