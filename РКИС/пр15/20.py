# File: 20.py
def task20():
    errors_by_day = {}
    with open('log.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if "ERROR" in line:
                # Предполагаем, что дата всегда первые 10 символов
                date = line[:10] 
                errors_by_day[date] = errors_by_day.get(date, 0) + 1
    
    for date, count in errors_by_day.items():
        print(f"{date}: {count}")
