# authservice

This service is in charge to generate the JWT token to be use across the workflow process and passed to all the endpoints.

Note: This is automatic in the workflow execution process, but if you want to test it via postman API you need to call the endpoint directly.

## Prepare your environment

    ## 1) mkdir Playvox (check if was already created)
    ## 2) cd Playvox
    ## 3) git clone https://github.com/magalvez/authservice.git
    ## 4) docker-compose up -d

# Service URL
http://localhost:8100/

## Testing via postmant
To test it with postman use the following collection:
https://www.getpostman.com/collections/e1daefda0d281339afeb

This is how you should generate the JWT token
<img src="https://firebasestorage.googleapis.com/v0/b/tennis-rank-prod.appspot.com/o/static%2FScreen%20Shot%202021-05-07%20at%209.11.50%20AM.png?alt=media&token=52dee3ae-042b-4248-85b4-f41cf8b7fded"></img>


---------------------------------------------

To use without dokcer pipenv follow this steps:

1) pip install pipenv
2) pipenv shell
3) pipenv install

Pipenv is going to look automatically the Pipfile and install the dependencies

Note if you want to analyze your dependencies you can run:
 * pipenv graph

Yo will something like this:
 
 Flask==1.1.2
  - click [required: >=5.1, installed: 7.1.2]
  - itsdangerous [required: >=0.24, installed: 1.1.0]
  - Jinja2 [required: >=2.10.1, installed: 2.11.3]
    - MarkupSafe [required: >=0.23, installed: 1.1.1]
  - Werkzeug [required: >=0.15, installed: 1.0.1]
  
Pipenv will generate a Pipfile.lock file to manages the following:
  * The Pipfile.lock file enables deterministic builds by specifying the exact 
    requirements for reproducing an environment. It contains exact versions for 
    packages and hashes to support more secure verification