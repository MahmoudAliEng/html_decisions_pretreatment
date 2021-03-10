from bs4 import BeautifulSoup

folder = 'data\\sortie 10-03-2021\\'
output_folder = 'data\\cleaned 10-03-2021\\'

f = open(folder + '1.html', 'r')
file_content = f.read()
f.close()
soup = BeautifulSoup(file_content , features="html.parser")
div = soup.find("div", {"id": "jurisprudence"})
content = str(div.get_text())
f = open(output_folder + '1.txt', 'w')
f.write(content)
f.close()
