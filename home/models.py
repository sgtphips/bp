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
		return self.text

# Need to add employment dates to this model
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
		return self.exp_title
		
# Need to add attendance dates and major to this model
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
		return self.school_title


class Skill(models.Model):
	author = models.ForeignKey('auth.User')
	skill = models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.skill

# Need to add date when aquired certification
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
		return self.cert_title
