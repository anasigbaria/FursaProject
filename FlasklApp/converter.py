
from flask import Flask
import requests, json
from flask import request

api_key = "c652aad8624cf514f2e3"
base_url = "https://free.currconv.com/api/v7/"



def currList():
    action ="currencies?apiKey="
    complete_url=base_url+action+api_key
    response = requests.get(complete_url) 
    x = response.json() 
    return (x["results"].keys())

def convert(amount,fr,to):
     action ="convert?apiKey="
     querry= "&q="+fr+"_"+to+","+to+"_"+"fr"
     complete_url= base_url+action+api_key+querry

     response = requests.get(complete_url) 
     x = response.json() 
     result= float(amount)*float(x["results"][fr+"_"+to]["val"])
     return result




app = Flask(__name__)

@app.route('/list')
def index():
    return str(currList())

@app.route('/convert', methods=['GET'])
def login():
    cfrom = request.args.get('cfrom')
    print(cfrom)
    cto= request.args.get('cto')
    print(cto)
    amount= int(request.args.get('amount'))
    print(amount)
    return str(convert(float(amount),cfrom,cto))



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=6666)
