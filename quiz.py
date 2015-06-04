import datetime
import random
from Question import Addition, Multiply
#needs to be tested 

class Quiz:
'''Makes lists of quiz questions and their answers'''
    questions = list() 
    answers = list()


    def __init__(self):
        #generate ten questions with number 1 to 10
        #add these questions to a list of questions
        question_types = (Addition, Multiply)
        #question_types[0](1,5)

        for _ in range(10):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = random.choice(question_types)(num1, num2) 
            self.questions.append()

    def take_quiz(self):
'''Creates quiz and timer, needs functions'''
        #log the start time
        #ask all of the questions
        #log if they got the question correct
        #log the end time
        #show a summary
        pass 
   
   def ask(self, question):
'''Asks questions, needs functions'''
       pass

       #log the start time
       #capture the answer 
       #check the answer
       #log the end time
       #if answer is correct, send back true
       #else false
       #send back the elapsed time
  
  def total_correct(self):
'''Returns total of questions answered correctly'''
      #return total number correct answers 
      total = 0
      for answer in self.answers:
          if answer[0]:
              total += 1 
      return total
     

  def summary(self):
'''Prints total correct and time it took'''
       #print total you got right
       print("You've got {} out of {} correct".format(self.total_correct, len(self.questions))

       #print the total amount of time 
       print("It took you {} seconds total".format(
       (self.end_time - self.start_time).seconds))
 
