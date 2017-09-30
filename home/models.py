from django.db import models
from django.utils import timezone

class Summary(models.Model):
	author = models.ForeignKey('auth.User')
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


class Experience(models.Model):
	author = models.ForeignKey('auth.User')
	exp_title = models.CharField(max_length=200)
	exp_sub_title = models.CharField(max_length=200)
	exp_skills = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class School(models.Model):
	author = models.ForeignKey('auth.User')
	school_title = models.CharField(max_length=200)
	school_info = models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


class Skill(models.Model):
	author = models.ForeignKey('auth.User')
	skill = models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


class Certification(models.Model):
	author = models.ForeignKey('auth.User')
	cert_title = models.CharField(max_length=200)
	cert_exp_date = models.DateTimeField(blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
