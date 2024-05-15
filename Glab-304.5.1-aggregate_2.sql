-- using MOD() function
select orderNumber, sum(quantityOrdered) as QTy,
if(mod(sum(quantityOrdered),2),'odd','even') as oddOrEeven
from orderdetails
group by orderNumber
order by orderNumber;


