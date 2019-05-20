# this script was created to accomplish,
# reorganising a single folder of video files into folders with the same name as the files.
# multiple files of the same name, with different extensions should be organised into single folders e.g. video, project, metadata files

import os
# s = enter the full path to the root directory containing your unsorted files. no training slash e.g. /path/to/your/folder
# d = enter the full path to the root directory where you want your sorted files. This can be the same as s. no training slash e.g. /path/to/your/folder
# extensions = only extensions listed in this variable will be sorted.
extensions = ["mkv","mp4","avi","srt"]
s = "/home/stuart/python-rename-folder/src-folder"
d = "/home/stuart/python-rename-folder/dst-folder"

# get the list of files and folders on the given path
# this should be improved to deal with files with more than one period i.e. file extension checking
for fn in os.listdir(s):
	fullpath = str(s + "/" + fn)
	filename = fn.split(".")
	print(filename,len(filename))

	if os.path.isdir(fullpath) == True:
		print("This is a directory")
		print("")

	elif filename[-1] in (extensions) and len(filename) > 1:
		ext = filename.pop()
		name = " ".join(filename)
		print('the extension is: ', ext)
		print('the filename is: ', " ".join(filename))
		print("")
	else:
		print("This file isn't an allowed type")
		print("")


#	if filename[-1] in ('mkv','mp4','avi'):
#		print('file has a video file extension')
#	else:
#		print("file doesn't have a video file extension")
#
#	if len(filename) == 2:
#		print('filename has 1 split on a period')
#	elif len(filename) > 2:
#		print('filename has more than 1 splits on a period')
#	else:
#		print('filename has NO splits on a period')

#	print('')






#	filename, extension = os.path.splitext(fn)
#	print("filename & extension is ",filename, " ", extension)
#
#	src = path+"/"+fn
#	print("source is ",src)
#
#	dst = path+"/"+filename+"/"+fn
#
#	folder = path+"/"+filename
#	print("destination is ",dst)
	#if not os.path.isdir(os.path.join(folder)):
	#	print("no folder at ",folder)
	#	os.makedirs(folder)
	#	os.rename(src,dst)
	#else:
	#	print("folder exists at ",folder)
	#	os.rename(src,dst)
