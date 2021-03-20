import hashlib
from os import walk, remove
from sys import argv

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

for i in range(1,len(argv)):
    folder = 'data\\'+ argv[i]+'\\cleaned\\'
    print(folder)
    _, _, filenames = next(walk(folder))
    files_hashes = dict()

    for filename in filenames:
        file_hash = md5(folder + filename)
        if file_hash not in files_hashes:
            files_hashes[file_hash] = filename
        else :
            print(f'{filename} is duplicated with {files_hashes[file_hash]}')
            remove(folder + filename)
            

    print(len(files_hashes))
