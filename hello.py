from colorama import init, Fore, Style 
init() 

def display(): 
    message = f"{Fore.GREEN}Bonjour {Fore.CYAN}tout le monde en FI1 !{Style.RESET_ALL}" 
    print(message)   

if __name__ == "__main__": 
    display() 