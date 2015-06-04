import datetime 

class Question:
'''Class for quiz questions'''
    answer = None 
    text = None

class Addition(Question):
'''Class for addition questions'''
    def __init__(self, num1, num2):
        self.text = "{} + {}".format(num1, num2)
        self.answer = num1 + num2


class Multiply(Question):
'''Class for multiplication questions'''
    def __init__(self, num1, num2):
        self.text = "{} x {}".format(num1, num2)
        self.answer = num1 * num2



