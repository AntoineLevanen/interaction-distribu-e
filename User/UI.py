# -*- coding: utf-8 -*-
"""
Prototype de logiciel pour suivre les sessions d'observation de l'OJBT.
Auteur: Alexis ZEMB
"""
import sys
import qtmodern.windows
from PyQt5 import QtWidgets, Qt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel
from qtmodern import styles
from qtpy import QtCore, QtGui
from datetime import datetime

path_logo = "Images_UI/upssitech.png"

class UserWindow(QMainWindow):
    """///////////////////////////// Fenêtre principale pour l'utilisateur ///////////////////////////////////"""
    def __init__(self, callback_message=None):
        super().__init__()

        self.callback_message = callback_message

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
        self.entree_message.setGeometry(5, 150, 390, 150)
        self.entree_message.setStyleSheet("color: rgb(255,255,255); background-color: rgb(67, 68, 83); border-radius:10px;")


        self.add_img_btn = QtWidgets.QPushButton(self)
        self.add_img_btn.setText("+ image")
        self.add_img_btn.setGeometry(5, 305, 100, 30)
        self.add_img_btn.setStyleSheet("QPushButton {background-color: rgb(211, 211, 211); color: rgb(0, 0, 0);font-weight: bold; "
            "border-radius: 15} QPushButton:pressed {background-color: lightblue;}")
        self.add_img_btn.clicked.connect(self.send_img)

        self.add_img_field = QtWidgets.QLineEdit(self)
        self.add_img_field.setPlaceholderText("https://image.jpg...")
        self.add_img_field.setGeometry(110, 305, 285, 30)
        self.add_img_field.setStyleSheet(
            "color: rgb(255,255,255); background-color: rgb(67, 68, 83); border-radius:5px; font-weight:bold;")

        self.btn_add_note = QtWidgets.QPushButton(self)
        self.btn_add_note.setText("+ note")
        self.btn_add_note.setGeometry(5, 340, 100, 30)
        self.btn_add_note.setStyleSheet("QPushButton {background-color: rgb(211, 211, 211); color: rgb(0, 0, 0);font-weight: bold; "
            "border-radius: 15} QPushButton:pressed {background-color: lightblue;}")
        self.btn_add_note.clicked.connect(self.send_note)

        self.add_note_field = QtWidgets.QTextEdit(self)
        self.add_note_field.setPlaceholderText("Ajoutez une note ici...")
        self.add_note_field.setGeometry(110, 340, 285, 120)
        self.add_note_field.setStyleSheet(
            "color: rgb(255,255,255); background-color: rgb(67, 68, 83); border-radius:5px; font-weight:bold;")

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

            url_img = self.add_img_field.text()
            note = self.add_note_field.toPlainText()

            # Appeler la fonction de rappel avec le message en paramètre
            if self.callback_message:
                self.callback_message('0', str(t)+'#'+str(pseudo)+'#'+str(msg))


    def send_img(self):
        str_url = str(self.add_img_field.text())
        if self.callback_message:
            self.callback_message('1', str_url)

    def send_note(self):
        str_note = str(self.add_note_field.toPlainText())
        if self.callback_message:
            self.callback_message('2', str_note)