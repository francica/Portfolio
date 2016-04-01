from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from utils import *
import os
import sys
import json
from django.conf import settings as se
from .models import *

# Create your views here.
def index(request):
	return render(request, 'land/index.html')

def secret(request):
	try:
		projects = loadAndParse(os.path.join(se.PROJECT_ROOT, 'svn_list.xml'), os.path.join(se.PROJECT_ROOT, 'svn_log.xml'))
		for key, project in projects.iteritems():
			print (1)
			p = Project.objects.create(project_title=project.title, project_date=project.date, project_version=project.version, project_summary=project.summary)
			p.save()
			print (2)
			for file in project.files:
				print (3)
				f = File.objects.create(file_size=file.size, file_type=file.type, file_path=file.path, project=p)
				f.save()
				print (4)
				for version in file.versions:
					print (version.revision)
					print (version.author)
					print (version.msg)
					print (version.date)
					v = Version.objects.create(version_revision=version.revision, version_author=version.author, version_msg=version.msg, version_date=version.date, file=f )
					print (5.5)
					v.save()
					print (6)
		return HttpResponse("success")
	except:
		return HttpResponse("fail")


def project(request, project_id):
	'''
	if request.method=="POST":
		username = request.POST['username']
		content = request.POST['content']
		c = Comment.objects.create(comment_username=username, comment_content=content, project=Project.objects.get(pk=project_id))
		c.save()
		comments = Comment.objects.filter(project_id=project_id)
		files = File.objects.filter(project_id=project_id).prefetch_related('version_set')
		#return render(request, 'assign3/project2.html', {"files": files, "project_id":project_id, "comments":comments})
		'''

	comments = Comment.objects.filter(project_id=project_id)
	files = File.objects.filter(project_id=project_id).prefetch_related('version_set')
	return render(request, 'assign3/project2.html', {"files": files, "project_id":project_id, "comments":comments})

def content(request):
	projects = Project.objects.all()
	return render(request, 'assign3/index.html', {"projects": projects})

def forAjax(request):
	if request.method=="POST":
		username = request.POST['user']
		content = request.POST['comment']
		project_id = request.POST['project_id']
		c = Comment.objects.create(comment_username=username, comment_content=content, project=Project.objects.get(pk=project_id))
		c.save()
		comments = Comment.objects.filter(project_id=project_id)
		files = File.objects.filter(project_id=project_id).prefetch_related('version_set')
        return HttpResponse(json.dumps([{"user":username, "content":content}]))
'''
def forFile(request):
	if request.method=="POST":
		filePath = request.POST['file_path']
	return render(request, 'https://subversion.ews.illinois.edu/svn/sp16-cs242/jzhao18/'+filePath)
'''