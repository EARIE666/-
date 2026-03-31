@echo off
chcp 65001 > nul
echo ========================================
echo   Платная поликлиника - Система учета
echo ========================================
echo.

if not exist database.db (
    echo База данных не найдена!
    echo Создание базы данных...
    python init_db.py
    echo.
)

echo Запуск сервера...
echo Откройте в браузере: http://localhost:5000
echo.
echo Для остановки сервера нажмите Ctrl+C
echo.
python app.py

pause