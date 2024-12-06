import sqlite3
 
 
conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()
 
#                      #
# Apagar tabela (DROP) #
#                      #
 
cursor.execute("DROP TABLE alunos;")
 
conexao.commit()
 
conexao.close()
 