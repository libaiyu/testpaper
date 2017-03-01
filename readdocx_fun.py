# _*_ coding: utf_8  _*_
#! python3
# read and print the docx successfully. 2017-2-26
# but 若用p=ui算得的功率值为 -_  5W, before 5W a symbol is missing.

import docx

def getparas(filename):
    doc = docx.Document(filename)
    fullparas = []
    for para in doc.paragraphs:
        fullparas.append('  '+para.text)
    return '\n'.join(fullparas)

