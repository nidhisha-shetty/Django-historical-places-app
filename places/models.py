from django.db import models

# Create your models here.
class Places(models.Model):
	place_name = models.CharField(max_length=100, default="");
	place_ratings = models.IntegerField(null=True, default="")
	place_image = models.ImageField(upload_to="images/", default="images/Varanasi-River-Gange.jpg")
	place_description = models.TextField(max_length=50, default="")

	def get_absolute_url_read(self):
		return f"/read/{self.id}/"

	def get_absolute_url_edit(self):
		return f"/edit/{self.id}/"

	def get_absolute_url_delete(self):
		return f"/delete/{self.id}/"
