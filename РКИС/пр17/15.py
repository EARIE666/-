import json

data = {
    "name": "Ivan",
    "age": 25,
    "skills": ["python", "data"]
}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
print("Данные сохранены в data.json")
