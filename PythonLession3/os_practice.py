import os

#print(os.uname().sysname)
#print(os.environ)

#Important!
#print(os.getcwd())

directory = os.getcwd()
#backup = directory + "/backup/"
files = os.listdir(directory)
#print(os.listdir(dir))

#print(directory + "/backup/")

def backup(path, args):
	if os.path.exists(path + "backup/") == False:
		os.system("mkdir {}".format(path + "/backup/"))
	for x in args:
		print("Copied {} to {}!".format(x, path + "/backup"))
		os.system("cp {}/{} {}/{}".format(path, x, path, "backup/"))
	
backup(directory, files)
