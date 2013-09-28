from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django_extensions.db.fields import AutoSlugField


class AccountManager(BaseUserManager):
    def create_user(self, facebook_id, **kwargs):
        user = self.model(facebook_id=facebook_id, **kwargs)
        user.set_unusable_password()
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    facebook_id = models.CharField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="name", separator="")
    email = models.EmailField(max_length=255, blank=True, null=True)
    oauth_token = models.TextField(null=True)

    # Django admin
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "facebook_id"
    REQUIRED_FIELDS = ['name']

    class Meta:
        ordering = ['name', 'email']

    def __str__(self):
        return '{name} <{facebook_id}>'.format(
            name=self.name,
            facebook_id=self.facebook_id,
        )

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    objects = AccountManager()
