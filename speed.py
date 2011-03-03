#!/usr/bin/python


import time, os, sys, stat
import optparse
import subprocess

RED ="\033[1;31m"
GREEN ="\033[1;32m"
BLACK = "\033[0m"
YELLOW ="\033[1;33m"
BLUE ="\033[1;34m"

codefolder="codes"
#liste des langages : (nom du langage, fichier source,fichier  executer, cmd de compile, cmd d'execution, cmd de nettoyage)
langages=[
{"name":"c","source":"<PRGM>.c","executable":"<PRGM>c","compile":"gcc -o <EXEC> <SRC> -O2","run":"./<EXEC> <ARGS>","clean":"rm <EXEC>","version":"gcc --version"},
{"name":"haskell","source":"<PRGM>.hs","executable":"<PRGM>hs","compile":"ghc --make <SRC> -o <EXEC> -O2","run":"./<EXEC> <ARGS>","clean":"rm <EXEC> <PRGM>.o <PRGM>.hi","version":"ghc --version"},
{"name":"java",	"source":"<PRGM>.java","executable":"<PRGM>","compile":"javac <SRC>","run":"java <EXEC> <ARGS>","clean":"rm <PRGM>.class","version":"java -version"},
{"name":"ocaml","source":"<PRGM>.ml","executable":None,"compile":None,"run":"ocaml <SRC> <ARGS>","clean":None,"version":"ocaml -version"},
{"name":"ocaml compile","source":"<PRGM>.ml",	"executable":"<PRGM>ml","compile":"ocamlopt <SRC> -o <EXEC>","run":"./<EXEC> <ARGS>","clean":"rm <EXEC> <PRGM>.cmx <PRGM>.cmi","version":"ocaml -version"},
{"name":"perl",	"source":"<PRGM>.pl","executable":None,"compile":None,"run":"perl <SRC> <ARGS>","clean":None,"version":"perl --version"},
{"name":"python","source":"<PRGM>.py","executable":None,"compile":None,"run":"python <SRC> <ARGS>","clean":None,"version":"python --version"},
{"name":"ruby","source":"<PRGM>.rb","executable":None,"compile":None,"run":"ruby <SRC> <ARGS>","clean":None,"version":"ruby --version"},
{"name":"php","source":"<PRGM>.php","executable":None,"compile":None,"run":"php <SRC> <ARGS>","clean":None,"version":"php --version"}]
#(program,[arguments],precmd,postcmd) liste d'arguemnts => plusieurs instances.
program = [("fibo",["%s"%s for s in range(39,41)],None,None),
("simpletri",["../../unsortedlist ../../sortedlist"],"codes/generate.unsorted.list.py 10000","rm ../../unsortedlist ../../sortedlist"),
("readandparse",["../../unsortedlist ../../unsortedlist2"],"codes/generate.unsorted.list.py 10000","rm ../../unsortedlist ../../unsortedlist2")]



class Balise():
	def __init__(self,name,value):
		self.name = name
		self.value = value
	def process(self, string):
		if self.value == None:
			return string
		return string.replace("<"+self.name+">",self.value)


def balise_recursive(string,listbalise):
	savestring = string
	for balise in listbalise:
		string = balise.process(string)
	if savestring == string:
		return string
	else:
		return balise_recursive(string,listbalise)


output = ""

def command(cmd,couleur=BLACK,verbose=False):
	if verbose:
		print couleur + cmd + BLACK
	proc = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	ret = proc.wait()
	return ret,proc

if __name__=="__main__":
	parser = optparse.OptionParser(usage="usage: %prog [options]")
	parser.add_option("-c" , "--clean" ,dest="clean",action="store_true",default=False,help="clean the directories")
	parser.add_option("-v" , "--verbose" ,dest="verbose",default=False ,action='store_true',help="verbose mode")
	parser.add_option("-V" , "--version" ,dest="version",default=False ,action='store_true',help="print versions used")
	parser.add_option("-l" , "--language" ,dest="lang",default=None,help="choose language [?] print possibility")
	parser.add_option("-p" , "--program" ,dest="prog",default=None ,help="choose program [?] print possibility")
	(option , arg ) = parser.parse_args(sys.argv)
#	set_folder_right(option.dir,option.verbose)

	if option.prog == "?":
		for prog,args,precmd,postcmd in program:
			print prog
		exit(0)
	if option.lang == "?":
		for lang in langages:
			print lang["name"]
		exit(0)
	if option.version:
		una = os.uname()
		for i in una:
			output = i + "\n" + output
		for lang in langages:
			ret,proc = command(lang["version"] ,YELLOW,option.verbose)
			print "--------------------------------------------"
			print lang["name"] + ":" + proc.stdout.read() + proc.stderr.read()
		
		exit(0)

	

	for prog,args,precmd,postcmd in program:
		if option.prog != None and option.prog != prog:
			continue
		balisePRGM = Balise("PRGM",prog)
		#preparation program
		for lang in langages:
			if option.lang != None and option.lang != lang["name"]:
				continue
			baliseSOURCE = Balise("SRC",lang["source"])
			baliseEXEC = Balise("EXEC",lang["executable"])
			#may be clean ???
			if lang["clean"] != None:
				os.chdir("codes/"+prog)
				command(balise_recursive( lang["clean"],[balisePRGM,baliseSOURCE,baliseEXEC]),YELLOW,option.verbose)
				os.chdir("../..")
			if option.clean :
				continue 

			#preparation
			if precmd != None:
				command(balise_recursive( precmd,[balisePRGM,baliseSOURCE,baliseEXEC]),YELLOW,option.verbose)
			#cd codes/prgm
			os.chdir("codes/"+prog)
#			os.system("pwd")
			if lang["compile"] != None:
				command(balise_recursive( lang["compile"],[balisePRGM,baliseSOURCE,baliseEXEC]),YELLOW,option.verbose)

			#execution
			for arg in args:
				baliseARGS = Balise("ARGS",arg)
				cmdline = balise_recursive( lang["run"],[balisePRGM,baliseSOURCE,baliseEXEC,baliseARGS])
				t1 = time.time()
				ret,proc = command(cmdline,BLUE,option.verbose)
				t2 = time.time()
				COUL = RED
				if ret == 0 :
					COUL = GREEN
					output = output + prog + " " + lang["name"] +" " +arg +" : " + "%f"%( t2-t1 ) + "\n"
				print COUL + prog + " " + lang["name"] +" " +arg +" : " , t2-t1 , BLACK
			if lang["clean"] != None:
				command(balise_recursive( lang["clean"],[balisePRGM,baliseSOURCE,baliseEXEC]),YELLOW,option.verbose)
			if postcmd != None:
				command(balise_recursive( postcmd,[balisePRGM,baliseSOURCE,baliseEXEC]),YELLOW,option.verbose)
			os.chdir("../..")

#	os.system("make -C "+codefolder+ " clean")
	una = os.uname()
	
	for i in una:
		output = i + "\n" + output
		
	una = os.uname()
	for i in una:
		output = i + "\n" + output
	for lang in langages:
		proc = subprocess.Popen(lang["version"] ,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		output = output + "--------------------------------------------\n"
		output = output + lang["name"] + ":" + proc.stdout.read() + proc.stderr.read()
			


	print output
	if option.prog == None  and option.lang == None:
		f = open("results/" + una[1],"w")
		f.write(output)
		f.close()

