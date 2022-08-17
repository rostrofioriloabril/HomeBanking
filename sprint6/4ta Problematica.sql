/* CUARTA PROBLEMATICA */
/* 1 */ LISTO
SELECT COUNT(customer_id) AS Cantidad_clientes,sucursal.branch_name as Nombre_sucursal
FROM cliente
INNER JOIN sucursal
ON sucursal.branch_id=cliente.branch_id
GROUP BY Nombre_sucursal
ORDER BY 1 DESC

/* 2 */ LISTO
SELECT COUNT(employee_id) AS Cantidad_empleados,sucursal.branch_name as Nombre_sucursal, customer_id as Cantidad_clientes,round(CAST(count(employee_id) AS FLOAT)/customer_id,2) as Clientes_X_Empleados
FROM empleado
INNER JOIN sucursal
ON sucursal.branch_id=empleado.branch_id
INNER JOIN cliente
ON cliente.branch_id = empleado.branch_id
GROUP BY Nombre_sucursal 

/* 3 */ LISTO
SELECT Tipo_tarjeta.type_card_name AS Tarjetas_credito, Marca_tarjeta.brand_card_name AS Marca_de_tarjeta, sucursal.branch_name AS Nombre_sucursal
FROM Tarjeta
INNER JOIN Marca_tarjeta
ON Marca_tarjeta.brand_card_id = Tarjeta.brand_card_id
INNER JOIN Tipo_tarjeta
ON Tipo_tarjeta.type_card_name = Tarjeta.type_card_name
INNER JOIN cliente
ON cliente.customer_id = Tarjeta.customer_id
INNER JOIN sucursal
ON sucursal.branch_id = cliente.branch_id
WHERE Tarjetas_credito = 'Credito'
GROUP BY sucursal.branch_name,
		Marca_tarjeta.brand_card_name


/* 4 */ LISTO
SELECT AVG(loan_total) AS Promedio_creditos, sucursal.branch_name AS Nombre_sucursal
FROM prestamo
INNER JOIN cliente
ON cliente.customer_id = prestamo.customer_id
INNER JOIN sucursal
ON sucursal.branch_id = cliente.branch_id
GROUP BY sucursal.branch_name
DROP TABLE Auditoria_cuenta
/* 5 */ LISTO
CREATE TABLE Auditoria_cuenta(
	old_id INTEGER PRIMARY KEY,
	new_id INTEGER NOT NULL,
	old_balance INTEGER NOT NULL,
	new_balance INTEGER NOT NULL,
	old_iban INTEGER NOT NULL,
	new_iban INTEGER NOT NULL,
	old_type INTEGER NOT NULL,
	new_type INTEGER NOT NULL,
	user_action TEXT NOT NULL,
	created_at TEXT NOT NULL
);
/*DROP TRIGGER insert_auditoria_cuenta*/
CREATE TRIGGER insert_auditoria_cuenta
AFTER UPDATE OF balance, iban, type_account ON cuenta
BEGIN
	INSERT INTO auditoria_cuenta (old_id, new_id, old_balance, new_balance, old_iban, new_iban, old_type, new_type, user_action, created_at)
	VALUES (OLD.account_id, NEW.account_id, OLD.balance, NEW.balance, OLD.iban, NEW.iban, OLD.type_account, NEW.type_account, 'UPDATE', datetime('now'));
END

UPDATE cuenta
SET balance = balance-100
WHERE account_id=10 OR account_id=11 OR account_id=12 OR account_id=13 OR account_id=14

SELECT *
FROM Auditoria_cuenta

/* 6 */ LISTO
CREATE UNIQUE INDEX IND_dni
on cliente (customer_DNI)

SELECT * 
FROM cliente
INDEXED BY IND_dni
/*DROP TABLE Movimientos*/
/* 7 */
CREATE TABLE Movimientos(
	movimiento_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	account_id INTEGER NOT NULL,
	signo TEXT NOT NULL,
	monto INTEGER NOT NULL,
	tipo_operacion TEXT NOT NULL,
	hora TEXT NOT NULL
)
END TRANSACTION;
BEGIN TRANSACTION;

UPDATE cuenta
	SET balance = balance - 1000
WHERE account_id = 200;

UPDATE cuenta 
	SET balance = balance + 1000
WHERE account_id = 400;

INSERT INTO Movimientos (account_id, signo, monto, tipo_operacion, hora)
VALUES (200, '-', 1000, 'Envio Transferencia', datetime('now'));

INSERT INTO Movimientos (account_id, signo, monto, tipo_operacion, hora)
VALUES (400, '+', 1000, 'Recibo Transferencia', datetime('now'));

COMMIT;

ROLLBACK;

SELECT *
FROM Movimientos