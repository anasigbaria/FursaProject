# FursaProject

the project is more than 50% ready:
 - the front end is ready
 - terraform ready
 - the code that converts currinceis=es using the api is ready

to-do:
 - the Audit(data base)
 - Kubernetes

commands to test evrey part alone:
- terraform part:
  - terraform init
  - terraform apply
  - then you need to enter the acssess and secrt key of your aws acc
- FlaskApp (the front end):
  - python ./FlasklApp/app.py 
  - the visit:  http://127.0.0.1:5000/  using the browser
- connverterapi (the part that connects to the api and does the conversion):
  - to convert x amount from cuurency A to Currency B use : python ./converterAPI/converter.py convert x A B
  - example: python ./converterAPI/converter.py convert 1 DKK XAG
  - to get the currincies list that the api provid use:
  - python ./converterAPI/converter.py currencyList