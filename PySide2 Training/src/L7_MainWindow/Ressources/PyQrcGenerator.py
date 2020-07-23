'''
Created on 30 sept. 2011

@author: rcavalier
'''

import os
import logging

BATCH_QRC = 'C:\python3\Scripts\pyside2-rcc.exe'


def genRessourcesFile():
    try:
        if os.path.isfile(BATCH_QRC): 
            command = "%s ressources.qrc -o ressources.py"%BATCH_QRC
            os.system(command)
            logging.info('OK')
        else:
            logging.error("Executable %s does not exist"%BATCH_QRC)
    except:
        logging.exception('Unable to generate ressources_rc.py because Lpyrcc4.bat does not exist!')

if __name__ == '__main__':
    
    logging.basicConfig(level=logging.INFO)
    genRessourcesFile()
