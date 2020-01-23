from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Headline(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField()
    url = models.TextField()

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_scrape = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.last_scrape}'
