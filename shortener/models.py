import random
import string
from django.db import models
from .utils import code_generator, create_shortcode

# Create your models here.
class YektanetURL(models.Model):
	url = models.CharField(max_length = 220,)
	shortcode = models.CharField(max_length = 15, unique = True, blank = True)
	timestamp = models.DateTimeField(auto_now_add = True)
	update = models.DateTimeField(auto_now = True)
	update = models.DateTimeField(auto_now_add = False, auto_now = False)

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode =='':
			self.shortcode = create_shortcode(self)
		super(YektanetURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)

	