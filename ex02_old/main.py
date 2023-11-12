from category import Category
from product import Product
from client import Client
from order import Order
from order import Order
from socialnetwork import SocialNetwork


def main():

    category = Category(1, "Moveis", "Moveis de madeira")

    product = Product("Mesa", "Mesa madeira branca 200x80cm", "8/11/2023", True, category)

    client = Client("Gabrie", "Zomer", "Av. da ruas 1234", "5199999999", "gabriel.zomer@email.com", "Masculino")

    order = Order(100.0, "Aprovado", client)

    orderItem = OrderItem(10, 900, order, product)
    
    print(orderItem)

    socialnetwork = SocialNetwork("@gabrielzomer", "Instagram")



if __name__ == "__main__":
    main()