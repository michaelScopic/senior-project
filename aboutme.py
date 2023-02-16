#   Source code for my seinor presentation.
#   Wrote it in python to be interactive and portable
#   Have fun looking around!
#   I've put comments in case you are curious on what the code does. :)
#   - Michael

#### Import modules here
import time
import os


#### Define text colors/formating here
class Colors:
    reset = "\033[0m"
    bold = "\033[1m"
    underline = "\033[4m"
    red = "\033[31m"
    redbg = "\033[41m"
    green = "\033[32m"
    greenbg = "\033[42m"
    yellow = "\033[33m"
    yellowbg = "\033[43m"
    blue = "\033[34m"
    bluebg = "\033[44m"
    purple = "\033[35m"
    purplebg = "\033[45m"
    cyan = "\033[36m"
    cyanbg = "\033[46m"


#### Define message blocks
# Info msg
def msg_info(*args):
    print(
        f"{Colors.yellow}{Colors.bold}[INFO]{Colors.reset} {' '.join(args)} {Colors.reset}"
    )


# Success msg
def msg_success(*args):
    print(
        f"{Colors.green}{Colors.bold}[SUCCESS]{Colors.reset} {' '.join(args)} {Colors.reset}"
    )


# Error msg
def msg_error(*args):
    print(
        f"{Colors.red}{Colors.bold}[ERROR]{Colors.reset} {' '.join(args)} {Colors.reset}"
    )


# Question msg
def msg_question(*args):
    print(
        f"{Colors.red}{Colors.bold}[QUESTION]{Colors.reset} >> {' '.join(args)} {Colors.reset}"
    )


# An 'ok' msg when faking intializing
def ok_stat(*args):
    print(f"[ {Colors.green}ok{Colors.reset} ] {' '.join(args)}")


### Clear the screen with this
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


### (Pretend to) initalize, just intentionally wastes some time
def init():
    clear_screen()
    print("==> Initalizing... <==")
    time.sleep(0.3)
    ok_stat("Set colors...")
    time.sleep(0.6)
    ok_stat("Set message functions...")
    time.sleep(1)
    ok_stat("Set 'clear_screen()' function...")
    time.sleep(0.4)
    ok_stat("Defining variables...")
    time.sleep(0.5)
    ok_stat("Setup intro...")
    time.sleep(0.4)
    ok_stat("Setup pillar one...")
    time.sleep(0.2)
    ok_stat("Setup pillar two...")
    time.sleep(0.3)
    ok_stat("Setup pillar three...")
    time.sleep(0.6)
    ok_stat("Setting up TUI menu...")
    time.sleep(1)
    ok_stat("Cracking nuclear launch codes...")
    time.sleep(0.4)
    ok_stat("Hacking into Russian satelllites....")
    ok_stat("Sending balistic missiles to: 40.41736° N, 82.90771° W ...")
    ok_stat("Done!")
    time.sleep(1)
    msg_success("==> Finished initalizing! <==\n")
    time.sleep(2)


#### Display intro
def intro():
    clear_screen()
    print(f"{Colors.bold}-------- [         INTRO        ] --------{Colors.reset}\n")
    print("This is my very creative Senior project.")
    print("I don't know how to fill up the rest of this space.")
    print("So I'll just do this.")
    print("A bit awkward but at least it's something.")
    print("You can view this script's source code at:")
    print(f"{Colors.blue}{Colors.underline}https://github.com/michaelScopic/senior-project{Colors.reset}")
    print("Note: Because this repository is public, I cannot disclose the name of my school.\n")
    print(f"{Colors.bold}------------------------------------------{Colors.reset}\n")


#### Display pillar one
def pillar_one():
    clear_screen()
    print(f"{Colors.bold}-------- [     PILLAR ONE     ] --------{Colors.reset}\n")
    msg_question("What challenges do you think you will face in the next phase of life?\n")
    msg_question("How has this school supported your growth in terms of life-readiness?\n")
    msg_question("Show how you are/aren't ready for the real world.\n")
    msg_question("Has this school, or anything for the last 4 years made you reflect/develop")
    msg_question("the skills necessary to survive alone? \n")
    msg_question("Do you think that you have made your own choices or just fit in with")
    msg_question("the social norm?\n")
    print(f"{Colors.bold}-----------------------------------------{Colors.reset}\n")

#### Display pillar two
def pillar_two():
    clear_screen()
    print(f"{Colors.bold}-------- [     PILLAR TWO     ] --------{Colors.reset}\n")
    
    
    print(f"{Colors.bold}-----------------------------------------{Colors.reset}\n")

### Display pillar three
def pillar_three():
    clear_screen()
    print(f"{Colors.bold}-------- [     PILLAR THREE     ] --------{Colors.reset}\n")
    
    
    print(f"{Colors.bold}------------------------------------------{Colors.reset}\n")


#### --> Start here <--
init()
clear_screen()

#### Display menu
while True:
    # Print menu options
    print(f"{Colors.bold}--- Please choose an option: ---{Colors.reset}")
    print(f"1.{Colors.blue} Intro {Colors.reset}")
    print(f"2.{Colors.yellow} Pillar one:{Colors.reset} College and career ready")
    print(f"3.{Colors.purple} Pillar two:{Colors.reset} Globally aware")
    print(f"4.{Colors.cyan} Pillar three:{Colors.reset} Future focused\n")
    print(f"0.{Colors.red}{Colors.bold} Exit program{Colors.reset}\n")
    print("Put your desired number here: ")

    # Get user input
    choice = input()

    # Process user input
    if choice == "1":
        msg_info("User chose: Intro\n")
        intro()

    elif choice == "2":
        msg_info("User chose: College and career ready\n")
        pillar_one()

    elif choice == "3":
        msg_info("User chose: Globally aware\n")


    elif choice == "4":
        msg_info("User chose: Future focused\n")
        
        
    elif choice == "0":
        msg_error("User quited...")
        msg_error("Goodbye!")
        break
        
    else:
        msg_error("Invalid choice, please try again.")
