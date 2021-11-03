#!/bin/bash/python3
import os

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
		if self.one_or_two == 'one':
			correct_input = True
		elif self.one_or_two == 'two':
			correct_input = True
			return self.gb_landing_two()
		else:
			print("That is not the correct input!")
			print("Please try again!")
	return self.replay()
	
#Landing for game/player selection for two player
def gb_landing_two(self):
	print("What is player one's name?")
	self.player_one = input("-->")
	self.player_one = self.player_one.capitalize()
	if self.player_one == "Amara":
		self.wife_flag = 1
	print("What is player two's name?")
	self.player_two = input("-->")
	self.player_two = self.player_two.capitalize()
	if self.player_two == "Amara":
		self.wife_flag = 2
	return self.turn_select()
	
#Player move selection
def play_select(self, name):
	selection = 0
	sel_list = ["1", "2", "3", "4", "5", "6"]
	print("{} is X and {} is O!".format(self.player_one, self.player_two))
	print("It's your turn, {}! Choose a column number.".format(name))
	selection_test = False
	while selection_test == False:
		selection = input("-->")
		if selection in sel_list:
			selection_test = True
			return self.change_row(selection)
		else:
			print("Something went wrong!")
			print("Please select again using a number. (ie. 4)")
