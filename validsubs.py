import subprocess,os
import requests
from sys import argv
from colorama import init,Fore


init()
RESET = Fore.RESET
BLACK = Fore.BLACK
WHITE = Fore.WHITE
GREEN = Fore.GREEN
RED = Fore.RED
CYAN = Fore.CYAN


class Valid_Subs :
    def __init__(self) -> None:
        pass
    def banner(self) :
        print(100*"-")
        print(f""" {WHITE}
        

 __   __  _______  ___      ___   ______     _______  __   __  _______  _______ 
|  | |  ||   _   ||   |    |   | |      |   |       ||  | |  ||  _    ||       |
|  |_|  ||  |_|  ||   |    |   | |  _    |  |  _____||  | |  || |_|   ||  _____|
|       ||       ||   |    |   | | | |   |  | |_____ |  |_|  ||       || |_____ 
|       ||       ||   |___ |   | | |_|   |  |_____  ||       ||  _   | |_____  |
 |     | |   _   ||       ||   | |       |   _____| ||       || |_|   | _____| |
  |___|  |__| |__||_______||___| |______|   |_______||_______||_______||_______|
                                                                  

                                                                                                                                               V 1.1     {WHITE}                                                                           
        Usage : python3 validsubs.py -u site.com

        Options :
        
                -u    ===> Domain
		

{RESET}                           

        """)
        print(100*"-")

    def validation_of_domain(self) :
        domain = f"http://{argv[2]}"
        try :
            res = requests.get(domain)
            return res.status_code
        except Exception : 
            os.system('clear')
            raise ValueError(f"[-] It is not valid domain . Check again ... ")



    def do(self) :
        print(f" {WHITE} [~] Your Target :  {RED} {argv[2]} {RESET}")
        try :
            assetfinder_Subs = list(subprocess.check_output(f"assetfinder {argv[2]} ", shell=True).decode().splitlines())
            # print(assetfinder_Subs)

            subfinder_Subs = list(subprocess.check_output(f"subfinder -d {argv[2]} ", shell=True).decode().splitlines())

            # print(subfinder_Subs)

            subdomains = set(subfinder_Subs + assetfinder_Subs)
            print(subdomains)

            for i in subdomains :

                print(i)
                with open('subs.txt','w') as subs :
                    for sub in subdomains :
                        subs.write(str(sub)+'\n')
                        # subs.close()
                print("[+] Saved to subs.txt")


            valid_hosts = subprocess.check_output(f"httpx -list subs.txt -silent -probe -status-code -ip -cdn -o all_httpx.txt", shell=True)
            valid_hosts = subprocess.check_output(f"awk '!/FAILED/' all_httpx.txt > true_httpx.txt", shell=True)
            print("! check all_httpx.txt and true_httpx.txt Files ")            
           # print(valid_hosts.decode())
        except Exception :  
            raise ValueError(f"[-] this Website Has Not SubDomain ... ")
              

      



if __name__ == '__main__' :
    os.system('clear')
    v = Valid_Subs()
    v.banner()
    is_true = v.validation_of_domain()
    if is_true == 200 :
        v.do()
    else :
        print(f" [-] It is not valid domain . Check again ...")    
