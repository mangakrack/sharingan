import whois
import os
from termcolor import cprint 

os.system("clear")

cprint('''
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
 _____ _                _                         
/  ___| |              (_)                        
\ `--.| |__   __ _ _ __ _ _ __   __ _  __ _ _ __  
 `--. \ '_ \ / _` | '__| | '_ \ / _` |/ _` | '_ \ 
/\__/ / | | | (_| | |  | | | | | (_| | (_| | | | |
\____/|_| |_|\__,_|_|  |_|_| |_|\__, |\__,_|_| |_|
                                 __/ |            
                                |___/             
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
''','red')
#whois
web = input ("dame el url de la pagina:")
whois=whois.query (web)
print (whois.__dict__)
#ping
hostname = (web)
response = os.system("ping -c 1 " + hostname)
#nslookup
os.system("nslookup " + hostname)
#nmap
os.system("nmap -sV --script=banner " + hostname)
