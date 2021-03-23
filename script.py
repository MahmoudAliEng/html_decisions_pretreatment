from bs4 import BeautifulSoup
from os import walk
from sys import argv

for i in range(1,len(argv)):
    folder = 'data\\'+argv[i]+'\\'
    print(folder)
    output_folder = folder + 'cleaned\\'

    _, _, filenames = next(walk(folder))

    for filename in filenames:
        f = open(folder + filename, 'r')
        file_content = f.read()
        f.close()
        soup = BeautifulSoup(file_content , features="html.parser")
        try:
            div = soup.find("div", {"id": "jurisprudence"})
            content = str(div.get_text())
        except Exception as e:
            print(filename)
        f = open(output_folder + filename.split('.')[0] +'.txt', 'w', encoding='utf-8')
        f.write(content)
        f.close()
