/* SEGUNDA PROBLEMATICA */
/* 1 */ LISTO
SELECT customer_id AS ID, branch_id AS Sucursal_ID,customer_name AS Nombre,customer_surname AS Apellido, customer_DNI as DNI,(strftime('%Y', 'now') - strftime('%Y', cliente.dob )) - (strftime('%m-%d', 'now') < strftime('%m-%d', cliente.dob )) AS Edad
FROM cliente
WHERE edad>40
ORDER BY 5 DESC

SELECT customer_id AS ID, branch_id AS Sucursal_ID,customer_name AS Nombre,customer_surname AS Apellido, customer_DNI as DNI,(strftime('%Y', 'now') - strftime('%Y', cliente.dob )) - (strftime('%m-%d', 'now') < strftime('%m-%d', cliente.dob )) AS Edad
FROM cliente
WHERE nombre LIKE 'Anne' OR nombre LIKE 'Tyler'
ORDER BY edad

/* 2 */ LISTO
INSERT INTO cliente(customer_name, customer_surname, customer_DNI, dob, branch_id)
VALUES	
	('Lois', 'Stout', 47730534, '1984-07-07', 80), 
	('Hall', 'Mcconnell', 52055464, '1968-04-30', 45),
	('Hilel', 'Mclean', 43625213, '1993-03-28', 77),
	('Jin', 'Cooley', 21207908, '1959-08-24', 96),
	('Gabriel', 'Harmon', 57063950, '1976-04-01', 27)

/* 3 */ LISTO
UPDATE cliente
SET branch_id = 10
WHERE customer_id >= 503

/* 4 */ LISTO
DELETE FROM cliente
WHERE customer_name='Noel' AND customer_surname='David';

/* 5 */ LISTO
SELECT * 
FROM prestamo
ORDER BY 4 DESC
LIMIT 1