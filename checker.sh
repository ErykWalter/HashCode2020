#!/bin/bash

total=0

for file in ./a_example.txt ./b_read_on.txt ./c_incunabula.txt ./d_tough_choices.txt ./e_so_many_books.txt  ./f_libraries_of_the_world.txt
do
	cat $file | ./main.py > ans.txt 2> ./improv.txt
	result=$(./checker.out $file ./ans.txt)
	echo $result
	num=$(echo $result | grep -o '[0-9]\+' | tail -n1)
	echo $num
	echo
	total=$((total + num))
done

echo "Total: $total"
