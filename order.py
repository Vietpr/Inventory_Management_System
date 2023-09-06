class Order:
    def __init__(self, pcode, ccode, quantity):
        self.pcode = str(pcode)
        self.ccode = str(ccode)
        self.quantity = quantity

class OrderList:
    def __init__(self):
        self.orders = []
    
    def input_order_data(self):
        num_orders = int(input("Enter the number of orders: "))
        for _ in range(num_orders):
            pcode = input("Enter product code: ")
            ccode = input("Enter customer code: ")
            quantity = int(input("Enter quantity: "))
            order = Order(pcode, ccode, quantity)
            self.orders.append(order)

    def display(self):
        if not self.orders:
            print("No orders to display.")
        else:
            for order in self.orders:
                print(f"Product Code: {order.pcode}")
                print(f"Customer Code: {order.ccode}")
                print(f"Quantity: {order.quantity}")
                print("--------------------")

    def sort_by_pcode(self):
        self.orders.sort(key=lambda x: x.pcode)

    def sort_by_ccode(self):
        self.orders.sort(key=lambda x: x.ccode)
