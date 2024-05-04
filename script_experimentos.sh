#!/bin/bash

gcc No_optimizado.c -o nopt -O0

for i in {1..10}
do
	for N in {1000000..5000000..100000}
	do
		./nopt $N
	done
done


