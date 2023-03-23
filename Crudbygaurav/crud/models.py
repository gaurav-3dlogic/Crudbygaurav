from xml.parsers.expat import model
from django.db import models



class Gaurav(models.Model):
    uname = models.CharField(max_length=100)
    uemail = models.EmailField(max_length=100)
    upassword = models.CharField(max_length=100)
    
    
    
    class Meta:
        db_table = "gaurav"
    
    



