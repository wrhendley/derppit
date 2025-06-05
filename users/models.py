from django.db import models
from django.contrib.auth.models import User

class DerppitUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='derppit_user')
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    bio = models.TextField(blank=True, null=True)
    karma = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    
