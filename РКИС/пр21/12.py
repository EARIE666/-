class User:
    __slots__ = ('login', 'password')

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def change_password(self, old_password, new_password):
        if self.password == old_password:
            self.password = new_password
            print(f"Пароль пользователя {self.login} изменён")
        else:
            print("Неверный старый пароль")

user = User("user123", "pass123")
user.change_password("pass123", "newpass456")