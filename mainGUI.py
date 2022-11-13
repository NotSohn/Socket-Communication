import socket
import sys
import socket
from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.uic import loadUi

IP = "127.0.0.1"
PORT = 3514

gui_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
gui_socket.connect((IP, PORT))

class GUI(QMainWindow):
  def __init__(self):
    super(GUI,self).__init__()
    loadUi("justinsohnGUI.ui",self)
    self.setWindowTitle('CPSC351 Assignment 4')
    self.sendMessageButton.clicked.connect(self.addTextFunction)
  
  def addTextFunction(self):
    gui_socket.send(bytes(self.msgBox.text()+ "\n", 'utf-8'))

    self.sendReceive.append('\n' + 'you: ' + self.msgBox.text() + '\n' + gui_socket.recv(1024).decode())

def main():

  app = QApplication(sys.argv)
  widget = GUI()
  widget.resize(800, 600)
  widget.show()
  sys.exit(app.exec())
if __name__ == "__main__":
  main()
  gui_socket.close()