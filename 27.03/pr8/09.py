
class Device:
    def action(self):
        print("Doing generic action")

class Phone(Device):
    def action(self):
        print("Making a call")

class Laptop(Device):
    def action(self):
        print("Running software")
