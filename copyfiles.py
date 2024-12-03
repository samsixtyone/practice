import os,re

def write_data(source, destination):
    if not os.path.isdir(destination):
        os.mkdir(destination, 666)

    for file in os.listdir(source):
        if re.search("File.*txt", file):
            with open(source+'/'+file,'r') as f, open(destination+'/'+file,'a') as s:
                for line in f:
                    s.write(line)

write_data('FolderA','FolderC')
write_data('FolderB','FolderC')
