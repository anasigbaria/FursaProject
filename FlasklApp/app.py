from flask import Flask, render_template
import requests, json
from flask import request

t_ip='http://172.28.0.1:6666'
t_ip= 'http://0.0.0.0:8087'
t_ip='http://127.0.0.1:6666'
app = Flask(__name__)

def conv(frm=1,to=1,amount=1):
    x = requests.get(t_ip+"/convert?cfrom="+str(frm)+"&cto="+str(to)+"&amount="+str(amount))
    return x.text


@app.route('/')
def index():
    x = requests.get(t_ip+"/list")
    lst= x.text
    lst= lst[17:-2].replace('[',"").replace("u","").replace(']',"").replace("'" , "").replace(" ","").split(",")

    return render_template('index.html', cfrom=lst,cto=lst)

@app.route("/", methods=['POST'])
def move_forward():
    x = requests.get(t_ip+"/list")
    lst= x.text
    lst= lst[17:-2].replace('[',"").replace("u","").replace(']',"").replace("'" , "").replace(" ","").split(",")

    z=(str(request.form['amount']))
    if z:
        z=int(z)
    else :
        z=0
    
    zz=1
    if request.form['amount']== "":
        zz=1
    else:
        zz=request.form['amount']
    resl=conv(amount=zz,to=request.form['cto'],frm=request.form['cfrom'])
    return render_template('index.html',res=resl, cfrom=lst,cto=lst)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
    
