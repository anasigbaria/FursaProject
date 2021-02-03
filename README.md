# FursaProject
# a small web app that you can convert cuurncies values using it

commands to test evrey part alone:
- terraform part:
  - cd terraform/
  - terraform init
  - terraform apply
  - then you need to enter the acssess and secret key of your aws account


- the app itself:

  - docker-compose up
  - then go to http://localhost:5000/ in your browser and you can use the site


  
- some explination about the project:
  - the project consists of 3 main part:
    - terraform , in this part you can creat all the infrastructure on your ws account to deploy the project on thiis cloud servers ( unfortunatly because of a problem in kubernetes we can creat the infrstructure but we cant deploy the project on it , but you can deploy it manuley but then we need some small changes in the code)
    - Flaskapp, this part is the front end of the app that connects to converter part and display the results on the browser.
    - conventerAPI, this part connects to https://free.currconv.com/api/v7/ and using the API of this site we do all the converting operations and the extraction of the names of the currencies, also the frontend conects to this part using REST API and sends some requests to it, and the onventer sends back the result of the request and the front end displays it.
