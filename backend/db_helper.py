# Database helper functions

import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="yash's_eatery"
)

# Function to call the MySQL stored procedure and insert an order item
def insert_order_item(food_item, quantity, order_id):
    """
    Insert an order item into the database using a MySQL stored procedure.
    
    Parameters:
    - food_item (str): The name of the food item to be inserted.
    - quantity (int): The quantity of the food item.
    - order_id (int): The ID of the order to which the item belongs.
    
    Returns:
    - int: 1 if the order item was inserted successfully, -1 if an error occurred.
    """
    try:
        cursor = cnx.cursor()

        # Calling the stored procedure
        cursor.callproc('insert_order_item', (food_item, quantity, order_id))

        # Committing the changes
        cnx.commit()

        # Closing the cursor
        cursor.close()

        print("Order item inserted successfully!")

        return 1

    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")

        # Rollback changes if necessary
        cnx.rollback()

        return -1

    except Exception as e:
        print(f"An error occurred: {e}")
        # Rollback changes if necessary
        cnx.rollback()

        return -1


# Function to insert a record into the order_tracking table
def insert_order_tracking(order_id, status):
    """
    Insert a record into the order_tracking table to track the status of an order.
    
    Parameters:
    - order_id (int): The ID of the order to track.
    - status (str): The status of the order.
    
    Returns:
    - None
    """
    cursor = cnx.cursor()

    # Inserting the record into the order_tracking table
    insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
    cursor.execute(insert_query, (order_id, status))

    # Committing the changes
    cnx.commit()

    # Closing the cursor
    cursor.close()



# Function to get the total order price for a given order ID
def get_total_order_price(order_id):
    """
    Retrieve the total order price for a given order ID from the database.
    
    Parameters:
    - order_id (int): The ID of the order.
    
    Returns:
    - float: The total order price.
    """
    cursor = cnx.cursor()

    # Executing the SQL query to get the total order price
    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()[0]

    # Closing the cursor
    cursor.close()

    return result
