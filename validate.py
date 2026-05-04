#Напиши скрипт validate.py с нуля.

#Требования:
#1. Принимает 1 аргумент: путь к JSON файлу (через argparse)
#. Проверяет что файл существует
#3. Проверяет что содержимое — валидный JSON
#4. Выводит [OK] + exit 0 при успехе
#5. Выводит [ERROR: причина] + exit 1 при ошибке
#6. Использует os.getenv() для переменной APP_ENV
#7. Если APP_ENV=debug — выводит дополнительную информацию
import argparse
import json
import os
import sys
def validate (file):
    if not os.path.isfile(file):
        print("[ERROR: File not exist]")
        sys.exit(1)
    app_env = os.getenv("APP_ENV")
    if app_env == "debug":
        print(f"[DEBUG: Проверяю файл {file}]")
    with open(file,'r',encoding="utf-8") as json_file:
        try:
            js_data=json.load(json_file)
            if not 'host' in js_data:
                print("[ERROR: host не найден]")
                sys.exit(1)
            if not isinstance(js_data['host'],str):
                print("[ERROR: host должен быть строкой]")
                sys.exit(1)
            if 'port' not in js_data:
                print("[ERROR: port не найден]")
                sys.exit(1)
            if not isinstance(js_data['port'],int):
                print("[ERROR: port должен быть числом]")
                sys.exit(1)
            if not (1 <= js_data['port'] <= 65535):
                print("[ERROR: порт должен быть 1-65535]")
                sys.exit(1)
            print("[OK]")
            sys.exit(0)
        except json.JSONDecodeError as e:
            print(f"[ERROR: {e}]")
            sys.exit(1)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Скрипт для проверки JSON-файла")
    parser.add_argument("file", help="путь к json")# ⚠️
    args = parser.parse_args()
    validate(args.file)

