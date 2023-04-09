USE mystore;

-- Top 5 customers with highest profits
SELECT ROUND(100 * SUM(profit) / (SELECT SUM(profit) from sale)) as percent_of_total_profits, ROUND(SUM(profit)) as expenditure, first_name, last_name
	FROM sale s
    JOIN customer c
		on s.customer_id = c.id
    GROUP BY customer_id
    ORDER BY percent_of_total_profits DESC
    LIMIT 5;
    
 -- Top 5 customers with highest amount of orders
SELECT ROUND(COUNT(*)) as total_orders, first_name, last_name
	FROM sale s
    JOIN customer c
		on s.customer_id = c.id
    GROUP BY customer_id
    ORDER BY total_orders DESC
    LIMIT 5;