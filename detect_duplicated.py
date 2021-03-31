import hashlib
from os import walk, remove
from sys import argv
import logging

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

if __name__ == '__main__':
    logger = logging.getLogger('script_logger')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages, default mode is a (create if not exists and append)
    fh = logging.FileHandler('script.log')
    fh.setLevel(logging.DEBUG)
    
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    
    # add the handlers to the logger
    logger.addHandler(fh)

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
