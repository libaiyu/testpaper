# _*_ coding: utf_8  _*_
#! python3
# try to write some content to a new Word document.

import docx
import getfilename

def addruns( filename, runs):
    # Add runs to a paragraph.
    doc = docx.Document(filename)
    for r in runs:
        doc.add_paragraph('  ').add_run(r)
    doc.save( filename)

def writepara( filename, para):
    # Write a paragraph to a new document.
    doc = docx.Document()
    doc.add_paragraph(para)
##    paraobj3 = doc.add_paragraph( 'This is a paraObj3.')
##    paraobj4 = doc.add_paragraph( 'This is a paraObj4.')
##    paraobj3.add_run('This is being added to the paraObj3')
##    paraobj4.add_run('This is being added to the paraObj4')
    doc.save( filename)
    

def main():
    # DSTDOC = 'writetestdoc.docx'
    DSTDOC = getfilename.getfilename('destinationfile')
    PARA = ['This is a paraObj1 on the first page!', 'This is a paraObj2.']
    writepara( DSTDOC, PARA)
    input('input anything')
    RUNS = ['This is being added to the paraObj1', 'This is being added to the paraObj2']
    addruns( DSTDOC, RUNS)

if __name__ == '__main__':
    main()
    





