import os
import psutil
import random
import sys

WHITE = "\033[1;37m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
GREEN = "\033[0;32m"
NC = "\033[0m"

if __name__ == "__main__":
	"""
	Get all student accounts and all student accounts that are currently login.
	"""
	all_users = [
			user
			for user
			in os.listdir("/home")
			if str(user).startswith("a")
			or str(user).startswith("m")
		]
	current_users = list(set(
			user.name
			for user
			in psutil.users()
			if str(user.name).startswith("a")
			or str(user.name).startswith("m")
		))
	random.shuffle(all_users)
	
	"""
	Get the input number and inspect if it is a number.
	"""
	if len(sys.argv) < 2:
		draw_number = 0
		print(f"{WHITE}Invalid input. "
			  f"Use {YELLOW}draw <number> {WHITE}to draw <number> students.{NC}"
		)
		exit()
	else:
		try:
			draw_number = int(sys.argv[1])
		except:
			print(f"{WHITE}Invalid input.{NC}")
			exit()

	"""
	If the input number is larger than the total number of students,
	set it to the max student number.
	"""
	if draw_number > len(all_users):
		draw_number = len(all_users)
	elif draw_number <= 0:
		print(f"{WHITE}Invalid input. The number should be larger than zero.{NC}")
		exit()

	"""
	Draw students.
	"""
	print(
			f"{YELLOW}Draw {draw_number} student(s):\n"
			f"{NC}=============================="
	)
	for idx in range(draw_number):
		print(f"{WHITE}No.{idx+1}:\t{all_users[idx].upper()}    ", end="")
		if all_users[idx] in current_users:
			print(f"{GREEN}ONLINE")
		else:
			print(f"{RED}OFFLINE")

	print(f"{NC}")
