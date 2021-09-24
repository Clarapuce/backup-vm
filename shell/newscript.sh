#! /bin/bash
touch $1.sh
chmod u+x $1.sh
echo '#! /bin/bash' > $1.sh
echo 'if [ $# = 1 ] \nthen\n\nelse\n\techo "Probleme avec les arguments"\nfi' >> $1.sh
gedit "$1.sh"& 
exit 0
