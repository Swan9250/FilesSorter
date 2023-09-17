#!/usr/bin/python3.11

import mysql.connector  # Для подключения к мускулю
import json  # Для работы с json
import datetime  # Для работы со временем
import os.path

from app.views.Image import Image


class Mysql:

    def __init__(self):
        ROOT_PATH = f"{os.path.expanduser('~')}/projects/FilesSorter/"

        with open(f'{ROOT_PATH}mysql.json', 'r') as credentials:
            self.params = json.loads(credentials.read())
            self.connection = self.__connect()
            self.cursor = self.connection.cursor()

    def __connect(self):
        try:  # Пытаемся подключиться с имеющимися данными
            connection = mysql.connector.connect(
                host=self.params['host'],
                user=self.params['user'],
                password=self.params['password'],
                database=self.params['database'],
                auth_plugin='mysql_native_password',
            )
            return connection
        except Exception as e:  # Желательно указывать конкретные Exception
            print(f"Database connection error: {e}")

    def add_image(self, image: Image, comment=None):
        ids_list = []
        date = datetime.datetime.now()  # Запоминаем текущее время
        if self.connection.is_closed():  # Проверяем, вдруг соединение закрыто - переоткрываем.
            self.__connect()

        try:
            self.cursor.execute(
                """
                INSERT INTO sorted_files(
                name,
                size,
                file_type,
                created,
                last_modified,
                added,
                path,
                comment
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    image.name,
                    image.size,
                    image.file_type,
                    image.created,
                    image.last_modified,
                    date,
                    image.path,
                    comment
                )
            )
            self.connection.commit()
        except Exception as e:
            print(f"Insert error: {e}")

    def find_one(self, path: str):
        if self.connection.is_closed():
            self.__connect()
        try:
            self.cursor.execute(
                """
                SELECT * FROM sorted_files
                WHERE path=%s
                """, (path,)
            )
        except Exception as e:
            print(f"Select error: {e}")
        return self.parse_from_db(self.cursor.fetchone())

    @staticmethod
    def parse_from_db(result):  # only for fetchone
        if result is not None:
            obj = Image(result[7])
            obj.id = result[0]
            obj.name = result[1]
            obj.size = result[2]
            obj.file_type = result[3]
            obj.created = result[4]
            obj.last_modified = result[5]
            return obj
        return None

    def close(self):  # Закрываем соединение
        self.connection.close()
