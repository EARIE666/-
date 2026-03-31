#!/bin/bash
echo "========================================"
echo "  Платная поликлиника - Система учета"
echo "========================================"
echo

if [ ! -f database.db ]; then
    echo "База данных не найдена!"
    echo "Создание базы данных..."
    python3 init_db.py
    echo
fi

echo "Запуск сервера..."
echo "Откройте в браузере: http://localhost:5000"
echo
python3 app.py