#! /bin/bash
if [ $# = 1 ]
then
	for i in `find *.c*`
	do
		cp $i $i.$1
	done
		
else
	echo "Mauvais nombre d'arguments"
fi
