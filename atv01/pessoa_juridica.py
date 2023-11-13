from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, razao_social, data_abertura, pessoa_nome, pessoa_endereco):
        Pessoa.__init__(self, pessoa_nome, pessoa_endereco)
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data_abertura = data_abertura

# Usando a classe pessoa para herdar os itens.