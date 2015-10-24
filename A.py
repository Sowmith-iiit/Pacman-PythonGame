from pacman import pacman
from random import *
import sys
l=[
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".","C","C","C","C","C","C","C",".",".",".",".",".","C","C","C","C",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".","C",".",".",".",".",".","C","C",".","C",".",".",".","."],
[".",".","C",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".","C",".",".",".",".",".",".","C",".",".",".",".",".","."],
[".",".","C","C","C",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","C",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".","C",".","C",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","C",".",".",".",".",".",".","C",".",".",".",".",".","."],
[".",".","C","C","C","C",".","C",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
["X","X","X","X","X","X","X","X","X","X",".","X","X","X","X","X","X","X","X","X",".","X","X","X","X","X","X","X","X","X","X","X","X","X","X"],
[".",".","X","X","C","C","C","C",".",".",".","X",".",".",".",".",".",".",".",".","C",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".","X","C","C","C","C",".",".",".","X",".",".",".",".",".",".",".",".","C",".",".",".",".","C","C",".",".",".",".",".",".",".","."],
[".",".","C","X","C","C",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".","C","C",".",".",".",".",".",".",".","."],
[".",".","C","X","C",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".","C","C",".",".",".",".",".",".",".","."],
["C","C","C","C","C",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".","C","C",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".","C","C",".",".",".",".",".",".",".","."],
]
		

reload_array=[
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".","C","C","C","C","C","C","C",".",".",".",".",".","C","C","C","C",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".","C",".",".",".",".",".","C","C",".","C",".",".",".","."],
[".",".","C",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".","C",".",".",".",".",".",".","C",".",".",".",".",".","."],
[".",".","C","C","C",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","C",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".","C",".","C",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","C",".",".",".",".",".",".","C",".",".",".",".",".","."],
[".",".","C","C","C","C",".","C",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
["X","X","X","X","X","X","X","X","X","X",".","X","X","X","X","X","X","X","X","X",".","X","X","X","X","X","X","X","X","X","X","X","X","X","X"],
[".",".","X","X","C","C","C","C",".",".",".","X",".",".",".",".",".",".",".",".","C",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
[".",".",".","X","C","C","C","C",".",".",".","X",".",".",".",".",".",".",".",".","C",".",".",".",".","C","C",".",".",".",".",".",".",".","."],
[".",".","C","X","C","C",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".","C","C",".",".",".",".",".",".",".","."],
[".",".","C","X","C",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".","C","C",".",".",".",".",".",".",".","."],
["C","C","C","C","C",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".","C","C",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".",".",".","X",".",".",".",".",".",".",".",".",".",".",".",".",".","C","C",".",".",".",".",".",".",".","."],
]

#person class
class person:
	x = None
	y = None

	def __init__(self):
		self.x = randint(0,14)
		self.y = randint(0,34)
		return None
	
	def move_left(self,val):
		if(self.y==0):
			return False
		elif(l[self.x][self.y-1]=="X"):
		 	return False
		if(val=="p"):
		 	l[self.x][self.y]="."
			self.y = self.y - 1 
		 	if(l[self.x][self.y]=="C"):
		 		self.count = self.count + 1
		 	l[self.x][self.y]=val
			return True
		else:
		 	l[self.x][self.y]=self.store
		 	self.y = self.y - 1
		 	self.store=l[self.x][self.y]
		 	l[self.x][self.y]=val
		 	return True

	def move_right(self,val):
		if(self.y==34):
			print self.y
			return False
		elif(l[self.x][self.y+1]=="X"):
		 	return False
		if(val=="p"):	
		 	l[self.x][self.y]="."
		 	self.y = self.y + 1
		 	if(l[self.x][self.y]=="C"):
		 		self.count = self.count + 1
		 	l[self.x][self.y]=val
		 	return True
		else:
		 	l[self.x][self.y]=self.store
		 	self.y = self.y + 1
		 	self.store=l[self.x][self.y]
		 	l[self.x][self.y]=val
		 	return True

	def move_down(self,val):
		if(self.x==14):
			return False
		elif(l[self.x+1][self.y]=="X"):
		 	return False
		if(val=="p"):
		 	l[self.x][self.y]="."
		 	self.x = self.x + 1
		 	if(l[self.x][self.y]=="C"):
		 		self.count = self.count + 1
		 	l[self.x][self.y]=val
		 	return True
		else:
		 	l[self.x][self.y]=self.store
		 	self.x = self.x + 1
		 	self.store=l[self.x][self.y]
		 	l[self.x][self.y]=val
		 	return True
	
	def move_up(self,val):
		if(self.x==0):
			return False
		elif(l[self.x-1][self.y]=="X"):
		 	return False
		if(val=="p"):
		 	l[self.x][self.y]="."
		 	self.x = self.x - 1
		 	if(l[self.x][self.y]=="C"):
		 		self.count = self.count + 1
		 	l[self.x][self.y]=val
		 	return True
		else:
		 	l[self.x][self.y]=self.store
		 	self.x = self.x - 1
		 	self.store=l[self.x][self.y]
		 	l[self.x][self.y]=val
		 	return True

class ghost(person):
	store = "."
	def __init__(self):
		person.__init__(self)
		l[self.x][self.y]="g"
		store="."
	def random(self):
		r_array=[]
		if(self.y!=34): 
			if(l[self.x][self.y+1]!="X"):
				r_array.append("d")
		if(self.y!=0):
			if(l[self.x][self.y-1]!="X"):
				r_array.append("a")
		if(self.x!=14):
			if(l[self.x+1][self.y]!="X"):
				r_array.append("s")
		if(self.x!=0):
			if(l[self.x-1][self.y]!="X"):
				r_array.append("w")
		length=len(r_array)-1
		index = randint(0,length)
		move = r_array[index]
		clever = randint(0,100)
		if(clever%6==0):
			if(l[self.x][self.y]=="p"):
				print "caught You"
				return 20
		elif(move=="w"):
			self.move_up("g")
		elif(move=="d"):
			self.move_right("g")
		elif(move=="s"):
			self.move_down("g")
		else:
			self.move_left("g")
		if(self.store=="p"):
		 	return 20


class pacman(person):
	count = 0
	def __init__(self):
		person.__init__(self)
	def random(self):
		print self.x

def game():
	def update():
		some=g1.random()
		if(some==20):
			return False
		some=g2.random()
		if(some==20):
			return False
		some=g3.random()
		if(some==20):
			return False
		return True
	g1 = ghost()
	g2 = ghost()
	g3 = ghost()
	pac=pacman()
	l[pac.x][pac.y]="p"
	for i in l:
		for j in i:
			sys.stdout.write(j+"  ")
		print ""
	
	while(1):
		print "enter your move:"
		move = raw_input()
		
		if(move=="q"):
			break
		
		elif(move=="w"):
			if(pac.move_up("p")):
				if(update()):
					pass
				else:
				 	break
			else:
				print "enter valid move"
				continue
		
		elif(move=="s"):
			if(pac.move_down("p")):
				if(update()):
					pass
				else:
				 	break
			else:
				print "enter valid move"
				continue
		
		elif(move=="a"):
			if(pac.move_left("p")):
				if(update()):
					pass
				else:
				 	break
			else:
				print "enter valid move"
				continue
		
		elif(move=="d"):
			if(pac.move_right("p")):
				if(update()):
					pass
				else:
				 	break
			else:
				print "enter valid move"
				continue
		l[pac.x][pac.y]="p"	
		for i in l:
			for j in i:
				sys.stdout.write(j+"  ")
			print ""
		print "\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+"score:"+str(pac.count)
		if(pac.count==60):
			global l
			global reload_array
			l = reload_array
			pac = pacman()
			l[self.x][self.y]="p"

game()
print "game Over :p Well Played"
