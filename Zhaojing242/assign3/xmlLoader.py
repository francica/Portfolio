from utils import * 
import xml.etree.ElementTree
#####THIS IS ONLY FOR XML PARSE TEST!!!
#####

def loadAndParse():
	projects = {}
	r = xml.etree.ElementTree.parse('svn_list.xml').getroot()
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

	r = xml.etree.ElementTree.parse('svn_log.xml').getroot()
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
						print "yes!"
	return projects

proj = loadAndParse()
print proj["Assignment1.1"].files[0].versions[0].date