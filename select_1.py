import pyodbc
from credenciais import credenciais

server = credenciais.get('SERVIDOR')
username = credenciais.get('NOME_USUARIO')
password = credenciais.get('SENHA')
driver = credenciais.get('DRIVER')

with open('bases.txt', 'r') as file:
    bases = [line.strip() for line in file]

def executar_select(base, results_file):
    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={base};UID={username};PWD={password}"
    connection = None
    cursor = None
    try:
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        sql = "Select CodBanco, TipoCobrança From BancosEmpresa Where (CodBanco = 41 And TipoCobrança=1) OR (CodBanco = 237 And TipoCobrança=9) OR (CodBanco = 1 And TipoCobrança=17) OR (CodBanco = 85 And TipoCobrança=1) OR (CodBanco = 341 And TipoCobrança=109) OR (CodBanco = 341 And TipoCobrança=112) OR (CodBanco = 422 And TipoCobrança=1) OR (CodBanco = 33 And TipoCobrança=1) OR (CodBanco = 756 And TipoCobrança=1) OR (CodBanco = 748 And TipoCobrança='A')"
        
        cursor.execute(sql)

        resultado = cursor.fetchall()

        with open(results_file, "a") as result_file:
            for row in resultado:
                result_file.write(f"Base: {base}, CodBanco: {row[0]}, TipoCobrança: {row[1]}\n")

    except Exception as e:
        print(f"Erro ao acessar a base {base}: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

results_file = "resultados.txt"

for base in bases:
    executar_select(base, results_file)
