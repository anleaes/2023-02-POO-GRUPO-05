from pessoa import Pessoa

class PessoaFisica:
    def __init__(self, cpf, data_nascimento, pessoa_nome, pessoa_endereco):
        self.nome = pessoa_nome
        self.endereco = pessoa_endereco
        self.cpf = cpf
        self.data_nascimento = data_nascimento

# Usando a classe pessoa para herdar os itens.