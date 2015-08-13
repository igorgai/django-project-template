from copy import deepcopy
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from custom_user.admin import EmailUserAdmin
from sorl.thumbnail.admin import AdminImageMixin
from apps.users.models import User


class UserAdmin(AdminImageMixin, EmailUserAdmin):
    list_display = ('email', 'get_full_name', 'is_staff',)

    def get_fieldsets(self, request, obj=None):
        fieldset_super = super(UserAdmin, self).get_fieldsets(request, obj)
        fieldset_extended = list(deepcopy(fieldset_super))
        fieldset_extended.insert(1, (_('User info'),
                                     {'fields': ('first_name', 'last_name')}))

        return tuple(fieldset_extended)

admin.site.register(User, UserAdmin)
