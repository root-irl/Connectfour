#!/bin/bash/python3
import os
		
#play function/display function
def print_gb(self):
	os.system('cls' if os.name == 'nt' else 'clear')
	print("  1   2   3   4   5   6   7")
	print(self.gb_dict["line_top"])
	for key in self.gb_dict.keys():
		if key != "line_top":
			for value in self.gb_dict[key]:
				print(value)
			print(self.gb_dict["line_top"])
	return
	
#Controls turns or passes to AI function
def turn_select(self):
	self.turn_num += 1
	self.print_gb()
	if self.turn_num % 2 == 1:
		self.xo_val = "X"
		return self.play_select(self.player_one)
	else:
		self.xo_val = "O"
		return self.play_select(self.player_two)	
		
#takes input and changes gb_dict and gb_ref
def change_row(self, selection):
	if selection == "1":
		self.find_row(0)
		if self.reselect_flag == True:
			self.reselect_flag = False
			return self.play_select
		self.gb_ref[self.row_key][0] = self.xo_val
		print(self.gb_ref)
		dict_count = 0
		for value in self.gb_dict[self.row_key]:
			count = 0
			new_list = ""
			for letter in value:
				if count not in range(1,4):
					new_list += letter
				else:
					new_list += self.xo_val
				count += 1
			self.gb_dict[self.row_key][dict_count] = new_list
			dict_count += 1
	elif selection == "2":
		self.find_row(1)
		if self.reselect_flag == True:
			self.reselect_flag = False
			return self.play_select
		self.gb_ref[self.row_key][1] = self.xo_val
		print(self.gb_ref)
		dict_count = 0
		for value in self.gb_dict[self.row_key]:
			count = 0
			new_list = ""
			for letter in value:
				if count not in range(5,8):
					new_list += letter
				else:
					new_list += self.xo_val
				count += 1
			self.gb_dict[self.row_key][dict_count] = new_list
			dict_count += 1
	elif selection == "3":
		self.find_row(2)
		if self.reselect_flag == True:
			self.reselect_flag = False
			return self.play_select
		self.gb_ref[self.row_key][2] = self.xo_val
		print(self.gb_ref)
		dict_count = 0
		for value in self.gb_dict[self.row_key]:
			count = 0
			new_list = ""
			for letter in value:
				if count not in range(9,12):
					new_list += letter
				else:
					new_list += self.xo_val
				count += 1
			self.gb_dict[self.row_key][dict_count] = new_list
			dict_count += 1
	elif selection == "4":
		self.find_row(3)
		if self.reselect_flag == True:
			self.reselect_flag = False
			return self.play_select
		self.gb_ref[self.row_key][3] = self.xo_val
		print(self.gb_ref)
		dict_count = 0
		for value in self.gb_dict[self.row_key]:
			count = 0
			new_list = ""
			for letter in value:
				if count not in range(13,16):
					new_list += letter
				else:
					new_list += self.xo_val
				count += 1
			self.gb_dict[self.row_key][dict_count] = new_list
			dict_count += 1
	elif selection == "5":
		self.find_row(4)
		if self.reselect_flag == True:
			self.reselect_flag = False
			return self.play_select
		self.gb_ref[self.row_key][4] = self.xo_val
		print(self.gb_ref)
		dict_count = 0
		for value in self.gb_dict[self.row_key]:
			count = 0
			new_list = ""
			for letter in value:
				if count not in range(17,20):
					new_list += letter
				else:
					new_list += self.xo_val
				count += 1
			self.gb_dict[self.row_key][dict_count] = new_list
			dict_count += 1
	elif selection == "6":
		self.find_row(5)
		if self.reselect_flag == True:
			self.reselect_flag = False
			return self.play_select
		self.gb_ref[self.row_key][5] = self.xo_val
		print(self.gb_ref)
		dict_count = 0
		for value in self.gb_dict[self.row_key]:
			count = 0
			new_list = ""
			for letter in value:
				if count not in range(21,24):
					new_list += letter
				else:
					new_list += self.xo_val
				count += 1
			self.gb_dict[self.row_key][dict_count] = new_list
			dict_count += 1
	return self.turn_select()
	
#Takes column input and figures out next available row
def find_row(self, column):
	string_list = ["1", "2", "3", "4", "5", "6"]
	for key in string_list:
		if self.gb_ref[key][column] != "X" and self.gb_ref[key][column] != "O":
			self.row_key = key
			return
	print("That column is full!  Please select a different column.")
	self.reselect_flag = True
	return

