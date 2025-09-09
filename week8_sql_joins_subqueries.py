-- Create Customers table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    country VARCHAR(50)
);

-- Create Orders table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    amount DECIMAL(10,2),
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Insert sample data
INSERT INTO Customers (customer_id, customer_name, country) VALUES
(1, 'Ali', 'Iran'),
(2, 'Sara', 'Germany'),
(3, 'John', 'USA'),
(4, 'Maria', 'Canada');

INSERT INTO Orders (order_id, customer_id, amount, order_date) VALUES
(101, 1, 250.00, '2023-01-10'),
(102, 2, 450.00, '2023-01-15'),
(103, 1, 300.00, '2023-01-20'),
(104, 3, 150.00, '2023-02-01'),
(105, 4, 500.00, '2023-02-05');

---------------------------------------------------
-- 1. Show all orders with customer name
SELECT Orders.order_id, Customers.customer_name, Orders.amount
FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id;

---------------------------------------------------
-- 2. Show customers with at least one order above 300
SELECT DISTINCT c.customer_name
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
WHERE o.amount > 300;

---------------------------------------------------
-- 3. Subquery: show customers with total purchases greater than 400
SELECT customer_name
FROM Customers
WHERE customer_id IN (
    SELECT customer_id
    FROM Orders
    GROUP BY customer_id
    HAVING SUM(amount) > 400
);

---------------------------------------------------
-- 4. Show number of orders per customer
SELECT c.customer_name, COUNT(o.order_id) AS total_orders
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_name;