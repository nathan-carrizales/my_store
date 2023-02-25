USE mystore;

-- Shipping preferences
SELECT ship_mode, ROUND(100*COUNT(ship_mode) / (SELECT COUNT(*) FROM sale)) AS percent, COUNT(ship_mode) AS orders
	FROM sale 
    GROUP BY ship_mode 
    ORDER BY orders 
    DESC LIMIT 5;

-- Order priority preferences
SELECT order_priority, ROUND(100*(COUNT(ship_mode)/ (SELECT COUNT(*) FROM sale))) as percent, COUNT(ship_mode) as orders
	FROM sale
    GROUP BY order_priority 
    ORDER BY orders DESC 
    LIMIT 5;

-- Top 5 countries with most most sales by volume
SELECT country, ROUND(100*COUNT(country)/(SELECT COUNT(*) FROM sale)) AS percent, COUNT(country) as total_sales 
	FROM sale
    GROUP BY country
    ORDER BY percent
    DESC LIMIT 5;

-- Top 5 countries with most profits
SELECT country, ROUND(100*ROUND(SUM(profit))/(SELECT SUM(profit) FROM sale)) AS percent, ROUND(SUM(profit)) AS total_profits
	FROM sale 
    GROUP BY country 
    ORDER BY percent 
    DESC LIMIT 5;

-- Top 5 dates with the highest profits
SELECT ROUND(100*SUM(profit)/(SELECT SUM(profit) FROM sale)) total_profit, order_date
	FROM sale 
    GROUP BY order_date
    ORDER BY total_profit DESC
    LIMIT 5;

-- Top 5 cities with the highest profits
SELECT city, MAX(country) as country, ROUND(100*COUNT(*)/(SELECT COUNT(*) FROM SALE)) AS percent,COUNT(*) AS total_orders
	FROM SALE
    GROUP BY city
    ORDER BY total_orders DESC
    LIMIT 5;

-- Sales by month of the year
SELECT MONTHNAME(order_date) AS month_name, ROUND(100*(COUNT(MONTHNAME(order_date))/ (SELECT COUNT(*) FROM sale))) as percent, COUNT(MONTHNAME(order_date)) AS total_sales
	from sale 
    GROUP BY MONTHNAME(order_date) 
    ORDER BY total_sales DESC;