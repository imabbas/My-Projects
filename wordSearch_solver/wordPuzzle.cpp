 // Aadil Abbas
 // aa4zw
 // 10.15.16
 // wordPuzzle.cpp
 // 0.026382 seconds
 // Big Theta (n^2)
 
#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include "hashTable.h"
#include "timer.h"
#include <sstream>

using namespace std;

#define MAXROWS 500
#define MAXCOLS 500
char table[MAXROWS][MAXCOLS];

// Forward declarations
bool readInTable (string filename, int &rows, int &cols);
char* getWordInTable (int startRow, int startCol, int dir, int len,
                      int numRows, int numCols);

bool checkprime(unsigned int p) {
    if ( p <= 1 ) // 0 and 1 are not primes; the are both special cases
        return false;
    if ( p == 2 ) // 2 is prime
        return true;
    if ( p % 2 == 0 ) // even numbers other than 2 are not prime
        return false;
    for ( int i = 3; i*i <= p; i += 2 ) // only go up to the sqrt of p
        if ( p % i == 0 )
            return false;
    return true;
}

unsigned int getNextPrime (unsigned int n) {
    while ( !checkprime(++n) );
    return n; // all your primes are belong to us
}


int main(int argc, char* argv[]) {
    
    vector<string> myvector;
    stringstream s;
    string temp;
    
    
    timer timer;
    
    HashTable myhash;
    
    int temp1 = 0;
    int temp2 = 0;
    int temp3 = 0;
    string temp4 = "";
    unsigned int numberoflines = 0;
    unsigned int a = 0;
    string direction;
    int wordsfound = 0;
    
    

    
    string line;
    ifstream file ((string(argv[1]).c_str()));
    while (getline(file,line)) {
        if(line == "")
            break;
        numberoflines++;
        myhash.insert(line);

    }
    

    
    int rows, cols;
    bool result = readInTable (argv[2], rows, cols);

    if ( !result ) {
        cout << "Error reading in file!" << endl;
        exit(1); 
    }
    
    timer.start();

    
        for( int j = 0; j < rows; j++) {
            for ( int k = 0; k < cols; k++){
                for ( int i = 0; i < 8; i++ ) {
                    for ( int l = 3; l <= 22; l++) {
                        if (string(getWordInTable(j,k,i,l,rows,cols)).length() >= 3 && (j != temp1 || k != temp2 || i != temp3 || getWordInTable(j,k,i,l,rows,cols) != temp4)) {
                            temp1 = j;
                            temp2 = k;
                            temp3 = i;
                            temp4 = getWordInTable(j,k,i,l,rows,cols); 
                            
                        if (myhash.find((string)(getWordInTable(j,k,i,l,rows,cols))) == true) {
                            wordsfound++;
                            if(i==0)
                                direction = "N";
                            if(i==1)
                                direction = "NE";
                            if(i==2)
                                direction = "E";
                            if(i==3)
                                direction = "SE";
                            if(i==4)
                                direction = "S";
                            if(i==5)
                                direction = "SW";
                            if(i==6)
                                direction = "W";
                            if(i==7)
                                direction = "NW";
                            
                            s << direction << "(" << j << "," << k << "):" << getWordInTable(j,k,i,l,rows,cols) << endl;
                            temp = s.str();
                            
                            
                        }
                            

                        }
                    
                        
                    }
                }
            }
        }
        
        timer.stop();
        cout << temp;
        
        
        cout << wordsfound << " words found" << endl;
        cout << "Found all words in " << timer.getTime() << " seconds" << endl;
        cout << ((int)timer.getTime()) * 1000 << endl;
    return 0;
}

    
    
    
    


bool readInTable (string filename, int &rows, int &cols) {
    string line;

    ifstream file(filename.c_str());
    // upon an error, return false
    if ( !file.is_open() )
        return false;
    // the first line is the number of rows: read it in
    file >> rows;
//     cout << "There are " << rows << " rows." << endl;
    getline (file,line); // eats up the return at the end of the line
    // the second line is the number of cols: read it in and parse it
    file >> cols;
//     cout << "There are " << cols << " cols." << endl;
    getline (file,line); // eats up the return at the end of the line
    // the third and last line is the data: read it in
    getline (file,line);
    // close the file
    file.close();
    // convert the string read in to the 2-D grid format into the
    // table[][] array.  In the process, we'll print the table to the
    // screen as well.
    int pos = 0; // the current position in the input data
    for ( int r = 0; r < rows; r++ ) {
        for ( int c = 0; c < cols; c++ ) {
            table[r][c] = line[pos++];
//             cout << table[r][c];
        }
//         cout << endl;
    }
    // return success!
    return true;
}

char* getWordInTable (int startRow, int startCol, int dir, int len,
                      int numRows, int numCols) {
    // the static-ness of this variable prevents it from being
    // re-declared upon each function invocataion.  It also prevents it
    // from being deallocated between invocations.  It's probably not
    // good programming practice, but it's an efficient means to return
    // a value.
    static char output[256];
    // make sure the length is not greater than the array size.
    if ( len >= 255 )
        len = 255;
    // the position in the output array, the current row, and the
    // current column
    int pos = 0, r = startRow, c = startCol;
    // iterate once for each character in the output
    for ( int i = 0; i < len; i++ ) {
        // if the current row or column is out of bounds, then break
        if ( (c >= numCols) || (r >= numRows) || (r < 0) || (c < 0) )
            break;
        // set the next character in the output array to the next letter
        // in the table
        output[pos++] = table[r][c];
        // move in the direction specified by the parameter
        switch (dir) { // assumes table[0][0] is in the upper-left
            case 0:
                r--;
                break; // north
            case 1:
                r--;
                c++;
                break; // north-east
            case 2:
                c++;
                break; // east
            case 3:
                r++;
                c++;
                break; // south-east
            case 4:
                r++;
                break; // south
            case 5:
                r++;
                c--;
                break; // south-west
            case 6:
                c--;
                break; // west
            case 7:
                r--;
                c--;
                break; // north-west
        }
    }
    // set the next character to zero (end-of-string)
    output[pos] = 0;
    // return the string (a C-style char* string, not a C++ string
    // object)
    return output;
}




