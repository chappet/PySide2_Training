'''
Created on 15 nov. 2019

@author: cchappet

Display a simple QWidget
'''
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication

import PySide6
print (PySide6.__version__)

    
if __name__ == "__main__":
    app = QApplication(sys.argv) # Création de l'environnement graphique

    wd = QtWidgets.QWidget() # Création d'une widget

    wd.show() # Affichage de la widget

    sys.exit(app.exec()) # Lancement de l'environnement graphique (affichage et gestion des évènements)
    # sys.exit n'est pas obligatoire mais c'est une bonne pratique

# GUESS : Que se passe t'il quand on ferme la widget ?
# GUESS : Que se passe t'il si on commente wd.show() ?