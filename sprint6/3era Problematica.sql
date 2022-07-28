/* TERCERA PROBLEMATICA */
/* 1 */ LISTO
SELECT * 
FROM cuenta 
WHERE balance<0

/* 2 */ LISTO
SELECT customer_name AS Nombre,customer_surname AS Apellido, (strftime('%Y', 'now') - strftime('%Y', cliente.dob )) - (strftime('%m-%d', 'now') < strftime('%m-%d', cliente.dob )) AS Edad
FROM cliente
WHERE Apellido LIKE '%z%'

/* 3 */ LISTO
SELECT customer_name AS Nombre,customer_surname AS Apellido, (strftime('%Y', 'now') - strftime('%Y', cliente.dob )) - (strftime('%m-%d', 'now') < strftime('%m-%d', cliente.dob )) AS Edad,sucursal.branch_name as Nombre_sucursal
FROM cliente
INNER JOIN sucursal
ON sucursal.branch_id=cliente.branch_id
WHERE Nombre LIKE 'Brendan'
ORDER BY 4

/* 4 */ LISTO
SELECT *
FROM prestamo
WHERE (loan_total)>80000 AND (loan_type)='PRENDARIO'
UNION
SELECT *
FROM prestamo
WHERE loan_type='PRENDARIO'

/* 5 */ LISTO
SELECT * 
FROM prestamo
WHERE loan_total > (SELECT AVG(loan_total) 
					FROM prestamo)
					

/* 6 */ LISTO
SELECT count((strftime('%Y', 'now') - strftime('%Y', cliente.dob )) - (strftime('%m-%d', 'now') < strftime('%m-%d', cliente.dob))) AS menores_de_50
FROM cliente
WHERE dob<50 

/* 7 */ LISTO
SELECT *
FROM cuenta
WHERE balance>8000
LIMIT 5

/* 8 */ LISTO
SELECT *
FROM prestamo
WHERE loan_date LIKE '%-04-%' OR loan_date LIKE '%-06-%' OR loan_date LIKE '%-08-%'
ORDER BY loan_total

/* 9 */ LISTO
SELECT SUM(loan_total) loan_total_accu
FROM prestamo
WHERE loan_type='HIPOTECARIO'
UNION
SELECT SUM(loan_total)
FROM prestamo
WHERE loan_type='PRENDARIO'
UNION
SELECT SUM(loan_total)
FROM prestamo
WHERE loan_type='PERSONAL'