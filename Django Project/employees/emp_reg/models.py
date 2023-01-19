from django.db import models

# Create your models here.
class position(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title


class emp(models.Model):
    fullname=models.CharField(max_length=50)
    empcode=models.CharField(max_length=10)
    mobile=models.CharField(max_length=10)
    position=models.ForeignKey(position,on_delete=models.CASCADE)
