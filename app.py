from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template("base.html")

@app.route('/login/',methods=['POST'])
def collect_data():
    name=request.form['name']
    return("Hello\t"+ name + "\tWelcome back")

if __name__=='__main__':
    app.run(debug=True)

