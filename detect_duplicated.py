import hashlib
from os import walk

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

folder = 'data\\2021-03-19 article 1147\\cleaned\\'
_, _, filenames = next(walk(folder))
files_hashes = dict()

for filename in filenames:
    file_hash = md5(folder + filename)
    if file_hash not in files_hashes:
        files_hashes[file_hash] = filename
    else :
        print(f'{filename} is duplicated with {files_hashes[file_hash]}')

print(len(files_hashes))
