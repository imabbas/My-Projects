#!/bin/bash

# User input for dictionary file
read -p "Dictionary file: " dictionary 

# User input for grid file
read -p "Grid File: " grid


# Run program 5 times using user input and save running time
RUNNING_TIME1=`./a.out $dictionary $grid | tail -1`
RUNNING_TIME2=`./a.out $dictionary $grid | tail -1`
RUNNING_TIME3=`./a.out $dictionary $grid | tail -1`
RUNNING_TIME4=`./a.out $dictionary $grid | tail -1`
RUNNING_TIME5=`./a.out $dictionary $grid | tail -1`

# Add 5 running times and divide by 5 to get average
echo $[($RUNNING_TIME1 + $RUNNING_TIME2 + $RUNNING_TIME3 + $RUNNING_TIME4 + $RUNNING_TIME5) / 5]
