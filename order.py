from database import get_connection
from product import view_products
from datetime import date
def create_orders():
    customer_id=int(input("enter the id :"))
    connection=get_connection()
    cursor=connection.execute("select * from customer where customer_id=?",customer_id)
    row=cursor.fetchone()
    if row:
        print("Customer Verified")
        order_items=[]
        total_amount=0
        while True:
            view_products()
            product_id=int(input("enter the product_id :"))
            cursor=connection.execute("select * from products where product_id=?",product_id)
            row=cursor.fetchone()
            if row:
                product_id,name,price,stock=row
                print("Product_id: ",product_id)
                print("Product Selected: ",name)
                print("Price: ",price)
                print("stock: ",stock)
                quantities=int(input("Enter Quantity: "))
                if quantities>stock:
                    print("Insufficient stock")
                else:
                    subtotal=quantities*price
                    order_items.append((product_id,quantities,price))
                    total_amount+=subtotal
                    choice=input("Do you want to add another product(Y/N):")
                    if choice.upper()=='N':
                        print("Final Bill:",total_amount)
                        print(order_items)
                        order_id = int(input("Enter Order ID: "))
                        order_date = date.today()
                        connection.execute("INSERT INTO ORDERS VALUES(?,?,?,?)",order_id,customer_id,order_date,total_amount)
                        for item in order_items:
                            product_id,quantities,price=item
                            connection.execute("insert into order_items values(?,?,?,?)",order_id,product_id,quantities,price)
                            cursor=connection.execute("update products set quantity=quantity-? where product_id=?",quantities,product_id)
                            print("Products updated:", cursor.rowcount)
                        connection.commit() 
                        print("Order placed successfully")   
                        break           
            else:
                print("Product not found")   
                connection.close()
                return
        connection.close()    
    else:
        print("Customer not found")   
        connection.close()
        return