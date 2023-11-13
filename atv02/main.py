from category import Category
from product import Product
from order_item import OrderItem
from order import Order
from client import Client
from client_socialnetwork import ClientSocialnetwork
from socialnetwork import Socialnetwork

# Criando instâncias de Category
category = Category(1, "Eletronicos", "Componentes Eletronicos")
product = Product("Laptop", "Laptop Gamer", "13/11/2023", True, category)
order_item = OrderItem(2, 1200.00, None, product)
client = Client("Anakin", "Skywalker", "Mos Espa", "(51)3333.3333", "anakin@notvader.com", "Not-a-Droid")
order = Order(3500.00, "Aguardando", client)
order_item.order = order
social_network = Socialnetwork("Twitter","just tweet it")
client_social_network = ClientSocialnetwork(client, social_network)

########################################################################
print("Category:")
print("Código de Identificação da Categoria:", category.id)
print("Nome da Categoria:", category.name)
print("Descrição da Categoria:", category.description)

print("\nProduto:")
print("Nome do Produto:", product.name)
print("Descrição do Produto:", product.description)
print("Data de Fabricaçao:", product.date_fabrication)
print("Está ativo:", product.is_active)
print("Categoria:", product.category.name)

print("\nPedido:")
print("Cliente:", order_item.order.client.first_name)
print("Produto:", order_item.product.name)
print("Quantidde:", order_item.quantity)
print("Valor Unitário: R$", order_item.unitary_price)
print("Valor total do Pedido: R$", order_item.order.total_price)
print("Status:", order_item.order.status)

print("\nCliente:")
print("Nome:", client.first_name)
print("Sobrenome:", client.last_name)
print("Endereço:", client.address)
print("Celular:", client.cell_phone)
print("Email:", client.email)
print("Genero:", client.gender)

print("\nResumo:")
print("Cliente:", order.client.first_name)
print("Valor Total: R$", order.total_price)
print("Situação:", order.status)

print("\nRede Social do Cliente:")
print("Cliente:", client_social_network.client.first_name)
print("Rede Social:", client_social_network.socialnetwork.name)