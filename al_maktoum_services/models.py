from django.db import models
from django.conf import settings

class Project(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    supervisor_name = models.CharField(max_length=255)
    supervisor_contact = models.CharField(max_length=20)
    project_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="expenses")
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    transaction_date = models.DateField(auto_now=True)
    receipt = models.FileField(upload_to="receipts/", blank=True, null=True)
