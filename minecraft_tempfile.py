# Manages the temp file for locations
def read_file(file):
    temp_temp = open(file).readlines()
    temp_list = [i.strip() for i in temp_temp]
    print temp_list
    return temp_list
    
def write_file(file):
    pass
    