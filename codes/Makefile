


all: clean


fiboc:fiboc.c
	gcc -o fiboc fiboc.c -O2

fibohs:fibohs.hs
	ghc --make fibohs.hs -o fibohs -O2

fibomlc:fibomlc.ml
	ocamlopt fibomlc.ml -o fibomlc

fibojava:fibojava.java 
	javac fibojava.java
	@echo -n "#" > fibojava
	@echo -n "!" >> fibojava
	@echo -n "/bin/sh\ncd codes\njava fibojava $$" >> fibojava
	@echo  "@" >> fibojava
	chmod u+x fibojava

simpletrihs:simpletrihs.hs
	ghc --make simpletrihs.hs -o simpletrihs -O2

simpletrijava:simpletrijava.java 
	javac simpletrijava.java
	@echo -n "#" > simpletrijava
	@echo -n "!" >> simpletrijava
	@echo -n "/bin/sh\ncd codes\njava simpletrijava $$" >> simpletrijava
	@echo  "@" >> simpletrijava
	chmod u+x simpletrijava

simpletric:simpletric.c
	gcc -o simpletric simpletric.c -O2

simpletrimlc:simpletrimlc.ml
	ocamlopt simpletrimlc.ml -o simpletrimlc




readandparsehs:readandparsehs.hs
	ghc --make simpletrihs.hs -o readandparsehs -O2

readandparsejava:readandparsejava.java 
	javac readandparsejava.java
	@echo -n "#" > readandparsejava
	@echo -n "!" >> readandparsejava
	@echo -n "/bin/sh\ncd codes\njava readandparsejava $$" >> readandparsejava
	@echo  "@" >> readandparsejava
	chmod u+x readandparsejava

readandparsec:readandparsec.c
	gcc -o readandparsec readandparsec.c -O2

readandparsemlc:readandparsemlc.ml
	ocamlopt readandparsemlc.ml -o readandparsemlc













clean:
	rm *.hi *.o *.cmi *.cmx fiboc fibohs fibomlc fibojava simpletrijava  simpletrihs  simpletric readandparsec readandparsemlc readandparsejava  readandparsehs


