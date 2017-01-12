
CXX	= clang++

CXXFLAGS	= -Wall -O2 -g 

OFILES	= wordPuzzle.o hashTable.o timer.o


.SUFFIXES: .o .cpp


main:	$(OFILES)
	$(CXX) $(OFILES)


clean:
	/bin/rm -f *.o *~


hashTable.o: hashTable.cpp hashTable.h 
wordPuzzle.o: wordPuzzle.cpp hashTable.h 
