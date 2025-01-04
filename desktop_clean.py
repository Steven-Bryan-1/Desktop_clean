import os
import datetime

#directory to cycle through.  I use Desktop area to clean

directory = 'C:\\path\\to\\your\\Desktop\\'

#loop through files in directory
for filename in os.listdir(directory):
	file_path = os.path.join(directory, filename)
	print(file_path)
	creation_time = os.path.getctime(file_path)
	#you can use below to find the value to use as the cutoff 
	#print(f"File: {filename}")
	#print(f"Creation date of the file: {creation_time}")
	
	#choose the creation time as a cutoff
	if creation_time > creation_time_based_on_above_results:
		#can add this if and then an else to delete certain files or add to other sub folders in the sub folder
		#if '.txt' in file_path:
			# Delete a single file
			#os.remove(file_path)
		#hardcoded destination path
		destination = 'C:\\path\\to\\your\\Desktop\\desktop_files\\' + filename	
		#move file
		os.rename(file_path, destination)
		
