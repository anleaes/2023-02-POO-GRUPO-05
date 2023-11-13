from pessoa import Pessoa
from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica
from aluno import Aluno
from curso import Curso
from inscricao import Inscricao
from autor import Autor
from livro import Livro

if __name__ == "__main__":
    pessoa1 = Pessoa("Fulano de Tal", "Casa da Mãe Joana")
    pessoa_fisica1 = PessoaFisica("12345678900", "12/11/2023", pessoa1.nome, pessoa1.endereco)
    pessoa_juridica = PessoaJuridica("15542114/0001-85", "Empresa Teste", "12/11/2023", "Nome Empresa", "Endereco Empresa")
    aluno1 = Aluno("2021001", pessoa_fisica1)
    autor1 = Autor("Churrasqueiro Mestre")
    curso1 = Curso("Curso de Churrasco", 40, 100.00)
    livro1 = Livro("Rei do Churrasco", autor1)
    inscricao1 = Inscricao(aluno1, curso1)

    print(f"\nMatricula: {aluno1.numero_matricula}") 
    print(f"Nome: {aluno1.pessoa_fisica.nome}")
    print(f"CPF: {pessoa_fisica1.cpf}")
    print(f"Data de Nascimento: {pessoa_fisica1.data_nascimento}")
    print(f"Endereço: {aluno1.pessoa_fisica.endereco}")
    print(f"Curso: {curso1.nome}, Carga Horária: {curso1.carga_horaria} horas, Preço: R${curso1.preco}")
    print(f"Livro: {livro1.titulo}, Autor: {livro1.autor.nome}")   
    print(f"Autor: {autor1.nome}")
    print(f"Inscrição: Aluno: {inscricao1.aluno.numero_matricula}, Curso: {inscricao1.curso.nome}")
    print(f"CNPJ: {pessoa_juridica.cnpj}")
    print(f"Razão Social: {pessoa_juridica.razao_social}")
    print(f"Data de Abertura: {pessoa_juridica.data_abertura}\n")