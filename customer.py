from database import get_connection
def view_customer():
    connection=get_connection()
    cursor=connection.execute("select * from customer")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    connection.close()   
def add_customer():
    customer_id=int(input("enter the cutomer_id :"))
    name=input("enter name of the cutomer : ")
    phone_no=input("enter the phonenumber of the cutomer:")
    connection=get_connection()
    cursor=connection.execute("insert into customer values(?,?,?)",customer_id,name,phone_no) 
    connection.commit() 
    print("cutomer added successfully")
    connection.close()
def search_customer():
    customer_id=int(input("enter the id :"))
    connection=get_connection()
    cursor=connection.execute("select * from customer where customer_id=?",customer_id)
    row=cursor.fetchone()
    if row:
        print(row)
    else:
        print("customer not found")   
    connection.close()
def  update_customer():
    customer_id=int(input("enter the id :"))
    connection=get_connection()
    cursor=connection.execute("select * from customer where customer_id=?",customer_id)
    row=cursor.fetchone()
    if row:
        print("enter the values to update")
        name=input("enter the name of the customer :")
        phone_number=input("enter phone number :")
        connection.execute("update customer set name=?,phone_number=? where customer_id=?",name,phone_number,customer_id)
        connection.commit()
        print("customer details  updated succesfully")   
    else:
        print("customer not found") 
    connection.close()