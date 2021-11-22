import os

def list_dicoms(scr,key,value)

    file_list = []
    for root, dirs, files in os.walk(src): 
        for file in files: 
            if ".dcm" in file:
                ds = load_header(file)
                if (ds[key]==value):
                    file_list.append(os.path.join(root, file))
    return file_list


