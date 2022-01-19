from django.db import models

# Create your models here.

from django.urls import reverse
from django.contrib.auth.models import User, timezone
# Create your models here.


class Post(models.Model):
    SLIDE1 = 'slide1'
    SLIDE2 = 'slide2'
    SLIDE3 = 'slide3'
    ABOUT = 'about'
    POST = 'post'

    CHOISE_GROUP = {
        (SLIDE1, 'slide1'),
        (ABOUT, 'about'),
        (SLIDE2, 'slide2'),
        (SLIDE3, 'slide3'),
        (POST, 'post'),
    }

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    post_date = models.DateField(auto_now_add=True)
    grop = models.CharField(max_length=20, choices=CHOISE_GROUP, default=POST)
    likes = models.ManyToManyField(User, related_name='blog_posts')


    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def __str__(self):
        return f'{self.title}'

class Contact(models.Model):
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   email = models.EmailField()
   message = models.TextField()
   timestamp = models.DateTimeField(auto_now=True)


   def __str__(self):
       return self.first_name + " - "+ self.last_name





class Slide1(models.Model):
    strength = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    post_date = models.DateField(auto_now_add=True)



    def __str__(self):
        return self.title + ' | ' + str(self.author)



