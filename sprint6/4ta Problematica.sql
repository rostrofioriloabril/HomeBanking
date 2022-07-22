/* CUARTA PROBLEMATICA */
/* 1 */ LISTO
SELECT COUNT(customer_id) AS Cantidad_clientes,sucursal.branch_name as Nombre_sucursal
FROM cliente
INNER JOIN sucursal
ON sucursal.branch_id=cliente.branch_id
GROUP BY Nombre_sucursal
ORDER BY 1 DESC

/* 2 */ (CANTIDAD DE EMPLEADOS x SUCURSAL, FALTA COMPARAR CONTRA CANTIDAD DE CLEINTES)
SELECT COUNT(employee_id) AS Cantidad_empleados,sucursal.branch_name as Nombre_sucursal
FROM empleado
INNER JOIN sucursal
ON sucursal.branch_id=empleado.branch_id
GROUP BY Nombre_sucursal
/* 3 */
/* 4 */
/* 5 */
/* 6 */
/* 7 */