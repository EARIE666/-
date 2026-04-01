CREATE TABLE Заказы (
    Идентификатор_заказа INT PRIMARY KEY AUTO_INCREMENT,
    Идентификатор_пользователя INT,
    Сумма_заказа DECIMAL(10, 2),
    Статус_заказа VARCHAR(50),
    FOREIGN KEY (Идентификатор_пользователя) REFERENCES Пользователи(Идентификатор)
);
