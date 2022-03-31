from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models import Model, ForeignKey, CASCADE
from imagekit.models import ProcessedImageField
from .managers import UserManager
from .processors import Watermark


class User(AbstractBaseUser, PermissionsMixin):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'male'),
        (FEMALE, 'female'),
    ]

    avatar = ProcessedImageField(
        upload_to='src/',
        blank=True,
        null=True,
        processors=[Watermark()]
    )
    sex = models.CharField(max_length=1, choices=GENDERS)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True, unique=True)

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name


class Match(Model):
    sender = ForeignKey(User, on_delete=CASCADE, related_name='senders')
    recipient = ForeignKey(User, on_delete=CASCADE, related_name='recipients')

    class Meta:
        unique_together = (
            'sender',
            'recipient',
        )
