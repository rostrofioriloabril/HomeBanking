/* SEGUNDA PROBLEMATICA */
/* 1 */ FALTA PONER LA EDAD

/*Hice la función para que reste la fecha actual con la fecha de nacimiento del cliente para calcular su edad. Falta mostrar en un Select el nombre, apellido, etc + esta subconsoluta de la edad*/
SELECT (strftime('%Y', 'now') - strftime('%Y', cliente.dob )) - (strftime('%m-%d', 'now') < strftime('%m-%d', cliente.dob )) AS Fecha_Nacimiento
FROM cliente;

/*una idea de por donde puede ir lo de arriba*/
SELECT customer_id AS ID, branch_id AS Sucursal_ID,customer_name AS Nombre,customer_surname AS Apellido, customer_DNI as DNI, dob AS edad
FROM cliente
WHERE(SELECT (strftime('%Y', 'now') - strftime('%Y', cliente.dob )) - (strftime('%m-%d', 'now') < strftime('%m-%d', cliente.dob )) AS Fecha_Nacimiento
		FROM cliente
		WHERE Fecha_Nacimiento = cliente.dob
		) = edad


SELECT customer_id AS ID, branch_id AS Sucursal_ID,customer_name AS Nombre,customer_surname AS Apellido, customer_DNI as DNI, dob AS edad
FROM cliente
WHERE edad>40
ORDER BY 5 DESC

SELECT (SELECT customer_id AS ID, branch_id AS Sucursal_ID,customer_name AS Nombre,customer_surname AS Apellido, customer_DNI as DNI, dob AS edad
		FROM cliente)
WHERE nombre LIKE 'Anne' OR nombre LIKE 'Tyler'
ORDER BY edad

/* 2 */

/* 3 */

/* 4 */ LISTO
DELETE FROM cliente
WHERE customer_name='Noel' AND customer_surname='David';

/* 5 */
SELECT * LISTO
FROM prestamo
ORDER BY 4 DESC
LIMIT 1