# debug_login.py
import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

email = 'patientadded@yandex.ru'
password = 'qwerty123'

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Получаем пользователя
user = cursor.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()

if user:
    print("="*50)
    print("ДИАГНОСТИКА ВХОДА")
    print("="*50)
    print(f"\n📧 Email: {email}")
    print(f"🔑 Введенный пароль: {password}")
    
    # Хеш введенного пароля
    entered_hash = hash_password(password)
    print(f"\n📝 Хеш введенного пароля: {entered_hash}")
    
    # Хеш в БД
    db_hash = user[2]
    print(f"💾 Хеш в БД: {db_hash}")
    
    print(f"\n🔍 Сравнение:")
    print(f"   {entered_hash}")
    print(f"   {db_hash}")
    
    if entered_hash == db_hash:
        print("\n✅ ПАРОЛЬ ВЕРНЫЙ! Вход должен работать")
    else:
        print("\n❌ ПАРОЛЬ НЕ ВЕРНЫЙ!")
        print("\nВозможные причины:")
        print("  1. Пароль при регистрации был другим")
        print("  2. В пароле есть лишние пробелы")
        print("  3. Регистр букв (пароль чувствителен к регистру)")
        
        # Обновляем пароль
        print("\n🔄 Обновляем пароль...")
        cursor.execute("UPDATE users SET password_hash = ? WHERE email = ?", (entered_hash, email))
        conn.commit()
        print("✅ Пароль обновлен! Теперь можно войти с паролем: " + password)
else:
    print(f"❌ Пользователь {email} не найден в БД!")

# Показываем всех пользователей
print("\n" + "="*50)
print("ВСЕ ПОЛЬЗОВАТЕЛИ В БД:")
print("="*50)
users = cursor.execute("SELECT id, email, role FROM users").fetchall()
for u in users:
    print(f"   ID: {u[0]}, Email: {u[1]}, Роль: {u[2]}")

conn.close()