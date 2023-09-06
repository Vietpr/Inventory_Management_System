import os
from product import Product, Node, BST
from customer import Customer, CustomerList
from order import Order, OrderList

def display_menu():
    print("Sales and Inventory Management System (SIMS) Menu:")
    print("1 Products")
    print("2 Customer list")
    print("3 Order list")
    print("0. Exit")

# Khởi tạo các đối tượng
bst = BST()
customer_list = CustomerList()
order_list = OrderList()

# Vòng lặp chính của chương trình
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            print("Products:")
            print("1.1 Load data from file")
            print("1.2 Input & insert data")
            print("1.3 In-order traversal")
            print("1.4 Breadth-first traversal")
            print("1.5 In-order traversal to file")
            print("1.6 Search by pcode")
            print("1.7 Delete by pcode by copying")
            print("1.8 Simply balancing")
            print("1.9 Count number of products")
            sub_choice = input("Enter your choice (Enter 0 to go back to main menu): ")

            if sub_choice == "1.1":
                bst.load_data_from_file("data.txt")  # Load dữ liệu từ file
                bst.display_data_from_file()  # In ra dữ liệu từ file

            elif sub_choice == "1.2":
                bst.input_and_insert_data()
            elif sub_choice == "1.3":
                bst.in_order_traversal()
            elif sub_choice == "1.4":
                bst.breadth_first_traversal()
            elif sub_choice == "1.5":
                bst.in_order_traversal_to_file()
            elif sub_choice == "1.6":
                pcode = input("Enter the product code: ")
                bst.search_by_pcode(pcode)
            elif sub_choice == "1.7":
                pcode = input("Enter the product code: ")
                bst.delete_by_pcode(pcode)
            elif sub_choice == "1.8":
                bst.simply_balance()
            elif sub_choice == "1.9":
                count = bst.count_products()
                print(f"Number of products: {count}")
            elif sub_choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == "2":
        while True:
            # Sub-menu for Customer list
            print("Customer list:")
            print("2.1 Load data from file")
            print("2.2 Input & add to the end")
            print("2.3 Display data")
            print("2.4 Save customer list to file")
            print("2.5 Search by ccode")
            print("2.6 Delete by ccode")
            sub_choice = input("Enter your choice (Enter 0 to go back to main menu): ")

            if sub_choice == "2.1":
                customer_list.load_data_from_file()
            elif sub_choice == "2.2":
                ccode = input("Enter customer code: ")
                cus_name = input("Enter customer name: ")
                phone = input("Enter phone number: ")
                customer = Customer(ccode, cus_name, phone)
                customer_list.append(customer)
            elif sub_choice == "2.3":
                customer_list.display()
            elif sub_choice == "2.4":
                customer_list.save_to_file()
            elif sub_choice == "2.5":
                ccode = input("Enter the customer code: ")
                customer_list.search_by_ccode(ccode)
            elif sub_choice == "2.6":
                ccode = input("Enter the customer code: ")
                customer_list.delete_by_ccode(ccode)
            elif sub_choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")


    elif choice == "3":
        while True:
            # Sub-menu for Order list
            print("Order list:")
            print("3.1 Input order data")
            print("3.2 Display orders")
            print("3.3 Sort orders by product code")
            print("3.4 Sort orders by customer code")
            sub_choice = input("Enter your choice (Enter 0 to go back to main menu): ")

            if sub_choice == "3.1":
                order_list.input_order_data()
            elif sub_choice == "3.2":
                order_list.display()
            elif sub_choice == "3.3":
                order_list.sort_by_pcode()
                order_list.display()
            elif sub_choice == "3.4":
                order_list.sort_by_ccode()
                order_list.display()
            elif sub_choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")


