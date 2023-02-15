from django.db import models

# Create your models here.

class Chat(models.Model):
    msg = models.CharField(max_length=500)
    msg_type = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        
        return self.prompt