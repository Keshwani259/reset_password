from django.db import models
from django.contrib.auth.models import User, AbstractUser ,Group, Permission
# Create your models here.class CustomUser(AbstractUser):
class CustomUser(AbstractUser):
    div = models.CharField(max_length=10,blank=True)
    sem = models.CharField(max_length=10)
    program = models.CharField(max_length=50)
    elective = models.CharField(max_length=50)
    honours = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Add this
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Add this
        blank=True
    )
