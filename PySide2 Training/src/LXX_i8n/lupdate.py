
import os
import logging
import glob

EXE_CMD = 'C:\python3\Lib\site-packages\PySide2\lupdate.exe'


def CreateTsFile(sFileName):
    try:
        if os.path.isfile(EXE_CMD): 
            sFileNameOut = os.path.basename(sFileName).replace('ui','ts')
            command = "{} {} -noobsolete -verbose -ts {}".format(EXE_CMD, sFileName, sFileNameOut)
            os.system(command)
            logging.info('OK')
        else:
            logging.error("Executable %s does not exist"%EXE_CMD)
    except:
        logging.exception('Unable to translate !')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    sFileName  = 'untitled.ui'
    CreateTsFile(sFileName)
