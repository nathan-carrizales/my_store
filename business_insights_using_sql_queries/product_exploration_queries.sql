USE mystore;

-- Total products by category
SELECT ROUND(100*COUNT(*)/ (SELECT COUNT(*) FROM product)) as percent, category
	FROM product
    GROUP BY category
    ORDER BY percent DESC;
    
-- Total products by subcategory
SELECT ROUND(100*(COUNT(*)/ (SELECT COUNT(*) FROM product))) as percent, COUNT(*) as raw_count, sub_category, MAX(category) AS category
	FROM product
    GROUP BY sub_category
    ORDER BY raw_count DESC
    LIMIT 10;
    
-- Top 5 Most requested products
SELECT COUNT(*) number_of_orders, product_name, category, sub_category
	from SALE s
    JOIN PRODUCT p
		on s.product_id = p.id
    GROUP BY product_id
    ORDER BY number_of_orders DESC;
    
    
-- Top 5 most profitable sub categories
SELECT ROUND(SUM(profit)) as total_profit, ROUND(100*SUM(profit)/ (SELECT SUM(profit) FROM sale)) as percent, sub_category
	FROM sale 
	JOIN product
		ON sale.product_id=product.id 
	GROUP BY sub_category 
	ORDER BY total_profit DESC 
    LIMIT 5;
