from sqlalchemy import create_engine
import psycopg2
import pandas as pd

engine=create_engine("postgresql+psycopg2://postgres:pw1234@northwind_db:5432/northwind_db")

def insert_data(file, table):

    df = pd.read_csv(file, delimiter=';')

    try:
        df.to_sql(table, engine, if_exists='replace', index=False)
    # except:
    #     print('Some error has occurred.')
    finally:
        engine.dispose()

if __name__ == '__main__':

    ## Categories
    file = 'data/raw/categories.csv'
    table = 'categories'
    insert_data(file, table)

    # ### Customers
    file = 'data/raw/customers.csv'
    table = 'customers'
    insert_data(file, table)

    ### Employees
    file = 'data/raw/employees.csv'
    table = 'employees'
    insert_data(file, table)

    ### Order Details
    file = 'data/raw/orderdetails.csv'
    table = 'orderdetails'
    insert_data(file, table)

    ### Order
    file = 'data/raw/orders.csv'
    table = 'orders'
    insert_data(file, table)

    ### Products
    file = 'data/raw/products.csv'
    table = 'products'
    insert_data(file, table)

    ### Shippers
    file = 'data/raw/shippers.csv'
    table = 'shippers'
    insert_data(file, table)

    ### Suppliers
    file = 'data/raw/suppliers.csv'
    table = 'suppliers'
    insert_data(file, table)