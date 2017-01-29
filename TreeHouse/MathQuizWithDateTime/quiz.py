import datetime
import random
import os

from questions import Add, Multiply

class Quiz(object):
	answers = []
	input_limits = (0, 10)
	question_types = (Add, Multiply)

	def summary(self):
		print '\n' + '='*20
		print 'Your score is {}/{}'.format(reduce(lambda x, y: x+y, map(lambda x: 1 if x else 0, self.answers)), len(self.answers))
		print 'Total time taken for the quiz was {} seconds!'.format(self.total_time.total_seconds())
		print '\n' + '='*20

	def take_quiz(self):
		self.total_time = datetime.timedelta()
		for question in self.questions:
			result, elapsed_time = self.ask(question)
			self.total_time += elapsed_time
			if result:
				print 'Congratulations! You got it right!'
			else:
				print 'Oops! Better luck next time!'
		self.summary()

	def ask(self, question):
		self.current_start_time = datetime.datetime.now()
		try:
			answer = int(raw_input('{} = '.format(question.text)))
		except ValueError:
			print 'Enter a valid number as an answer.'
			return self.ask(question)
		else:
			self.answers.append(answer == question.answer)
			return answer == question.answer, datetime.datetime.now() - self.current_start_time

	def __init__(self):
		self.questions = map(lambda x: random.choice(self.question_types)(random.randint(*self.input_limits), random.randint(*self.input_limits)), range(int(raw_input('How many questions do you want to play with?\n> '))))


while True:
	Quiz().take_quiz()
	if(raw_input('Wanna play again? Y/n: ').lower() == 'n'):
		break
	else:
		os.system("cls" if os.name == "nt" else "clear")
		continue
