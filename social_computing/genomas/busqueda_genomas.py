import os

dir = "C:/Users/sergi/Desktop/misia/social_computing/genomas/genomas"

def buscar(dir, txt="wax synthase"):
    for name_dir, dirs, files in os.walk(dir):
        for name_file in files:
            extension = os.path.splitext(name_file)[1]
            if extension == ".txt":
                path = name_dir + "/" + name_file
                print(path)
                with open(path, 'r') as f:
                    for line in f.readlines():
                        if txt in line:
                            print(line)


buscar(dir)
