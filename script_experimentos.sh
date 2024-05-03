#!/bin/bash

gcc No_optimizado.c -o nopt -O0

for i in {1..10}
do
	for N in {10000..500000..10000}
	do
		./nopt $N
	done
done


