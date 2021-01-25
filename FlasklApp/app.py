from flask import Flask, render_template
import requests, json
import subprocess



app = Flask(__name__)

@app.route('/')
def index():
    cfrom = subprocess.check_output(['curl', 'http://127.0.0.1:8087/list'],shell=True)
    cto = ['INS', 'EUR', 'DLR']
    print(cto)
    return render_template('index.html', cfrom=cfrom,cto=cto)



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
    