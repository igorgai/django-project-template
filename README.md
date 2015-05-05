# README #

### Creating new project from this template

```
#!bash

django-admin startproject <projectname> --template=https://github.com/igorgai/django-project-template/archive/master.zip --name=.gitignore --name=README.md
```

### Basic setup ###
#### Python dependencies and database setup
 
 In the terminal (with your python virtualenv activated):
 
```
#!python
pip install -r requirements/dev.txt

```

Next copy the file *{{ project_name }}/settings/local.example.py* and place it in the same directory under name *"local.py"*.

#### Html/css/js dependencies

```
#!bash

npm -g install bower (Node should be installed)
```

```
#!python
python manage.py bower install

```