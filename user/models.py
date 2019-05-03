from django.db import models

# Create your models here.
class User(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=100,blank=True,null=True)
    last_name=models.CharField(max_length=100,blank=True,null=True)
    company_name=models.TextField(max_length=200,blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    state=models.CharField(max_length=10,blank=True,null=True)
    zip=models.IntegerField(blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    web=models.CharField(max_length=100,blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return "{}".format(self.id)
