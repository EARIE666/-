"""
app.py - Простое веб-приложение
================================
"""

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import hashlib
import os
import datetime

app = Flask(__name__)
app.secret_key = 'secret-key-2024'

DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password):
    """Хеширование пароля"""
    return hashlib.sha256(password.encode()).hexdigest()

# ==================== ГЛАВНЫЕ СТРАНИЦЫ ====================

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Страница входа"""
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        
        print(f"=== ПОПЫТКА ВХОДА ===")
        print(f"Email: '{email}'")
        print(f"Пароль: '{password}'")
        
        if not email or not password:
            return render_template('login.html', error='Введите email и пароль')
        
        conn = get_db()
        
        # Ищем пользователя по email
        user = conn.execute(
            'SELECT * FROM users WHERE email = ?',
            (email,)
        ).fetchone()
        
        if not user:
            print(f"❌ Пользователь с email '{email}' не найден")
            conn.close()
            return render_template('login.html', error='Неверный email или пароль')
        
        print(f"✅ Пользователь найден: ID={user['id']}, Role={user['role']}")
        print(f"   Hash в БД: {user['password_hash']}")
        
        # Хешируем введенный пароль
        password_hash = hash_password(password)
        print(f"   Хеш введенного: {password_hash}")
        
        # Сравниваем
        if user['password_hash'] == password_hash:
            print(f"✅ Пароль верный! Вход разрешен")
            
            session['user_id'] = user['id']
            session['email'] = user['email']
            session['role'] = user['role']
            
            # Получаем имя
            if user['role'] == 'patient':
                patient = conn.execute('SELECT full_name FROM patients WHERE user_id = ?', (user['id'],)).fetchone()
                session['full_name'] = patient['full_name'] if patient else user['email']
                print(f"   Имя пациента: {session['full_name']}")
            else:
                session['full_name'] = 'Администратор'
            
            conn.close()
            return redirect(url_for('dashboard'))
        else:
            print(f"❌ Пароль НЕ верный!")
            conn.close()
            return render_template('login.html', error='Неверный email или пароль')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Регистрация нового пациента"""
    if request.method == 'POST':
        full_name = request.form.get('full_name', '').strip()
        phone = request.form.get('phone', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        print(f"=== РЕГИСТРАЦИЯ ===")
        print(f"Email: {email}")
        print(f"Пароль: {password}")
        
        # Проверки
        if not full_name or not phone or not email or not password:
            return render_template('register.html', error='Заполните все поля')
        
        if password != confirm_password:
            return render_template('register.html', error='Пароли не совпадают')
        
        if len(password) < 3:
            return render_template('register.html', error='Пароль должен быть не менее 3 символов')
        
        conn = get_db()
        
        # Проверяем email
        existing = conn.execute('SELECT id FROM users WHERE email = ?', (email,)).fetchone()
        if existing:
            conn.close()
            return render_template('register.html', error='Email уже зарегистрирован')
        
        # Проверяем телефон
        existing = conn.execute('SELECT id FROM patients WHERE phone = ?', (phone,)).fetchone()
        if existing:
            conn.close()
            return render_template('register.html', error='Телефон уже зарегистрирован')
        
        # Хешируем пароль
        password_hash = hash_password(password)
        
        # Создаем пользователя
        cursor = conn.execute('''
            INSERT INTO users (email, password_hash, role)
            VALUES (?, ?, 'patient')
        ''', (email, password_hash))
        user_id = cursor.lastrowid
        
        # Создаем пациента
        conn.execute('''
            INSERT INTO patients (user_id, full_name, phone)
            VALUES (?, ?, ?)
        ''', (user_id, full_name, phone))
        
        conn.commit()
        conn.close()
        
        print(f"✅ Пользователь {email} успешно зарегистрирован")
        
        return redirect(url_for('login', message='Регистрация успешна! Войдите в систему'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db()
    role = session['role']
    data = {}
    
    if role == 'admin':
        # Статистика
        data['total_patients'] = conn.execute('SELECT COUNT(*) as c FROM patients').fetchone()['c']
        data['total_doctors'] = conn.execute('SELECT COUNT(*) as c FROM doctors').fetchone()['c']
        data['total_appointments'] = conn.execute('SELECT COUNT(*) as c FROM appointments').fetchone()['c']
        
        # Список врачей
        data['doctors'] = conn.execute('SELECT * FROM doctors').fetchall()
        
        # Список пациентов
        data['patients'] = conn.execute('''
            SELECT p.*, u.email 
            FROM patients p 
            JOIN users u ON p.user_id = u.id
            ORDER BY p.created_at DESC
        ''').fetchall()
        
        # Записи
        data['appointments'] = conn.execute('''
            SELECT a.*, p.full_name as patient_name, d.full_name as doctor_name
            FROM appointments a
            JOIN patients p ON a.patient_id = p.id
            JOIN doctors d ON a.doctor_id = d.id
            ORDER BY a.appointment_datetime DESC
            LIMIT 20
        ''').fetchall()
        
    else:  # patient
        patient = conn.execute('SELECT id, full_name FROM patients WHERE user_id = ?', (session['user_id'],)).fetchone()
        if patient:
            data['patient'] = patient
            
            # Активные записи
            data['active_appointments'] = conn.execute('''
                SELECT a.*, d.full_name as doctor_name, d.specialization, d.consultation_price
                FROM appointments a
                JOIN doctors d ON a.doctor_id = d.id
                WHERE a.patient_id = ? AND a.status = 'active'
                ORDER BY a.appointment_datetime
            ''', (patient['id'],)).fetchall()
            
            # История
            data['history'] = conn.execute('''
                SELECT a.*, d.full_name as doctor_name, d.specialization,
                       m.diagnosis, m.recommendations
                FROM appointments a
                JOIN doctors d ON a.doctor_id = d.id
                LEFT JOIN medical_records m ON a.id = m.appointment_id
                WHERE a.patient_id = ? AND a.status IN ('completed', 'cancelled')
                ORDER BY a.appointment_datetime DESC
                LIMIT 10
            ''', (patient['id'],)).fetchall()
    
    conn.close()
    return render_template('dashboard.html', role=role, data=data)

# ==================== ДЕЙСТВИЯ ====================

@app.route('/book', methods=['GET', 'POST'])
def book():
    """Запись на прием"""
    if 'user_id' not in session or session['role'] != 'patient':
        return redirect(url_for('login'))
    
    conn = get_db()
    doctors = conn.execute('SELECT * FROM doctors').fetchall()
    
    if request.method == 'POST':
        doctor_id = request.form['doctor_id']
        appointment_date = request.form['appointment_date']
        appointment_time = request.form['appointment_time']
        appointment_datetime = f"{appointment_date} {appointment_time}:00"
        
        patient = conn.execute('SELECT id FROM patients WHERE user_id = ?', (session['user_id'],)).fetchone()
        
        # Проверяем, не занято ли время
        existing = conn.execute('''
            SELECT id FROM appointments 
            WHERE doctor_id = ? AND appointment_datetime = ? AND status = 'active'
        ''', (doctor_id, appointment_datetime)).fetchone()
        
        if existing:
            conn.close()
            return render_template('book.html', doctors=doctors, error='Это время уже занято')
        
        # Создаем запись
        conn.execute('''
            INSERT INTO appointments (patient_id, doctor_id, appointment_datetime, status)
            VALUES (?, ?, ?, 'active')
        ''', (patient['id'], doctor_id, appointment_datetime))
        conn.commit()
        conn.close()
        
        return redirect(url_for('dashboard'))
    
    conn.close()
    return render_template('book.html', doctors=doctors)

@app.route('/cancel/<int:appointment_id>')
def cancel(appointment_id):
    """Отмена записи"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db()
    conn.execute('UPDATE appointments SET status = "cancelled" WHERE id = ?', (appointment_id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('dashboard'))

@app.route('/complete/<int:appointment_id>')
def complete(appointment_id):
    """Завершение приема (только для админа)"""
    if 'user_id' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))
    
    conn = get_db()
    
    # Получаем стоимость
    appointment = conn.execute('''
        SELECT a.*, d.consultation_price
        FROM appointments a
        JOIN doctors d ON a.doctor_id = d.id
        WHERE a.id = ?
    ''', (appointment_id,)).fetchone()
    
    if appointment:
        # Добавляем платеж
        conn.execute('''
            INSERT INTO payments (appointment_id, amount)
            VALUES (?, ?)
        ''', (appointment_id, appointment['consultation_price']))
        
        # Обновляем статус
        conn.execute('UPDATE appointments SET status = "completed" WHERE id = ?', (appointment_id,))
        conn.commit()
    
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    """Добавление врача (только для админа)"""
    if 'user_id' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))
    
    full_name = request.form['full_name']
    specialization = request.form['specialization']
    price = request.form['price']
    
    conn = get_db()
    conn.execute('''
        INSERT INTO doctors (full_name, specialization, consultation_price)
        VALUES (?, ?, ?)
    ''', (full_name, specialization, price))
    conn.commit()
    conn.close()
    
    return redirect(url_for('dashboard'))

@app.route('/add_medical_record/<int:appointment_id>', methods=['POST'])
def add_medical_record(appointment_id):
    """Добавление медицинской записи (только для админа)"""
    if 'user_id' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))
    
    complaints = request.form['complaints']
    diagnosis = request.form['diagnosis']
    recommendations = request.form['recommendations']
    
    conn = get_db()
    
    # Проверяем, есть ли уже запись
    existing = conn.execute('SELECT id FROM medical_records WHERE appointment_id = ?', (appointment_id,)).fetchone()
    
    if existing:
        conn.execute('''
            UPDATE medical_records 
            SET complaints = ?, diagnosis = ?, recommendations = ?
            WHERE appointment_id = ?
        ''', (complaints, diagnosis, recommendations, appointment_id))
    else:
        conn.execute('''
            INSERT INTO medical_records (appointment_id, complaints, diagnosis, recommendations)
            VALUES (?, ?, ?, ?)
        ''', (appointment_id, complaints, diagnosis, recommendations))
    
    conn.commit()
    conn.close()
    
    return redirect(url_for('dashboard'))

# ==================== ЗАПУСК ====================

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        print("❌ База данных не найдена! Запустите: python init_db.py")
    else:
        print("\n" + "="*50)
        print("🚀 ЗАПУСК СЕРВЕРА")
        print("="*50)
        print("🌐 http://localhost:5000")
        print("="*50)
        print("\n📋 ДОСТУП:")
        print("   👤 Админ: admin@clinic.ru / admin123")
        print("   🧑 Пациент: ivanov@mail.ru / 123")
        print("   🧑 Пациент: petrova@mail.ru / 123")
        print("   🧑 Пациент: patientadded@yandex.ru / qwerty123")
        print("\n📝 ИЛИ зарегистрируйтесь как новый пациент")
        print("="*50 + "\n")
        
        app.run(debug=True, host='0.0.0.0', port=5000)