# this script was created to accomplish,
# reorganising a single folder of video files into folders with the same name as the files.
# multiple files of the same name, with different extensions should be organised into single folders e.g. video, project, metadata files

import os
import shutil

# s = enter the full path to the root directory containing your unsorted files inc trailing slash e.g. /path/to/your/folder/
# d = enter the full path to the root directory where you want your sorted files inc trailing slash e.g. /path/to/your/folder/.
# d folder can be the same as s.
# extensions = only extensions listed in this variable will be sorted.
extensions = ["mkv","mp4","avi","srt"]
move = False

if input('The default extensions are {}, would you like to use custom values? y/n: '.format(extensions)) == "y":
	extensions = input('Enter extensions in comma separated format i.e. mkv,avi,mp3: ').split(",")
print(extensions)

def set_folders(direction):
	check = False
	path = ""
	while check == False:
		path = input("Type the full path to your {} directory inc trailing slash e.g. /path/to/directory/ : ".format(direction))
		if os.path.isdir(path) == False:
			print("Please enter a valid folder path")
		elif path[-1] != "/":
			path = path + "/"
			print("Your selected {} folder is {}".format(direction,path))
			return path
		else:
			print("Your selected {} folder is {}".format(direction,path))
			return path

s = set_folders("source")
d = set_folders("destination")

if input("Would you like to move the files (default is to copy)? y/n: ") == "y":
	move = True

# walk the files, run checks on extensions, directories etc and buld useful file paths
for fn in os.listdir(s):
	fullpath = str(s + fn)
	filenamelist = fn.split(".")
	print("----------------------------------------------")
	print(fn,filenamelist,len(filenamelist))

	if os.path.isdir(fullpath) == True:
		print("This is a directory and will be ignored")
		print("")

	elif filenamelist[-1] not in (extensions):
		print("This file isn't an allowed type and will be skipped. If you want it included, add the extension to the var 'extensions'")
		print("")

	elif filenamelist[-1] in (extensions) and len(filenamelist) > 1:
		ext = filenamelist.pop()
		namejoined = " ".join(filenamelist)
		namefixed = namejoined.title()
		print('The filename is:',namefixed, '. The extension is: ', ext)

# now we have a valid file and filename, we do the sorting
		newfolder = os.path.join(d,namefixed)
		newfile = os.path.join(newfolder,namefixed + "." + ext)
		print(newfolder)
		print(fullpath)
		print(newfile)

		if not os.path.isdir(newfolder):	# if no existing folder, create it
			os.makedirs(newfolder)
			print("Folder",namefixed,"created.")
			if move == True:
				os.rename(fullpath,newfile)
				print("file moved to new directory")
			else:
				try:
					shutil.copy(fullpath,newfile)
				except IOError as e:
					print("Unable to copy file. %s" % e)
				except:
					print("Unexpected error:", sys.exc_info())
		else:
			if move == True:
				os.rename(fullpath,newfile)
				print("file moved to new directory")
			else:
				try:
					shutil.copy(fullpath,newfile)
				except IOError as e:
					print("Unable to copy file. %s" % e)
				except:
					print("Unexpected error:", sys.exc_info())
