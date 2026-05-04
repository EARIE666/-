k = 0

with open('input.txt', 'r', encoding = 'utf-8') as file:
    for i in file:
        k += len(i.split())

print(k)
