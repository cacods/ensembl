# Installation instructions in a GNU/Linux environment (to test locally)

1. Prerequisites:
* git, Python 3, virtualenv, sqlite3, mysql (client)
* to consume the API from command line: httpie or curl


1. Create and activate virtual environment (virtualenv) with Python 3 

    ```bash
    $ virtualenv ROOT_DIR -p python3
    $ source bin/activate
    ```

1. Clone the project from GitHub

    ```bash
    $ git clone https://github.com/caco13/ensembl.git
    ```

1. Install requirements

    ```bash
    $ pip install -r requirements.txt
    ```

1. Run migrations

    ```bash
    $ python manage.py migrate
    ```

1. Run the application

    ```bash
    $ python manage.py runserver
    ```
    This will run the virtual server in localhost:8000. If port 8000 is 
    occupied by another service run the server in other free port with
    
    ```bash
    $ python manage.py runserver localhost:<PORT>
    ```
    
### Testing API

1. From command line
    
    With httpie:
    ```bash
    $ http http://localhost:8000/gene_suggest/mem/danio_rerio/10
    ```
    With curl:
    ```bash
    $ curl -H 'Accept: application/json; indent=4' http://localhost:8000/gene_suggest/mem/danio_rerio/10
    ```

1. From web browser

    Just type the url with the search terms in it:
    ```bash
    http://localhost:8000/gene_suggest/mem/danio_rerio/10
    ```
    

