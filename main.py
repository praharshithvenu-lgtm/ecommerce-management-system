
from product import view_products,add_product,search_product,update_product
from customer import view_customer,add_customer,search_customer,update_customer
from order import create_orders
while True:
    print("===== E-COMMERCE MANAGEMENT SYSTEM =====")
    print("1. Product Management")
    print("2. Customer Management")
    print("3. Order Management")
    print("4.Exit")
    choice=int(input("Enter you choice :" ))
    if choice==1:
        while True:
            print("----------------------MENU-----------------------")
            print("1.View products")
            print("2.Add Product")
            print("3.Search product")
            print("4.Update Product")
            print("5.Back")
            choice=int(input("Enter your choice : "))
            if choice==1:
                view_products()
            elif choice==2:
                add_product()
            elif choice==3:
                search_product()
            elif choice==4:
                update_product()
            elif choice==5:
                break
            else:
                print("Invalid choice")
    elif choice==2:
        while True:
            print("----------------------MENU-----------------------")
            print("1.View customer")
            print("2.Add customer")
            print("3.Search customer")
            print("4.Update customer")
            print("5.Back")
            choice=int(input("Enter your choice : "))
            if choice==1:
                view_customer()
            elif choice==2:
                add_customer()
            elif choice==3:
                search_customer()
            elif choice==4:
                update_customer()
            elif choice==5:
                break
            else:
                print("Invalid choice")
    elif choice==3:
        create_orders()         
    elif choice==4:
        print("Exiting Application")
        break
    else:
        print("Invalid choice")     
