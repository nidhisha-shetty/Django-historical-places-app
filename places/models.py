from django.db import models

# Create your models here.
class Places(models.Model):
	place_name = models.CharField(max_length=100, default="");
	place_ratings = models.IntegerField(null=True, default="")
	place_image = models.ImageField(upload_to="images/", default="images/Varanasi-River-Gange")
	place_description = models.TextField(max_length=50, default="")