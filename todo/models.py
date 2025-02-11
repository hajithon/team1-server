from django.db import models
from user.models import User
from django.utils import timezone

class Todo(models.Model):
    todo_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)
    title = models.CharField(max_length=1000)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Todo'

