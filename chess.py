import sys
'''Pieces Classes'''

class Piece :
	color=None
	name=None
	was_moved=False

	def is_legal_move(self,current_location:(int,int), destination:(int,int)):
		pass

	def toString(self,x,y) :
		if ( (x+y)%2==0 ):
			return " ༶ "
		return "   "
				


class Pawn(Piece):

	def __init__(self,Color:str):
		self.name="P"
		self.color=Color
		
	def toString(self,x,y) :
		if(Boared[x][y].color=='W'):
			return " ♙ "
		return " ♟ "

	def is_legal_move(self,current_location:(int,int), destination:(int,int)):
		x,y = current_location,destination
		if(self.color=='W'):
			if(x[0]==y[0]-1):
				if(x[1]==y[1] and Boared[y[0]][y[1]].name==None or abs(x[1]-y[1])==1 and Boared[y[0]][y[1]].color!=None and Boared[y[0]][y[1]].color!=self.color):
					return True
			elif(x[0]==y[0]-2 and x[1]==y[1] and  Boared[x[0]][x[1]].was_moved==False and Boared[y[0]][y[1]].name==None):
				return True
		else:
			if(x[0]-1==y[0]):
				if(x[1]==y[1] and Boared[y[0]][y[1]].name==None or abs(x[1]-y[1])==1 and Boared[y[0]][y[1]].color!=None and Boared[y[0]][y[1]].color!=self.color):
					return True
			elif(x[0]-2==y[0] and x[1]==y[1] and Boared[x[0]][x[1]].was_moved==False and Boared[y[0]][y[1]].name==None):
				return True

		return False



class Rock(Piece):
	def __init__(self,Color:str):
		self.name="R"
		self.color=Color
	
	def toString(self,x,y) :
		if(Boared[x][y].color=='W'):
			return " ♖ "
		return " ♜ "
		
	def is_legal_move(self,current_location:(int,int), destination:(int,int)):
		x,y = current_location,destination
		if(x[0]==y[0]):
			s,e = min(x[1],y[1]), max(x[1],y[1])
			for i in range(s+1,e):
				if(Boared[x[0]][i].color!=None):
					return False
			return True
		elif(x[1]==y[1]):
			s,e = min(x[0],y[0]), max(x[0],y[0])
			for i in range(s+1,e):
				if(Boared[i][x[1]].color!=None):
					return False
			return True

		return False



class Knight(Piece):
	def __init__(self,Color:str):
		self.name="N"
		self.color=Color
		
	def toString(self,x,y) :
		if(Boared[x][y].color=='W'):
			return " ♘ "
		return " ♞ "
	
	def is_legal_move(self,current_location:(int,int), destination:(int,int)):
		x,y = current_location,destination
		if(abs(x[0]-y[0])==1 and abs(x[1]-y[1])==2 or abs(x[0]-y[0])==2 and abs(x[1]-y[1])==1):
			return True
		
		return False



class Bishop(Piece):
	def __init__(self,Color:str):
		self.name="B"
		self.color=Color
	
	def toString(self,x,y) :
		if(Boared[x][y].color=='W'):
			return " ♗ "
		return " ♝ "
	
	def is_legal_move(self,current_location:(int,int), destination:(int,int)):
		x,y = current_location,destination
		if(abs(x[0]-y[0]) != abs(x[1]-y[1])):
			return False

		if(y[1]<x[1]):
			x,y=y,x

		if(x[0]<y[0]):
			for i in range(1,y[1]-x[1]):
				if(Boared[x[0]+i][x[1]+i].name!=None):
					return False
		else :
			for i in range(1,y[1]-x[1]):
				if(Boared[x[0]-i][x[1]+i].name!=None):
					return False

		return True


		

class Queen(Piece):
	def __init__(self,Color:str):
		self.name="Q"
		self.color=Color
	
	def toString(self,x,y) :
		if(Boared[x][y].color=='W'):
			return " ♕ "
		return " ♛ "
	
	def is_legal_move(self,current_location:(int,int), destination:(int,int)):
		x,y = current_location,destination
		if(x[0]==y[0]):
			s,e = min(x[1],y[1]), max(x[1],y[1])
			for i in range(s+1,e):
				if(Boared[x[0]][i].color!=None):
					return False
			return True
		elif(x[1]==y[1]):
			s,e = min(x[0],y[0]), max(x[0],y[0])
			for i in range(s+1,e):
				if(Boared[i][x[1]].color!=None):
					return False
			return True


		if(abs(x[0]-y[0]) != abs(x[1]-y[1])):
			return False

		if(y[1]<x[1]):
			x,y=y,x

		if(x[0]<y[0]):
			for i in range(1,y[1]-x[1]):
				if(Boared[x[0]+i][x[1]+i].name!=None):
					return False
		else :
			for i in range(1,y[1]-x[1]):
				if(Boared[x[0]-i][x[1]+i].name!=None):
					return False

		return True



class King(Piece):
	def __init__(self,Color:str):
		self.name="K"
		self.color=Color
	
	def toString(self,x,y) :
		if(Boared[x][y].color=='W'):
			return " ♔ "
		return " ♚ "
	
	def is_legal_move(self,current_location:(int,int), destination:(int,int)):
		x,y = current_location,destination

		if(x[0]==0 and x[1]==4 and y[0]==0 and y[1]==6):
			if(Boared[0][4].name=="K" and Boared[0][4].color=="W" and Boared[0][4].was_moved==False):
				if(Boared[0][7].name=="R" and Boared[0][7].color=="W" and Boared[0][7].was_moved==False):
					if(Boared[0][5].name==None and Boared[0][6].name==None):
						if(legal_for_cussel(0,4,'W') and legal_for_cussel(0,5,'W') and legal_for_cussel(0,6,'W')):
							Boared[0][5],Boared[0][7]=Boared[0][7],Piece()
							Boared[0][5].was_moved=True
							return True

		if(x[0]==0 and x[1]==4 and y[0]==0 and y[1]==2):
			if(Boared[0][4].name=="K" and Boared[0][4].color=="W" and Boared[0][4].was_moved==False):
				if(Boared[0][0].name=="R" and Boared[0][0].color=="W" and Boared[0][0].was_moved==False):
					if(Boared[0][3].name==None and Boared[0][2].name==None and Boared[0][1]):
						if(legal_for_cussel(0,4,'W') and legal_for_cussel(0,3,'W') and legal_for_cussel(0,2,'W') and legal_for_cussel(0,1,'W')):
							Boared[0][3],Boared[0][0]=Boared[0][0],Piece()
							Boared[0][0].was_moved=True
							return True

		if(x[0]==7 and x[1]==4 and y[0]==8 and y[1]==6):
			if(Boared[7][4].name=="K" and Boared[7][4].color=="B" and Boared[7][4].was_moved==False):
				if(Boared[7][7].name=="R" and Boared[7][7].color=="B" and Boared[7][7].was_moved==False):
					if(Boared[7][5].name==None and Boared[7][6].name==None):				
						if(legal_for_cussel(7,4,'B') and legal_for_cussel(7,5,'B') and legal_for_cussel(7,6,'B')):
							Boared[7][5],Boared[7][7]=Boared[7][7],Piece()
							Boared[7][5].was_moved=True
							return True

		if(x[0]==7 and x[1]==4 and y[0]==7 and y[1]==2):
			if(Boared[7][4].name=="K" and Boared[7][4].color=="B" and Boared[7][4].was_moved==False):
				if(Boared[7][0].name=="R" and Boared[7][0].color=="B" and Boared[7][0].was_moved==False):
					if(Boared[7][3].name==None and Boared[7][2].name==None and Boared[7][1]):
						if(legal_for_cussel(7,4,'B') and legal_for_cussel(7,3,'B') and legal_for_cussel(7,2,'B') and legal_for_cussel(7,1,'B')):
							Boared[7][3],Boared[7][0]=Boared[7][0],Piece()
							Boared[7][0].was_moved=True
							return True


		if(abs(x[0]-y[0])>=0 and abs(x[0]-y[0])<=1 and abs(x[1]-y[1])>=0 and abs(x[1]-y[1])<=1 ):
			return True

		return False


#-------------------------------------------------------------------------------------------------------------#
'''neccesary functions'''

def Boared_Create():
	first_W_row = [Rock('W'),Knight('W'),Bishop('W'),Queen('W'),King('W'),Bishop('W'),Knight('W'),Rock('W')]
	first_B_row = [Rock('B'),Knight('B'),Bishop('B'),Queen('B'),King('B'),Bishop('B'),Knight('B'),Rock('B')]
	line_of_W_Pawns = [Pawn('W') for i in range(8)]		
	line_of_B_Pawns = [Pawn('B') for i in range(8)]

	Boared[0]=first_W_row
	Boared[7]=first_B_row
	Boared[1]=line_of_W_Pawns
	Boared[6]=line_of_B_Pawns



def Boared_Update():
	print("\n"*9)
	for i in range (8):
		print("")
		print("  "+str(8-i)+"  |  ",end='')
		for j in range(8):
			print(Boared[7-i][j].toString(7-i,j),end='  ')
		print("")
	print("        ",end='')
	for i in range(8):
		print("___ ",end=' ')

	print("\n")
	print("         ",end='')
	for i in range(8):
		print(chr(ord('a') + i),end='    ')

	for i in range(2):
		print ("")

def Valid_current_location(x:int, y:int):
	if(x>=0 and x<8 and y>=0 and y<8):
		return Boared[x][y].color==Current_Tern
	return False


def Valid_destination(x:int, y:int):
	if(x>=0 and x<8 and y>=0 and y<8):
		return Boared[x][y].color!=Current_Tern
	return False

def king_dead_move(loon:str):
	x,y=0,0
	for i in range(8):
		for j in range(8):
			if(Boared[i][j].name=="K" and Boared[i][j].color==loon):
				x,y=i,j
				break

	for i in range(8):
		for j in range(8):
			if(Boared[i][j].color!=None and Boared[i][j].color!=loon):
				if(Boared[i][j].is_legal_move((i,j),(x,y))):
					return True

	return False

def legal_for_cussel(x:int , y:int, Color):
	for i in range(8):
		for j in range(8):
			if(Boared[i][j].color!=None and Boared[i][j].color!=Color):
				if(Boared[i][j].is_legal_move((i,j),(x,y))):
					return False

	return True


def there_is_a_move():
	for i in range(8):
		for j in range(8):
			if(Boared[i][j].color==Current_Tern):
				for h in range(8):
					for g in range(8):
						if(Boared[h][g].color!=Current_Tern):
							if(Boared[i][j].is_legal_move((i,j),(h,g))):
								backupx=Boared[i][j]
								backupy=Boared[h][g]

								Boared[h][g],Boared[i][j] = Boared[i][j],Piece()
								if(not king_dead_move(Current_Tern)):
									Boared[i][j], Boared[h][g]=backupx,backupy
									return True
								Boared[i][j], Boared[h][g]=backupx,backupy


	return False



def lets_play():
	while(True):
		global Current_Tern
		x,y=[-1,-1],[-1,-1]
		while(x[0]<0):
			try:
				Tern="Black"
				if(Current_Tern=='W'):
					Tern="White"

				curr=input("  "+Tern+" Tern, .. Enter the current location of the Piece you want to move , example(e2)  ")
				if(curr == 'close'):
					print("press Enter to continue")
					return
				x[1]=ord(curr[0])-ord('a')
				x[0]=int(curr[1])-1
			except :
				print ("\n  Oops!  That was invalid location.  Try again...\n\n")
				x[0]=-1
				continue
			if(not Valid_current_location(x[0],x[1])):
				print ("\n  Oops!  That was invalid location.  Try again...\n\n")
				x[0]=-1
				continue

			try:
				dest=input("\n  Enter the destination , example(e4)  ")
				y[1]=ord(dest[0])-ord('a')
				y[0]=int(dest[1])-1
			except :
				print ("\n  Oops!  That was invalid intput.  Try again...\n\n")
				x[0]=-1
				continue

			if(not Valid_destination(y[0],y[1])):
				print ("\n  Oops!  That was illegal move.  Try again...\n\n")
				x[0]=-1 

				continue

			if(not Boared[x[0]][x[1]].is_legal_move((x[0],x[1]),(y[0],y[1]))):
				print ("\n  Oops!  That was illegal move.  Try again...\n\n")
				x[0]=-1
				continue
			backupx=Boared[x[0]][x[1]]
			backupy=Boared[y[0]][y[1]]

			Boared[y[0]][y[1]],Boared[x[0]][x[1]] = Boared[x[0]][x[1]],Piece()
			Boared[y[0]][y[1]].was_moved=True

			if(king_dead_move(Current_Tern)):
				print ("\n  Oops!  That was illegal move.  Try again...\n\n")
				Boared[x[0]][x[1]], Boared[y[0]][y[1]]=backupx,backupy
				x[0]=-1
				continue
			
			if(Boared[y[0]][y[1]].name=='P' and (y[0]==7 or y[0]==0)):
				while(True):
					try:
						choice=int(input("\n1) Queen,  2) Knight,   3) Rock,   4)Bishop\n Enter your choice  "))
						if (choice > 4 or choice < 1):
							continue
						if(choice==1):
							Boared[y[0]][y[1]]=Queen(Current_Tern)
						elif(choice==2):
							Boared[y[0]][y[1]]=Knight(Current_Tern)
						elif(choice==3):
							Boared[y[0]][y[1]]=Rock(Current_Tern)
						elif(choice==4):
							Boared[y[0]][y[1]]=Bishop(Current_Tern)
						break
						
					except :
						print ("\n  Oops!  That was invalid number.  Try again...\n\n")
						
			
			
			Boared_Update()

			if(Current_Tern=="W"):
				Current_Tern="B"
			else:
				Current_Tern="W"
				
			if(not there_is_a_move()):
				if(king_dead_move(Current_Tern)):
					Tern="Black"
					if(Current_Tern=='B'):
						Tern="White"
					input("-"*20 +"\n"+"  "+Tern + " Won! ;)"+"\n"*2 + "press Enter to continue")
				else:
					input("-"*20 +"\n"+"  its a Draw! :)"+"\n"*2 + "press Enter to continue")
				return

	
#-------------------------------------------------------------------------------------------------------------#

'''Main'''

Current_Tern="W"
Boared = [[Piece() for i in range(8)] for j in range(8)]
Boared_Create()
Boared_Update()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~		
lets_play()


