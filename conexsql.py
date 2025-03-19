import sqlite3
from pathlib import Path

#ROOT_PATH = Path(__file__).parent
#conexao = sqlite3.connect(ROOT_PATH / "clientes.db")

# Conectar ao banco de dados
conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

# Criar uma tabela
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)")

# Inserir dados
cursor.execute("INSERT INTO usuarios (nome) VALUES ('Alice')")

# Confirmar a transação
conexao.commit()

data = (nome, email, id)
#atualizando dados
cursor.execute('UPDATE usuarios SET nome=?, email=? WHERE id=?;', data)
conexao.commit()

#deletando dados
cursor.execute('DELETE FROM usuarios WHERE id=?;', id)
conexao.commit()

#inserindo em lote
cursor.executemany('INSERT INTO usuarios (nome, email) VALUES (?,?);', data)
Crie uma introdução para um trabalho acadêmico sobre redes de computadores

# Fechar a conexão
conexao.close()