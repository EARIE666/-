
class EmailAccount:
    def __init__(self):
        self.__email = ""
    
    def set_email(self, email):
        if '@' in email:
            self.__email = email
    
    def get_email(self):
        return self.__email
