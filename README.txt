

Hello! :)
_____________________________________________________________________

Please install dockerdesktop
Extentions in VSCode: 
intsall Remote - Container 
install Remote WSL 

you can follow https://code.visualstudio.com/docs/containers/overview
or  https://code.visualstudio.com/docs/remote/containers
_____________________________________________________________________
I use this code to create docker configuratoin: https://github.com/erroneousboat/docker-django
use /workspace/.devcontainer/docker-compose.yml to install docker

please pay attention if you have any container with these name:
docker-django
docker-django_webapp
docker-django_db
docker-django_webserver

if you have plase change the docker-compose.yml config
 
docker-compose.yml will install /workspace/webapp/requirement.txt which contains
asgiref==3.3.4
Django==3.2.4
djangorestframework==3.12.4
psycopg2-binary==2.7.6.1
pytz==2021.1
sqlparse==0.4.1
typing-extensions==3.10.0.0
uWSGI==2.0.17.1


---------------------------------------------------------------------
I consider level of happiness between [1-10] according to https://buffer.com/resources/measuring-employee-satisfaction/
I have provided unittest, however, I should add more test, and apply some changes.


For second api, which provides different result for autheticated and unathenticated user,
 I added date filter, to have a per day aggregation.

