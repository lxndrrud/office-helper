# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QTextEdit, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(935, 685)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 921, 671))
        self.excel_tab = QWidget()
        self.excel_tab.setObjectName(u"excel_tab")
        self.groupBox = QGroupBox(self.excel_tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 911, 611))
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 30, 881, 80))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.fileExplorerInput = QTextEdit(self.groupBox_2)
        self.fileExplorerInput.setObjectName(u"fileExplorerInput")
        self.fileExplorerInput.setGeometry(QRect(10, 30, 591, 31))
        font = QFont()
        font.setPointSize(9)
        self.fileExplorerInput.setFont(font)
        self.fileExplorerInput.setReadOnly(True)
        self.fileExplorerInput.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.fileExplorerButton = QPushButton(self.groupBox_2)
        self.fileExplorerButton.setObjectName(u"fileExplorerButton")
        self.fileExplorerButton.setGeometry(QRect(600, 30, 121, 31))
        self.fileExplorerButton.setFont(font)
        self.mergeFilesOperationButton = QPushButton(self.groupBox_2)
        self.mergeFilesOperationButton.setObjectName(u"mergeFilesOperationButton")
        self.mergeFilesOperationButton.setGeometry(QRect(760, 30, 101, 31))
        self.mergeFilesOperationButton.setFont(font)
        self.tabWidget.addTab(self.excel_tab, "")

        self.retranslateUi(mainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u043c\u043e\u0449\u043d\u0438\u043a Office", None))
#if QT_CONFIG(whatsthis)
        self.excel_tab.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.excel_tab.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.groupBox.setTitle(QCoreApplication.translate("mainWindow", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("mainWindow", u"\u0421\u043b\u0438\u044f\u043d\u0438\u0435 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u0438\u0445 \u0444\u0430\u0439\u043b\u043e\u0432 \u0432 \u043e\u0434\u0438\u043d", None))
        self.fileExplorerInput.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435", None))
        self.fileExplorerButton.setText(QCoreApplication.translate("mainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443", None))
        self.mergeFilesOperationButton.setText(QCoreApplication.translate("mainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.excel_tab), QCoreApplication.translate("mainWindow", u"Excel", None))
    # retranslateUi

