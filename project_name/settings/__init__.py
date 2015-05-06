# settings module itself should return local settings so that
# manage.py commands work.
try:
    from .local import *
except ImportError as e:
    settings_path = '{{ project_name }}/settings'
    error_message = '{mes} (did you copy {path}/local.example.py to {path}/local.py?)'.format(
        mes=e.args[0],
        path=settings_path
    )
    e.args = tuple([error_message])

    raise e
