-- Drop database if it exists
DROP DATABASE IF EXISTS mystore;

-- Create the database
CREATE DATABASE mystore;

-- Use the database
USE mystore;

-- Create the customer table
CREATE TABLE customer (
    id VARCHAR(17) NOT NULL,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	CONSTRAINT pk_customer
		PRIMARY KEY (id)
);

-- Create the product table
CREATE TABLE product (
	id VARCHAR(17) NOT NULL,
    category VARCHAR(30),
    sub_category VARCHAR(30),
    product_name TINYTEXT,
    CONSTRAINT pk_product
		PRIMARY KEY (id)
);

-- Create the sale table
CREATE TABLE sale (
	id INT NOT NULL AUTO_INCREMENT,
	order_id VARCHAR(17),
	product_id VARCHAR(17) NOT NULL,
	customer_id VARCHAR(17) NOT NULL,
	order_date DATE,
	ship_date DATE,
	ship_mode VARCHAR(16),
	shipping_cost DECIMAL(16,2),
	segment VARCHAR(12),
	city VARCHAR(40),
	state VARCHAR(40),
	country VARCHAR(40),
	postal_code VARCHAR(30),
	market VARCHAR(30),
	region VARCHAR(40),
	sales DECIMAL(16,2),
	quantity INT,
	discount DECIMAL(4, 3),
	profit DECIMAL(16,2),
	order_priority VARCHAR(30),
	CONSTRAINT pk_sales 
		PRIMARY KEY (id),
	CONSTRAINT fk_product_id 
		FOREIGN KEY (product_id) 
		REFERENCES product(id),
	CONSTRAINT fk_customer_id 
		FOREIGN KEY (customer_id)
		REFERENCES customer(id),
	CONSTRAINT discount_above_0
		CHECK (discount>=0),
	CONSTRAINT quantity_above_0
		CHECK (quantity>=0)
);