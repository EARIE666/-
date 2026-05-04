import random
from datetime import datetime, timedelta

def get_random_date_2024():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    
    # Разница в днях
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    
    return start_date + timedelta(days=random_days)

print(get_random_date_2024().strftime('%Y-%m-%d'))
