"""
This script is meant to take in a csv of store data, and write it to a SQL database.
SQL database is expected to have 3 tables: 'customer', 'product', and 'sale'. The schema of each table can be found
in the file 'database_and_table_schema.sql'.
"""
import pandas as pd
import mysql.connector
import os
from mysql.connector import (connection)


SQL_PASSWORD = os.environ.get("SQL_PASSWORD")
SQL_DATABASE = os.environ.get("SQL_DATABASE")


def extract_customer_data(data: pd.DataFrame):
    """

    :param data: Pandas Dataframe that holds the entire data
    :return: a dataframe with the columns 'customer', 'id', 'customer_first_name', and 'customer_last_name'
    """

    customers = data[['Customer Name', 'Customer ID']].copy()

    customers.loc[:, 'first_name'] = customers.loc[:, 'Customer Name'].apply(lambda x: x.split(' ')[0])
    customers.loc[:, 'last_name'] = customers.loc[:, 'Customer Name'].apply(lambda x: x.split(' ')[1])
    customers.rename(columns={'Customer ID': 'customer_id'}, inplace=True)

    return customers[['first_name', 'last_name', 'customer_id']]


def extract_product_data(data: pd.DataFrame):
    """

    :param data: Pandas Dataframe that holds the entire data
    :return: a dataframe with the columns 'customer', 'id', 'customer_first_name', and 'customer_last_name'
    """

    products = data[['Product ID', 'Product Name', 'Category', 'Sub-Category']].copy()

    products.rename(
        columns={
            'Product ID': 'id',
            'Product Name': 'name',
            'Category': 'category',
            'Sub-Category': 'subcategory'
        },
        inplace=True
    )

    return products


def extract_sale_data(data: pd.DataFrame):
    """

    :param data: Pandas Dataframe that holds the entire data
    :return: a dataframe with the columns 'customer', 'id', 'customer_first_name', and 'customer_last_name'
    """

    sale = data[
        [
            'Order ID',
            'Order Date',
            'Ship Date',
            'Ship Mode',
            'Customer ID',
            'Segment',
            'City',
            'State',
            'Country',
            'Postal Code',
            'Market',
            'Region',
            'Product ID',
            'Sales',
            'Quantity',
            'Discount',
            'Profit',
            'Shipping Cost',
            'Order Priority'
        ]
    ].copy()

    sale.rename(
        columns={
            'Order ID': 'order_id',
            'Order Date': 'order_date',
            'Ship Date': 'ship_date',
            'Ship Mode': 'ship_mode',
            'Customer ID': 'customer_id',
            'Segment': 'segment',
            'City': 'city',
            'State': 'state',
            'Country': 'country',
            'Postal Code': 'postal_code',
            'Market': 'market',
            'Region': 'region',
            'Product ID': 'product_id',
            'Sales': 'sales',
            'Quantity': 'quantity',
            'Discount': 'discount',
            'Profit': 'profit',
            'Shipping Cost': 'shipping_cost',
            'Order Priority': 'order_priority'
        },
        inplace=True
    )

    sale['order_date'] = pd.to_datetime(sale['order_date'])
    sale['ship_date'] = pd.to_datetime(sale['ship_date'])

    return sale


def push_customer_data(my_sql_client: connection.MySQLConnection, customer_data: pd.DataFrame):

    my_cursor = my_sql_client.cursor()

    for _, row in customer_data.iterrows():

        first_name = row['first_name']
        last_name = row['last_name']
        index = row['customer_id']

        sql = f'INSERT INTO customer (id, first_name, last_name) VALUES ("{index}", "{first_name}", "{last_name}")'
        try:
            my_cursor.execute(sql)
        except Exception as E:
            if E.errno != 1062:
                raise E

    mydb.commit()

    print(my_cursor.rowcount, "record inserted.")


def push_sale_data(my_sql_client: connection.MySQLConnection, sale_data: pd.DataFrame):

    my_cursor = my_sql_client.cursor()

    for _, row in sale_data.iterrows():

        order_id = row['order_id']
        product_id = row['product_id']
        customer_id = row['customer_id']
        order_date = row['order_date']
        ship_date = row['ship_date']
        ship_mode = row['ship_mode']
        shipping_cost = row['shipping_cost']
        segment = row['segment']
        city = row['city']
        state = row['state']
        country = row['country']
        postal = row['postal_code']
        market = row['market']
        region = row['region']
        sales = row['sales']
        quantity = row['quantity']
        discount = row['discount']
        profit = row['profit']
        order_priority = row['order_priority']

        sql = f'INSERT INTO sale (' \
              f'order_id, product_id, customer_id, order_date, ship_date, ship_mode, shipping_cost, segment, city,' \
              f' state, country, postal_code, market, region, sales, quantity, discount, profit, order_priority' \
              f') VALUES ("{order_id}", "{product_id}", "{customer_id}", "{order_date}",  "{ship_date}", "{ship_mode}", ' \
              f' "{shipping_cost}", "{segment}", "{city}", "{state}", "{country}", "{postal}",' \
              f' "{market}", "{region}", "{sales}", "{quantity}", "{discount}", "{profit}", "{order_priority}")'

        try:
            my_cursor.execute(sql)
        except Exception as E:
            if E.errno != 1062:
                raise E

    mydb.commit()

    print(my_cursor.rowcount, "record inserted.")


def push_product_data(my_sql_client: connection.MySQLConnection, product_data: pd.DataFrame):

    my_cursor = my_sql_client.cursor()

    for _, row in product_data.iterrows():

        index = row['id']
        name = row['name'].replace('"', "'")
        category = row['category']
        subcategory = row['subcategory']

        sql = f'INSERT INTO product (id, product_name, category, sub_category) VALUES' \
              f' ("{index}", "{name}", "{category}", "{subcategory}")'

        try:
            my_cursor.execute(sql)
        except Exception as E:
            if E.errno != 1062:
                raise E

    mydb.commit()

    print(my_cursor.rowcount, "record(s) inserted.")


mydb = connection.MySQLConnection(
    host="localhost",
    user="root",
    port='3306',
    password=SQL_PASSWORD,
    database='mystore',
)

raw_data = pd.read_csv("/Users/nathan/Desktop/personal/my_store/Global_Superstore2.csv", encoding='unicode_escape')

customer_data_processed = extract_customer_data(data=raw_data)
push_customer_data(my_sql_client=mydb, customer_data=customer_data_processed)

product_data_processed = extract_product_data(data=raw_data)
push_product_data(my_sql_client=mydb, product_data=product_data_processed)


sale_data_processed = extract_sale_data(data= raw_data)
push_sale_data(my_sql_client=mydb, sale_data=sale_data_processed)
print()
