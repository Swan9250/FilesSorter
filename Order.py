import argparse
import os
import time
from datetime import datetime
import logging

home_dir = os.path.expanduser('~')

start_dir = home_dir + '/Неразобранное/'
archives = home_dir + '/Архивы/'
images = home_dir + '/Изображения/'
musics = home_dir + '/Музыка/'
videos = home_dir + '/Видео/'
docs = home_dir + '/Документы/'
programs = home_dir + '/Программы/'
packages = home_dir + '/Пакеты/'

file_types = {
    'archive': ['.zip', '.tar.gz', '.tar', '.tar.bz', '.7z', '.rar', 'tar.xz'],
    'image': ['.jpg', '.jpeg', '.gif', '.png'],
    'music': ['.mp3', '.flac'],
    'video': ['.mp4', '.mov', '.avi', '.mkv'],
    'document': ['.log', '.txt', '.doc', '.odt', '.docx', '.pdf'],
    'program': ['.py', '.php', '.sh', '.exe'],
    'package': ['.deb', '.iso']
}


def type_match(file: str, search_type: str) -> str:
    file = file.lower()
    for choice in file_types[search_type]:
        if file.endswith(choice):
            return 'is_{}'.format(search_type)
    return ''


def create_parser():
    parser_obj = argparse.ArgumentParser()
    parser_obj.add_argument('-r', '--recursive', action='store_true')
    return parser_obj


def replace_controller(path: str, recursive: bool):
    list_files: list[os.DirEntry]
    with os.scandir(path) as list_files:
        for file in list_files:
            if file.is_file():
                replace_by_type(path, file)
                # year_replace(file)
            elif file.is_dir() and recursive:
                print(file.name, 'is_dir')
    return True


def replace_by_type(path: str, file):
    results = {
        'is_archive': archives,
        'is_image': images,
        'is_music': musics,
        'is_video': videos,
        'is_document': docs,
        'is_program': programs,
        'is_package': packages,
    }

    if not file.name.startswith('.'):
        for file_type in file_types.keys():
            print(file_type)
            result = type_match(file.name, file_type)
            print(result)
            if result != '':
                needed_path = results.get(result, 'type was not found')
                print(needed_path)
                try:
                    print(path + file.name, needed_path + file.name)
                    # os.replace(path + file.name, needed_path + file.name)
                    os.replace(path + file.name, year_replace(needed_path, file) + file.name)
                    break
                except FileNotFoundError:
                    os.mkdir(needed_path)
                    # os.replace(path + file.name, needed_path + file.name)
                    os.replace(path + file.name, year_replace(needed_path, file) + file.name)
                    break

    else:
        print('secret_file')


def year_replace(path, file) -> str:
    needed_year = "/" + get_needed_time(file.stat(follow_symlinks=False).st_mtime, "%Y")
    try:
        os.listdir(path + needed_year)
    except FileNotFoundError:
        os.mkdir(path + needed_year)
    except NotADirectoryError:
        print(f"File {path + needed_year} exists, but it's not a dir.")

    return month_replace(path + needed_year, file)


def month_replace(path, file) -> str:
    needed_month = "/" + get_needed_time(file.stat(follow_symlinks=False).st_mtime, "%m")
    try:
        os.listdir(path + needed_month)
    except FileNotFoundError:
        os.mkdir(path + needed_month)
    except NotADirectoryError:
        print(f"File {path + needed_month} exists, but it's not a dir.")

    return day_replace(path + needed_month, file)


def day_replace(path, file) -> str:
    needed_day = "/" + get_needed_time(file.stat(follow_symlinks=False).st_mtime, "%d")
    try:
        os.listdir(path + needed_day)
    except FileNotFoundError:
        os.mkdir(path + needed_day)
    except NotADirectoryError:
        print(f"File {path + needed_day} exists, but it's not a dir.")

    return path + needed_day + "/"


def get_needed_time(create_time, order):
    print(datetime.strptime(time.ctime(create_time), "%a %b %d %H:%M:%S %Y"))
    return datetime.strptime(time.ctime(create_time), "%a %b %d %H:%M:%S %Y").strftime(order)


if __name__ == '__main__':
    os.chdir(start_dir)
    print(os.getcwd())
    parser = create_parser()
    namespace = parser.parse_args()

    replace_controller(start_dir, namespace.recursive)

    print(namespace)
    if namespace.recursive:
        print('e')
