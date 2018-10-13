from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):

        user=models.OneToOneField(User)

        def __str__(self):
                return self.user.first_name
                return self.user.last_name
                return self.user.email
                return self.user.ngo





