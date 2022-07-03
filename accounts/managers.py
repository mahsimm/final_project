from django.contrib.auth.base_user import BaseUserManager
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password
from .enums import RoleCodes
from django.db.transaction import commit


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        password = make_password(str(password))
        user.password = password
        try:
            user.role
        except ObjectDoesNotExist:
            role = apps.get_model(app_label='accounts', model_name='Role')
            if user.is_superuser:
                user.role = role.objects.get(code=RoleCodes.ADMIN.value)
            else:
                user.role = role.objects.get(code=RoleCodes.NORMAL.value)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)
