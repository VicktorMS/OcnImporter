# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ocn_importer_prototype.qt_ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(704, 598)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.io_imports_layout = QVBoxLayout()
        self.io_imports_layout.setSpacing(0)
        self.io_imports_layout.setObjectName(u"io_imports_layout")
        self.io_imports_layout.setContentsMargins(6, 6, 6, 6)
        self.io_imports_tab_widget = QTabWidget(self.centralwidget)
        self.io_imports_tab_widget.setObjectName(u"io_imports_tab_widget")
        self.a_set_imports_tab_layout = QWidget()
        self.a_set_imports_tab_layout.setObjectName(u"a_set_imports_tab_layout")
        self.verticalLayout_8 = QVBoxLayout(self.a_set_imports_tab_layout)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.set_import_btns_layout = QHBoxLayout()
        self.set_import_btns_layout.setSpacing(42)
        self.set_import_btns_layout.setObjectName(u"set_import_btns_layout")
        self.use_import_list_file_btn = QPushButton(self.a_set_imports_tab_layout)
        self.use_import_list_file_btn.setObjectName(u"use_import_list_file_btn")

        self.set_import_btns_layout.addWidget(self.use_import_list_file_btn)

        self.paste_import_list_btn = QPushButton(self.a_set_imports_tab_layout)
        self.paste_import_list_btn.setObjectName(u"paste_import_list_btn")

        self.set_import_btns_layout.addWidget(self.paste_import_list_btn)


        self.verticalLayout_8.addLayout(self.set_import_btns_layout)

        self.input_import_list_text_edit = QTextEdit(self.a_set_imports_tab_layout)
        self.input_import_list_text_edit.setObjectName(u"input_import_list_text_edit")

        self.verticalLayout_8.addWidget(self.input_import_list_text_edit)

        self.io_imports_tab_widget.addTab(self.a_set_imports_tab_layout, "")
        self.imports_results_tab_layout = QWidget()
        self.imports_results_tab_layout.setObjectName(u"imports_results_tab_layout")
        self.verticalLayout_10 = QVBoxLayout(self.imports_results_tab_layout)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.import_results_btns_layout = QHBoxLayout()
        self.import_results_btns_layout.setSpacing(42)
        self.import_results_btns_layout.setObjectName(u"import_results_btns_layout")
        self.export_import_results_btn = QPushButton(self.imports_results_tab_layout)
        self.export_import_results_btn.setObjectName(u"export_import_results_btn")

        self.import_results_btns_layout.addWidget(self.export_import_results_btn)

        self.copy_import_results_btn = QPushButton(self.imports_results_tab_layout)
        self.copy_import_results_btn.setObjectName(u"copy_import_results_btn")

        self.import_results_btns_layout.addWidget(self.copy_import_results_btn)


        self.verticalLayout_10.addLayout(self.import_results_btns_layout)

        self.output_import_result_text_edit = QTextEdit(self.imports_results_tab_layout)
        self.output_import_result_text_edit.setObjectName(u"output_import_result_text_edit")
        self.output_import_result_text_edit.setReadOnly(True)
        self.output_import_result_text_edit.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_10.addWidget(self.output_import_result_text_edit)

        self.io_imports_tab_widget.addTab(self.imports_results_tab_layout, "")

        self.io_imports_layout.addWidget(self.io_imports_tab_widget)


        self.horizontalLayout_2.addLayout(self.io_imports_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(128)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setSizeConstraint(QLayout.SetMaximumSize)
        self.main_layout.setContentsMargins(12, 12, 12, 12)
        self.main_title_layout = QVBoxLayout()
        self.main_title_layout.setObjectName(u"main_title_layout")
        self.main_title_layout.setContentsMargins(-1, 42, -1, -1)
        self.main_title_label = QLabel(self.centralwidget)
        self.main_title_label.setObjectName(u"main_title_label")
        self.main_title_label.setStyleSheet(u"font-weight: 900;\n"
"font-size: 24px;")

        self.main_title_layout.addWidget(self.main_title_label)

        self.main_title_layout.setStretch(0, 2)

        self.main_layout.addLayout(self.main_title_layout)

        self.input_src_and_dest_paths_layouts = QVBoxLayout()
        self.input_src_and_dest_paths_layouts.setSpacing(0)
        self.input_src_and_dest_paths_layouts.setObjectName(u"input_src_and_dest_paths_layouts")
        self.input_src_and_dest_paths_layouts.setContentsMargins(-1, 0, -1, 24)
        self.input_souce_dir_layout = QVBoxLayout()
        self.input_souce_dir_layout.setSpacing(0)
        self.input_souce_dir_layout.setObjectName(u"input_souce_dir_layout")
        self.input_souce_dir_layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.input_souce_dir_layout.setContentsMargins(8, 8, 8, 8)
        self.source_dir_label = QLabel(self.centralwidget)
        self.source_dir_label.setObjectName(u"source_dir_label")

        self.input_souce_dir_layout.addWidget(self.source_dir_label)

        self.source_dir_line_edit = QLineEdit(self.centralwidget)
        self.source_dir_line_edit.setObjectName(u"source_dir_line_edit")

        self.input_souce_dir_layout.addWidget(self.source_dir_line_edit)


        self.input_src_and_dest_paths_layouts.addLayout(self.input_souce_dir_layout)

        self.input_destination_dir_layout = QVBoxLayout()
        self.input_destination_dir_layout.setSpacing(0)
        self.input_destination_dir_layout.setObjectName(u"input_destination_dir_layout")
        self.input_destination_dir_layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.input_destination_dir_layout.setContentsMargins(8, 8, 8, 8)
        self.destination_dir_label = QLabel(self.centralwidget)
        self.destination_dir_label.setObjectName(u"destination_dir_label")

        self.input_destination_dir_layout.addWidget(self.destination_dir_label)

        self.destination_dir_line_edit = QLineEdit(self.centralwidget)
        self.destination_dir_line_edit.setObjectName(u"destination_dir_line_edit")

        self.input_destination_dir_layout.addWidget(self.destination_dir_line_edit)


        self.input_src_and_dest_paths_layouts.addLayout(self.input_destination_dir_layout)


        self.main_layout.addLayout(self.input_src_and_dest_paths_layouts)

        self.main_import_btns_layouts = QHBoxLayout()
        self.main_import_btns_layouts.setSpacing(24)
        self.main_import_btns_layouts.setObjectName(u"main_import_btns_layouts")
        self.main_import_btns_layouts.setContentsMargins(24, 24, 24, 24)
        self.check_import_btn = QPushButton(self.centralwidget)
        self.check_import_btn.setObjectName(u"check_import_btn")

        self.main_import_btns_layouts.addWidget(self.check_import_btn)

        self.import_btn = QPushButton(self.centralwidget)
        self.import_btn.setObjectName(u"import_btn")

        self.main_import_btns_layouts.addWidget(self.import_btn)


        self.main_layout.addLayout(self.main_import_btns_layouts)


        self.horizontalLayout_2.addLayout(self.main_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 704, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.io_imports_tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.use_import_list_file_btn.setText(QCoreApplication.translate("MainWindow", u"Usar Arquivo", None))
        self.paste_import_list_btn.setText(QCoreApplication.translate("MainWindow", u"Colar", None))
        self.io_imports_tab_widget.setTabText(self.io_imports_tab_widget.indexOf(self.a_set_imports_tab_layout), QCoreApplication.translate("MainWindow", u"Definir Importa\u00e7\u00e3o", None))
        self.export_import_results_btn.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.copy_import_results_btn.setText(QCoreApplication.translate("MainWindow", u"Copiar", None))
        self.io_imports_tab_widget.setTabText(self.io_imports_tab_widget.indexOf(self.imports_results_tab_layout), QCoreApplication.translate("MainWindow", u"Resultado da Importa\u00e7\u00e3o", None))
        self.main_title_label.setText(QCoreApplication.translate("MainWindow", u"OCN Importer", None))
        self.source_dir_label.setText(QCoreApplication.translate("MainWindow", u"Caminho de Busca (HIST)", None))
        self.destination_dir_label.setText(QCoreApplication.translate("MainWindow", u"Caminho destino", None))
        self.check_import_btn.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.import_btn.setText(QCoreApplication.translate("MainWindow", u"Import", None))
    # retranslateUi

