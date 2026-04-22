# File: 19.py
text = "Name: John Age: 25"

pattern = r"Name:\s*(\w+)\s+Age:\s*(\d+)"

match = re.search(pattern, text)

if match:
    name = match.group(1)
    age = match.group(2)
    
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
