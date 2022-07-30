/*Direccion*/
CREATE TABLE Direccion(
	direccion_id INTEGER NOT NULL,
	calle TEXT NOT NULL,
	numero TEXT NOT NULL,
	ciudad TEXT NOT NULL,
	provincia TEXT NOT NULL,
	pais TEXT NOT NULL,
	employee_id INTEGER ,
	customer_id INTEGER,
	branch_id  INTEGER DEFAULT 0 NULL,
	FOREIGN KEY (employee_id)
	REFERENCES empleado(employee_id)
	FOREIGN KEY (customer_id)
	REFERENCES cliente(customer_id)
	FOREIGN KEY (branch_id)
	REFERENCES sucursal(branch_id)
	 
)
/*Queda para revisar, no funciona*/
-- SELECT employee_id,customer_id,branch_id
-- 	CASE 
-- 		 WHEN employee_id=0 THEN NULL
-- 		 WHEN customer_id=0 THEN NULL
-- 		 WHEN branch_id =0 THEN NULL
-- 	END 
-- FROM Direccion;

/*Entendiendo que si no es empleado ni tampoco cliente debe ser una sucursal*/
ALTER TABLE Direccion
ADD Ente TEXT;

-- SELECT employee_id, customer_id, branch_id,
-- 		CASE 
-- 			WHEN employee_id >0 AND branch_id = 0 AND customer_id = 0 THEN customer_id = NULL AND branch_id = NULL AND 'empleado'
-- 			WHEN customer_id >0 AND employee_id = 0 AND branch_id= 0 THEN employee_id = NULL AND branch_id = NULL AND 'cliente'
-- 			WHEN branch_id>0 AND employee_id = 0 AND customer_id = 0 THEN customer_id = NULL AND employee_id =NULL AND 'sucursal' 
-- 			END Ente
-- FROM Direccion;

/* 7 REVISAR(falta aclarar situacion de como deben ir los id)*/
INSERT INTO Direccion (direccion_id,calle,numero,ciudad,provincia,pais,employee_id,customer_id, branch_id)
VALUES(1,'amet ultricies',201,'Lagos','Misiones','Argentina',172,258,37),
  (2,'leo. Morbi',633,'Don Pedro','Mendoza','Argentina',405,340,40),
  (3,'penatibus et',448,'San Martin','Mendoza','Argentina',313,279,47),
  (4,'Donec non',137,'Lagos','Córdoba','Argentina',402,205,22),
  (5,'et',533,'Pilar','Córdoba','Argentina',421,91,1),
  (6,'In nec',242,'Don Pedro','Mendoza','Argentina',340,486,87),
  (7,'augue porttitor',283,'Villa Tortuga','Tucumán','Argentina',155,191,24),
  (8,'velit.',478,'Lagos','Tucumán','Argentina',447,207,42),
  (9,'Sed',61,'Villa Tortuga','Tierra del Fuego','Argentina',486,100,94),
  (10,'Lorem',363,'Pilar','Mendoza','Argentina',47,141,85);
INSERT INTO Direccion (direccion_id,calle,numero,ciudad,provincia,pais,employee_id,customer_id, branch_id)
VALUES
  (11,'ligula eu',94,'San Martin','Córdoba','Argentina', 21,325,23),
  (12,'Donec',626,'San Ignacio','Salta','Argentina',72,157,10),
  (13,'non',774,'Yapeyu','Buenos Aires','Argentina',100,241,22),
  (14,'tincidunt pede',601,'San Ignacio','Santa Fe','Argentina',293,116,40),
  (15,'lacus.',205,'Yapeyu','Corrientes','Argentina',328,407,2),
  (16,'ornare. Fusce',586,'Lagos','Buenos Aires','Argentina',329,255,68),
  (17,'Cras',471,'Pilar','Corrientes','Argentina',216,459,49),
  (18,'egestas lacinia.',903,'Yapeyu','Buenos Aires','Argentina',370,172,91),
  (19,'Fusce mi',254,'Villa Tortuga','Córdoba','Argentina',250,269,41),
  (20,'venenatis a,',893,'Lagos','Misiones','Argentina',432,267,48);
INSERT INTO Direccion (direccion_id,calle,numero,ciudad,provincia,pais,employee_id,customer_id, branch_id)
VALUES
  (21,'imperdiet',726,'San Ignacio','Salta','Argentina',422,64,55),
  (22,'ac',610,'San Fernando','Misiones','Argentina',298,225,27),
  (23,'sagittis.',970,'Don Pedro','Corrientes','Argentina',492,37,99),
  (24,'quis',89,'Don Pedro','Tucumán','Argentina',166,428,54),
  (25,'tincidunt',949,'Don Pedro','Tierra del Fuego','Argentina',214,396,93),
  (26,'aliquam arcu.',918,'San Ignacio','Córdoba','Argentina',158,440,17),
  (27,'vehicula. Pellentesque',596,'Pilar','Buenos Aires','Argentina',343,407,16),
  (28,'eu',355,'Yapeyu','Salta','Argentina',108,142,73),
  (29,'felis ullamcorper',895,'Lagos','Tucumán','Argentina',10,424,78),
  (30,'sed dolor.',286,'San Martin','Tucumán','Argentina',29,440,92);
INSERT INTO Direccion (direccion_id,calle,numero,ciudad,provincia,pais,employee_id,customer_id, branch_id)
VALUES
  (31,'eget laoreet',417,'Don Pedro','Mendoza','Argentina',189,135,39),
  (32,'risus',910,'Lagos','Tierra del Fuego','Argentina',459,27,30),
  (33,'nibh.',941,'Belgrano','Córdoba','Argentina',304,111,77),
  (34,'magna.',594,'Yapeyu','Tucumán','Argentina',261,142,29),
  (35,'ut odio',557,'Villa Tortuga','Misiones','Argentina',164,283,9),
  (36,'orci, consectetuer',572,'Lagos','Misiones','Argentina',402,440,99),
  (37,'eget',25,'San Martin','Mendoza','Argentina',113,297,74),
  (38,'tellus.',833,'San Ignacio','Tucumán','Argentina',214,339,98),
  (39,'turpis. In',615,'Lagos','Santa Fe','Argentina',271,178,17),
  (40,'faucibus',71,'Don Pedro','Córdoba','Argentina',243,7,39);
INSERT INTO Direccion (direccion_id,calle,numero,ciudad,provincia,pais,employee_id,customer_id, branch_id)
VALUES
  (41,'Nulla',75,'San Fernando','Mendoza','Argentina',161,132,86),
  (42,'iaculis',429,'San Fernando','Buenos Aires','Argentina',366,319,59),
  (43,'fermentum arcu.',823,'Villa Tortuga','Misiones','Argentina',232,43,89),
  (44,'felis purus',703,'Don Pedro','Tierra del Fuego','Argentina',264,310,80),
  (45,'in, cursus',180,'Lagos','Misiones','Argentina',285,362,41),
  (46,'pede, ultrices',888,'Lagos','Salta','Argentina',139,77,70),
  (47,'dictum.',110,'Belgrano','Mendoza','Argentina',49,478,68),
  (48,'nulla',455,'Yapeyu','Salta','Argentina',99,414,83),
  (49,'faucibus',587,'San Fernando','Buenos Aires','Argentina',183,125,98),
  (50,'augue porttitor',194,'Belgrano','Santa Fe','Argentina',177,289,7);
INSERT INTO Direccion (direccion_id,calle,numero,ciudad,provincia,pais,employee_id,customer_id, branch_id)
VALUES
  (51,'id',909,'Villa Tortuga','Salta','Argentina',119,203,26),
  (52,'lectus sit',88,'Don Pedro','Buenos Aires','Argentina',487,252,22),
  (53,'lacus,',279,'Pilar','Córdoba','Argentina',113,489,78),
  (54,'facilisis lorem',332,'Lagos','Santa Fe','Argentina',398,107,90),
  (55,'vehicula et,',730,'Villa Tortuga','Buenos Aires','Argentina',92,366,56),
  (56,'convallis',47,'Belgrano','Santa Fe','Argentina',90,423,58),
  (57,'leo',986,'Belgrano','Salta','Argentina',50,457,94),
  (58,'convallis',236,'Yapeyu','Mendoza','Argentina',272,67,5),
  (59,'mollis non,',638,'San Martin','Salta','Argentina',25,422,73),
  (60,'parturient montes,',500,'San Ignacio','Buenos Aires','Argentina',68,115,25);
INSERT INTO Direccion (direccion_id,calle,numero,ciudad,provincia,pais,employee_id,customer_id, branch_id)
VALUES
  (61,'Maecenas malesuada',466,'Villa Tortuga','Tucumán','Argentina',169,171,22),
  (62,'Cum',863,'San Martin','Misiones','Argentina',117,294,78),
  (63,'risus.',878,'Pilar','Mendoza','Argentina',178,365,94),
  (64,'Nulla tincidunt,',493,'San Ignacio','Córdoba','Argentina',27,320,40),
  (65,'nec ante.',924,'San Fernando','Misiones','Argentina',13,377,37),
  (66,'eleifend egestas.',736,'Pilar','Santa Fe','Argentina',294,98,10),
  (67,'adipiscing. Mauris',474,'San Ignacio','Tierra del Fuego','Argentina',421,505,44),
  (68,'odio sagittis',616,'San Ignacio','Corrientes','Argentina',399,28,61),
  (69,'tellus. Aenean',727,'San Martin','Tucumán','Argentina',231,435,16),
  (70,'dictum',475,'San Ignacio','Mendoza','Argentina',398,237,82);
INSERT INTO Direccion (direccion_id,calle,numero,ciudad,provincia,pais,employee_id,customer_id, branch_id)
VALUES
  (71,'sed, est.',222,'Lagos','Tucumán','Argentina',59,354,17),
  (72,'ante dictum',807,'San Ignacio','Tierra del Fuego','Argentina',425,294,37),
  (73,'nascetur',287,'Yapeyu','Tucumán','Argentina',455,114,58),
  (74,'felis, adipiscing',595,'San Fernando','Tierra del Fuego','Argentina',61,200,2),
  (75,'sed,',345,'San Ignacio','Mendoza','Argentina',474,111,27),
  (76,'Proin',992,'Pilar','Mendoza','Argentina',480,187,94),
  (77,'Phasellus vitae',137,'Belgrano','Misiones','Argentina',86,322,61),
  (78,'tortor. Nunc',62,'San Fernando','Corrientes','Argentina',26,482,49),
  (79,'est',221,'San Fernando','Tucumán','Argentina',219,473,30),
  (80,'fringilla.',611,'San Ignacio','Tierra del Fuego','Argentina',428,359,16);
INSERT INTO Direccion (direccion_id,calle,numero,ciudad,provincia,pais,employee_id,customer_id, branch_id)
VALUES
  (81,'et,',851,'San Martin','Tucumán','Argentina',445,57,30),
  (82,'habitant',72,'San Ignacio','Buenos Aires','Argentina',344,463,74),
  (83,'arcu',949,'Yapeyu','Buenos Aires','Argentina',41,436,29),
  (84,'suscipit nonummy.',104,'Yapeyu','Córdoba','Argentina',184,374,73),
  (85,'Nulla facilisis.',630,'San Fernando','Mendoza','Argentina',140,136,54),
  (86,'pede ac',452,'Pilar','Salta','Argentina',280,338,34),
  (87,'et, rutrum',305,'Pilar','Buenos Aires','Argentina',316,135,6),
  (88,'ipsum.',31,'San Ignacio','Tucumán','Argentina',470,250,60),
  (89,'lacus,',150,'Belgrano','Misiones','Argentina',393,86,42),
  (90,'leo',300,'San Martin','Mendoza','Argentina',273,164,57);
INSERT INTO Direccion (direccion_id,calle,numero,ciudad,provincia,pais,employee_id,customer_id,branch_id)
VALUES
  (91,'lectus.',338,'Don Pedro','Mendoza','Argentina',99,317,99),
  (92,'luctus, ipsum',228,'Pilar','Salta','Argentina',190,4,43),
  (93,'ut quam',989,'San Ignacio','Santa Fe','Argentina',440,282,77),
  (94,'In condimentum.',860,'San Ignacio','Tucumán','Argentina',279,180,4),
  (95,'semper erat,',816,'Pilar','Misiones','Argentina',98,412,37),
  (96,'varius ultrices,',706,'Pilar','Buenos Aires','Argentina',292,99,2),
  (97,'quam,',874,'Don Pedro','Mendoza','Argentina',85,450,30),
  (98,'Fusce',141,'Pilar','Mendoza','Argentina',139,93,87),
  (99,'at,',140,'San Fernando','Salta','Argentina',88,252,37),
  (100,'porttitor scelerisque',299,'Don Pedro','Misiones','Argentina',316,26,25);

 /*Como llamar para ver la tabla con sus respectivos id*/
 
SELECT *
FROM Direccion as d
INNER JOIN empleado as e, cliente AS c, sucursal AS s
ON d.employee_id = e.employee_id AND d.customer_id = c.customer_id AND d.branch_id = s.branch_id;
