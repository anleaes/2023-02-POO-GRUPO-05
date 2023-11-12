Atividade:
- Crie um projeto de pedidos a partir do diagrama de classes, 
- Separe a atividade entre os participantes 
- Crie branchs para cada etapa do projeto e colaborador. 
- Crie uma classe main para instanciar os objetos e executar o programa.

#####################################################################

Diagrama:

@startuml Diagrama de Classes Pedidos

class Category{
    id
    name
    description
}

class Product{
    name
    description  
    date_fabrication  
    is_active  
    category: Category
}

class OrderItem{
    quantity  
    unitary_price  
    order: Order
    product: Product
}

class Order{
    total_price  
    status  
    client: Client
}

class Client{
    first_name  
    last_name  
    address  
    cell_phone  
    email  
    gender  
}

class ClientSocialnetwork{
    client: Client
    socialnetwork: Socialnetwork
}

class Socialnetwork{
    name  
    description
}

Product o-- Category
Client --o ClientSocialnetwork
Socialnetwork --o  ClientSocialnetwork
Client --o Order
Order --o OrderItem
Product --o OrderItem

@enduml

#####################################################################

Classes a serem criadas e seus responsáveis:
    Category (id, name, description) Gabriel
    Product (name, description, date_fabrication, is_active, category) Gabriel 
    OrderItem (quantity, unitary_price, order, product ) Raphael
    Order (total_price, status, client ) Raphael
    Client (first_name, last_name, address, cell_phone, email, gender) Ricardo
    ClientSocialnetwork (client, socialnetwork) Ricardo
    Socialnetwork (name, description) Gabriel
    **MAIN EM CONJUNTO

#####################################################################
