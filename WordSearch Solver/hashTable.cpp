// Aadil Abbas
// aa4zw
// 10.16.16
// hashTable.cpp

#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include "hashTable.h"

using namespace std; 

HashTable::HashTable() {
    
    int x = 2897;
    tablesize = x;
    hashtable.resize(x);
}

bool HashTable::find(string word) {
    
    list<string>::iterator it;
    unsigned int x = hash(word);
    
    for(it = hashtable.at(x).begin(); it != hashtable.at(x).end(); it++) {
        if(word.compare(*it) == 0)
            return true;
    }
      
        return false;

    
    
}

void HashTable::insert(string word) {
    
    hashtable.at(hash(word)).push_back(word);
    
}

unsigned int HashTable::hash(string word) {
    
    unsigned int final = 0;
    unsigned int first = 0;
    
    for(int k = 0; k < (word.length()); k++) {
        
        first = first + (int)((word[k] * (41*k)));
        first = first + word.length();
    }
    final = (first % tablesize);

    
    return final;
    
}


void HashTable::resize(unsigned int x) {
    hashtable.resize(x);
}



