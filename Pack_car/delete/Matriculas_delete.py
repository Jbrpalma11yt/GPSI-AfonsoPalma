import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('Pack_car.db')
cursor = conexao.cursor()

# Função para exibir todos os registros
def exibir_registros():
    cursor.execute('SELECT * FROM matricula')
    resultados = cursor.fetchall()
    print("\nDados na tabela:")
    for matricula in resultados:
        print(matricula)

# Exibir registros antes de qualquer operação
exibir_registros()

# Perguntar ao utilizador o que ele deseja fazer
opcao = input("\nVocê deseja: \n1. Deletar um registro específico \n2. Deletar múltiplos registros \n3. Deletar todos os registros \nEscolha uma opção (1, 2 ou 3): ")

if opcao == '1':
    # Deletar um registro específico
    id_deletar = int(input("Digite o ID do registro que deseja deletar: "))
    cursor.execute('DELETE FROM matricula WHERE id = ?', (id_deletar,))
    print(f"Registro com ID {id_deletar} deletado.")

elif opcao == '2':
    # Deletar múltiplos registros
    ids_deletar = input("Digite os IDs dos registros que deseja deletar (separados por vírgula): ")
    ids_list = [int(id.strip()) for id in ids_deletar.split(',')]
    cursor.executemany('DELETE FROM matricula WHERE id = ?', [(id,) for id in ids_list])
    print(f"Registros com IDs {ids_list} deletados.")

elif opcao == '3':
    # Deletar todos os registros
    cursor.execute('DELETE FROM matricula')
    print("Todos os registros foram deletados.")

else:
    print("Opção inválida.")

# Confirmar as alterações1
conexao.commit()

# Exibir registros após a operação
exibir_registros()

# Fechar a conexão
conexao.close()
# Fechar a conexão
conexao.close()