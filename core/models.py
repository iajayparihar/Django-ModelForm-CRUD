from django.db import models

class userModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
    