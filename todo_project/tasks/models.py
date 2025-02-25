from django.db import models

#vytvoření modelu tabulky databáze
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="tasks_photos/", blank=True, null=True)

    def __str__(self):
        return self.title
