from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
import psycopg2
@app.route('/',methods = ['GET'])
def index():
   return render_template('index.html')
     
@app.route('/parking-ticket',methods = ['POST', 'GET'])
def ParkingTicket():
   if request.method == 'POST':
      return render_template('parking-ticket.html', uID=request.form['uID'])
   else:
      return redirect(url_for('index'))
if __name__ == '__main__':
   app.run(port=8080)
