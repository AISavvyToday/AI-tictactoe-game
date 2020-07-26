import re
sym = ['_', '_', '_','_', '_', '_','_', '_', '_']

def playField():
	print('---------')
	print('|', sym[0], sym[1], sym[2], '|')
	print('|', sym[3], sym[4], sym[5], '|')
	print('|', sym[6], sym[7], sym[8], '|')
	print('---------')

playField()

x_wins = False
o_wins = False

def eval():
	global x_wins, o_wins, sym
	if sym[0] == sym[1] == sym[2] == 'X'\
		or sym[3] == sym[4] == sym[5] == 'X'\
		or sym[6] == sym[7] == sym[8] == 'X'\
		or sym[0] == sym[3] == sym[6] == 'X'\
		or sym[1] == sym[4] == sym[7] == 'X'\
		or sym[2] == sym[5] == sym[8] == 'X'\
		or sym[0] == sym[4] == sym[8] == 'X'\
		or sym[2] == sym[4] == sym[6] == 'X':
		x_wins = True
			
	elif sym[0] == sym[1] == sym[2] == 'O'\
		or sym[3] == sym[4] == sym[5] == 'O'\
		or sym[6] == sym[7] == sym[8] == 'O'\
		or sym[0] == sym[3] == sym[6] == 'O'\
		or sym[1] == sym[4] == sym[7] == 'O'\
		or sym[2] == sym[5] == sym[8] == 'O'\
		or sym[0] == sym[4] == sym[8] == 'O'\
		or sym[2] == sym[4] == sym[6] == 'O':
		o_wins = True

last_entry = ''
while True:
	try:
		x, y = input('Enter the coordinates: ').split()
		try:
			re.search('[0-9]', x) and re.search('[0-9]', y)
			x = int(x)
			y = int(y)
			if (x >= 1 and x <= 3) and (y >= 1 and y <= 3):
					(x, y) = x, y
					symTup = (
					(sym[0], (1,3)),
					(sym[1], (2,3)),
					(sym[2], (3,3)),
					(sym[3], (1,2)),
					(sym[4], (2,2)),
					(sym[5], (3,2)),
					(sym[6], (1,1)),
					(sym[7], (2,1)),
					(sym[8], (3,1)),
					)					
					for i in range(0,9):
						
						if sym[i] == '_' and symTup[i][1] == (x,y):
							if last_entry == '' or last_entry == 'O':
								sym[i] = 'X'
								last_entry = 'X'
							elif last_entry == 'X':
								sym[i] = 'O'
								last_entry = 'O'							
						elif sym[i] != '_' and symTup[i][1] == (x,y):
							print('This cell is occupied! Choose another one!')					
			else:
				print("Coordinates should be from 1 to 3!")
		except:
			print('You should enter numbers!')
	except:
		print('You should enter numbers!')
	eval()
	playField()
	if x_wins == True:
		print('X wins')
		break
	elif o_wins == True:
		print('O wins')
		break
	elif (x_wins == False and o_wins == False) and not ('_' in sym):
		print('Draw')
		break
