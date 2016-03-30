from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
	project_title = models.CharField(max_length=200)
	project_date = models.CharField(max_length=200)
	project_version = models.IntegerField(default=0)
	project_summary = models.CharField(max_length=200, blank=True, null=True)

class File(models.Model):
	file_size=models.IntegerField(default=0)
	file_type = models.CharField(max_length=200)
	file_path =models.CharField(max_length=200)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Version(models.Model):
	version_revision=models.IntegerField(default=0)
	version_author=models.CharField(max_length=200)
	version_msg=models.CharField(max_length=200, blank=True, null=True)
	version_date=models.CharField(max_length=200)
	file = models.ForeignKey(File, on_delete=models.CASCADE)

class Comment(models.Model):
	comment_username=models.CharField(max_length=200)
	comment_content=models.CharField(max_length=200)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)



