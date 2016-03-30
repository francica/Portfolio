class Project:
	title = ""
	date = ""
	version = 0
	summary = ""
	files = []

	def __init__(self, t, d, v):
		self.title = t
		self.date = d
		self.version = v
		self.files = []

class File:
	size = 0
	type = ""
	path = ""
	versions = []

	def __init__(self, s, t, p):
		self.size = s
		self.type = t
		self.path = p
		self.versions = []

class Version:
	revision = 0
	author = ""
	msg = ""
	date = ""

	def __init__(self, r, a, m, d):
		self.revision = r
		self.author = a
		self.msg = m
		self.date = d

import xml.etree.ElementTree

def loadAndParse(xmlList, xmlLog):
	projects = {}
	r = xml.etree.ElementTree.parse(xmlList).getroot()
	Alist = r[0]

	for entry in Alist:
		if entry.attrib["kind"] == "dir":
			name = entry.find("name").text
			if name.find('/') == -1:
				newProject = Project(name, entry.find("commit").find("date").text, entry.find("commit").attrib["revision"])
				projects[name] = newProject
		elif entry.attrib["kind"] == "file":
			path = entry.find("name").text
			size = int(entry.find("size").text)
			name = path[path.rfind('/'): ]
			projectName = path[0: path.find('/')]
			type = name[name.rfind('.')+1: ]
			newFile = File(size, type, path)
			projects[projectName].files.append(newFile)

	r = xml.etree.ElementTree.parse(xmlLog).getroot()
	for logentry in r:
		revision = int(logentry.attrib["revision"])
		author = logentry.find("author").text
		date = logentry.find("date").text
		paths = logentry.find("paths")
		msg = ""
		if logentry.find("msg") != None:
			msg = logentry.find("msg").text
		for path in paths:
			if path.attrib["kind"] == "file":
				fileName = path.text.strip()
				fileName = fileName[1:]
				fileName = fileName[fileName.find('/')+ 1: ]
				projectName = fileName[0: fileName.find('/')]
				version = Version(revision, author, msg, date)
				for f in projects[projectName].files:
					if f.path == fileName:
						f.versions.append(version)

	return projects