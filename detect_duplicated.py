
from os import walk
from json import dump

folder = 'data\\cleaned 10-03-2021\\'

def detect_duplicated_decisions():
    _, _, filenames = next(walk(folder))
    duplicated = {}
    for filename in filenames:
        f = open(folder + filename, 'r')
        file_content = f.read()
        f.close()
        for filename2 in filenames:
            if (filename != filename2):
                f2 = open(folder + filename, 'r')
                file_content2 = f2.read()
                f2.close()
                if (file_content2 == file_content and filename not in duplicated):
                    duplicated[filename] = filename2
    print(len(duplicated))
    with open(folder + '\\duplicated_files.json', 'w', encoding='utf-8') as f:
        dump(duplicated, f, indent=4)
