import os, glob

#Great way to operate on lists

a_list = [1,9,18,4]
print(a_list)
b_list = [num **2 for num in a_list]
print(b_list)

#Finding files of particular extension
txt_file_path_list = [os.path.realpath(f) for f in glob.glob('*.txt')]
print(txt_file_path_list)

