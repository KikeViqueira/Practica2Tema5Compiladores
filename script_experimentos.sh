#!/bin/bash

gcc No_optimizado.c -o nopt -O0

for i in {1..10}
do
	for N in {100000..600000..10000}
	do
		./nopt $N
	done
done


