#!/bin/bash/python3
import sys
sys.path.append(".")
import GameText
import GameBoard

#Code for choosing the game mode
class ConnectFour:
	def __init__(self):
		self.one_or_two = ''
		self.gb_dict = {"line_top": " --- --- --- --- --- --- --- ", "row_1": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "row_2": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "row_3": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "row_4": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "row_5": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "row_6": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"]}
		self.player_one = ""
		self.player_two = ""
		self.wife_flag = 0
		self.turn_num = 1
		
#Define functions from GameText.py
	def beginning_game(self):
		GameText.beginning_game(self)
		
	def replay(self):
		GameText.replay(self)
		
	def game_selection(self):
		GameText.game_selection(self)
	
	def gb_landing_two(self):
		GameText.gb_landing_two(self)
	
	def play_select(self, name):
		GameText.play_select(self, name)

#Define functions from GameBoard.py
	def print_gb(self):
		GameBoard.print_gb(self)
		
	def turn_select(self):
		GameBoard.turn_select(self)
	
	def change_row(self, selection):
		GameBoard.change_row(self, selection)
	
		
ready_player_1 = ConnectFour()
ready_player_1.beginning_game()



