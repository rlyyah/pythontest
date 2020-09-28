import os, glob

# Great way to operate on lists
a_list = [1,9,18,4]
print(a_list)
b_list = [num **2 for num in a_list]
print(b_list)

# Finding files of particular extension
txt_file_path_list = [os.path.realpath(f) for f in glob.glob('*.txt')]
print(txt_file_path_list)

# You can even add a condition into the list
txt_files_list_under_6000 = [f for f in glob.glob('*.txt') if os.stat(f).st_size < 6000]
print(txt_file_path_list)

# Creating tuples of file size and path and packing it into a list
file_sizes_and_paths = [(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.txt')]
print(file_sizes_and_paths)
