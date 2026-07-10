try :
    import sys 
    import requests 
    import platform
    import os 
    from datetime import datetime

    if sys.platform == 'win32' or platform.system() == 'windows' :
        os.system('color')
    

except ModuleNotFoundError : 
    print('''
  [!] Critical Error: Core modules failed to import.
  Please verify your Python environment and dependencies.
        ''')
    exit()

except Exception as e:
    print(f'[!] Unexpected Initialization Error: {e}')
    exit()


banner = '''
                  ;               ,           
                 ,;                 '.         
                ;:                   :;        
               ::                     ::       
               ::                     ::       
               ':                     :        
                :.                    :        
             ;' ::                   ::  '     
            .'  ';                   ;'  '.    
           ::    :;                 ;:    ::   
           ;      :;.             ,;:     ::   
           :;      :;:           ,;"      ::   
           ::.      ':;  ..,.;  ;:'     ,.;:   
            "'"...   '::,::::: ;:   .;.;""'    
                '"""....;:::::;,;.;"""         
            .:::.....'"':::::::'",...;::::;.   
           ;:' '""'"";.,;:::::;.'""""""  ':;   
          ::'         ;::;:::;::..         :;  
         ::         ,;:::::::::::;:..       :: 
         ;'     ,;;:;::::::::::::::;";..    ':.
        ::     ;:"  ::::::"""'::::::  ":     ::
         :.    ::   ::::::;  :::::::   :     ; 
          ;    ::   :::::::  :::::::   :    ;  
           '   ::   ::::::....:::::'  ,:   '   
            '  ::    :::::::::::::"   ::       
               ::     ':::::::::"'    ::       
               ':       """""""'      ::       
                ::                   ;:        
                ':;                 ;:"        
                  ';              ,;'          
                    "'           '           
                      '

'''

# Terminal Color Codes
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
MAROON = "\033[31m"
RESET = "\033[0m"

time = datetime.now()

def header() :
    # Print Header & developer details
    print(MAROON + banner+ RESET)
    print(YELLOW + "    [Developer : Swayam]")
    print(YELLOW + "    [LinkedIn  : https://www.linkedin.com/in/swayam-swapnila-das]")
    print(YELLOW + f'    [Date      : {time.date()}]' + RESET)
    print(YELLOW + f'    [Time      : {time.time()}]' + RESET)
    print('\n' + '='*55 + '\n')


def brute_force(url,wordlist) :
    print(BLUE + 'Wait until you get the completion message...' + RESET)
    if not url.startswith((r'https://',r'http://')) :
        url = rf'https://{url}'

    try :
        with open(wordlist,'r') as file :
            for word in file :
                word = word.strip()
                if not word :
                    continue 
                target_url = rf'{url}/{word}'
                response = requests.get(target_url,allow_redirects = False)
                Status = response.status_code
                if Status >= 200 and Status <= 299 :
                    print(GREEN + f'Page found at : {target_url}' + RESET)
                elif Status >= 500 :
                    print(RED + f'Internal server error at {target_url}' + RESET)
                elif Status >= 300 and Status <= 399 :
                    redirect_location = response.headers.get('Location')
                    print(YELLOW + f"{target_url}" + RESET + ' is moved to ' + BLUE + f"{redirect_location}" + RESET)
                else :
                    continue 

    except FileExistsError :
        print(RED + '    [-]file not exists' + RESET)
    except FileNotFoundError :
        print(RED + '    [-]file not found' + RESET)
    except Exception as e :
        print(RED + f'    [-]Error : {e}' + RESET)
    print(GREEN + '    Process Completed' + RESET)

arguments = sys.argv

if len(arguments) == 3 :
    url = arguments[1]
    wordlist = arguments[2]
    header()
    brute_force(url,wordlist)
else :
    print(RED + 'INVALID ARGUMENTS' + RESET)
    print(YELLOW + 'USE IT LIKE : python spider.py <target_url> <wordlist_path>' + RESET)
