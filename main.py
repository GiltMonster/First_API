from flask import Flask, jsonify, request
import json
import sqlite3 as sql
import functions

app = Flask(__name__)


@app.route('/listar',methods=['GET'])
def getTasks():

  conn = functions.get_database()
  conn.row_factory = sql.Row
  cursor = conn.cursor()
  cursor.execute('''SELECT * FROM pessoa''')
  result = cursor.fetchall();
  conn.close()
  return json.dumps([dict(ix) for ix in result]) 
  
  
@app.route('/cadastrar',methods=['POST'])
def insert():  
  people_details = request.get_json()
  nome = people_details["nome"]
  sobrenome = people_details["sobrenome"]
  cpf = people_details["cpf"]
  rg = people_details["rg"]
  data_nasc = people_details["data_nasc"]
  result = functions.createUser(nome, sobrenome, rg, cpf, data_nasc)
  return jsonify(result)

@app.route('/pesquisar/<id>',methods=['GET'])
def pesquisa(id):  
  conn = functions.get_database()
  cursor = conn.cursor() 
  query = "SELECT * FROM pessoa WHERE id = ?"
  cursor.execute(query, [id])
  result = cursor.fetchall();
  conn.commit()
  conn.close()
  return json.dumps(result)
  
@app.route('/atualizar',methods=['PUT'])
def updatePeople():
    people_details = request.get_json()
    id = people_details["id"]
    nome = people_details["nome"]
    sobrenome = people_details["sobrenome"]
    cpf = people_details["cpf"]
    rg = people_details["rg"]
    data_nasc = people_details["data_nasc"]
    result = functions.atualizaUser(id, nome, sobrenome, cpf, rg, data_nasc)
    return json.dumps(result)
  
@app.route('/deletar/<id>',methods=['DELETE'])
def deleteTask(id):
    result = functions.deletaUser(id)
    return json.dumps(result)

app.run(host='0.0.0.0', port=81)
