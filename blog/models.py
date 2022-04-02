
from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import PROTECT
from ckeditor.fields import RichTextField
from django_extensions.db.fields import AutoSlugField
 
class MyUser(AbstractUser):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'),)
    email = models.EmailField(verbose_name='email address',max_length=160)
    mobileNumber = models.CharField(verbose_name='mobilenumber',max_length=160,null=True)
    company= models.CharField(verbose_name='Company',max_length=160)
    city = models.CharField(verbose_name='city',max_length=160)
    country = models.CharField(verbose_name='country',max_length=160)
    image = models.ImageField(upload_to='user/',null=True,blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    author = models.BooleanField(default=False)
    
    def __str__(self):
        return self.email
    
class Category(models.Model):
	name = models.CharField(max_length=100)
	desc = models.TextField() 
	slug = AutoSlugField(populate_from='name', max_length=200,editable=False,unique=True)
	
	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=100)
	desc = models.TextField()
	slug = AutoSlugField(populate_from='name', max_length=200, editable=False,unique=True)
	def __str__(self):
		return self.name


class Post(models.Model):    
    category = models.ForeignKey(Category, on_delete=PROTECT,null=True,blank=True)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', max_length=210, editable=False,unique=True) 
    text = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    feature_image = models.ImageField(upload_to='image/',null=True,blank=True)
    thumbnail_image = models.ImageField(upload_to='image/',null=True,blank=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
        def __str__(self):
            return self.title

class Comments(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,related_name='replies')
    def __str__(self):
        return self.name


