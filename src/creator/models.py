from django.db import models
from django.contrib.auth.models import User 



class Creator(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, max_length=500)
    image = models.ImageField(upload_to="uploads/creators", default = 'images/person.jpg')
    user = models.OneToOneField(User, related_name="creator", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Support(models.Model):
    creator = models.ForeignKey(Creator, related_name='supports', on_delete=models.CASCADE)
    amount = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    email = models.EmailField()
    payment_uuid = models.UUIDField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
  