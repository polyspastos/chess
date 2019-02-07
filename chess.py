# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import sleep as s
from os import system as sys
import values


#todo: new input logics: 1) a2a4 2) Ra4
class chess():

	def draw_board(self, state):
		for row in range(0, len(state)):
			print(state[len(state) - row - 1])
			print("\n")

	def get_input(self, state, side, mn):
		sys("cls")
		chess.draw_board(self, state)
		# print("side: ", side)
		print("White's turn" if side == False else "Black's turn", "       [0][0] is a1")
		print("{}. move".format(mn))
		non_adherent_input = True
		while non_adherent_input:
			from_square_column = "00"
			from_square_row = "00"
			to_square_column = "00"
			to_square_row = "00"
			while from_square_column not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] or from_square_row not in ['1', '2', '3', '4', '5', '6', '7', '8']:
				from_square = input("From square: \nRequired input: (a-h) and (1-8), e.g.: e2\n")
				if len(from_square) == 2:
					from_square_row = from_square[1]
					from_square_column = from_square[0]
					non_adherent_input = False

			while to_square_column not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] or to_square_row not in ['1', '2', '3', '4', '5', '6', '7', '8']:
				to_square = input("To square: \nRequired input: (a-h) and (1-8), e.g.: e4\n")
				if len(to_square) == 2:
					to_square_row = to_square[1]
					to_square_column = to_square[0]
					non_adherent_input = False

		return (from_square_row, from_square_column, to_square_row, to_square_column)

	def convert_input(self, mi):
		from_square_row = mi[0]
		from_square_column = mi[1]
		to_square_row = mi[2]
		to_square_column = mi[3]

		#
		# while not finished_moving:


		# print("from_square_row: ", from_square_row)
		# print("from_square_column: ", from_square_column)
		# print("to_square_row: ", to_square_row)
		# print("to_square_column: ", to_square_column)
		# input()

		if from_square_column == 'a':
			f2 = 0
		elif from_square_column == 'b':
			f2 = 1
		elif from_square_column == 'c':
			f2 = 2
		elif from_square_column == 'd':
			f2 = 3
		elif from_square_column == 'e':
			f2 = 4
		elif from_square_column == 'f':
			f2 = 5
		elif from_square_column == 'g':
			f2 = 6
		elif from_square_column == 'h':
			f2 = 7

		f1 = int(from_square_row) - 1

		if to_square_column == 'a':
			t2 = 0
		elif to_square_column == 'b':
			t2 = 1
		elif to_square_column == 'c':
			t2 = 2
		elif to_square_column == 'd':
			t2 = 3
		elif to_square_column == 'e':
			t2 = 4
		elif to_square_column == 'f':
			t2 = 5
		elif to_square_column == 'g':
			t2 = 6
		elif to_square_column == 'h':
			t2 = 7

		t1 = int(to_square_row) - 1

		# print("f1: ", f1)
		# print("f2: ", f2)
		# print("t1: ", t1)
		# print("t2: ", t2)
		# input()

		return (f1, f2, t1, t2)

	def move(self, side, state, cm):
		# finished_moving = False
		# legal_move_made = False
		#

		# print("itt start")

		f1 = cm[0]
		f2 = cm[1]
		t1 = cm[2]
		t2 = cm[3]

		state[t1][t2] = state[f1][f2]
		state[f1][f2] = ' '

		# print("t1: ", t1)
		# input()

		if state[t1][t2] == 'P' and t1 == 7:
			# print("itt1")
			# print("state[t1][t2]: ", state[t1][t2])
			# input()
			print("The pawn has reached its promotion square. What would you like to have it changed to?")
			print("(Q)ueen, (R)ook, (B)ishop or a k(N)ight?")
			promoted = input().upper()
			while promoted not in ["Q", "R", "B", "N", "q", "r", "b", "n"]:
				promoted = input().upper()

			state[7][f2] = "{}".format(promoted.upper())
			# print("Promotion done.")
			# print("state[7][{}]: ".format(f2), state[7][f2])
			# input()

		if state[t1][t2] == 'p' and t1 == 0:
			# print("itt2")
			# print("state[t1][t2]: ", state[t1][t2])
			# input()
			print("The pawn has reached its promotion square. What would you like to have it changed to?")
			print("(Q)ueen, (R)ook, (B)ishop or a k(N)ight?")
			promoted = input().lower()
			while promoted not in ["Q", "R", "B", "N", "q", "r", "b", "n"]:
				promoted = input().lower()

			state[0][f2] = "{}".format(promoted.lower())
			# print("Promotion done.")
			# print("state[0][{}]: ".format(f2), state[0][f2])
			# input()

		# input()

			# else:
			# 	return False
			# else:
			# 	print("Illegal move, please try again.")
			# 	input()
			# 	chess.get_input(self, values.board_state, side)
			# 	chess.move(self, side, state, mi) #?
			# 	finished_moving = True #?

		# print("itt")
		last_move = chess.remember_move(self, f1, f2, t1, t2, state[t1][t2])

		return (state, side, last_move)

	def change_side(side):
		if side == False: #ez működik?
			# print("side True-ra vált")
			side = True
		elif side == True:
			# print("side False-ra vált")
			side = False

		# print("oldalváltoztatás kész")
		# input()
		return side

	def check_empty(self, state, row, column, row_dest, column_dest, side):
		print("chess.check_empty fut")
		if state[row][column] != ' ' and row == row_dest and column == column_dest:
			if ((side == False) and (state[f1][f2] in ['R', 'N', 'B', 'Q', 'K', 'P'])) \
			or ((side == True) and (state[f1][f2] in ['r', 'n', 'b', 'q', 'k', 'p'])):
				print("Can't take your own pieces!")
				input()
				return False
		elif state[row][column] == ' ':
			print("Square is empty.")
			input()
			return True
		else:
			print("Square is occupied!")
			input()
			return False


	def check_legal(self, side, state, mi, lm):
		# print("check_legal elindul")
		# input()

		# if lm != ['0', '0', '0', '0', '0']:
		# print("The last move has been: ", lm) #debug
		# else:
		# 	print("This has been the first move.")
		# input() #debug

		f1 = mi[0]
		f2 = mi[1]
		t1 = mi[2]
		t2 = mi[3]

		# print("f1: {}, f2: {}".format(f1, f2)) #debug
		# print("f2: ", f2)
		# print("t1: {}, t2: {}".format(t1, t2)) #debug
		# print("t2: ", t2)
		# input()

		if f1 + f2 + t1 + t2 < 33:
			# print("f1 + f2 + t1 + t2 < 33")
			# input()

			if ' ' in state[f1][f2]:
				# print("return1")
				# input()
				return False

			if ((side == False) and (state[f1][f2] in ['r', 'n', 'b', 'q', 'k', 'p'])) \
			 or ((side == True) and (state[f1][f2] in ['R', 'N', 'B', 'Q', 'K', 'P'])):
				print("(side == False) and (state[f1][f2] in ['r', 'n', 'b', 'q', 'k', 'p']): ", (side == False) and (state[f1][f2] in ['r', 'n', 'b', 'q', 'k', 'p']))
				print("(side == True) and (state[f1][f2] in ['R', 'N', 'B', 'Q', 'K', 'P']): ", (side == True) and (state[f1][f2] in ['R', 'N', 'B', 'Q', 'K', 'P']))
				print("Would you please leave your opponent's pieces alone? Thank you.")
				input()
				return False

			if (('r' in state[f1][f2]) and (side == True) or ('R' in state[f1][f2]) and (side == False)):
				if (f1 == t1):
					# print("abs(f2 - t2): ", abs(f2 - t2))
					# input()
					if f2 >= t2:
						# print("első1 külső")
						# print("f2, t2: ", f2, t2)
						# print("range(f2, (f2 - t2) + 1): ", range(f2, t2 + 1))
						input()
						for bw in range(f2 - 1, t2, -1):
							# print("első1")
							# print("Ellenőrzött mező: {}{}".format(bw, f1))
							# print("state[{}][{}]: ".format(f1, bw), state[f1][bw])
							# print(state[f1][abs(f2 - t2)])
							# state[f1][abs(f2 - t2)]
							input()
							if chess.check_empty(self, values.board_state, f1, bw, t1, t2, side) == False:
								return False
						return True
					if f2 <= t2:
						# print("első2 külső")
						# print("range(f2, (f2 - t2) + 1): ", range(f2, (t2 - f2) + 1))
						input()
						for bw in range(f2 + 1, t2): #ennél működik a check_empty #érdekes-e ebből a szempontból, hogy történt-e ütés?
							# print("első2")
							# print("Ellenőrzött mező: {}{}".format(f1, bw))
							# print("state[{}][{}]: ".format(f1, bw), state[f1][bw])
							# print(state[f1][abs(f2 - t2)])
							# state[f1][abs(f2 - t2)]
							input()
							if chess.check_empty(self, values.board_state, f1, bw, t1, t2, side) == False:
								return False
						return True
				if (f2 == t2):
					# print("abs(f1 - t1): ", abs(f1 - t1))
					# input()
					if f1 <= t1: #kész
						# print("második1 külső") #ez működik
						# print("range(f1, (t1 - f1) + 1): ", range(f1, (t1 - f1) + 1))
						# input()
						for bw in range(f1 + 1, t1):
							# print("második1 ELLENŐRIZENDŐ") #abszolútértékkel működik
							# print("Ellenőrzött mező: {}{}".format(bw, f2))
							# print("state[{}][{}]: ".format(bw, f2), state[bw][f2])
							# print(state[abs(f1 - t1)][f2])
							# state[f1][abs(f1 - t1)]
							# input()
							if chess.check_empty(self, values.board_state, bw, f2, t1, t2, side) == False:
								return False
						return True
					if f1 >= t1:
						# print("második2 külső") #ez működik
						# print("range(f1, (f1 - t1) + 1): ", range(f1, t1 + 1))
						# input()
						for bw in range(f1 - 1, t1, -1):
							# print("második2")
							# print("Ellenőrzött mező: {}{}".format(bw, f2))
							# print("state[{}][{}]: ".format(bw, f2), state[bw][f2])
							# print(state[abs(f1 - t1)][f2])
							# state[f1][abs(f1 - t1)]
							# input()
							if chess.check_empty(self, values.board_state, bw, f2, t1, t2, side) == False:
								return False

						return True

			if (('b' in state[f1][f2]) and (side == True) or ('B' in state[f1][f2]) and (side == False)):
				# print("if (('b' in state[f1][f2]) and (side_to_move == True) or ('B' in state[f1][f2]) and (side_to_move == False)):")
				# input()


				if ((f1 == f2 and t1 == t2) or (f1 + f2 == t1 + t2) or (t1 - f1 == t2 - f2)):
					# print("A legal move with a bishop.")
					# input()
					return True

			if (('p' in state[f1][f2]) and (side == True) or ('P' in state[f1][f2]) and (side == False)): #todo: taking --> en passant
				# print("if (('b' in state[f1][f2]) and (side_to_move == True) or ('B' in state[f1][f2]) and (side_to_move == False)):")
				# print()

				# print("haliho")
				# print("state[f1+1][f2+1]: ", state[f1+1][f2+1])
				# print("state[f1-1][f2-1]: ", state[f1-1][f2-1])
				# input()

				if side == False: #if a white pawn is moving
					# print("if (('p' in state[f1][f2]) and ... -n belül az if side == False")
					# print(type(lm))
					# input()
					if 'p' in lm[4]:
						# print("the last move was made with a black pawn!")
						# input()
						# try:
						# 	# if (t1 == lm[2]-1 and t2 == lm[3]) or (t1 == lm[2]+1 and t2 == lm[3]):
						# 	if (t1 == lm[2] and t2 == lm[3]+1) or (t1 == lm[2] and t2 == lm[3]-1):
						# 		if lm[0]-lm[2] == 2:
						# 			en_passant_possible = True
						# 			print("En passant capture is possible.")
						# 			input()
						# except Exception as e:
						# 	print(e)
						# 	input()
						# 	return False #?

						try:
							if lm[0]-lm[2] == 2:
								# print("The last move was a double pawn move by black.")
								# print("(t1 == ((lm[0] + lm[2]) / 2) and (t2 == lm[3])): ", (t1 == ((lm[0] + lm[2]) / 2) and (t2 == lm[3])))
								# input()
								# print("t1: ", t1)
								# print("lm[0]: ", lm[0])
								# print("lm[2]: ", lm[2])
								# print("t2: ", t2)
								# print("lm[3]: ", lm[3])

								if (t1 == ((lm[0] + lm[2]) / 2) and (t2 == lm[3])):
									en_passant_possible = True
									# print("En passant capture is possible.")
									chess.special_move_en_passant(self, state, lm)
									# input() #debug
									return True
						except Exception as e:
							print(e)
							print("en passant loop error")
							input()

					try:
						if (state[f1+1][f2+1] in ['r', 'n', 'b', 'q', 'p']): #capture
							if t1 == f1+1 and t2 == f2+1:
								# print("gyalogütés jobbra föl")
								# input()
								return True
					except Exception as e:
						print(e)
						print("capture loop error")
						input()

					# while True:
					# 	print("haliiiiiii")
					# 	s(0.5)

					try:
						if (state[f1+1][f2-1] in ['r', 'n', 'b', 'q', 'p']): #capture
							if t1 == f1+1 and t2 == f2-1:
								# print("gyalogütés balra föl")
								# input()
								return True
					except Exception as e:
						print(e)
						pass

					if f1 + 1 == t1 and f2 == t2: #regular move
						# print("return3")
						# input()
						return True

					if (state[f1][f2] == state[1][f2]): #double move from starting position
						if f1 + 2 == t1 and f2 == t2:
							# print("return4")
							# input()
							return True

				if side == True: #black pawn moves
					if 'P' in lm[4]: #¤¤¤
						# print("the last move was made with a black pawn!")
						# input()

						try:
							# print("lm[2]-lm[0]: ", lm[2]-lm[0])
							# input()
							if lm[2]-lm[0] == 2:
								# print("The last move was a double pawn move by white.")
								# print("(t1 == ((lm[0] + lm[2]) / 2) and (t2 == lm[3])): ", (t1 == ((lm[0] + lm[2]) / 2) and (t2 == lm[3])))
								# input()
								# print("t1: ", t1)
								# print("lm[0]: ", lm[0])
								# print("lm[2]: ", lm[2])
								# print("t2: ", t2)
								# print("lm[3]: ", lm[3])

								if (t1 == ((lm[0] + lm[2]) / 2) and (t2 == lm[3])):
									en_passant_possible = True
									# print("En passant capture is possible.")
									chess.special_move_en_passant(self, state, lm)
									# input()
									return True
						except Exception as e:
							print(e)
							print("en passant loop error")
							input()







					if (state[f1-1][f2-1] in ['R', 'N', 'B', 'Q', 'P']): #capture
						# print("itt234234")
						if t1 == f1-1 and t2 == f2-1:
							# print("gyalogütés balra le")
							# input()
							return True

					try:
						if (state[f1-1][f2+1] in ['R', 'N', 'B', 'Q', 'P']): #capture
							# print("itt234235")
							if t1 == f1-1 and t2 == f2+1:
								# print("gyalogütés jobbra le")
								# input()
								return True
					except Exception as e:
						print(e)
						print("capture loop error")
						input()

					# while True:
					# 	print("haliii")
					# 	s(0.5)

					if f1 - 1 == t1 and f2 == t2: #regular move
							return True #?

					if (state[f1][f2] == state[6][f2]): #double move from starting position
						if f1 - 2 == t1 and f2 == t2:
							# print("return6")
							# input()
							return True

			# else:
				# print("return8")
				# input()

		else:
			return False
		# print("itt8")
		# input()
		return False

	def special_move_en_passant(self, state, lm):
		state[lm[2]][lm[3]] = ' '
		return state

	def remember_move(self, f1, f2, t1, t2, s):
		lm = [f1, f2, t1, t2, s]
		# print("The move is: ", lm) #debug
		return lm

	def game_loop(self, state, side):
		move_number = 1
		while not values.end:
			illegal = 1
			while illegal == 1:
				sys("cls")
				chess.draw_board(self, values.board_state)
				# print("side a váltás előtt: ", side)
				move_input = chess.get_input(self, values.board_state, side, move_number)
				# print("move_input: ", move_input)
				# input()
				converted_move = chess.convert_input(self, move_input)
				# print("converted_move: ", converted_move)
				# input()
				if move_number == 1:
					last_move_made = ['0', '0', '0', '0', '0']
				if chess.check_legal(self, side, state, converted_move, last_move_made) == True:
					last_move_made = chess.move(self, side, values.board_state, converted_move)[2]
					# print("last move: ", last_move_made)
					# input() #debug
					illegal = 0
				else:
					print("Illegal move, please try again!")
					# input()
			side = chess.change_side(side)
			move_number += 1
			# print("side a váltás után: ", side)
			# input()

side = False
chessgame = chess()
chessgame.game_loop(values.board_state, values.side_to_move)