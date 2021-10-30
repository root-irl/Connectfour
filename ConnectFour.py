#!/bin/bash/python3

#Code for choosing the game mode
class Main:
	def __init__(self):
		self.one_or_two = ''

#For starting the game the first time
	def beginning_game(self):
		print("Welcome to Connect Four!")
		print("Would you like to play against the computer or with a friend?")
		return self.game_selection()
		
#For starting the game for replay
	def replay(self):
		correct_input = False
		print("Would you like to play again?")
		print("Type: Yes or No.")
		while correct_input == False:
			self.one_or_two = input('-->')
			self.one_or_two = self.one_or_two.lower()
			if self.one_or_two == 'yes':
				print("Awesome, thank you for playing again!")
				return self.game_selection()
			elif  self.one_or_two == 'no':
				print("Awesome, thank you for playing!")
				correct_input = True
			else:
				print("That is not the correct input!")
				print("Please try again!")
		return 
		
#Game mode selection
	def game_selection(self):
		correct_input = False
		print("Select one or two players.")
		print("Type: One or Two.")
		while correct_input == False:
			self.one_or_two = input('-->')
			self.one_or_two = self.one_or_two.lower()
			if self.one_or_two == 'one' or self.one_or_two == 'two':
				correct_input = True
			else:
				print("That is not the correct input!")
				print("Please try again!")
		return self.game_mode_test(self.one_or_two)

#For testing purposes
	def game_mode_test(self, game_choice):
		print("You are in game mode {} and you \"played\" the game".format(game_choice))
		return self.replay()
		
welcome_1 = Main()
welcome_1.beginning_game()



