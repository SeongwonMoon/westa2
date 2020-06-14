from django.db import models

# Create your models here.
class Comments(models.Model):
    name = models.CharField(max_length = 50)
    comment = models.CharField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'user_comments'
