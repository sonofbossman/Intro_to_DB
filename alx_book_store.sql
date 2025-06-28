-- Books: Stores information about books available in the bookstore.
CREATE TABLE IF NOT EXISTS books(
  book_id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(130),
  author_id INT,
  price DOUBLE,
  publication_date DATE,
  FOREIGN KEY(author_id) REFERENCES authors(author_id)
)


-- Authors: Stores information about authors.
CREATE TABLE IF NOT EXISTS authors(
  author_id INT AUTO_INCREMENT PRIMARY KEY,
  author_name VARCHAR(130)
)


-- Customers: Stores information about customers.
CREATE TABLE IF NOT EXISTS customers(
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_name VARCHAR(215),
  email VARCHAR(215),
  address TEXT
)


-- Stores information about orders placed by customers.
CREATE TABLE IF NOT EXISTS orders(
  order_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
)


-- Stores information about the books included in each order.
CREATE TABLE IF NOT EXISTS order_details(
  orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
  order_id INT,
  book_id INT,
  quantity DOUBLE,
  FOREIGN KEY(order_id) REFERENCES orders(order_id),
  FOREIGN KEY(book_id) REFERENCES books(book_id),
)