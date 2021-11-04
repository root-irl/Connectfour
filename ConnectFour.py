#!/bin/bash/python3
import os
import sys
sys.path.append(".")
import GameText
import GameBoard

#Code for choosing the game mode
class ConnectFour:
	def __init__(self):
		self.one_or_two = ''
		self.gb_dict = {"line_top": " --- --- --- --- --- --- --- ", "6": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "5": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "4": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "3": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "2": ["|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |", "|   |   |   |   |   |   |   |"], "1": ["|1  |   |   |   |   |   |   |", "|1  |   |   |   |   |   |   |", "|1  |   |   |   |   |   |   |"]}
		self.gb_ref = {"1": [ " ", " ", " ", " ", " ", " ", " "], "2": [ " ", " ", " ", " ", " ", " ", " "], "3": [ " ", " ", " ", " ", " ", " ", " "], "4": [ " ", " ", " ", " ", " ", " ", " "], "5": [ " ", " ", " ", " ", " ", " ", " "], "6": [ " ", " ", " ", " ", " ", " ", " "]}
		self.player_one = ""
		self.player_two = ""
		self.wife_flag = 0
		self.turn_num = 0
		self.row_key = ""
		self.xo_val = ""
		self.reselect_flag = False
		self.current_player = ""
		self.winner = ""
		self.win_condition = False
		
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
		
	def winner(self):
		GameText.winner(self)

#Define functions from GameBoard.py
	def print_gb(self):
		GameBoard.print_gb(self)
		
	def turn_select(self):
		GameBoard.turn_select(self)
	
	def change_row(self, selection):
		GameBoard.change_row(self, selection)
		
	def find_row(self, column):
		GameBoard.find_row(self, column)
		
	def win_test(self):
		GameBoard.win_test(self)
	
		
ready_player_1 = ConnectFour()
ready_player_1.beginning_game()



