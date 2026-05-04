class InstanceCounter:
    count = 0

    def __init__(self):
        InstanceCounter.count += 1


a = InstanceCounter()
b = InstanceCounter()
c = InstanceCounter()
print(InstanceCounter.count)  # 3
