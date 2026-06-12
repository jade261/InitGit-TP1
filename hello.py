from colorama import init, Fore, Style 
init() 

def display(): 
<<<<<<< HEAD
    message = f"{Fore.GREEN}Bonjour les {Fore.CYAN}tout le monde !{Style.RESET_ALL}" 
=======
    message = f"{Fore.GREEN}Ceci est une {Fore.CYAN}modification{Style.RESET_ALL}" 
>>>>>>> 012d6a556a2281ef95bb8d86543bf25f72db0a85
    print(message)   

if __name__ == "__main__": 
    display() 