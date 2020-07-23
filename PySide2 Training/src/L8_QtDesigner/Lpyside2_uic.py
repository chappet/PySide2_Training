
import os
import logging
import glob

EXE_CMD = 'C:\python3\Scripts\pyside2-uic.exe'


def Convert2ui(sFileName):
    try:
        if os.path.isfile(EXE_CMD): 
            sFileNameOut = os.path.basename(sFileName).replace('ui','py')
            command = "{} {} -o {}".format(EXE_CMD, sFileName, sFileNameOut)
            os.system(command)
            logging.info('OK')
        else:
            logging.error("Executable %s does not exist"%EXE_CMD)
    except:
        logging.exception('Unable to convert uic to py !')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    for sFileName in glob.glob("./ui/*.ui"):
        print ("Convert {}".format(sFileName))
    
        Convert2ui(sFileName)
