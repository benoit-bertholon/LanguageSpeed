#!/usr/bin/python


import time, os, sys, stat
import optparse



codefolder="codes"
#liste des langages : (nom du langage, fichier source,fichier  executer, cmd de compile, cmd d'execution, cmd de nettoyage)
langages=[
{"name":"c","source":"<PRGM>.c","executable":"<PRGM>c","compile":"gcc -o <EXEC> <SRC> -O2","run":"<EXEC> <ARGS>","clean":"rm <EXEC>"},
{"name":"haskell","source":"<PRGM>.hs","executable":"<PRGM>hs","compile":"ghc --make <SRC> -o <EXEC> -O2","run":"<EXEC> <ARGS>","clean":"rm <EXEC> <EXEC>.o <EXEC>.hi"},
{"name":"java",	"source":"<PRGM>.java","executable":"<PRGM>.class","compile":"javac <SRC>","run":"java <EXEC> <ARGS>","clean":"rm <EXEC>"},
{"name":"ocaml","source":"<PRGM>.ml","executable":None,"compile":None,"run":"ocaml <SRC> <ARGS>","clean":None},
{"name":"ocaml compile","source":"<PRGM>.ml",	"executable":"<PRGM>ml","compile":"ocamlopt <SRC> -o <EXEC>","run":"<EXEC> <ARGS>","clean":"rm <EXEC> <EXEC>.cmx <EXEC>.cmi"},
{"name":"perl",	"source":"<PRGM>.pl","executable":None,"compile":None,"run":"perl <SRC>","clean":None},
{"name":"python","source":"<PRGM>.py","executable":None,"compile":None,"run":"python <SRC>","clean":None},
{"name":"ruby","source":"<PRGM>.rb","executable":None,"compile":None,"run":"ruby <SRC>","clean":None},
{"name":"php","source":"<PRGM>.php","executable":None,"compile":None,"run":"php <SRC>","clean":None}]
#(program,[arguments],precmd,postcmd) liste d'arguemnts => plusieurs instances.
program = [("fibo",["%s"%s for s in range(40,41)],None,None),
("simpletri",["../../unsortedlist ../../sortedlist"],"codes/generate.unsorted.list.py 10000","rm unsortedlist sortedlist"),
("readandparse",["../../unsortedlist ../../unsortedlist2"],"codes/generate.unsorted.list.py 10000","rm unsortedlist unsortedlist2")]



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



if __name__=="__main__":
	parser = optparse.OptionParser(usage="usage: %prog [options]")
#	parser.add_option("-d" , "--dir" ,dest="dir",default=".",help="directory to set the right right")
#	parser.add_option("-v" , "--verbose" ,dest="verbose",default=False ,action='store_true',help="verbose mode")
#	(option , arg ) = parser.parse_args(sys.argv)
#	set_folder_right(option.dir,option.verbose)
	
 
	for prog,args,precmd,postcmd in program:
		balisePRGM = Balise("PRGM",prog)
		#preparation program
		for lang in langages:
			baliseSOURCE = Balise("SRC",lang["source"])
			baliseEXEC = Balise("EXEC",lang["executable"])
			#preparation
			if precmd != None:
				os.system(balise_recursive( precmd,[balisePRGM,baliseSOURCE,baliseEXEC]))
			#cd codes/prgm
			os.curdir = sys.path[0] + "/codes/"+prog
			if lang["compile"] != None:
				os.system(balise_recursive( lang["compile"],[balisePRGM,baliseSOURCE,baliseEXEC]))
			#execution
			for arg in args:
				baliseARGS = Balise("ARGS",arg)
				cmdline = balise_recursive( lang["run"],[balisePRGM,baliseSOURCE,baliseEXEC,baliseARGS])
				print cmdline 
				t1 = time.time()
				os.system(cmdline)
				t2 = time.time()
				print prog + " " + lang["name"] +" " +arg +" : " , t2-t1
				output = output + prog + " " + lang["name"] +" " +arg +" : " + "%f"%( t2-t1 ) + "\n"
			if lang["clean"] != None:
				os.system(balise_recursive( lang["clean"],[balisePRGM,baliseSOURCE,baliseEXEC]))
			if postcmd != None:
				os.system(balise_recursive( postcmd,[balisePRGM,baliseSOURCE,baliseEXEC]))


	os.system("make -C "+codefolder+ " clean")
	print output

