DELIMITER //

CREATE TRIGGER trg_Заказы_Статус
BEFORE INSERT ON Заказы
FOR EACH ROW
BEGIN
    IF NEW.Сумма_заказа > 1000 THEN
        SET NEW.Статус_заказа = 'Завершен';
    END IF;
END; //

DELIMITER ;
