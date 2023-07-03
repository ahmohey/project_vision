from django.db import models

class User(models.Model):
  class Meta:
    db_table = "user"
    
  user_id = models.CharField(max_length=255)
  user_pass = models.CharField(max_length=255)
  user_name = models.CharField(max_length=255)
  user_email = models.CharField(max_length=255)
  user_agree = models.BooleanField(default="False")
