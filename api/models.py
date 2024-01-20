from django.db import models
from django.contrib.auth.models import AbstractUser

from api.services.company_services import validate_image_size
from api.managers.Usermanagers import UserManager



class CustomUser(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]

    objects=UserManager()
    def str(self) :
        return self.email
    
class Company(models.Model):
    company_name = models.CharField(max_length=255, unique=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
      return self.company_name

class Employee(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile_images/', validators=[validate_image_size])
    profile_img_thumbnail = models.ImageField(upload_to='profile_pics/thumbnails/', null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    birthdate = models.DateField(null=False)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    

