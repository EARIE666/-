
# Задача 4 — finally
def read_number(s):
    try:
        result = int(s)
        return result
    except ValueError:
        return "Error"
    finally:
        print("Done")

print(read_number("10"))
print(read_number("abc"))


