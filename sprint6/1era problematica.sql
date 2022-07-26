/* PRIMERA PROBLEMATICA */
/* 1 */
CREATE TABLE Tipos_Cliente(
	type_account_id INTEGER PRIMARY KEY,
	type_customer_name TEXT NOT NULL
)

CREATE TABLE Tipo_Cuenta (
	type_account_id INTEGER PRIMARY KEY,
	type_account_name TEXT NOT NULL
)

CREATE TABLE Marca_Tarjeta (
	brand_card_id INTEGER PRIMARY KEY,
	brand_card_name TEXT NOT NULL
)

/* 2 */
CREATE TABLE Tarjeta (
	card_id INTEGER PRIMARY KEY ,
	card_number INTEGER CHECK (length(card_number <= 20)),
	card_cvv INTEGER NOT NULL,
	card_expired_date INTEGER NOT NULL,
	card_ valid_date INTEGER NOT NULL,
	card_type TEXT NOT NULL,
	customer_id INTEGER NOT NULL
	FOREIGN KEY (customer_id) 
	REFERENCES cliente(customer_id)
	ON UPDATE SET NULL
	ON DELETE SET NULL
	brand_card_id INTEGER NOT NULL
	FOREIGN KEY (brand_card_id)
	REFERENCES Marca_Tarjeta(brand_card_id)
	ON UPDATE SET NULL
	ON DELETE SET NULL
)

/* 3 */

/* 4 */

/* 5 */

/* 6 */

/* 7 */

/* 8 */

/* 9 */

/* 10 */