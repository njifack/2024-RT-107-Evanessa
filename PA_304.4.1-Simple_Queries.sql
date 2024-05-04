 -- Display the name, product line, and buy price of all products
 
SELECT productName ,productLine,buyPrice
FROM products
ORDER BY buyPrice DESC;

-- Display the first name, last name, and city name of all customers from Germany

SELECT contactLastName, contactFirstName, city 
FROM customers
ORDER BY contactLastName ASC;

-- Display each of the unique values of the status field in the orders table

SELECT DISTINCT(status)
FROM orders
ORDER BY status;

-- Display all fields from the payments table for payments made on or after January 1, 2005

SELECT *
FROM payments
WHERE paymentDate = '2005-01-01' OR paymentDate > '2005-01-01'
ORDER BY paymentDate DESC;

/* Display the last Name, first Name, email address, 
and job title of all employees working out 
of the San Francisco office */

SELECT  employees.lastName, employees.firstName,employees.email, employees.jobTitle, offices.city
FROM employees
RIGHT JOIN offices ON offices.officeCode=employees.officeCode
WHERE city = 'San Francisco'
ORDER BY employees.lastName;


-- Display the name, product line, scale, and vendor of all of the car products – both classic and vintage.
SELECT productName, productLine, productScale ,productVendor productDescription
FROM products
WHERE productLine = 'Classic Cars' OR  productLine = 'Vintage Cars'
ORDER BY productLine DESC;





















 