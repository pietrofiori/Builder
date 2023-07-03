class Pessoa:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.endereco = None

    def definir_nome(self, nome):
        self.nome = nome
        return self

    def definir_idade(self, idade):
        self.idade = idade
        return self

    def definir_endereco(self, endereco):
        self.endereco = endereco
        return self

    def construir(self):
        return self

pessoa = (
    Pessoa()
    .definir_nome("João")
    .definir_idade(19)
    .definir_endereco("Rua Nehita Martins Ramos,208")
    .construir()
)