CREATE TABLE IF NOT EXISTS orders (
    id int AUTO_INCREMENT NOT NULL,
    customer_name varchar(255),
    customer_phone_1 varchar(255) NOT NULL,
    customer_phone_2 int,
    customer_main_address_id int NOT NULL,
    customer_address_1 varchar(255),
    customer_address_2 varchar(255),
    preferred_delivery_day date,
    preferred_delivery_time time,
    order_type varchar(255) NOT NULL DEFAULT 'new order',
    is_it_pickup tinyint DEFAULT '0',
    products_total_price decimal(10,2) NOT NULL DEFAULT '0.0',
    delivery_fee decimal(10,2) NOT NULL DEFAULT '0.0',
    discount_amount decimal(10,2) NOT NULL DEFAULT '0.0',
    total decimal(10,2) NOT NULL DEFAULT '0.0',
    delivery_service_id int NOT NULL,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    note varchar(255) NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS products (
    id int AUTO_INCREMENT NOT NULL,
    product_name varchar(255) NOT NULL,
    default_selling_price decimal(10,2) NOT NULL DEFAULT '0.0',
    default_buying_price decimal(10,2) NOT NULL DEFAULT '0.0',
    quantity int NOT NULL DEFAULT '0',
    PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS nawris_addresses (
    id int AUTO_INCREMENT NOT NULL,
    state varchar(255) NOT NULL,
    city varchar(255),
    delivery_fee decimal(10,2) NOT NULL DEFAULT '10',
    note int NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT uc_nawris_address UNIQUE (state, city)
);
CREATE TABLE IF NOT EXISTS delivery_services (
    id int AUTO_INCREMENT NOT NULL,
    delivery_service_name varchar(255) NOT NULL,
    description varchar(255) NOT NULL,
    note varchar(255),
    PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS statuses (
    id int AUTO_INCREMENT NOT NULL,
    status varchar(255) NOT NULL,
    description varchar(255) NOT NULL,
    note varchar(255),
    PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS order_events (
    id int AUTO_INCREMENT NOT NULL,
    order_id int NOT NULL,
    status_id int NOT NULL,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    note varchar(255),
    PRIMARY KEY (id),
    CONSTRAINT order_events_fk1 FOREIGN KEY (order_id) REFERENCES orders (id),
    CONSTRAINT order_events_fk2 FOREIGN KEY (status_id) REFERENCES statuses (id)
);
CREATE TABLE IF NOT EXISTS ordered_products (
    id int AUTO_INCREMENT NOT NULL,
    order_id int NOT NULL,
    product_id int NOT NULL,
    ordered_quantity int NOT NULL DEFAULT '1',
    note varchar(255),
    PRIMARY KEY (id),
    CONSTRAINT ordered_products_fk1 FOREIGN KEY (order_id) REFERENCES orders (id),
    CONSTRAINT ordered_products_fk2 FOREIGN KEY (product_id) REFERENCES products (id),
    CONSTRAINT uc_ordered_product UNIQUE (order_id, product_id)
);
