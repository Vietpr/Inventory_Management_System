import os
class Customer:
    def __init__(self, ccode, cus_name, phone):
        self.ccode = ccode
        self.cus_name = cus_name
        self.phone = phone
        self.next = None

class CustomerList:
    def __init__(self):
        self.head = None
        self.filename = "customer.txt"
        self.ccode_set = set()

    def load_data_from_file(self):
        file_path = os.path.join(os.path.dirname(__file__), self.filename)

        customer_list = []  # Danh sách khách hàng từ dữ liệu file

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split("\t")
                    if len(data) == 3:
                        customer = Customer(data[0], data[1], data[2])
                        customer_list.append(customer)  # Thêm khách hàng vào danh sách

            print("Data loaded successfully.")

            # In thông tin khách hàng từ danh sách
            if len(customer_list) == 0:
                print("No customer data.")
            else:
                for customer in customer_list:
                    print(f"Customer Code: {customer.ccode}")
                    print(f"Customer Name: {customer.cus_name}")
                    print(f"Phone: {customer.phone}")
                    print("-----------------------")
        except FileNotFoundError:
            print("File not found.")

    def append(self, customer):
        if customer.ccode in self.ccode_set:
            print("Customer code already exists. Unable to add customer.")
            return

        try:
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(f"{customer.ccode}\t{customer.cus_name}\t{customer.phone}\n")
        except FileNotFoundError:
            print("File not found.")

        self.ccode_set.add(customer.ccode)  # Thêm ccode vào set

        print("Customer added successfully.")

    def display(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
                if not lines:
                    print("No customer data.")
                else:
                    for line in lines:
                        data = line.strip().split("\t")
                        if len(data) == 3:
                            ccode = data[0]
                            cus_name = data[1]
                            phone = data[2]
                            print(f"Customer Code: {ccode}")
                            print(f"Customer Name: {cus_name}")
                            print(f"Phone: {phone}")
                            print("-----------------------")
        except FileNotFoundError:
            print("File not found.")

    def save_to_file(self):
        file_path = os.path.join(os.path.dirname(__file__), self.filename)

        try:
            with open(file_path, "a", encoding="utf-8") as file:
                current = self.head
                while current:
                    file.write(f"{current.ccode}\t{current.cus_name}\t{current.phone}\n")
                    current = current.next
            print("Customer list saved to file successfully.")
        except FileNotFoundError:
            print("File not found.")

    def search_by_ccode(self, ccode):
        file_path = os.path.join(os.path.dirname(__file__), self.filename)
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split("\t")
                    if len(data) == 3 and data[0] == ccode:
                        cus_name = data[1]
                        phone = data[2]
                        print(f"Customer Code: {ccode}")
                        print(f"Customer Name: {cus_name}")
                        print(f"Phone: {phone}")
                        return
                print("Customer does not exist.")
        except FileNotFoundError:
            print("File not found.")

    def delete_by_ccode(self, ccode):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
            with open(self.filename, "w", encoding="utf-8") as file:
                deleted = False
                for line in lines:
                    data = line.strip().split("\t")
                    if len(data) == 3 and data[0] != ccode:
                        file.write(line)
                    else:
                        deleted = True
                if deleted:
                    print("Customer deleted.")
                else:
                    print("Customer does not exist.")
        except FileNotFoundError:
            print("File not found.")
