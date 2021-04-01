import hashlib
from bs4 import BeautifulSoup
from os import walk, makedirs, remove
from os.path import exists
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

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') #%(name)s => logger name
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    # Converting to text files
    for i in range(1,len(argv)):
        folder = 'data\\'+argv[i]+'\\'
        logger.info('\n\n##########\tTreating {} folder...\t##########\n'.format(folder))
        output_folder = folder + 'cleaned\\'
        if not exists(output_folder):
            makedirs(output_folder)

        _, _, filenames = next(walk(folder))

        for filename in filenames:
            f = open(folder + filename, 'r')#, encoding='utf-8')
            file_content = f.read()
            f.close()
            soup = BeautifulSoup(file_content , features="html.parser")
            try:
                div = soup.find("div", {"id": "jurisprudence" }) #"cCn"}) # cCn if lamy line and jurisprudence if other
                content = str(div.get_text())
            except Exception as e:
                logger.error('Can not find content in this file: "{0}", error: {1}'.format(filename, e))
            f = open(output_folder + filename.split('.')[0] +'.txt', 'w', encoding='utf-8')
            f.write(content)
            f.close()

    # Remove duplicated files
    for i in range(1,len(argv)):
        folder = 'data\\'+ argv[i]+'\\cleaned\\'
        logger.info('Detecting duplicate decisions in {} folder...'.format(folder))
        _, _, filenames = next(walk(folder))
        files_hashes = dict()

        for filename in filenames:
            file_hash = md5(folder + filename)
            if file_hash not in files_hashes:
                files_hashes[file_hash] = filename
            else :
                logger.warning(f'{filename} is duplicated with {files_hashes[file_hash]}')
                remove(folder + filename)

        logger.info(f'\n\n\tThis folder {folder} contains {len(files_hashes)} files now')
