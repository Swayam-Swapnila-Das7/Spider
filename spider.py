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
            .:::.....'''::::::'",...;::::;.   
           ;:' '""'"';.,;:::::;.''""""  ':;   
          ::'         ;::;:::;::..         :;  
         ::         ,;:::::::::::;:..       :: 
         ;'     ,;;:;::::::::::::::;";..    ':.
        ::     ;:"  ::::::"""'::::::  ":     ::
         :.    ::   ::::::;  :::::::   :     ; 
          ;    ::   :::::::  :::::::   :    ;  
           '   ::   ::::::....:::::'  ,:   '   
            '  ::    ::::::::::::;"   ::       
               ::     '::::::::;"'    ::       
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

def show_header() :
    # Print Header & developer details
    print(MAROON + banner+ RESET)
    print(YELLOW + "    [Developer : Swayam]")
    print(YELLOW + "    [LinkedIn  : https://www.linkedin.com/in/swayam-swapnila-das]")
    print(YELLOW + f'    [Date      : {time.date()}]' + RESET)
    print(YELLOW + f'    [Time      : {time.time()}]' + RESET)
    print('\n' + '='*55 + '\n')


def show_help():
    print(BLUE + "\n    " + "="*55 + RESET)
    print(YELLOW + "                URL Directory Enumerator Help" + RESET)
    print(BLUE + "    " + "="*55 + RESET)
    print(f"""
    This tool is designed to perform directory and page enumeration against 
    a target URL using a provided wordlist to identify accessible paths.

    {GREEN}USAGE MODES:{RESET}

    1. {BLUE}Interactive Menu (CLI Loop){RESET}
        Simply run the script without any arguments:
        {YELLOW}python script.py{RESET}
        The program will guide you through entering the target URL and wordlist path.

    2. {BLUE}Direct Command Line Arguments{RESET}
        Pass the target URL and wordlist file path directly when launching:
        {YELLOW}python script.py <Target_URL> <Path_To_Wordlist>{RESET}
         Example:
        python script.py example.com common.txt

    {GREEN}ARGUMENT DETAILS:{RESET}
        {YELLOW}Target URL:{RESET}     The domain or IP address to scan.
                   The script automatically enforces HTTPS protocols if missing.
        {YELLOW}Wordlist File:{RESET}  A plain text file containing directories/filenames to test 
                   (one entry per line).

    {GREEN}OPTIONS:{RESET}
        {YELLOW}help OR h(NOT CASE SENSITIVE){RESET}            Displays this reference guide.

    ------------------------------------- NOTE --------------------------------------
    ONLY USE THIS ON THE NETWORKS YOU OWN OR HAVE EXPLICIT PERMISSION TO USE AND TEST
    ---------------------------------------------------------------------------------
    """)
    print(BLUE + "    " + "="*55 + "\n" + RESET)


def execute_brute_force(url,wordlist) :
    print(BLUE + 'Wait until you get the completion message...' + RESET)
    if not url.startswith((r'https://',r'http://')) :
        url = rf'https://{url}'

    try :
        with open(wordlist,'r') as file :
            for word in file :
                #remove all leading and ending white spaces form word
                word = word.strip() 

                #Check ,if there was any word or not
                if not word :
                    continue 
                    
                #set the url,before sending get request
                target_url = rf'{url}/{word}'   
                
                response = requests.get(target_url,allow_redirects = False)
                Status = response.status_code
                if Status >= 200 and Status <= 299 :                   #Status codes for Success
                    print(GREEN + f'  [+] Page found at : {target_url}\n' + RESET)
                elif Status >= 500 :                                   #status code for internal server error
                    print(RED + f'  [-] Internal server error at {target_url}\n' + RESET)
                elif Status >= 300 and Status <= 399 :                   #if the page redirect to some where else
                    redirect_location = response.headers.get('Location')
                    print(YELLOW + f"  [!]{target_url}" + RESET + ' is moved to \n' + BLUE + f"{redirect_location}" + RESET)
                elif Status in [401,403,405] :                            #if target exist but require permission/verification/authentication
                    print(RED + '  [!] Page Exists but need verification : {target_url}\n' + RESET)
                else :                                                   #else skip and keep going ,don't mess the output window
                    continue 

    except FileExistsError :
        print(RED + '    [-]file not exists' + RESET)
    except FileNotFoundError :
        print(RED + '    [-]file not found' + RESET)
    except Exception as e :
        print(RED + f'    [-]Error : {e}' + RESET)
    print(GREEN + '    Process Completed' + RESET)



def open_interactive_menu():
    header()
    # Main Interactive CLI Loop
    while True:
        print(MAROON + '\n[ MAIN INTERFACE ]' + RESET)
        print(BLUE + '  [1] Start Brute force' + RESET)
        print(BLUE + '  [2] Help' + RESET)
        print(BLUE + '  [3] Terminate Program' + RESET)
    
        choice = input('\nSelect option ID (1-3): ').strip()
    
        match choice:
            case '1':
                url = input(YELLOW + 'Enter the target URL Address : ' + RESET)
                wordlist = input(YELLOW + 'Enter the Wordlist File Path: ' + RESET)
                brute_force(url,wordlist)
            case '2':
                help()
            case '3':
                print(GREEN + "\n[+] Session closed safely !" + RESET)
                break 
            case _:
                print(RED + '\n[-] Invalid Input: Please specify a choice between available valid options !' + RESET)
                

arguments = sys.argv

if len(arguments) == 3 :
    url = arguments[1]
    wordlist = arguments[2]
    show_header()
    execute_brute_force(url,wordlist)
elif len(arguments) == 2 and arguments[1].lower() in ['help','-h'] :
    show_help()
elif len(arguments) == 1 :
    open_interactive_menu()
elif len(arguments) > 3 :
    print(RED + '    too much argument passed' + RESET)
else : 
    print(RED + '    invalid argument' + RESET)
