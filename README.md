My Store
-------------
# Overview:
This repository aims at the folowing:
1) building a database in MySQL using a CSV of publicly available sale data found at Kaggle.
2) gaining analytic insight into the data using SQL queries.
3) writing a report in Tableau that visualizes some KPI's. 

Additionally, Python is used to aid data cleaning and insert data into the database.


# The Data:
The csv data ("global_superstore.csv") is available to download courtesey of [Apoorva Mahalingappa](https://www.kaggle.com/apoorvaappz) on Kaggle through this [link](https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset). This dataset contains ~50,000 individual sales, where each sale contains information about the product, customer, location, profit, and quantity among other things.


# The Database:
Three tables were choosen based off of the principles of normalization: `customer`, `sale`, `product`. Together, they make up the database (schema) called `mystore`. Here is a entity-relationship model visualizing the structure of the database:

![Alt text](/er_diagram.jpg "Optional title")

# Data Cleaning via Python:
Python is used to 1) clean the data using *pandas* and 2) insert the data using the *mysql* library. In order to run it, it is advised to create a virtual environment.

# SQL Queries:
Queries written in SQL have been written to understand the data. They have also been placed in one of three files depending on the context of the query. Here is an example of a query that retrieves the 5 countries with the highest profits:
```
SELECT city, MAX(country) as country, ROUND(100*COUNT(*)/(SELECT COUNT(*) FROM SALE)) AS percent,COUNT(*) AS total_orders
  FROM SALE
  GROUP BY city
  ORDER BY total_orders DESC
  LIMIT 5;
```

# Tableau:
Placeholder
