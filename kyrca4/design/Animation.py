from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from design.DesignWindow import Ui_MainWindow

class AnimationButtons:
    def __init__(self, main_window):
        super().__init__()
        self.mainwindow = main_window
        
    def animation_add(self):
        if self.mainwindow.add.isChecked():
            self.mainwindow.groupBox_create.show()
            self.mainwindow.groupBox_create.resize(191, 0)
            self.anim_1 = QPropertyAnimation(self.mainwindow.groupBox_create, b"size")
            self.anim_1.setEndValue(QSize(191, 231))
            self.anim_1.setDuration(0)
            self.animation_off_change()
            self.mainwindow.change.setChecked(False)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim_3)
            self.anim_group.start()
        else:
            self.anim_1 = QPropertyAnimation(self.mainwindow.groupBox_create, b"size")
            self.anim_1.setEndValue(QSize(191, 0))
            self.anim_1.setDuration(0)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
            self.mainwindow.add.setText("Добавить")

    def animation_add_2(self):
        if self.mainwindow.add_2.isChecked():
            self.mainwindow.groupBox_create_2.show()
            self.mainwindow.groupBox_create_2.resize(191, 0)
            self.anim_1 = QPropertyAnimation(self.mainwindow.groupBox_create_2, b"size")
            self.anim_1.setEndValue(QSize(191, 231))
            self.anim_1.setDuration(0)
            self.animation_off_change_2()
            self.mainwindow.change_2.setChecked(False)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim_3)
            self.anim_group.start()
        else:
            self.anim_1 = QPropertyAnimation(self.mainwindow.groupBox_create_2, b"size")
            self.anim_1.setEndValue(QSize(191, 0))
            self.anim_1.setDuration(0)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
            self.mainwindow.add_2.setText("Добавить")
            
    def animation_add_3(self):
        if self.mainwindow.add_3.isChecked():
            self.mainwindow.groupBox_create_3.show()
            self.mainwindow.groupBox_create_3.resize(201, 0)
            self.anim_1 = QPropertyAnimation(self.mainwindow.groupBox_create_3, b"size")
            self.anim_1.setEndValue(QSize(201, 231))
            self.anim_1.setDuration(0)
            self.animation_off_change_3()
            self.mainwindow.change_3.setChecked(False)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim_3)
            self.anim_group.start()
        else:
            self.anim_1 = QPropertyAnimation(self.mainwindow.groupBox_create_3, b"size")
            self.anim_1.setEndValue(QSize(201, 0))
            self.anim_1.setDuration(0)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
            self.mainwindow.add_3.setText("Добавить")
            
    def animation_change(self):
        if self.mainwindow.change.isChecked():
            self.mainwindow.groupBox_change.show()
            self.mainwindow.groupBox_change.resize(191, 0)
            self.anim_1 = QPropertyAnimation(self.mainwindow.groupBox_change, b"size")
            self.anim_1.setEndValue(QSize(191, 231))
            self.anim_1.setDuration(0)
            self.animation_off_add()
            self.mainwindow.add.setChecked(False)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim_3)
            self.anim_group.start()
        else:
            self.anim_1 = QPropertyAnimation(self.mainwindow.groupBox_change, b"size")
            self.anim_1.setEndValue(QSize(191, 0))
            self.anim_1.setDuration(0)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
            self.mainwindow.change.setText("Изменить")
            
    def animation_change_2(self):
        if self.mainwindow.change_2.isChecked():
            self.mainwindow.groupBox_change_2.show()
            self.mainwindow.groupBox_change_2.resize(191, 0)
            self.anim_1 = QPropertyAnimation(self.mainwindow.groupBox_change_2, b"size")
            self.anim_1.setEndValue(QSize(191, 231))
            self.anim_1.setDuration(0)
            self.animation_off_add_2()
            self.mainwindow.add_2.setChecked(False)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim_3)
            self.anim_group.start()
        else:
            self.anim_1 = QPropertyAnimation(self.mainwindow.groupBox_change_2, b"size")
            self.anim_1.setEndValue(QSize(191, 0))
            self.anim_1.setDuration(0)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
            self.mainwindow.change_2.setText("Изменить")
            
    def animation_change_3(self):
        if self.mainwindow.change_3.isChecked():
            self.mainwindow.groupBox_change_3.show()
            self.mainwindow.groupBox_change_3.resize(201, 0)
            self.anim_1 = QPropertyAnimation(self.mainwindow.groupBox_change_3, b"size")
            self.anim_1.setEndValue(QSize(201, 231))
            self.anim_1.setDuration(0)
            self.animation_off_add_3()
            self.mainwindow.add_3.setChecked(False)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim_3)
            self.anim_group.start()
        else:
            self.anim_1 = QPropertyAnimation(self.mainwindow.groupBox_change_3, b"size")
            self.anim_1.setEndValue(QSize(201, 0))
            self.anim_1.setDuration(0)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
            self.mainwindow.change_3.setText("Изменить")
            
        
    def animation_off_add(self):
        self.anim_3 = QPropertyAnimation(self.mainwindow.groupBox_create, b"size")
        self.anim_3.setEndValue(QSize(191, 0))
        self.anim_3.setDuration(0)
        self.mainwindow.add.setText("Добавить")
    
    def animation_off_add_2(self):
        self.anim_3 = QPropertyAnimation(self.mainwindow.groupBox_create_2, b"size")
        self.anim_3.setEndValue(QSize(191, 0))
        self.anim_3.setDuration(0)
        self.mainwindow.add_2.setText("Добавить")

        
    def animation_off_add_3(self):
        self.anim_3 = QPropertyAnimation(self.mainwindow.groupBox_create_3, b"size")
        self.anim_3.setEndValue(QSize(201, 0))
        self.anim_3.setDuration(0)
        self.mainwindow.add_3.setText("Добавить")
        
    def animation_off_change(self):
        self.anim_3 = QPropertyAnimation(self.mainwindow.groupBox_change, b"size")
        self.anim_3.setEndValue(QSize(191, 0))
        self.anim_3.setDuration(0)
        self.mainwindow.change.setText("Изменить")
        
    def animation_off_change_2(self):
        self.anim_3 = QPropertyAnimation(self.mainwindow.groupBox_change_2, b"size")
        self.anim_3.setEndValue(QSize(191, 0))
        self.anim_3.setDuration(0)
        self.mainwindow.change_2.setText("Изменить")
        
    def animation_off_change_3(self):
        self.anim_3 = QPropertyAnimation(self.mainwindow.groupBox_change_3, b"size")
        self.anim_3.setEndValue(QSize(201, 0))
        self.anim_3.setDuration(0)
        self.mainwindow.change_3.setText("Изменить")
