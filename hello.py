from colorama import init, Fore, Style 
init() 

def display(): 
    message = f"{Fore.GREEN}Bonjour les {Fore.CYAN}tout le monde !{Style.RESET_ALL}" 
    print(message)   

if __name__ == "__main__": 
    display() 