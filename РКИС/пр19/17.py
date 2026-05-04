import csv

users = [
    ['Name', 'Age', 'Role'],
    ['Alice', 30, 'Dev'],
    ['Bob', 25, 'Designer']
]

with open('users.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(users)
print("CSV файл создан")
