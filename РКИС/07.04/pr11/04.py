# ================== Задача 4 — Перегрузка метода с default-параметрами ==================
class Printer:
    def print_message(self, msg, times=1):
        for _ in range(times):
            print(msg)

# Проверка задачи 4
print("\n=== Задача 4 ===")
p = Printer()
p.print_message("Hello")
p.print_message("Hi", 3)
