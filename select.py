import pyodbc

# Configurações de conexão ao SQL Server
server = '.'
username = '.'
password = '.'
driver = 'SQL Server'

# Ler a lista de bases de dados a partir do arquivo
with open('c:/bases.txt', 'r') as file:
    bases_de_dados = [line.strip() for line in file]

# Função para executar o update em cada base de dados
def select(base_de_dados):
    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={base_de_dados};UID={username};PWD={password}"
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    sql = f"Select Top 1 CodEmpresa From Empresas"
    cursor.execute(sql)
    connection.commit()

    cursor.close()
    connection.close()

# Executar o update em cada base de dados
for base_de_dados in bases_de_dados:
    print(f"Executando o select em: {base_de_dados}")
    select(base_de_dados)

print("Select de teste concluído em todas as bases de dados.")
