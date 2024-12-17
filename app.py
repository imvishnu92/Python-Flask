from flask import Flask, render_template, jsonify
app = Flask(__name__)

PRODUCTS = [
    {'id':1,
    'title':'Solder Preforms',
    'description':'Solder Preforms'},
    {'id':2,
    'title':'Solder Pins',
    'description':'Solder Pins'},
    {'id':3,
    'title':'Solder Strips',
    'description':'Solder Strips'},
    {'id':4,
    'title':'Solder Jacks',
    'description': 'Solder Jacks'}
]

@app.route('/')
def hello_sriram():
    return render_template('home.html', products=PRODUCTS)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)