#!/usr/bin/env python3

import os
from random import choice
from time import time, sleep
import argparse

def clear():	
	os.system('cls' if os.name == 'nt' else 'clear')

parser = argparse.ArgumentParser(description='plays word game')

parser.add_argument('--size', '-s', type=str, choices=['2', '3'], help='size of letter prompts')
parser.add_argument('--amount', '-a', type=str,  help='amount of letter prompts')
parser.add_argument('--verbose', '-v', help='increase verbosity', action='store_true')
parser.add_argument('--history', '-k', help='keep prompt history when playing', action='store_true')
args = parser.parse_args()


def mainGame(prompts: list):

	if args.verbose:
		print(prompts)

	if not args.history:
		clear()

	print('Get ready! \nType \'-stop\' or press Ctrl+C to end\n')
	sleep(1)

	with open('dict.txt', 'r') as f:
		dictionary = f.readlines()

	used = []
	
	try:
		currentPrompt = choice(prompts)

		while True:
			startTime = time()
			print('Quick! Type an english word containing: ' + currentPrompt)
			answer = input('\n> ').upper()

			if answer == "-STOP":
				print('bye bye')
				sleep(0.5)
				exit()

			if currentPrompt in answer:
				if answer + '\n' in dictionary:
					if answer not in used:
						currentPrompt = choice(prompts)
						used.append(answer)

						if not args.history:
							clear()

						print('nice! ' + str(round(time()-startTime, 2)) + 's elapsed\n')
					else:
						if not args.history:
							clear()

						print('\33[91mAlready used!\33[0m\n')
				else:
					if not args.history:
						clear()

					print('\33[91mNot in the dictionary!\33[0m\n')
			else:
				if not args.history:
					clear()
					
				print('\33[91mDoesn\'t contain the prompt!\33[0m\n')

	except KeyboardInterrupt:
		print('\nbye bye')
		sleep(0.5)
		exit()


def startup():
	clear()

	size, amount = args.size, args.amount

	# get size
	if not size:
		print("""
		welcome to word explosive!!
		
		please choose prompt type: 
		2: 2 letter prompts
		3: 3 letter prompts

		""")
		size = input('> ')

		while not size in ('2', '3'):
			print("""
		invalid input
		2: 2 letter prompts
		3: 3 letter prompts

			""")
			size = input('> ')
	
	if not amount:
		print("""
		enter how many prompts you want (higher = more difficult)
		open bigrams.txt or trigrams.txt to see prompts in order with frequency

		""")
		amount = input('> ')

		while not amount.isdigit():
			print("""
		invalid input

		enter how many prompts you want (higher = more difficult)
		open bigrams.txt or trigrams.txt to see prompts in order with frequency

		""")
			amount = input('> ')
	
# add try except for amount number too big
	prompts = []
	if size == '2':
		with open('bigrams.txt', 'r') as f:
			for i in range(int(amount)):
				prompts.append(f.readline()[:2])
	else:
		with open('trigrams.txt', 'r') as f:
			for i in range(int(amount)):
				prompts.append(f.readline()[:3])
	
	mainGame(prompts)


def main():
	startup()


if __name__ == "__main__":
  main()


