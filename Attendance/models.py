from django.db import models


class Contact(models.Model):
    image = models.ImageField(upload_to='attendance_images/',blank=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    age=models.IntegerField()
    phoneNumber=models.IntegerField()
    position=models.CharField(max_length=50)
    def __str__(self):
        return self.name
