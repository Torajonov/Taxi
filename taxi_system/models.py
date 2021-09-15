from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to='poster/')
	body = models.TextField()

	class Meta:
		verbose_name = 'Maqola'
		verbose_name_plural = 'Maqolalar'
		ordering = ['-id']

	def __str__(self):
		return self.title	
# Create your models here.





class Buyurtmalar(models.Model):
	name = models.CharField('Ismi', max_length=50)
	email = models.EmailField('Emaili', max_length=200)
	qayerdan = models.CharField('Qayerdan', max_length=100)
	qayergacha = models.CharField('Qayergacha', max_length=100)
	time = models.TimeField('Time', max_length=70)
	date = models.DateField('Date', max_length=80)
	CHOICES = (
        ('Cheap'),
        ('Standard'),
        ('Lux'),
        (0),
        (1),
        (2),
        (3),
)
	comfort = models.CharField(max_length=50)
	adults = models.CharField(max_length=50)
	children = models.CharField(max_length=50)
	message = models.CharField('Xabari', max_length=50)

	def __str__(self):
		return f"{self.name}"	
 
	class Meta:
		verbose_name = 'buyurtma'
		verbose_name_plural = 'buyurtmalar'




class Contact(models.Model):
	name = models.CharField('Ismi', max_length=50)
	email = models.EmailField('Emaili', max_length=200)
	phone = models.CharField('Phone', max_length=50)
	message = models.CharField('Xabari', max_length=250)

	class Meta:
		verbose_name = 'contact'
		verbose_name_plural = 'Contactlar'

	def __str__(self):
		return f"{self.email}"
