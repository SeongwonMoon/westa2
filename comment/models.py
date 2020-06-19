from django.db import models
from signup.models import Users

# Create your models here.
class Comments(models.Model):
    name = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment = models.CharField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'user_comments'
