from funcionario import Funcionario  # Importa a classe Funcionario do módulo funcionario
import shelve  # Importa o módulo shelve para manipulação de arquivos de armazenamento
# Abre o arquivo shelve para leitura
db = shelve.open('funcionarios.db')  # Certifique-se de usar o mesmo nome do arquivo
# Itera sobre todas as chaves no banco de dados shelve
for key in db:
    # Imprime o objeto associado à chave atual
    print(db[key])
# Fecha o arquivo shelve após a leitura
db.close()
