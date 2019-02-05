#!/bin/bash
 export negro='\033[1;30m'
 export red='\033[1;31m'
 export green='\033[1;32m'
 export yellow='\033[1;33m'
 export blue='\033[1;34m'
 export magenta='\033[1;35m'
 export cyan='\033[1;36m'
 export white='\033[0m'
function sport {
	clear
	printf "$cyan [$yellow!$cyan]$magenta Select a port // Selecciona un puerto $white
	"
	while read -p ">> " puerto && [ -z $puerto ];do 
		printf "$red Type Something // Escribe algo $white
		"
		sport 
	done
}
function soption {
	clear
	printf "$cyan [$Yellow!$cyan]$magenta Select an option // Selecciona una opcion $white 
	" 
	printf "$magenta 1) Localhost $white 
	" 
	printf "$magenta 2) Localhost + Serveo.net $white 
	" 
	while read -n 1 -p " >> " opc && [ -z $opc ];do
		printf "$red Select an option! // Selecciona una opcion! $white 
		" 
		soption 
	done
}
function srdoc {
	clear
	printf "$cyan [$yellow!$cyan]$magenta rootdocument? EX(/data/data/com.termux/files/home/phproot/)
	" 
	while read -p " >> " rdoc && [ -z $rdoc ];do 
		printf " $red O-ops "
		sleep 2
		srdoc
	done
}
function ssrdoc {
	clear 
	echo "option = $opc 
	" 
	printf "$cyan [$yellow!$cyan]$magenta rootdocument? EX(/data/data/com.termux/files/home/phproot/) 
	" 
	while read -p " >> " srdoc && [ -z $rdoc ];do
		printf " $red O-ops " 
		sleep 2 
		ssrdoc 
	done
}
clear
printf "$cyan [$yellow!$cyan]$magenta Configure it! // Configuralo! $white
"
sleep 2
printf "$cyan [$yellow*$cyan]$magenta Select a port // Selecciona un puerto $white
"
while read -p ">> " puerto && [ -z $puerto ];do
	printf "$red Type Something // Escribe algo $white
	"
	sport
done
echo "port // puerto = $puerto
"
printf "$cyan [$yellow!$cyan]$magenta Select an option // Selecciona una opcion $white
"
printf "$magenta 1) Localhost $white
"
printf "$magenta 2) Localhost + Serveo.net $white
"
while read -p " >> " opc && [ -z $opc ];do
	printf "$red Select an option! // Selecciona una opcion! $white
	"
	soption
done
case $opc in
	1)
		clear
		echo "option = $opc
		"
		printf "$cyan [$yellow!$cyan]$magenta rootdocument? EX(/data/data/com.termux/files/home/phproot/)
		"
		while read -p " >> " rdoc && [ -z $rdoc ];do
			printf " $red O-ops "
			sleep 2
			srdoc
		done
		php -S 127.0.0.1:$puerto -t $rdoc
		;;
	2)
		clear 
		echo "option = $opc 
		" 
		printf "$cyan [$yellow!$cyan]$magenta rootdocument? EX(/data/data/com.termux/files/home/phproot/) 
		" 
		while read -p " >> " srdoc && [ -z $rdoc ];do
			printf " $red O-ops " 
			sleep 2 
			ssrdoc 
		done
		php -S 127.0.0.1:$puerto & ssh -R $puerto:localhost:$puerto serveo.net
		;;
esac

