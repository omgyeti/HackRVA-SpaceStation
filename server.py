from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
import config
@app.route('/',methods = ['POST', 'GET'])
def index():
   if request.method == 'POST':
      uID = request.form['uID']
      return render_template('template.html', uid=uID)
   else:
     return render_template('index.html')
if __name__ == '__main__':
   app.run(port=config.port)