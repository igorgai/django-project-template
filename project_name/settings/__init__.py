# settings module itself should return local settings so that
# manage.py commands work.
try:
    from .local import *
except ImportError as e:
    settings_path = '{{ project_name }}/settings'
    error_message = '{orig_msg}\n\n\t(Have you copied {path}/local.example.py to {path}/local.py?)\n'.format(
        orig_msg=e.args[0],
        path=settings_path,
    )

    raise type(e)(error_message) from e
