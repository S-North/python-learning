# this script was created to accomplish,
# reorganising a single folder of video files into folders with the same name as the files.
# multiple files of the same name, with different extensions should be organised into single folders e.g. video, project, metadata files

import os

# get the list of files and folders on the given path
# this should be improved to deal with files with more than one period i.e. file extension checking

path = '/media/fileserver/films/'
for fn in os.listdir(path):
	filename, extension = os.path.splitext(fn)
#	print("filename & extension is ",filename, " ", extension)



	src = path+fn
	dst = path+filename+"/"+fn
	folder = path+filename

	if not os.path.isdir(os.path.join(folder)):
		continue
#		print("")
#		print("source is ",src)
#		print("create folder at ",folder)
#		print("and move file to ",dst)
#		os.makedirs(folder)
#		os.rename(src,dst)
	else:
		continue
#		print("")
#		print("source is ",src)
#		print("folder already exists at ",folder)
#		print("moving file to folder")
#		os.rename(src,dst)
