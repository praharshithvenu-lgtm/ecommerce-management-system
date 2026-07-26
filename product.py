from database import get_connection
def view_products():
    connection=get_connection()
    cursor=connection.execute("select * from products")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    connection.close()   
def add_product():
    product_id=int(input("enter the id :"))
    name=input("enter name of the product : ")
    price=float(input("enter the price of the product :")) 
    quantity=int(input("enter how many items :"))
    connection=get_connection()
    cursor=connection.execute("insert into products values(?,?,?,?)",product_id,name,price,quantity) 
    connection.commit() 
    print("Product added successfully")
    connection.close()
def search_product():
    product_id=int(input("enter the id :"))
    connection=get_connection()
    cursor=connection.execute("select * from products where product_id=?",product_id)
    row=cursor.fetchone()
    if row:
        print(row)
    else:
        print("Product not found")   
    connection.close()
def  update_product():
    product_id=int(input("enter the id :"))
    connection=get_connection()
    cursor=connection.execute("select * from products where product_id=?",product_id)
    row=cursor.fetchone()
    if row:
        print("enter the values to update")
        price=float(input("enter the price of the product :")) 
        quantity=int(input("enter how many items :"))
        connection.execute("update products set price=?,quantity=? where product_id=?",price,quantity,product_id)
        connection.commit()
        print("product updated succesfully")   
    else:
        print("Product not found") 
    connection.close()      


    
