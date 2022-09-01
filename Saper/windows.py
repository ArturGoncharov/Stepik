# -*- coding: utf-8 -*-
import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import Form, Button, TextBox, Label
clr.AddReference('System.Drawing')
from System.Drawing import Point, Size


class Window(Form):
    def __init__(self):
        self._operator = Label()
        self._operator.Text = '+'
        self._operator.Size = Size(10, 10)
        self._operator.Location = Point(80, 20)
        self._operator.Location = Point(80, 20)
        self.Controls.Add(self._operator)
        self.Controls.Add(self._operator)
        self.Size = Size(180, 130)
        self.CenterToScreen()
        self._initialize_components()

    def _initialize_components(self):
        self._operand_1 = TextBox()
        self._operand_1.Name = 'first'
        self._operand_1.Size = Size(50, 20)
        self._operand_1.Location = Point(20, 20)
        self.Controls.Add(self._operand_1)


        self._operand_2 = TextBox()
        self._operand_2.Name = 'second'
        self._operand_2.Size = Size(50, 20)
        self._operand_2.Location = Point(100, 20)
        self.Controls.Add(self._operand_2)

        self._btn = Button()
        self._btn.Text = 'test'
        self._btn.Location = Point(45, 50)
        self.Controls.Add(self._btn)

    def set_button_click_handler(self, handler):
        self._btn.Click+=handler

    def set_text_changed_handler(self, handler):
        self._operand_1.TextChanged+=handler
        self._operand_2.TextChanged+=handler



class Calculator(object):
    def __init__(self):
        self._number_1 = ''
        self._number_2 = ''
        self._error = 'Оба операнда должны быть числами'

    def text_changed(self, sender, event_args):
        if sender.Name == 'first':
            self._number_1 = sender.Text
        if sender.Name == 'second':
            self._number_2 = sender.Text

    def execute(self, sender, event_args):
        if self._number_1.isdigit() and self._number_2.isdigit():
            print int(self._number_1) + int(self._number_2)
        else:
            print self._error

class Presenter(object):
    def __init__(self):
        self._calc = Calculator()
        self._window=Window()
        self._window.set_button_click_handler(self._calc.execute)
        self._window.set_text_changed_handler(self._calc.text_changed)

    def run(self):
        self._window.ShowDialog()

if __name__ == '__main__':
    p = Presenter()
    p.run()
