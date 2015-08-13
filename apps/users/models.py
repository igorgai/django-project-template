from django.db import models
from django.utils.translation import ugettext as _
from custom_user.models import AbstractEmailUser


class User(AbstractEmailUser):
    """
    Extending custom user EmailUser model
    """

    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)

    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return super(User, self).get_full_name()

    get_full_name.short_description = 'Full name'
