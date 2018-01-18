# README #

### Creating a new project from this template

```
django-admin.py startproject <projectname> --template=https://github.com/igorgai/django-project-template/archive/master.zip --name=.gitignore,README.md,.bowerrc --extension=json,py,md,txt,less
```

### Basic setup ###
#### Python dependencies and database setup

1. Install pipenv (in case you don't have it installed yet). 
    In the terminal:
    ```
    pip install pipenv
    ```
    (https://docs.pipenv.org/#install-pipenv-today)
    
2. Initialize virtual environment:
    ```
    pipenv install --three
    ```
3. Copy the file at *{{ project_name }}/settings/local.example.py* and save it in the same directory under the name of *"local.py"*:

    ```
    cp {{ project_name }}/settings/local.example.py {{ project_name }}/settings/local.py
    ```

4. Install dependencies and initial data: 
    ```
    pipenv run fab initial_data
    ```

#### Create superuser

```
python manage.py createsuperuser
```

#### Html/css/js dependencies

```
npm -g install bower (Node should be installed)
bower install
```

