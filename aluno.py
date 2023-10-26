class Aluno:
    def __init__(self, matricula):
        self._matricula = matricula
        self.curso = None

    def escolher_curso(self, curso):
          self.curso = curso