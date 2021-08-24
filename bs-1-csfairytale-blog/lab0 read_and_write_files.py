import os

# ENTER your filename here
filename = 'fileA.txt'
# Then, what about filenames containing spaces?
filename = 'file A.txt' 
# , works well in the follownig code =)
filename = 'fileA.html'
# , also works

# --------------------------
code_dir = os.path.dirname(__file__)
print('code_dir = ' + code_dir)
file_path = os.path.join(code_dir, filename)

# f = open('fileA.txt','w');
with open(file_path,'w') as f:
    data_write = 'This is the data in fileA.txt. \n'
    f.write(data_write)

with open(file_path,'r') as f:
    data_read = f.read()
    print(data_read)


# --------------------------
def read_file_from_current_dir(filename):
    filename = filename
    code_dir = os.path.dirname(__file__)
    # print('code_dir = ' + code_dir)
    file_path = os.path.join(code_dir, filename)

    with open(file_path,'r') as f:
        data_read = f.read()
    #print(data_read)
    return data_read


read_file_from_current_dir(filename)
