import os
class Product:
    def __init__(self, pcode, pro_name, quantity, saled, price):
        self.pcode = pcode
        self.pro_name = pro_name
        self.quantity = quantity
        self.saled = saled
        self.price = price

    def __str__(self):
        return f"{self.pcode}\t{self.pro_name}\t{self.quantity}\t{self.saled}\t{self.price}"


class Node:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None



class BST:

    def __init__(self):
        self.root = None
        self.filename = "data.txt"

    def is_pcode_unique(self, pcode):
        return self._is_pcode_unique_helper(self.root, pcode)

    def _is_pcode_unique_helper(self, node, pcode):
        if node is None:
            return True

        if pcode == node.product.pcode:
            return False

        if pcode < node.product.pcode:
            return self._is_pcode_unique_helper(node.left, pcode)
        else:
            return self._is_pcode_unique_helper(node.right, pcode)

    def load_data_from_file(self, filename):
        file_path = os.path.join(os.path.dirname(__file__), filename)

        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                for line in lines[1:]:
                    data = line.strip().split()
                    if len(data) < 5:
                        print(f"Invalid data format: {line.strip()}. Skipped insertion.")
                        continue
                    pcode = data[0]
                    pro_name = data[1]
                    quantity = int(data[2])
                    saled = int(data[3])
                    price = float(data[4])
                    
                    if self.is_pcode_unique(pcode):
                        product = Product(pcode, pro_name, quantity, saled, price)
                        self.insert(product)
                    else:
                        print(f"Duplicate product code: {pcode}. Skipped insertion.")
                        
                print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")


    def display_data_from_file(self):
        filename = "data.txt"
        file_path = os.path.join(os.path.dirname(__file__), filename)

        try:
            with open(file_path, "r") as file:
                print("{:<8} | {:<12} | {:<12} | {:<6} | {:<8}".format("pcode", "pro_name", "quantity", "saled", "price"))
                print("-" * 60)
                lines = file.readlines()
                for line in lines[1:]:
                    data = line.strip().split()
                    if len(data) >= 5:
                        pcode = data[0]
                        pro_name = data[1]
                        quantity = data[2]
                        saled = data[3]
                        price = data[4]
                        print("{:<8} | {:<12} | {:<12} | {:<6} | {:<8}".format(pcode, pro_name, quantity, saled, price))
        except FileNotFoundError:
            print(f"File '{filename}' not found.")




    def input_and_insert_data(self):
        num_products = int(input("Enter the number of products: "))
        for _ in range(num_products):
            pcode = input("Enter product code: ")
            if not self.is_pcode_unique(pcode):
                print("Product pcode already exists. Please enter a unique product pcode.")
                continue

            pro_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            saled = int(input("Enter saled: "))
            price = float(input("Enter price: "))
            product = Product(pcode, pro_name, quantity, saled, price)
            self.insert(product)
            self.append_to_file(product)
            print("Product inserted successfully.")



    def insert(self, product):
        if self.root is None:
            self.root = Node(product)
        else:
            self._insert_rec(self.root, product)

    def _insert_rec(self, node, product):
        if product.pcode < node.product.pcode:
            if node.left is None:
                node.left = Node(product)
            else:
                self._insert_rec(node.left, product)
        elif product.pcode > node.product.pcode:
            if node.right is None:
                node.right = Node(product)
            else:
                self._insert_rec(node.right, product)
        else:
            return False
    def sort_data_file(self):
        filename = "data.txt"
        file_path = os.path.join(os.path.dirname(__file__), filename)
        sorted_data = []
        self._inorder_traversal(self.root, sorted_data)

        with open(file_path, "w") as file:
            file.write("pcode\t| pro_name\t| quantity\t| saled\t| price\n")
            file.write("------------------------------------------\n")
            for product in sorted_data:
                file.write(str(product) + "\n")

    def append_to_file(self, product):
        filename = "data.txt"
        file_path = os.path.join(os.path.dirname(__file__), filename)

        with open(file_path, "a") as file:
            file.write(str(product) + "\n")


    def in_order_traversal(self):
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, root):
        if root is not None:
            self._in_order_traversal(root.left)
            print(f"Product Code: {root.product.pcode}\tProduct Name: {root.product.pro_name}\tQuantity: {root.product.quantity}\tSaled: {root.product.saled}\tPrice: {root.product.price}")
            self._in_order_traversal(root.right)

    def breadth_first_traversal(self):
        if self.root is None:
            print("BST is empty.")
            return

        queue = [self.root]

        while queue:
            node = queue.pop(0)
            pcode = node.product.pcode
            pro_name = node.product.pro_name
            quantity = str(node.product.quantity)
            saled = str(node.product.saled)
            price = str(node.product.price)

            row = f"Product Code: {pcode:<8s} Product Name: {pro_name:<10s} Quantity: {quantity:<6s} Saled: {saled:<6s} Price: {price:<6s}"
            print(row)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def search_by_pcode(self, pcode):
        product = self._search_by_pcode(self.root, pcode)
        if product is not None:
            print(f"Product Code: {product.pcode}")
            print(f"Product Name: {product.pro_name}")
            print(f"Quantity: {product.quantity}")
            print(f"Saled: {product.saled}")
            print(f"Price: {product.price}")
        else:
            print("Product does not exist.")

    def _search_by_pcode(self, root, pcode):
        if root is None or root.product.pcode == pcode:
            return root.product
        if pcode < root.product.pcode:
            return self._search_by_pcode(root.left, pcode)
        return self._search_by_pcode(root.right, pcode)

    def delete_by_pcode(self, pcode):
        self.root = self._delete_by_pcode(self.root, pcode)
        self.save_data_to_file(pcode)  # Ghi lại dữ liệu sau khi xóa

    def _delete_by_pcode(self, root, pcode):
        if root is None:
            return root
        if pcode < root.product.pcode:
            root.left = self._delete_by_pcode(root.left, pcode)
        elif pcode > root.product.pcode:
            root.right = self._delete_by_pcode(root.right, pcode)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self._find_min(root.right)
            root.product.pcode = temp.product.pcode
            root.product.pro_name = temp.product.pro_name
            root.product.quantity = temp.product.quantity
            root.product.saled = temp.product.saled
            root.product.price = temp.product.price
            root.right = self._delete_by_pcode(root.right, temp.product.pcode)
        return root

    def save_data_to_file(self, deleted_pcode=None):
        filename = "data.txt"
        file_path = os.path.join(os.path.dirname(__file__), filename)

        with open(file_path, "r") as file:
            lines = file.readlines()

        with open(file_path, "w") as file:
            for line in lines:
                data = line.strip().split()
                if len(data) >= 1 and data[0] != deleted_pcode:
                    file.write(line)


    def _find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def in_order_traversal_to_file(self):
        filename = "data.txt"
        data_list = self._in_order_traversal_to_list(self.root)  # Duyệt cây và lưu dữ liệu vào danh sách
        with open(filename, 'w') as file:
            for data in data_list:
                file.write(data + "\n")

    def _in_order_traversal_to_list(self, root):
        data_list = []
        if root is not None:
            data_list.extend(self._in_order_traversal_to_list(root.left))
            data_list.append(f"{root.product.pcode:<10} {root.product.pro_name:<10} {root.product.quantity:<10} {root.product.saled:<10} {root.product.price:<10}")
            data_list.extend(self._in_order_traversal_to_list(root.right))
        return data_list



    def simply_balance(self):
        nodes = []
        self._store_nodes_inorder(self.root, nodes)
        n = len(nodes)
        return self._build_balanced_tree(nodes, 0, n - 1)

    def _store_nodes_inorder(self, root, nodes):
        if root is not None:
            self._store_nodes_inorder(root.left, nodes)
            nodes.append(root)
            self._store_nodes_inorder(root.right, nodes)

    def _build_balanced_tree(self, nodes, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = nodes[mid]
        node.left = self._build_balanced_tree(nodes, start, mid - 1)
        node.right = self._build_balanced_tree(nodes, mid + 1, end)
        return node

    def count_products(self):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
            return len(lines)
        except FileNotFoundError:
            print("File not found.")