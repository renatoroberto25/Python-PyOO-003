import shelve  # Importa o módulo shelve para persistir objetos em um banco de dados simples.

class Funcionario:
    # Construtor da classe Funcionario
    def __init__(self, id, nome="InsiraNome", idade=0, cargo="InsiraCargo", setor="InsiraSetor"):
        # Inicializa um novo objeto Funcionario com valores padrão e armazena as propriedades em variáveis privadas.
        self.setId(id)          # Utiliza o setter para atribuir o ID
        self.setNome(nome)          
        self.setIdade(idade)        
        self.setCargo(cargo)        
        self.setSetor(setor)
        self._compromissos = []  # Lista para armazenar compromissos (atributo protegido).

    # Métodos getters e setters para acessar e modificar as propriedades privadas
    def getId(self):
        return self.__id  # Retorna o ID do funcionário

    def setId(self, id):
        self.__id = id  # Define o ID do funcionário

    def getNome(self):
        return self.__nome  # Retorna o nome do funcionário

    def setNome(self, nome):
        self.__nome = nome  # Define o nome do funcionário

    def getIdade(self):
        return self.__idade  # Retorna a idade do funcionário

    def setIdade(self, idade):
        self.__idade = idade  # Define a idade do funcionário

    def getCargo(self):
        return self.__cargo  # Retorna o cargo do funcionário

    def setCargo(self, cargo):
        self.__cargo = cargo  # Define o cargo do funcionário

    def getSetor(self):
        return self.__setor  # Retorna o setor do funcionário

    def setSetor(self, setor):
        self.__setor = setor  # Define o setor do funcionário

    def salvar_compromisso(self, tarefa):
        # Adiciona um compromisso à lista de compromissos (método público).
        self._compromissos.append(tarefa)

    def mostra_agenda(self):
        # Exibe os compromissos na agenda (método público).
        if not self._compromissos:
            print("Sem compromissos na agenda.")
        else:
            print("Eventos na agenda:")
            for compromisso in self._compromissos:
                print(f"- {compromisso}")

    def __calcular_idade(self):
        # Calcula a idade com base no ano atual (método privado).
        from datetime import datetime
        ano_atual = datetime.now().year
        return ano_atual - self.__idade

    def __str__(self):
        # Retorna uma representação em string do objeto Funcionario (método público).
        return (f"ID: {self.__id}\n"
                f"Nome: {self.__nome}\n"
                f"Idade: {self.__idade} (calculada internamente: {self.__calcular_idade()})\n"
                f"Cargo: {self.__cargo}\n"
                f"Setor: {self.__setor}\n"
                f"Compromissos: {', '.join(self._compromissos) if self._compromissos else 'Nenhum'}")

    def salvar_objeto(self, db_name):
        # Salva o objeto Funcionario em um banco de dados shelve (método público).
        with shelve.open(db_name, writeback=True) as db:
            db[str(self.__id)] = self

    @staticmethod
    def carregar_objeto(db_name, id):
        # Carrega um objeto Funcionario do banco de dados shelve com base no ID (método estático).
        with shelve.open(db_name) as db:
            return db.get(str(id))

# Função para adicionar um novo Funcionario e salvá-lo no banco de dados
def adicionar_funcionario(id, nome, idade, cargo, setor, db_name):
    funcionario = Funcionario(id, nome, idade, cargo, setor)  # Cria um novo Funcionario
    funcionario.salvar_objeto(db_name)  # Salva o Funcionario no banco de dados
    print(f"Funcionário {nome} salvo com sucesso!")

# Função para carregar e mostrar todos os Funcionários do banco de dados
def carregar_e_mostrar_funcionarios(db_name):
    with shelve.open(db_name) as db:
        for key in db:
            print(db[key])  # Exibe cada Funcionario no banco de dados

# Exemplo de uso interativo
if __name__ == "__main__":
    db_name = 'funcionarios.db'  # Nome do arquivo do banco de dados.

    while True:
        # Coleta informações do usuário para criar um novo Funcionario.
        id = int(input("Digite o ID do funcionário: "))
        nome = input("Digite o nome do funcionário: ")
        idade = int(input("Digite a idade do funcionário: "))
        cargo = input("Digite o cargo do funcionário: ")
        setor = input("Digite o setor do funcionário: ")
        
        funcionario = Funcionario(id, nome, idade, cargo, setor)
        funcionario.salvar_objeto(db_name)
        
        while True:
            # Coleta compromissos do usuário e os adiciona à agenda do Funcionario.
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
