from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField("タスク名", max_length=20)
    description = models.TextField("詳細", blank=True)
    status = models.BooleanField("状態")

    def __str__(self):
        return self.title