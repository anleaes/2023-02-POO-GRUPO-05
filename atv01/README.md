Atividade:

- Os clientes são pessoas físicas e jurídicas e ambos podem contratar cursos.
- Trabalhe utilizando herança (Pessoa jurídica e física), agregação (Livro e Autor) e Polimorfismo. 

- Crie uma classe main (E fazer funcionar).
- Usar o GIT conforme aula.

#####################################################################

Diagrama:
@startuml
class Aluno{
- numero_matricula
- pessoa_fisica: PessoaFisica
}

class Pessoa{
    - nome: String 
    - endereco: String
    + construtor(nome, endereco)
}

class PessoaFisica{
    - cpf: String
    - data_nascimento: Date 
    - pessoa: Pessoa
    + construtor(cpf, data_nascimento, pessoa)
}

class PessoaJuridica{
    - cnpj: String
    - razao_social: String
    - data_abertura: Date
    - pessoa: Pessoa
    + construtor(cnpj, data_abertura, pessoa)
}

class Inscricao{
    -valor_inscrico
    -data_matricula
    -curso: Curso
    -aluno_matriculado: Aluno
    -contratante: Pessoa 
    + construtor(numero_matricula, data_matricula, curso, aluno, contratante)
}


class Curso {
    -Nome String 
    -carga_horaria String
    + construtor(nome, carga_horaria)
}

Inscricao *-- Curso
Inscricao *-- Aluno
Inscricao *-- Pessoa
PessoaFisica --|> Aluno
Pessoa --|> PessoaFisica
Pessoa --|> PessoaJuridica
@enduml

#####################################################################

Classes a serem criadas:
    Aluno (numero_matricula, pessoa_fisica)
    Pessoa (nome, endereco)
    PessoaFisica (cpf, data_nascimento, pessoa)
    PessoaJuridica (cnpj, razao_social, data_abertura, pessoa)
    Inscricao (valor_inscricao, data_matricula, curso, aluno_matriculado, contratante)
    Curso (Nome, carga_horaria)

#####################################################################