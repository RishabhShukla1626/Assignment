from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ADMINISTRATOR = 'ADMINISTRATOR'
    MODERATOR = 'MODERATOR'
    DEBATER = 'DEBATER'
    GUEST = 'GUEST'
    ROLES_CHOICES = [
        (ADMINISTRATOR, 'Administrator'),
        (MODERATOR, 'Moderator'),
        (DEBATER, 'Debater'),
        (GUEST, 'Guests'),
    ]
    assigned_permission = models.CharField(max_length=15, choices=ROLES_CHOICES, default=GUEST)

    def __str__(self):
        return '@' + str(self.username)

# Create your models here.
