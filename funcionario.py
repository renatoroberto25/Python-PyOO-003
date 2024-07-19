import shelve

class Funcionario:
    def __init__(self, id, nome="InsiraNome", idade=0, cargo="InsiraCargo", setor="InsiraSetor"):
        self.setId(id)
        self.setNome(nome)          
        self.setIdade(idade)        
        self.setCargo(cargo)        
        self.setSetor(setor)
        self._compromissos = []

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getIdade(self):
        return self.__idade

    def setIdade(self, idade):
        self.__idade = idade

    def getCargo(self):
        return self.__cargo

    def setCargo(self, cargo):
        self.__cargo = cargo

    def getSetor(self):
        return self.__setor

    def setSetor(self, setor):
        self.__setor = setor

    def salvar_compromisso(self, tarefa):
        self._compromissos.append(tarefa)

    def mostra_agenda(self):
        if not self._compromissos:
            print("Sem compromissos na agenda.")
        else:
            print("Eventos na agenda:")
            for compromisso in self._compromissos:
                print(f"- {compromisso}")

    def __calcular_idade(self):
        from datetime import datetime
        ano_atual = datetime.now().year
        return ano_atual - self.__idade

    def __str__(self):
        return (f"ID: {self.__id}\n"
                f"Nome: {self.__nome}\n"
                f"Idade: {self.__idade} (calculada internamente: {self.__calcular_idade()})\n"
                f"Cargo: {self.__cargo}\n"
                f"Setor: {self.__setor}\n"
                f"Compromissos: {', '.join(self._compromissos) if self._compromissos else 'Nenhum'}")

    def salvar_objeto(self, db_name):
        with shelve.open(db_name, writeback=True) as db:
            db[str(self.__id)] = self

    @staticmethod
    def carregar_objeto(db_name, id):
        with shelve.open(db_name) as db:
            return db.get(str(id))

def adicionar_funcionario(id, nome, idade, cargo, setor, db_name):
    funcionario = Funcionario(id, nome, idade, cargo, setor)
    funcionario.salvar_objeto(db_name)
    print(f"Funcionário {nome} salvo com sucesso!")

def carregar_e_mostrar_funcionarios(db_name):
    with shelve.open(db_name) as db:
        for key in db:
            print(db[key])

# Exemplo de uso interativo
if __name__ == "__main__":
    db_name = 'funcionarios.db'
    
    while True:
        id = int(input("Digite o ID do funcionário: "))
        nome = input("Digite o nome do funcionário: ")
        idade = int(input("Digite a idade do funcionário: "))
        cargo = input("Digite o cargo do funcionário: ")
        setor = input("Digite o setor do funcionário: ")
        
        funcionario = Funcionario(id, nome, idade, cargo, setor)
        funcionario.salvar_objeto(db_name)
        
        while True:
            compromisso = input("Digite um compromisso (ou 'fim' para encerrar): ")
            if compromisso.lower() == 'fim':
                break
            funcionario.salvar_compromisso(compromisso)
        
        funcionario.salvar_objeto(db_name)  # Atualiza o objeto no banco de dados com os compromissos

        continuar = input("Deseja adicionar outro funcionário? (s/n): ")
        if continuar.lower() != 's':
            break

    # Carregar e mostrar funcionários
    carregar_e_mostrar_funcionarios(db_name)
