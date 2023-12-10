from flask import Flask,render_template, request, redirect

app = Flask(__name__)

# INDEX
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/proyectos', methods=['POST', 'GET'])
def proyectos():
    return render_template('proyectos.html')

@app.route('/sobremi', methods=['POST', 'GET'])
def sobremi():
    return render_template('sobre_mi.html')

if __name__ == "__main__":
        app.run(debug=True)
