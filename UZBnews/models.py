from django.db import models

# create model class


from django.db import models


class KunlikNewuz(models.Model):
    text = models.TextField(null=False, max_length=255)  # Removed max_length for TextField
    time_create = models.DateTimeField(auto_now_add=True)  # Changed to DateTimeField
    photo = models.ImageField(null=False, upload_to='images/')  # Changed to ImageField and corrected upload_to path
    autor = models.CharField(max_length=255, null=False)  # Added max_length for CharField
    def __str__(self):
        _ = f"{self.time_create} : {self.autor}"
        return _
# Create your models here.
