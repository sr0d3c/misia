import os

directory = "C:/Users/sergi/Desktop/misia/social_computing/genomas/genomas"


def buscar(dir, txt="wax synthase"):
    for name_dir, dirs, files in os.walk(dir):
        for name_file in files:
            show = False
            extension = os.path.splitext(name_file)[1]
            if extension == ".txt":
                path = name_dir.replace("\\", '/') + "/" + name_file
                with open(path, 'r') as f:
                    lines = []
                    for readline in f.readlines():
                        if txt in readline:
                            lines.append(readline)
                            show = True
                if show:
                    print(path)
                    for line in lines:
                        print(line)


buscar(directory)
