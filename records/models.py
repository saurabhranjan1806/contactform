# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Info(models.Model):

	firstName = models.CharField(max_length = 30)
	lastName = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.firstName