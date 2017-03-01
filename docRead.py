#! python3
# _*_ coding: utf_8  _*_

import logging
import os
import re
import docx

logging.basicConfig( level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s' )
# logging.basicConfig( level = logging.ERROR, format = ' %(asctime)s - %(levelname)s - %(message)s' )


class testpaper():
    """    compose test paper.
    """
    def __init__(self):
        # initial.
        self.lines = []
        
    def readdoc(self, sourcefile):
        # read the text content in the given file.        
        with open(sourcefile, 'rb') as srcfile:
            for line in srcfile.readlines():
                self.lines.append(line)
                
    def writedoc(self, destfile):
        # write the text content in the given file.        
        with open(destfile, 'wb') as dstfile:
            for line in self.lines:
                dstfile.writelines(line)
                input('test2')
                
##  File "D:\_PythonWorks\testpaper\docRead.py", line 34, in writedoc
##    dstfile.writelines(line)
##TypeError: 'int' does not support the buffer interface

            
def main():
    SRCDIR = 'd:\\_PythonWorks\\testpaper\\data\\模拟电子技术基础试卷1-稳压管.DOC'
    DSTDIR = 'd:\\_PythonWorks\\testpaper\\data\\testpaper-稳压管.DOC'
    paperA = testpaper()
    paperA.readdoc(SRCDIR)
    input('finish readdoc')
    paperA.writedoc(DSTDIR)
    input('finish writedoc')

if __name__ == '__main__':
    logging.critical('--------Start of program---------')
    main()
    logging.critical('--------End---------')
