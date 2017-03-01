# _*_ coding: utf_8  _*_
#! python3
# use class ReadDocx to read the test document.

import getfilename
import readdocx
import writedocx   

def main():
    # get the docx.
    SRCDOC = getfilename.getfilename('sourcefile')
    # read the docx.
    para = readdocx.getparas(SRCDOC)

    # prepare the document.
    DSTDOC = getfilename.getfilename('destinationfile')
    # write.
    writedocx.writepara( DSTDOC, para)

if __name__ == '__main__':
    main()

    





