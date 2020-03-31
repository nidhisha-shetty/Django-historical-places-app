from django.db import models

# Create your models here.
class Places(models.Model):
	place_name = models.TextField(max_length=100, default="Please add name");
	place_ratings = models.IntegerField(null=True, default=2)
	place_image = models.ImageField(upload_to="images/", default="images/Varanasi-River-Gange")
	place_description = models.TextField(max_length=50, default="Please add description")