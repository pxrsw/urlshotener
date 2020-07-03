import random
import string
from django.db import models

def code_generator(size = 6, chars = string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


# Create your models here.
class YektanetURL(models.Model):
	url = models.CharField(max_length = 220,)
	shortcode = models.CharField(max_length = 15, unique = True)
	timestamp = models.DateTimeField(auto_now_add = True)
	update = models.DateTimeField(auto_now = True)
	update = models.DateTimeField(auto_now_add = False, auto_now = False)

	def save(self, *args, **kwargs):
		print('test')
		self.shortcode = code_generator()
		super(YektanetURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)

	