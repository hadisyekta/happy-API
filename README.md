# d1g1thappiness
## The second largest heading

_____________________________________________________________________
d1g1thappiness is an application that was implemented by Django rest-framework and Docker,
  it provides a REST API for inserting level of happiness per day, and a daily report.

## requirement
[Docker Desktop](https://www.docker.com/products/docker-desktop)

###### Extentions in VSCode:
Remote - Containers 
Remote WSL 
Please check the Details tab on VSCode Extentions of These two extentions, for more information.

###### Documentation for Docker
[Docker](https://docs.docker.com/get-docker/)
[Docker - Working with containers](https://code.visualstudio.com/docs/containers/overview).
[Remote - containers](https://code.visualstudio.com/docs/remote/containers)
_____________________________________________________________________
## Installation
###### Working with container in VSCode
I used this code to create docker configuratoin:[Docker Configuration](https://github.com/erroneousboat/docker-django)
Use docker-compose.yml to install docker containers and the project requirements.
###### Please pay attention if you have any container with these name:
docker-django
docker-django_webapp
docker-django_db
docker-django_webserver

if you have plase change the docker-compose.yml config

Use this tutorial, [Remote development in Containers](https://code.visualstudio.com/docs/remote/containers-tutorial)
1. Follow the installation steps above.
2. Clone https://github.com/Microsoft/vscode-remote-try-node locally.
3. Start VS Code
4. Run the Remote-Containers: Open Folder in Container... command and select the local folder.


###### Django
docker-compose.yml will install requirement.txt which contains:
```
asgiref==3.3.4
Django==3.2.4
djangorestframework==3.12.4
psycopg2-binary==2.7.6.1
pytz==2021.1
sqlparse==0.4.1
typing-extensions==3.10.0.0
uWSGI==2.0.17.1
```

## Assumptions
_____________________________________________________________________
I consider level of happiness between [1-10] according to Employee Net Promoter Scores (eNPS) 

For second api, which provides different result for autheticated and unathenticated user,
 I added date filter, to have a per day aggregation.
 
I can add anotehr API to get number of days and then provide a report during taht days.

## Tests
###### Unit Tests:
run:
`python manage.py test`

## Images
![user-employee](https://github.com/hadisyekta/happyd1g1t/blob/master/webapp/starter/statics/user-employee.PNG)

![admin](https://github.com/hadisyekta/happyd1g1t/blob/master/webapp/starter/statics/admin.PNG)
![creation](https://github.com/hadisyekta/happyd1g1t/blob/master/webapp/starter/statics/creation.PNG
![creation-201](https://github.com/hadisyekta/happyd1g1t/blob/master/webapp/starter/statics/creation-201.PNG)
![creation-400](https://github.com/hadisyekta/happyd1g1t/blob/master/webapp/starter/statics/creation-400.PNG)
![creation-403](https://github.com/hadisyekta/happyd1g1t/blob/master/webapp/starter/statics/creation-403.PNG)
![error-notesm-report](https://github.com/hadisyekta/happyd1g1t/tree/master/webapp/statics/starter/error-notesm-report.PNG)
![auth-report](https://github.com/hadisyekta/happyd1g1t/blob/master/webapp/starter/statics/auth-report.PNG)
![unauth-report](https://github.com/hadisyekta/happyd1g1t/blob/master/webapp/starter/statics/unauth-report.PNG)