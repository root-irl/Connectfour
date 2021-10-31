#!/bin/bash/python3

#function to set up game board
class GameBoard:
	def __init__(self):
		self.gb_dict = {"line_top": " --- --- --- --- --- --- --- ", "row_1": ["|x x|   |   |   |   |   |ooo|", "| x |   |   |   |   |   |o o|", "|x x|   |   |   |   |   |ooo|"], "row_2": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "row_3": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "row_4": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "row_5": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "row_6": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"]}
		
#play function/display function
	def print_gb(self):
		print(self.gb_dict["line_top"])
		for key in self.gb_dict.keys():
			if key != "line_top":
				for value in self.gb_dict[key]:
					print(value)
				print(self.gb_dict["line_top"])
		return
	
	
#test code
x = GameBoard()
x.print_gb()
