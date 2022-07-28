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