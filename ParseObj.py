import os
import sys

def main():

    check_args_number()
    
    #parse arg
    paths = sys.argv[1]
    function = sys.argv[2]

    check_path_corect(paths)

    parse_func(paths, function)
    
    for each in files:
        print(each)
        
    print("Element with = ", len(files))

files = []

def parse_func(paths, function):
    """Can decline acccess in directory"""
    for path in os.listdir(paths):
        if os.path.isdir(paths+path+"\\"):
            parse_func(paths+path+"\\",function)
            continue
            print("Check directory ", paths+path)
        if os.path.isfile(paths+path):
            f = open(paths+path, 'br')
            if function.encode('utf-8') in f.read():
                files.append(paths+path)
            f.close()
            print("Check file ", paths+path)
        # If have func - append in array

def check_path_corect(paths):
    """checks if the path is correct"""
    if not os.path.exists(paths):
        print("Path missed!")
        exit()

def check_args_number():
    """check args"""
    if len(sys.argv) < 3:
        print("Use args: path function")
        exit()



    
if __name__ == "__main__":
    main()
