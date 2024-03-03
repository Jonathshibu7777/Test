from django.db import models

# Create your models here.
class tbl_Team(models.Model):
    Team_Name=models.CharField(max_length=50)
    Team_Password=models.CharField(max_length=50)
    Team_Photo = models.FileField(upload_to='Assets/Team_Photo/')
    Team_Status = models.IntegerField(default="0")

class tbl_Player_Category(models.Model):
    Player_Category=models.CharField(max_length=50)