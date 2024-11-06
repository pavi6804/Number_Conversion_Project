from flask import Flask, render_template, request
from tcp_client import send_number_to_server 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    number = request.form['number']
    from_base = request.form['from_base']
    to_base = request.form['to_base']
    result = send_number_to_server(number, from_base, to_base)
    return render_template('index.html', result=result, number=number, from_base=from_base, to_base=to_base)

if __name__ == "__main__":
    app.run(debug=True)
