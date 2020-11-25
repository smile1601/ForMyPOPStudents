# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.15.1

from theoolWallet import Ui_MainWindow
from plug import Ui_plug
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Settings = QtWidgets.QMenu(self.menubar)
        self.menu_Settings.setObjectName("menu_Settings")
        self.menu_Options = QtWidgets.QMenu(self.menu_Settings)
        self.menu_Options.setObjectName("menu_Options")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Debug_window = QtWidgets.QMenu(self.menu_Help)
        self.menu_Debug_window.setObjectName("menu_Debug_window")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Encrypt_Wallet = QtWidgets.QAction(MainWindow)
        self.action_Encrypt_Wallet.setObjectName("action_Encrypt_Wallet")
        self.action_Options = QtWidgets.QAction(MainWindow)
        self.action_Options.setObjectName("action_Options")
        self.action_Command_line_option = QtWidgets.QAction(MainWindow)
        self.action_Command_line_option.setObjectName("action_Command_line_option")
        self.action_About_the_program = QtWidgets.QAction(MainWindow)
        self.action_About_the_program.setObjectName("action_About_the_program")
        self.action_About_the_library = QtWidgets.QAction(MainWindow)
        self.action_About_the_library.setObjectName("action_About_the_library")
        self.action_Encrypt = QtWidgets.QAction(MainWindow)
        self.action_Encrypt.setObjectName("action_Encrypt")
        self.action_Change_Passphrase_2 = QtWidgets.QAction(MainWindow)
        self.action_Change_Passphrase_2.setObjectName("action_Change_Passphrase_2")
        self.action_Main = QtWidgets.QAction(MainWindow)
        self.action_Main.setObjectName("action_Main")
        self.action_Wallet = QtWidgets.QAction(MainWindow)
        self.action_Wallet.setObjectName("action_Wallet")
        self.action_Network = QtWidgets.QAction(MainWindow)
        self.action_Network.setObjectName("action_Network")
        self.action_Display = QtWidgets.QAction(MainWindow)
        self.action_Display.setObjectName("action_Display")
        self.action_Information = QtWidgets.QAction(MainWindow)
        self.action_Information.setObjectName("action_Information")
        self.action_Console = QtWidgets.QAction(MainWindow)
        self.action_Console.setObjectName("action_Console")
        self.action_Network_Tra = QtWidgets.QAction(MainWindow)
        self.action_Network_Tra.setObjectName("action_Network_Tra")
        self.menu_File.addAction(self.action_Open)
        self.menu_Options.addAction(self.action_Main)
        self.menu_Options.addAction(self.action_Wallet)
        self.menu_Options.addAction(self.action_Network)
        self.menu_Options.addAction(self.action_Display)
        self.menu_Settings.addAction(self.action_Encrypt)
        self.menu_Settings.addAction(self.action_Change_Passphrase_2)
        self.menu_Settings.addSeparator()
        self.menu_Settings.addAction(self.menu_Options.menuAction())
        self.menu_Debug_window.addAction(self.action_Information)
        self.menu_Debug_window.addAction(self.action_Console)
        self.menu_Debug_window.addAction(self.action_Network_Tra)
        self.menu_Help.addAction(self.menu_Debug_window.menuAction())
        self.menu_Help.addAction(self.action_Command_line_option)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.action_About_the_program)
        self.menu_Help.addAction(self.action_About_the_library)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Settings.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def __init__(self):
        super(menu_File.setObjectName("menu_File"), self).__init__()
        uic.loadUi('menu_File', self)
        
        action = self.findChild(menu_File.setObjectName("menu_File")
        action.triggered.connect(self.Ui_plug)

        self.show()

    def Ui_plug(self):
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Settings.setTitle(_translate("MainWindow", "&Settings"))
        self.menu_Options.setTitle(_translate("MainWindow", "&Options"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.menu_Debug_window.setTitle(_translate("MainWindow", "&Debug window"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_Open.setText(_translate("MainWindow", "&Open"))
        self.action_Encrypt_Wallet.setText(_translate("MainWindow", "&Encrypt Wallet"))
        self.action_Options.setText(_translate("MainWindow", "&Options"))
        self.action_Command_line_option.setText(_translate("MainWindow", "&Command line option"))
        self.action_About_the_program.setText(_translate("MainWindow", "&About the program"))
        self.action_About_the_library.setText(_translate("MainWindow", "&About the library"))
        self.action_Encrypt.setText(_translate("MainWindow", "&Encrypt Wallet"))
        self.action_Change_Passphrase_2.setText(_translate("MainWindow", "&Change Passphrase"))
        self.action_Main.setText(_translate("MainWindow", "&Main"))
        self.action_Wallet.setText(_translate("MainWindow", "&Wallet"))
        self.action_Network.setText(_translate("MainWindow", "&Network"))
        self.action_Display.setText(_translate("MainWindow", "&Display"))
        self.action_Information.setText(_translate("MainWindow", "&Information"))
        self.action_Console.setText(_translate("MainWindow", "&Console"))
        self.action_Network_Tra.setText(_translate("MainWindow", "&Network Traffic"))


    