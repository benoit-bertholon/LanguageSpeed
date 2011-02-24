#!/usr/bin/python


import time, os, sys, stat
import optparse



codefolder="codes"
langages=["c","hs","java","ml","pl","mlc","py","rb","php"]
program = [("fibo",["%s"%s for s in range(40,41)]),("simpletri",["unsortedlist l"]),("readandparse",["biglist l"])]







output = ""



if __name__=="__main__":
	parser = optparse.OptionParser(usage="usage: %prog [options]")
#	parser.add_option("-d" , "--dir" ,dest="dir",default=".",help="directory to set the right right")
#	parser.add_option("-v" , "--verbose" ,dest="verbose",default=False ,action='store_true',help="verbose mode")
#	(option , arg ) = parser.parse_args(sys.argv)
#	set_folder_right(option.dir,option.verbose)
	

	for prog,args in program:
		for lang in langages:
			os.system("make -C "+codefolder+ " " + prog + lang)
		for lang in langages:
			for arg in args:
				t1 = time.time()
				cmdline = codefolder + "/" +prog + lang + " " + arg
				print cmdline 
				os.system(cmdline)
				t2 = time.time()
				print prog + lang +" " +arg +" : " , t2-t1
				output = output + prog + lang +" " +arg +" : " + "%f"%( t2-t1 ) + "\n"


	os.system("make -C "+codefolder+ " clean")
	print output

