#!/bin/bash/python3

#function to set up game board
class GameBoard:
	def __init__(self):
		self.gb_dict = {"line_top": " --- --- --- --- --- --- --- ", "row_1": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "row_2": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "row_3": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "row_4": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "row_5": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "row_6": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"]}
		self.player_one = ""
		self.player_two = ""
		self.wife_flag = 0
		self.turn_num = 1
		
#play function/display function
	def print_gb(self):
		print(self.gb_dict["line_top"])
		for key in self.gb_dict.keys():
			if key != "line_top":
				for value in self.gb_dict[key]:
					print(value)
				print(self.gb_dict["line_top"])
		return
	
#Landding for game/player selection for two player
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
	
#Controls turns or passes to AI function
	def turn_select(self):
		if self.turn_num % 2 == 1:
			self.turn_num += 1
			return self.player_one
		else:
			self.turn_num += 1
			return self.player_two
			
#Player move selection
	def play_select(self, name):
		print("  1   2   3   4   5   6   7")
		self.print_gb()
		print("{} is X and {} is O!".format(self.player_one, self.player_two))
		print("It's your turn to choose a column, {}!".format(name))
		return self.change_row(input("-->"))
			
#Takes return from selection function and changes gb_dict
	def change_row(self, selection):
		if selection[0] == 1:
			print("column_1")
		elif selection[0] == 2:
			print("column_2")
		elif selection[0] == 3:
			print("column_3")
		elif selection[0] == 4:
			print("column_4")
		elif selection[0] == 5:
			print("column_5")
		elif selection[0] == 6:
			print("column_6")
		else:
			print("Something went wrong!")
			print("Please select again")
		return
	
#test code

