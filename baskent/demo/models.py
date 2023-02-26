from django.db import models

# Our class structure for Database.
class Message(models.Model):
    fullName = models.CharField(max_length=50)
    mailAddress = models.CharField(max_length=50)
    uMessage = models.CharField(max_length=300)
    
    def __str__(self):
        return self.fullName, self.mailAddress, self.uMessage