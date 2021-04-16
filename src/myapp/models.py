from __future__ import unicode_literals

from django.db import models
from django.db import connections
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin, User)
from django.utils.translation import ugettext_lazy as _

import uuid

class DemoModel(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="demo_images")

    def __str__(self):
        return self.title

class UserManager(BaseUserManager):
    def _create_user(self, **kwargs):
        password = kwargs.pop('password', '12345')
        kwargs['email'] = self.normalize_email(kwargs['email'])
        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, **kwargs):
        kwargs['is_staff'] = False
        return self._create_user(**kwargs)


    def create_superuser(self, **kwargs):
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = True
        return self._create_user(**kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=65530)
    
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    objects = UserManager()

