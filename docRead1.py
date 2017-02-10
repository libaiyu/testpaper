# _*_ coding: utf_8  _*_
#! python3


import logging
import os,re
import docx,PyPDF2
import pprint


logging.basicConfig( level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s' )

logging.critical('--------Start of program---------')



def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
