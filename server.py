from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
import psycopg2
import config
@app.route('/',methods = ['POST', 'GET'])
def index():
   if request.method == 'POST':
      uID = request.form['uID']
      try:
         connection = psycopg2.connect(user=config.dbconfig.user,password=config.dbconfig.password,host=config.dbconfig.host,port=config.dbconfig.port,database=config.dbconfig.database)
         cursor = connection.cursor()
         selectstatement = "SELECT uname, email FROM test.aaaaaaaaaaaaaaa WHERE userid = '"+uID+"'"
         cursor.execute(selectstatement)
         record = cursor.fetchone()
         print(record)
      finally:
         if (connection):
            cursor.close()
            connection.close()
         if record is None:
            return render_template('index.html')
         else:
            return render_template('template.html', uid=record[0])
   else:
     return render_template('index.html')
if __name__ == '__main__':
   app.run(port=config.port)
