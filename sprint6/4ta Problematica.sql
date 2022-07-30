/* CUARTA PROBLEMATICA */
/* 1 */ LISTO
SELECT COUNT(customer_id) AS Cantidad_clientes,sucursal.branch_name as Nombre_sucursal
FROM cliente
INNER JOIN sucursal
ON sucursal.branch_id=cliente.branch_id
GROUP BY Nombre_sucursal
ORDER BY 1 DESC

/* 2 */ (FALTA DIVIDIR CANTIDAD DE CLIENTES POR EMPLEADO, EN CADA SUCURSAL)
SELECT COUNT(employee_id) AS Cantidad_empleados,sucursal.branch_name as Nombre_sucursal, customer_id as Cantidad_clientes
FROM empleado
INNER JOIN sucursal
ON sucursal.branch_id=empleado.branch_id
INNER JOIN cliente
ON cliente.branch_id = empleado.branch_id
GROUP BY Nombre_sucursal 

/* 3 */ LISTO
SELECT COUNT(card_type) AS Tarjetas_credito, Marca_tarjeta.brand_card_name AS Marca_de_tarjeta, sucursal.branch_name AS Nombre_sucursal
FROM Tarjeta
INNER JOIN Marca_tarjeta
ON Marca_tarjeta.brand_card_id = Tarjeta.brand_card_id
INNER JOIN cliente
ON cliente.customer_id = Tarjeta.customer_id
INNER JOIN sucursal
ON sucursal.branch_id = cliente.branch_id
WHERE card_type = 'Credito'
GROUP BY sucursal.branch_id,
		Marca_tarjeta.brand_card_name


/* 4 */ LISTO
SELECT AVG(loan_total) AS Promedio_creditos, sucursal.branch_name AS Nombre_sucursal
FROM prestamo
INNER JOIN cliente
ON cliente.customer_id = prestamo.customer_id
INNER JOIN sucursal
ON sucursal.branch_id = cliente.branch_id
GROUP BY sucursal.branch_name

/* 5 */
/* 6 */
/* 7 */