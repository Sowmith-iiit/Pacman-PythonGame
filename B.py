import os
import shutil
from time import *
from stat import *
import sys
import pwd
import grp

def check(arg):
	if(arg=="1"):
		return "--x"
	elif(arg=="2"):
		return "-w-"
	elif(arg=="3"):
		return "-wx"
	elif(arg=="4"):
		return "r--"
	elif(arg=="5"):
		return "r-x"
	elif(arg=="6"):
		return "rw-"
	elif(arg=="7"):
		return "rwx"
	elif(arg=="0"):
		return "---"

def print_tabs(count):
	for i in range(0,count):
		sys.stdout.write("  ")

def print_lines(count):
	for i in range(0,count):
		sys.stdout.write("  |")

def dirstr(directory,count):
	listdir = os.listdir(directory)
	for i in listdir:
		print_lines(count)
		print ""
		print_lines(count-1)
		if(os.path.isdir(directory+"/"+i)):
			print "  #------------------- Folder Name:"+directory+"/"+str(i)+"-----------------------#"
			if os.listdir(directory+"/"+i)==[]:
				print "                          (Empty Folder)                             "
			else:
				dirstr(directory+"/"+str(i),count+1)
		else:
			print "  #-"+i

print "enter command on prompt..if u want to exit press enter" 
while(1):
	command = raw_input()
	command = command.split(" ")
	if(command[0]=="cd"):
		try:
			if(len(command)==2):
				print "wtf"
				os.chdir(command[1])
			else:
				print "fts"
				os.chdir(os.getenv("HOME"))
		except:
			print "check your address of the directory"

	if(command[0]=="cp"):
		try:
			if(os.path.isdir(command[1])):
				shutil.copytree(command[1],command[2])
			else:
				shutil.copy(command[1],command[2])
		except:
			print "Input Error"
		
	if(command[0]=="mv"):
		try:
			shutil.move(command[1],command[2])
		except:
			print "Input Error"

	if(command[0]=="rm"):
		try:
			if(os.path.isdir(command[1])):
				os.removetree(command[1]);	
			else:
				os.remove(command[1]);
		except:
			print "Input Error"

	if(command[0]=="dirstr"):
		print "#-------------------Folder Name:"+os.getcwd()+"-----------------------#"
		dirstr(os.getcwd(),1)
		print "\n"

	if(command[0]=="ls"):
		if(len(command)==2):
			if(command[1]=="-l"):
				pass
		else:
			for i in os.listdir("."):
				print i
			continue
		files = os.listdir(".")
		for fi in files:
			name=fi
			links=os.stat(fi).st_nlink
			creation=ctime(os.stat(fi).st_mtime)
			per=oct(os.stat(fi)[ST_MODE])[-3:]
			per=str(per)
			per=list(per)
			ans=[]
			pw=pwd.getpwuid(os.stat(fi).st_uid)[0]
			gp=grp.getgrgid(os.stat(fi).st_gid)[0]
			size=os.path.getsize(fi)
			if(os.path.isdir(fi)):
				ans.append("d")
			else:
				ans.append("-")
			for i in per:
				ans.append(check(i))
			for i in ans:
				sys.stdout.write(i)
			print ". "+" "+str(links)+" "+str(pw)+" "+str(gp)+" "+creation+" "+str(size)+" "+name
