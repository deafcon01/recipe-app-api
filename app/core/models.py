from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates new user"""
        if not email:
            raise ValueError('Users must provide email')
        user =  self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, password):
        """Create superuser"""
        user = self.create_user(user, email)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model supports using email instead username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'