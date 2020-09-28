import os, glob, humansize

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

# Using external function in the list
just_another_list = [(humansize.approximate_size(os.stat(f).st_size), os.path.realpath(f)) for f in glob.glob('*.txt')]
print(just_another_list)

# Dictionary Comprehensions
metadata = [(f, os.stat(f)) for f in glob.glob('*.txt')]
print()
print(metadata)
metadata_dict =  {f: os.stat(f) for f in glob.glob('*.txt')}
print(metadata_dict)
print(metadata_dict.keys())
print()
print(metadata_dict['kappa.txt'])

# Dictionary Comprehensions with conditions

humansize_dict = {os.path.splitext(f)[0]:humansize.approximate_size(meta.st_size) for f, meta in metadata_dict.items() if meta.st_size < 6000}
print()
print(humansize_dict)

# Swapping keys with items in dict
a_dict = {'a':1,'b':2, 'c':3,'d':4}
print(a_dict)
print()
print(a_dict.items())
b_dict = {value:key for key, value in a_dict.items()}
print(b_dict)

# Set comprehation
a_set = set(range(10))
print(a_set)
b_set = {num **2 for num in a_set}
print(b_set)
c_set = {num for num in a_set if num%2==0}
print(c_set)
