#This code was made in Python 3.7 
#and was devloped by HamzaOPLEX 
#Facebook : facebook.com/Hamza0plex
#Website : www.freetechways.xyz
#Youtube : https://www.youtube.com/channel/UCbeSJJWGNppv5decBIjsfuw
#github : github.com/HamzaOPLEX

import os
import sys
print("Enter the user file Path : ")
path_in_check = input("File-PATH>>>")
if_exist = os.path.exists(path_in_check)
if_file = os.path.isfile(path_in_check)
if if_exist and if_file is True :
    print("[+] File Found")
    filepath = path_in_check
if if_exist == False :
    print("[!] File Not Found")
    sys.exit()
if if_file == False :
    print("[!] File Not Found")
    sys.exit()
file_open = open(filepath,'r')
N_lines = len(file_open.readlines())
file_open.close()
Dc_DN = input("Enter your Domain Controller DN\nExample DN :dc=OPLEX,dc=com\nDC-DN>>>")
Users_DN = input("Where do you want to add this users (DN)\nExample DN :ou=NASA,dc=OPLEX,dc=com\nOU-DN>>>")
def dsadd(): ############################################################ add users in File

################################################################# check if users in file are exist
    dsquery = 'dsquery user "{}" -name {}'
    dsquery_run = dsquery.format(Dc_DN.strip(),line.strip())
    dsquery_cmd = os.popen(dsquery_run).read()
    if dsquery_cmd: #if exist exit
        check = "{} is exist".format(line.strip())
        print(check)
############################################################# if not exist add them 
    if not dsquery_cmd:
        dsadd = 'dsadd user "Cn={},{}" -disabled yes'
        dsadd_run = dsadd.format(line.strip(),Users_DN.strip())
        os.system(dsadd_run)
        print(dsadd_run)
def dsrm(): ######################## remove the users in file
    dsrm = 'dsrm "Cn={},ou=NASA,dc=ismontic,dc=ma" -noprompt'
    dsrm_run = dsrm.format(line.strip())
    os.system(dsrm_run)
    print(dsrm_run)
def dsget(): ####################### show the users DN in file |if not exist print Object not found
    dsquery2 = 'dsquery user "dc=ismontic,dc=ma" -name {}'
    dsquery2_run = dsquery2.format(line.strip())
    dsquery2_cmd = os.popen(dsquery2_run).read()
    if dsquery2_cmd:
        a = "[+] {} : {}"
        print(a.format(line.strip(),dsquery2_cmd))
    if not dsquery2_cmd :
        b = "[!] {} : Object Not Found"
        print(b.format(line.strip()))
while True: #Run All The Functions 
    print("Welcom to use the script Type : \n1-add(a) : for adding users\n2-modify(m) : for modification in attribute\n3-delete(d) : for deleting users\n4-get(g) : for check and show the users dn\n")
    AD_ask = input("CMD>>>")
    with open(filepath) as fp:
       for i in range(N_lines):
           line = fp.readline()
           if AD_ask == "add":
               dsadd()
           if AD_ask == "modify":
                if i == 0 :
                    print("\n")  
                    print("\tEnter The dsmod options and be careful in writing them\n\t(see the help of the command here)")
                    print("dsmod option : \nExample : >>>-desc <description> -pwd <Pawssowrd> -upn <UPN> ....")
                    print("\n\t#######################################################")
                    print("\n\t For more dsmod Option use the command 'dsmod /?' ")
                    print("\n\t#######################################################")
                    dsmod_option = input("dsmod>>>")
                dsmod = 'dsmod user "Cn={},{}" {}'
                dsmod_run = dsmod.format(line.strip(),Users_DN.strip(),dsmod_option.strip())
                os.system(dsmod_run)
                print(dsmod_run)
           if AD_ask == "delete":
               dsrm()
           if AD_ask == "get":
               dsget()
