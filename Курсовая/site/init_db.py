"""
init_db.py - Создание базы данных для учета обращений пациентов
==============================================================
Курсовая работа: Проектирование базы данных
==============================================================
"""

import sqlite3
import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_database():
    # Удаляем старую БД
    if os.path.exists('database.db'):
        os.remove('database.db')
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    print("="*60)
    print("  СОЗДАНИЕ БАЗЫ ДАННЫХ")
    print("="*60)
    
    # 1. Таблица пользователей
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('admin', 'patient')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    print("✓ Таблица users")
    
    # 2. Таблица пациентов
    cursor.execute('''
        CREATE TABLE patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE REFERENCES users(id) ON DELETE CASCADE,
            full_name TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL,
            birth_date DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    print("✓ Таблица patients")
    
    # 3. Таблица врачей
    cursor.execute('''
        CREATE TABLE doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            specialization TEXT NOT NULL,
            consultation_price REAL NOT NULL
        )
    ''')
    print("✓ Таблица doctors")
    
    # 4. Таблица услуг
    cursor.execute('''
        CREATE TABLE services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    print("✓ Таблица services")
    
    # 5. Таблица записей
    cursor.execute('''
        CREATE TABLE appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL REFERENCES patients(id),
            doctor_id INTEGER NOT NULL REFERENCES doctors(id),
            appointment_datetime TIMESTAMP NOT NULL,
            status TEXT NOT NULL DEFAULT 'active' CHECK(status IN ('active', 'completed', 'cancelled')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    print("✓ Таблица appointments")
    
    # 6. Таблица медицинских записей
    cursor.execute('''
        CREATE TABLE medical_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            appointment_id INTEGER UNIQUE NOT NULL REFERENCES appointments(id) ON DELETE CASCADE,
            complaints TEXT,
            diagnosis TEXT,
            recommendations TEXT
        )
    ''')
    print("✓ Таблица medical_records")
    
    # 7. Таблица платежей
    cursor.execute('''
        CREATE TABLE payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            appointment_id INTEGER NOT NULL REFERENCES appointments(id),
            amount REAL NOT NULL,
            status TEXT DEFAULT 'paid'
        )
    ''')
    print("✓ Таблица payments")
    
    # Создаем индексы
    cursor.execute('CREATE INDEX idx_appointments_datetime ON appointments(appointment_datetime)')
    cursor.execute('CREATE INDEX idx_patients_phone ON patients(phone)')
    print("✓ Индексы созданы")
    
    # ========== ДОБАВЛЯЕМ ТЕСТОВЫЕ ДАННЫЕ ==========
    print("\nДобавление тестовых данных...")
    
    # Администратор
    cursor.execute("INSERT INTO users (email, password_hash, role) VALUES (?, ?, ?)",
                   ('admin@clinic.ru', hash_password('admin123'), 'admin'))
    print("  ✓ Администратор: admin@clinic.ru / admin123")
    
    # Пациент 1
    cursor.execute("INSERT INTO users (email, password_hash, role) VALUES (?, ?, ?)",
                   ('ivanov@mail.ru', hash_password('123'), 'patient'))
    user_id = cursor.lastrowid
    cursor.execute("INSERT INTO patients (user_id, full_name, phone) VALUES (?, ?, ?)",
                   (user_id, 'Иванов Иван Иванович', '+7 999 111-22-33'))
    
    # Пациент 2
    cursor.execute("INSERT INTO users (email, password_hash, role) VALUES (?, ?, ?)",
                   ('petrova@mail.ru', hash_password('123'), 'patient'))
    user_id = cursor.lastrowid
    cursor.execute("INSERT INTO patients (user_id, full_name, phone) VALUES (?, ?, ?)",
                   (user_id, 'Петрова Анна Сергеевна', '+7 999 444-55-66'))
    
    print("  ✓ Пациенты: 2 добавлено")
    
    # Врачи
    doctors = [
        ('Иванова Мария Ивановна', 'Терапевт', 2500),
        ('Петров Александр Сергеевич', 'Кардиолог', 3200),
        ('Сидорова Елена Владимировна', 'Невролог', 3000),
    ]
    for name, spec, price in doctors:
        cursor.execute("INSERT INTO doctors (full_name, specialization, consultation_price) VALUES (?, ?, ?)",
                       (name, spec, price))
    print(f"  ✓ Врачи: {len(doctors)} добавлено")
    
    # Услуги
    services = [
        ('Прием терапевта', 2500),
        ('Прием кардиолога', 3200),
        ('Прием невролога', 3000),
        ('Общий анализ крови', 800),
        ('УЗИ', 3500),
        ('ЭКГ', 1200),
    ]
    for name, price in services:
        cursor.execute("INSERT INTO services (name, price) VALUES (?, ?)", (name, price))
    print(f"  ✓ Услуги: {len(services)} добавлено")
    
    # Тестовая запись
    cursor.execute('''
        INSERT INTO appointments (patient_id, doctor_id, appointment_datetime, status)
        VALUES (1, 1, datetime('now', '+1 day', '+10 hours'), 'active')
    ''')
    print("  ✓ Тестовая запись добавлена")
    
    conn.commit()
    conn.close()
    
    print("\n" + "="*60)
    print("✅ БАЗА ДАННЫХ СОЗДАНА!")
    print("="*60)
    print("\n📋 ДОСТУП:")
    print("   👤 Администратор: admin@clinic.ru / admin123")
    print("   🧑 Пациент: ivanov@mail.ru / 123")
    print("   🧑 Пациент: petrova@mail.ru / 123")
    print("\n🚀 Запуск: python app.py")

if __name__ == '__main__':
    create_database()