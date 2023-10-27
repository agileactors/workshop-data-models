--####################################################--
------------------ Creating Schemas --------------------
--####################################################--

CREATE SCHEMA IF NOT EXISTS ecommerce_schema;

--####################################################--
------------------ Ecommerce Database ------------------
--####################################################--

CREATE TABLE IF NOT EXISTS ecommerce_schema.users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    registration_date DATE NOT NULL,
    user_type TEXT CHECK (user_type IN ('admin', 'customer'))
);

CREATE TABLE IF NOT EXISTS ecommerce_schema.supplier (
    supplier_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    contact_details VARCHAR
);

CREATE TABLE IF NOT EXISTS ecommerce_schema.product (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    description VARCHAR,
    price FLOAT NOT NULL,
    stock_count INT NOT NULL,
    category VARCHAR,
    parent_product_id INT REFERENCES ecommerce_schema.product(product_id),
    supplier_id INT REFERENCES ecommerce_schema.supplier(supplier_id)
);

CREATE TABLE IF NOT EXISTS ecommerce_schema.orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES ecommerce_schema.users(user_id),
    order_date DATE NOT NULL,
    shipping_date DATE,
    status TEXT CHECK (status IN ('pending', 'shipped', 'delivered', 'cancelled'))
);

CREATE TABLE IF NOT EXISTS ecommerce_schema.orderdetails (
    order_id INT REFERENCES ecommerce_schema.orders(order_id),
    product_id INT REFERENCES ecommerce_schema.product(product_id),
    quantity INT NOT NULL,
    PRIMARY KEY (order_id, product_id)
);

CREATE TABLE IF NOT EXISTS ecommerce_schema.payment (
    payment_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES ecommerce_schema.orders(order_id),
    payment_method TEXT CHECK (payment_method IN ('credit_card', 'paypal', 'bank_transfer')),
    payment_date DATE NOT NULL,
    amount FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS ecommerce_schema.review (
    review_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES ecommerce_schema.product(product_id),
    user_id INT REFERENCES ecommerce_schema.users(user_id),
    rating INT CHECK (rating BETWEEN 1 AND 5),
    review_text VARCHAR
);

CREATE TABLE IF NOT EXISTS ecommerce_schema.wishlist (
    wishlist_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES ecommerce_schema.users(user_id),
    product_id INT REFERENCES ecommerce_schema.product(product_id)
);

CREATE TABLE IF NOT EXISTS ecommerce_schema.shipment (
    shipment_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES ecommerce_schema.orders(order_id),
    tracking_number VARCHAR,
    carrier VARCHAR,
    estimated_arrival DATE
);

---------------------------------------------------------------------------------------------------------

-- Deleting data in reverse order of dependency
DELETE FROM ecommerce_schema.shipment;
DELETE FROM ecommerce_schema.wishlist;
DELETE FROM ecommerce_schema.review;
DELETE FROM ecommerce_schema.payment;
DELETE FROM ecommerce_schema.orderdetails;
DELETE FROM ecommerce_schema.orders;
DELETE FROM ecommerce_schema.product;
DELETE FROM ecommerce_schema.supplier;
DELETE FROM ecommerce_schema.users;

---------------------------------------------------------------------------------------------------------

-- Reset sequences for tables with SERIAL primary keys
DO $$ 
BEGIN
    
    IF EXISTS (SELECT 1 FROM information_schema.sequences WHERE sequence_schema = 'ecommerce_schema' AND sequence_name = 'users_user_id_seq') THEN
        ALTER SEQUENCE ecommerce_schema.users_user_id_seq RESTART WITH 1;
    END IF;
    
    IF EXISTS (SELECT 1 FROM information_schema.sequences WHERE sequence_schema = 'ecommerce_schema' AND sequence_name = 'supplier_supplier_id_seq') THEN
        ALTER SEQUENCE ecommerce_schema.supplier_supplier_id_seq RESTART WITH 1;
    END IF;    
    
    IF EXISTS (SELECT 1 FROM information_schema.sequences WHERE sequence_schema = 'ecommerce_schema' AND sequence_name = 'product_product_id_seq') THEN
        ALTER SEQUENCE ecommerce_schema.product_product_id_seq RESTART WITH 1;
    END IF;
    
    IF EXISTS (SELECT 1 FROM information_schema.sequences WHERE sequence_schema = 'ecommerce_schema' AND sequence_name = 'orders_order_id_seq') THEN
        ALTER SEQUENCE ecommerce_schema.orders_order_id_seq RESTART WITH 1;
    END IF;
    
    IF EXISTS (SELECT 1 FROM information_schema.sequences WHERE sequence_schema = 'ecommerce_schema' AND sequence_name = 'payment_payment_id_seq') THEN
        ALTER SEQUENCE ecommerce_schema.payment_payment_id_seq RESTART WITH 1;
    END IF;
    
    IF EXISTS (SELECT 1 FROM information_schema.sequences WHERE sequence_schema = 'ecommerce_schema' AND sequence_name = 'review_review_id_seq') THEN
        ALTER SEQUENCE ecommerce_schema.review_review_id_seq RESTART WITH 1;
    END IF;

    IF EXISTS (SELECT 1 FROM information_schema.sequences WHERE sequence_schema = 'ecommerce_schema' AND sequence_name = 'wishlist_wishlist_id_seq') THEN
        ALTER SEQUENCE ecommerce_schema.wishlist_wishlist_id_seq RESTART WITH 1;
    END IF;
    
    IF EXISTS (SELECT 1 FROM information_schema.sequences WHERE sequence_schema = 'ecommerce_schema' AND sequence_name = 'shipment_shipment_id_seq') THEN
        ALTER SEQUENCE ecommerce_schema.shipment_shipment_id_seq RESTART WITH 1;
    END IF;

END $$;

---------------------------------------------------------------------------------------------------------

-- Inserting data in the order of dependency
INSERT INTO ecommerce_schema.users (username, password, email, registration_date, user_type) VALUES
('john_doe', 'password123', 'john.doe@example.com', '2023-10-19', 'customer'),
('alice_smith', 'securepass', 'alice.smith@example.com', '2023-09-15', 'admin');

INSERT INTO ecommerce_schema.supplier (name, contact_details) VALUES
('TechSupplier Inc.', '1234 Tech St, Silicon Valley'),
('StyleHouse', '5678 Fashion Ave, New York');

INSERT INTO ecommerce_schema.product (name, description, price, stock_count, category, parent_product_id, supplier_id) VALUES
('Laptop', 'Dell XPS 13', 1000.50, 100, 'Electronics', NULL, 1),
('Fashion Hat', 'Stylish summer hat', 25.00, 200, 'Fashion', NULL, 2);

INSERT INTO ecommerce_schema.orders (user_id, order_date, shipping_date, status) VALUES
(1, '2023-10-10', '2023-10-12', 'shipped'),
(2, '2023-09-20', '2023-09-23', 'delivered');

INSERT INTO ecommerce_schema.orderdetails (order_id, product_id, quantity) VALUES
(1, 1, 2),
(2, 2, 3);

INSERT INTO ecommerce_schema.payment (order_id, payment_method, payment_date, amount) VALUES
(1, 'credit_card', '2023-10-10', 2001.00),
(2, 'paypal', '2023-09-20', 75.00);

INSERT INTO ecommerce_schema.review (product_id, user_id, rating, review_text) VALUES
(1, 1, 4, 'Good laptop but a bit expensive.'),
(2, 2, 5, 'Love this hat!');

INSERT INTO ecommerce_schema.wishlist (user_id, product_id) VALUES
(1, 2);

INSERT INTO ecommerce_schema.shipment (order_id, tracking_number, carrier, estimated_arrival) VALUES
(1, 'TRACK12345', 'FedEx', '2023-10-15'),
(2, 'TRACK67890', 'UPS', '2023-09-25');

---------------------------------------------------------------------------------------------------------
