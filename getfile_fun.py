#! python3

def getfilename(file):
    try:
        fullname = 'd:\\' + file + '.txt'
        filename = open( fullname).read()
    except IOError:
        print('No such file.')
        filename = input('Please input the file name:')
        f = open( fullname, 'w')
        f.write(filename)
        f.close()
        print('file name has been written in ' + fullname)
        pass
    else:
        print('We have got file name in ' + fullname)
        pass
    return filename
