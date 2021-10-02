from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os


app = Flask(__name__)


#IMPLEMENTAR CORS PARA NO TENER ERRORES AL TRATAR ACCEDER AL SERVIDOR DESDE OTRO SERVER EN DIFERENTE LOCACIÓN
CORS(app)

DB_HOST = "localhost"
DB_NAME = "pruebadb"
DB_USER = "jd1_jose"
DB_PASS = "1234"
try:
    con = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST)
    
    cur = con.cursor()
    
    print(con.status)
    

    @app.route("/")
    def hello():
      return "<h1 style='color:blue'>ESTAMOS EN EL LABORATORIO DE ARCHIVOS !</h1>"

#obtengo todos los registros de mi tabla movies que cree en mi BD
    @app.route('/toda', methods=['GET'])
    def fetch_all_movies():
        cur.execute('SELECT * FROM movies')
        rows = cur.fetchall()
        print(rows)

        return jsonify(rows)
    
  
    
    if __name__ == "__main__":
     app.run(host='0.0.0.0')        

except:
    print('Error')