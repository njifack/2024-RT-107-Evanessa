/* selects items from the orderdetails table 
and calculates the subtotal for each line item, 
and sorts the result based on the subtotal */

SELECT orderNumber, orderLineNumber,quantityOrdered * priceEach 
FROM orderdetails 
ORDER BY quantityOrdered * priceEach DESC
LIMIT 5;

-- Using aliases
SELECT orderNumber, orderLineNumber,(quantityOrdered * priceEach) AS Subtotal
FROM orderdetails 
ORDER BY Subtotal  DESC
LIMIT 5;

--  MySQL ORDER BY and NULL Values
SELECT    firstName, lastName, reportsTo
FROM    employees
ORDER BY reportsTo
LIMIT 5;

--  MySQL ORDER BY and NULL Values WITH DESC
SELECT    firstName, lastName, reportsTo
FROM    employees
ORDER BY reportsTo DESC
LIMIT 5;







