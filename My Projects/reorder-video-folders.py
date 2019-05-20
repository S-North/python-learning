# this script was created to accomplish,
# reorganising a single folder of video files into folders with the same name as the files.
# multiple files of the same name, with different extensions should be organised into single folders e.g. video, project, metadata files

import os

# s = enter the full path to the root directory containing your unsorted files. no training slash e.g. /path/to/your/folder
# d = enter the full path to the root directory where you want your sorted files. This can be the same as s. no training slash e.g. /path/to/your/folder
# extensions = only extensions listed in this variable will be sorted.
extensions = ["mkv","mp4","avi","srt","obs","uxv"]
s = "/home/stuart/python-rename-folder/src-folder/"
d = "/home/stuart/python-rename-folder/dst-folder/"

# get the list of files and folders on the given path
# this should be improved to deal with files with more than one period i.e. file extension checking
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
		namefixed = " ".join(filenamelist)
		print('the extension is: ', ext)
		print('the filename is:',namefixed)
		print("")

# now we have a valid file and filename, we do the sorting
		newfolder = d + namefixed
		newfile = newfolder + "/" + namefixed + "." + ext
		#print(newfolder)
		#print(fullpath)
		#print(newfile)

		if not os.path.isdir(newfolder):	# if no existing folder, create it
			print("no folder at ",namefixed)
			os.makedirs(newfolder)
			os.rename(fullpath,newfile)
		else:
			os.rename(fullpath,newfile)
