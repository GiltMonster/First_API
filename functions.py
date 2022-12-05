import sqlite3 as sql

def get_database():
    conn = sql.connect('DB.db')
    return conn

def createUser(nome, sobrenome, cpf, rg, data_nasc):
    conn = get_database()
    cursor = conn.cursor()
    query = "INSERT INTO pessoa(nome, sobrenome, cpf, rg, data_nasc) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, [nome, sobrenome, cpf, rg, data_nasc])
    conn.commit()
    conn.close() 
    return True  
    
def atualizaUser(id, nome, sobrenome, cpf, rg, data_nasc):
    conn = get_database()
    cursor = conn.cursor()
    query = "UPDATE pessoa SET nome = ?, sobrenome = ?, cpf = ?, rg = ?, data_nasc = ? WHERE id = ?"
    cursor.execute(query, [nome, sobrenome, cpf, rg, data_nasc, id])
    conn.commit()
    conn.close() 
    return True

def deletaUser(id):
    conn = get_database()
    cursor = conn.cursor()
    query = "DELETE FROM pessoa WHERE id = ?"
    cursor.execute(query, [id])
    conn.commit()
    conn.close()
    return True 