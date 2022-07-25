/* SEGUNDA PROBLEMATICA */
/* 1 */ FALTA PONER LA EDAD
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