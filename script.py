from bs4 import BeautifulSoup
from os import walk

folder = 'data\\sortie 10-03-2021\\'
output_folder = 'data\\cleaned 10-03-2021\\'

_, _, filenames = next(walk(folder))

for filename in filenames:
    f = open(folder + filename, 'r')
    file_content = f.read()
    f.close()
    soup = BeautifulSoup(file_content , features="html.parser")
    div = soup.find("div", {"id": "jurisprudence"})
    content = str(div.get_text())
    f = open(output_folder + filename.split('.')[0] +'.txt', 'w', encoding='utf-8')
    f.write(content)
    f.close()
