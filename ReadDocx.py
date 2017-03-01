# _*_ coding: utf_8  _*_
#! python3
# read and print the docx successfully. 2017-2-26
# but 若用p=ui算得的功率值为 -_  5W, before 5W a symbol is missing.
# pictures will missing. subscript can not display correctly.

import docx

def getparas(filename):
    # read the paregraphs in the given document.
    doc = docx.Document(filename)
    fullparas = []
    for para in doc.paragraphs:
        fullparas.append('  '+para.text)
    return '\n'.join(fullparas)

def getruns(filename, row):
    # read the runs.
    doc = docx.Document(filename)
    run_ = ''
    for k in range(len(doc.paragraphs[row].runs)):
        print(k, doc.paragraphs[row].runs[k].text, ' ')   #
        run_ += doc.paragraphs[row].runs[k].text
    return run_

def getpara(filename, row):
    # read the given paragraph.
    doc = docx.Document(filename)
    return doc.paragraphs[row].text

def main():
##    SRCDOC = 'testDoc-电路ch1.docx'
    import getfilename
    SRCDOC = getfilename.getfilename('sourcefile')
    paras = getparas(SRCDOC)
    print(paras[0:60])
    input('\n...............')
    for k in range(len(paras)):
        print(paras[k], end='')
    print('\n', k)
    input('\n...............')
    for k in range(11):
        line = getpara(SRCDOC, k)
        print(k, line)
    input('\n...............')
    for k in range(8):
        run = getruns(SRCDOC, k)
        print('\n', k, run, '\n')

if __name__ == '__main__':
    main()
