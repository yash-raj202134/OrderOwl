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


# Function to get the next available order_id
def get_next_order_id():
    """
    Retrieve the next available order ID from the database.
    
    Returns:
    - int: The next available order ID.
    """
    cursor = cnx.cursor()

    # Executing the SQL query to get the next available order_id
    query = "SELECT MAX(order_id) FROM orders"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()[0]

    # Closing the cursor
    cursor.close()

    # Returning the next available order_id
    if result is None:
        return 1
    else:
        return result + 1

# Function to fetch the order status from the order_tracking table
def get_order_status(order_id):
    """
    Retrieve the order status for a given order ID from the order_tracking table in the database.
    
    Parameters:
    - order_id (int): The ID of the order.
    
    Returns:
    - str or None: The order status if found, otherwise None.
    """
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = f"SELECT status FROM order_tracking WHERE order_id = {order_id}"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # Returning the order status
    if result:
        return result[0]
    else:
        return None


if __name__ == "__main__":
    
    # Example usage of get_total_order_price function
    # print(get_total_order_price(56))
    
    # Example usage of insert_order_item function
    # insert_order_item('Samosa', 3, 99)
    # insert_order_item('Pav Bhaji', 1, 99)
    
    # Example usage of insert_order_tracking function
    # insert_order_tracking(99, "in progress")
    
    # Example usage of get_next_order_id function
    print(get_next_order_id())