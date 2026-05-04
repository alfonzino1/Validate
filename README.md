# Config Validator

CLI-скрипт для проверки JSON-конфигураций.

## Что проверяет

- ✅ Валидность JSON
- ✅ Наличие полей: host, port, timeout
- ✅ Типы данных (строка, число)
- ✅ Диапазон порта (1-65535)

## Использование

```bash
# Базовый запуск
python validate.py config.json
# Сборка
docker build -t config-validator .
# Запуск
docker run -v $(pwd)/config.json:/app/config.json config-validator /app/config.json
# Debug режим
APP_ENV=debug python validate.py config.json
