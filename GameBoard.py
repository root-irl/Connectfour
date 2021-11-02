#!/bin/bash/python3

		
#play function/display function
def print_gb(self):
	print(self.gb_dict["line_top"])
	for key in self.gb_dict.keys():
		if key != "line_top":
			for value in self.gb_dict[key]:
				print(value)
			print(self.gb_dict["line_top"])
	return
	
#Controls turns or passes to AI function
def turn_select(self):
	if self.turn_num % 2 == 1:
		self.turn_num += 1
		return self.player_one
	else:
		self.turn_num += 1
		return self.player_two
		
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

