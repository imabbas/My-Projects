#include <iostream>
#include <string>
#include <list>
#include <vector>
using namespace std;


class HashTable {
    
public:
    HashTable();     
    void insert(string word);
    int tablesize;  
    vector<list<string> > hashtable;
    bool find(string word);
    void resize(unsigned int x);
 
private: 
    unsigned int hash(string word);
       
};
