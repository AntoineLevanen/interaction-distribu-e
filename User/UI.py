# -*- coding: utf-8 -*-
"""
Prototype de logiciel pour suivre les sessions d'observation de l'OJBT.
Auteur: Alexis ZEMB
"""
import sys
import qtmodern.windows
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel
from qtmodern import styles
from qtpy import QtCore, QtGui
from datetime import datetime

path_logo = "Images_UI/upssitech.png"

class UserWindow(QMainWindow):
    """///////////////////////////// Fenêtre principale pour l'utilisateur ///////////////////////////////////"""
    def __init__(self, callback=None):
        super().__init__()

        self.callback = callback

        self.setFixedSize(400, 510)

        self.background = QtWidgets.QLabel(self)
        self.background.setGeometry(0, -10, 400, 550)
        self.background.setStyleSheet("background-color: rgb(34, 34, 34);border-radius:5px;")

        """Logo de l'upssitech sur l'interface"""
        self.label_logo = QtWidgets.QLabel(self)
        self.label_logo.setGeometry(100, 0, 200, 75)
        image = QtGui.QPixmap(path_logo)
        scaled_image = image.scaled((self.label_logo.size()), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label_logo.setPixmap(scaled_image)

        """Label du pseudo de l'utilisateur"""
        self.label_pseudo = QLabel(self)
        self.label_pseudo.setText("Votre pseudo: ")
        self.label_pseudo.setStyleSheet("font-weight:bold;color: rgb(255,255,255)")
        self.label_pseudo.setGeometry(5, 80, 200, 30)

        """Widget d'entrée du pseudo de l'utilisateur"""
        self.entree_pseudo = QtWidgets.QLineEdit(self)
        self.entree_pseudo.setGeometry(120, 80, 270, 30)
        self.entree_pseudo.setStyleSheet("color: rgb(255,255,255); background-color: rgb(67, 68, 83)")

        """Label du pseudo de l'utilisateur"""
        self.label_message = QLabel(self)
        self.label_message.setText("Votre message: ")
        self.label_message.setStyleSheet("font-weight:bold;color: rgb(255,255,255)")
        self.label_message.setGeometry(5, 120, 200, 30)

        """Widget d'entrée du pseudo de l'utilisateur"""
        self.entree_message = QtWidgets.QTextEdit(self)
        self.entree_message.setGeometry(5, 150, 390, 300)
        self.entree_message.setStyleSheet("color: rgb(255,255,255); background-color: rgb(67, 68, 83)")

        """Bouton d'envoi du message"""
        self.btn_envoi = QtWidgets.QPushButton(self)
        self.btn_envoi.setText("Envoyer")
        self.btn_envoi.setGeometry(5, 465, 390, 30)
        self.btn_envoi.setStyleSheet("font-weight:bold; color: rgb(255,255,255); background-color: rgb(17, 184, 0); border-radius: 15px")
        self.btn_envoi.clicked.connect(self.send_msg)

    def send_msg(self):
        """Fonction appelée lors de l'appui sur le bouton d'envoi"""
        if (self.entree_message.toPlainText() != '') and (self.entree_pseudo.text() != ''):
            pseudo = self.entree_pseudo.text()
            msg = self.entree_message.toPlainText()
            t = datetime.now()
            t = t.strftime('%H:%M:%S')
            self.entree_message.clear()

            # Appeler la fonction de rappel avec le message en paramètre
            if self.callback:
                self.callback(str(t)+'#'+str(pseudo)+'#'+str(msg))
