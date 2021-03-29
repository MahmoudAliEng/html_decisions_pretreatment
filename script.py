from bs4 import BeautifulSoup
from os import walk, makedirs
from os.path import exists
from sys import argv

for i in range(1,len(argv)):
    folder = 'data\\'+argv[i]+'\\'
    print(folder)
    output_folder = folder + 'cleaned\\'
    if not exists(output_folder):
        makedirs(output_folder)

    _, _, filenames = next(walk(folder))

    for filename in filenames:
        f = open(folder + filename, 'r', encoding='utf-8')
        file_content = f.read()
        f.close()
        soup = BeautifulSoup(file_content , features="html.parser")
        try:
            div = soup.find("div", {"id": "cCn" }) #"jurisprudence"})
            content = str(div.get_text())
        except Exception as e:
            print(filename)
        f = open(output_folder + filename.split('.')[0] +'.txt', 'w', encoding='utf-8')
        f.write(content)
        f.close()
