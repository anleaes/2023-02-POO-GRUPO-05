class OrderItem:
    def __init__(self, quantity, unitary_price, order, product):
        self.quantity = quantity
        self.unitary_price = unitary_price
        self.order = order
        self.product = product

class Order:
    def __init__(self, total_price, status, client):
        self.total_price = total_price
        self.status = status
        self.client = client