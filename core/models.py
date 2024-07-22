from django.db import models
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.contrib.auth.models  import AbstractUser, BaseUserManager

class MyUserManager(BaseUserManager):
     def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError("User must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=self.normalize_email(email), full_name=full_name)
        
        if password:
            try:
                validate_password(password, user)
            except DjangoValidationError as e:
                raise ValueError(str(e))
            
            user.set_password(password)
        
        user.save(using=self._db)
        return user
    
     def create_superuser(self, full_name, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    
class User(AbstractUser):
    email = models.EmailField( verbose_name="email address", max_length=255,unique=True)
    username = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = MyUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]
    
    def __str__(self):
        return self.email


