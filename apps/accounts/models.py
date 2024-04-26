import uuid
from . import utils
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE=(("P","P"), ("B", "B"))
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)
    slug = models.SlugField(unique=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=100, unique=True, null=False, blank=False)
    full_name = models.CharField(max_length=255, null=False, blank=False)
    otp = models.CharField(max_length=100, null=True, blank=True)
    reset_token  = models.CharField(max_length=1000, null=True, blank=True)
    type = models.CharField(max_length=1, choices=USER_TYPE, default="P")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.email
    
    def save(self, *args, **kwargs) -> None:
        email_username, _ = self.email.split('@')
        names = self.full_name.split(" ")
        if names:
            self.first_name = names[0]
            self.last_name = names[-1]
        elif self.first_name and self.last_name:
            self.full_name = f"{self.first_name} {self.last_name}"

        elif self.full_name == "" or self.full_name == None:
            self.full_name = email_username
        if self.username == "" or self.username == None:
            self.username = email_username
        
        if not self.slug:
            self.slug = slugify(self.full_name)
        return super(User, self).save(*args, **kwargs)
    


class Sector(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name', 'created_at']
        verbose_name_plural = "Sectores Empresarial"
    
    def __str__(self) -> str:
        return self.name

    
class AbstractProfile(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="perfil", blank=True)
    phone = models.CharField(max_length=20, unique=True, null=True)
    address = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class PersonalProfile(AbstractProfile):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="personal_profile")
    bi = models.CharField(max_length=14, null=False, unique=True)
    gender = models.CharField(max_length=50, choices=utils.GENDER, default=utils.GENDER[0])
    birthday = models.DateField(null=True,blank=True)


    class Meta:
        verbose_name_plural = "Perfils de Usuários"
        ordering = ["user"]

    def __str__(self) -> str:
        return self.get_full_name()
    
    def get_full_name(self) -> str:
        return self.user.get_full_name()
    
    def get_gender(self):
        """Retorna a representação amigável para exibição do campo 'gender'."""
        return [item for item in (utils.GENDER) ]

    def get_absolute_url(self):
        return reverse("edit-user", kwargs={"slug": self.slug})



class CompanyProfile(AbstractProfile):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="company_profile")
    sector = models.ForeignKey(Sector, models.PROTECT)
    nif = models.CharField(max_length=14, null=False, unique=True)
    website = models.URLField(max_length=255,blank=True)
    
    class Meta:
        verbose_name_plural = "Perfils Empresariais"
        ordering = ["user"]

    def __str__(self) -> str:
        return self.get_full_name()
    
    def get_full_name(self) -> str:
        return self.user.get_full_name()
    

    def get_absolute_url(self):
        return reverse("edit-user", kwargs={"slug": self.slug})
    

