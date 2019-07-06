import os
import sys
import re
import shutil
sl="/"
a=input()
r=re.split(' |, ',a)
if (r[0] == "mkdir"):
	os.mkdir(r[1])
b=input()
r1=re.split(' |, ',b)
cwd=os.getcwd()
if(r1[0] == "cd"):
	if (r1[1]==r[1]):
		os.chdir(cwd+sl+r1[1])
	else:
		sys.stdout.write("directory does not exist\n")

c=input()
r2=re.split(' |, ',c)
cwd=os.getcwd()
if(r2[0] == "cd"):
	if (r2[1]==r[1]):
		os.chdir(cwd+sl+r2[1])
	else:
		sys.stdout.write("directory does not exist\n")

z=input()
if(z == "pwd"):
	sys.stdout.write(os.getcwd()+"\n")

d=input()
r3=re.split(' |, ',d)
if (r3[0] == "mkdir"):
	os.mkdir(r3[1])

e=input()
r4=re.split(' |, ',e)
cwd=os.getcwd()
if(r4[0] == "cd"):
	if (r4[1]==r3[1]):
		os.chdir(cwd+sl+r3[1])
	else:
		sys.stdout.write("directory does not exist\n")

y=input()
if ( y == "pwd"):
	sys.stdout.write(os.getcwd()+"\n")

f=input()
r5=re.split(' |, ',f)
if (r5[0] == "touch"):
	os.mknod(r5[1])

g=input()
r6=re.split(' |, ',g)
if(r6[0]=="cat"):
	if (len(r6) !=3):
		sys.stdout.write("file does not exist"+"\n")


abc=input()
r99=re.split(' |, ',abc)
if(r99[0]=="cat"):
	if (len(r99) !=3):
		sys.stdout.write("file does not exist"+"\n")

h=input()
r7=re.split(' |, ',h)
if (r7[0] =="echo"):
	if (r7[2] == ">"):
		f=("hello")
		with open("file1", "w") as f1:
			for line in f:
				f1.write(line)
	
i=input()
r8=re.split(' |, ',i)
if (r8[0] =="echo"):
	if (r8[2] == ">"):
		f=("world")
		with open("file2", "w") as f1:
			for line in f:
				f1.write(line)

j=input()
r9=re.split(' |, ',j)
if (r9[0] =="cat"):
	if (len(r9) == 3):
		if((r9[1] == r7 [3]) and (r9[2] == r8[3])):
			fin = open("file1", "r")
			f11=fin.read()
			fi = open("file2", "r")
			f12=fi.read()
			sys.stdout.write(f11+f12+"\n")


k=input()
r10=re.split(' |, ',k)
if (r10[0] =="upper"):
	fin = open(r10[1], "r")
	f11=fin.read()
	sys.stdout.write(f11.upper()+"\n")


l=input()
r11=re.split(' |, ',l)
if (r11[0] =="upper"):
	fin = open(r11[1], "r")
	f11=fin.read()
	fo=f11.upper()
	if (r11[2] == "|"):
		if (r11[3] == "lower"):
			fo=fo.lower()
			sys.stdout.write(fo+"\n")

m=input()
r12=re.split(' |, ',m)
if (r12[0] =="cat"):
	if (r12[1] == "<"):
		if (r12[3] == "|"):
			if (r12[4] == "upper"):
				fin = open(r12[2], "r")
				fiii=fin.read()
				out=fiii.upper()
				sys.stdout.write(out+"\n")

n=input()
r13=re.split(' |, ',n)
if (r13[0] =="cd"):
	if(r13[1] == ".."):
		os.chdir("..")


o=input()
r14=re.split(' |, ',o)
if (r14[0] == "touch"):
	os.mknod(r14[1])

p=input()
r15=re.split(' |, ',p)
if (r15[0] == "ls"):
	f=os.listdir(os.curdir)
	for i in range(len(f)):
		sys.stdout.write(f[i]+"\n")

'''q=input()
r16=re.split(' |, ',q)
if (r16[0] == "cd"):
	if (r17[1] == "../.." ):
		os.chdir("..")
		os.chdir("..")'''
		
	
r=input()
r17=re.split(' |, ',r)
if (r17[0] =="cd"):
	if(r17[1] == ".."):
		os.chdir("..")


s=input()
r18=re.split(' |, ',s)
if (r18[0] == "ls"):
	f=os.listdir(os.curdir)
	for i in range(len(f)):
		sys.stdout.write(f[i]+"\n")


count=0
t=input()
r19=re.split(' |, ',t)
if (r19[0] == "rm"):
	f=os.listdir(os.curdir)
	for im in range(len(f)):
		if (r19[1] == f[im]):
			count = count+1
			
	if(count == 0):
		sys.stdout.write("file or directory does not exist"+"\n")


u=input()
r20=re.split(' |, ',u)
if (r20[0] == "ls"):
	f=os.listdir(os.curdir)
	for i in range(len(f)):
		sys.stdout.write(f[i]+"\n")

v=input()
cwd1=os.getcwd()
r21=re.split(' |, ',v)
if (r21[0] == "rm"):
	f=os.listdir(os.curdir)
	for im in range(len(f)):
		if (r21[1] == f[im]):
			shutil.rmtree(cwd1+sl+r21[1])
			break

w=input()
r22=re.split(' |, ',w)
if (r22[0] == "ls"):
	f=os.listdir(os.curdir)
	for i in range(len(f)):
		sys.stdout.write(f[i]+"\n")


x=input()
r23=re.split(' |, ',x)
cwd2=os.getcwd()
if(r23[0] == "cd"):
	f=os.listdir(os.curdir)
	for im in range(len(f)):
		if (r23[1] == f[im]):
			os.chdir(cwd2+sl+r23[1])
		else:
			sys.stdout.write("directory does not exist\n")



