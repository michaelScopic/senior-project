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
    reset = '\033[0m'
    bold = '\033[1m'
    red = '\033[31m'
    redbg = '\033[41m'
    green = '\033[32m'
    greenbg = '\033[42m'
    yellow = '\033[33m'
    yellowbg = '\033[43m'
    blue = '\033[34m'
    bluebg = '\033[44m'
    purple = '\033[35m'
    purplebg = '\033[45m'
    cyan = '\033[36m'
    cyanbg = '\033[46m'

#### Define message blocks
# Info msg
def msg_info(*args):
    print(f"{Colors.yellow}{Colors.bold}[INFO]{Colors.reset} {' '.join(args)} {Colors.reset}")

# Success msg
def msg_success(*args):
    print(f"{Colors.green}{Colors.bold}[SUCCESS]{Colors.reset} {' '.join(args)} {Colors.reset}")

# Error msg
def msg_error(*args):
    print(f"{Colors.red}{Colors.bold}[ERROR]{Colors.reset} {' '.join(args)} {Colors.reset}")

# Question msg
def msg_question(*args):
    print(f"{Colors.red}{Colors.bold}[QUESTION]{Colors.reset} ?? {' '.join(args)} {Colors.reset}")

# Answer msg
def msg_answer(*args):
    print(f"{Colors.blue}{Colors.bold}[ANSWER]{Colors.reset} >> {' '.join(args)} {Colors.reset}")

### Clear the screen with this
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


#### Define a function to display the intro
def intro():
    clear_screen()
    print("-------- [        INTRO        ] --------")
    msg_info("This is my very creative Senior project.")
    msg_info("I don't know how to fill up the rest of this space.")
    msg_info("So I'll just do this.")
    msg_info("A bit awkward but at least it's something.")
    msg_info("You can view this script's source code at:") 
    msg_info("https://github.com/michaelScopic/senior-project")
    msg_success("--- Finished intro. ---")
    print("------------------------------------------\n")

#### Function to display the college and career ready section
def college_career():
    clear_screen()
    print("-------- [     PILLAR ONE     ] --------")
    msg_question("What challenges do you think you will face in the next phase of life?") 
    msg_question("Are you prepared for those challenges?\n")
    msg_answer("Most of my challenges will probably be getting a job and living independantly.")
    msg_answer("I have mental disorders/disabilities, so being independant will be a challenge for me,")
    msg_answer("as I have difficulty remembering to do tasks.")
    
    print("-----------------------------------------\n")

### (Pretend to) initalize, just intentionally wastes some time (I'll need this even if it last for a few secs)
print("--- Initalizing... ---")
time.sleep(0.3)
print("[ ok ] Set colors...")
time.sleep(0.6)
print("[ ok ] Set message functions...")
time.sleep(1)
print("[ ok ] Set 'clear_screen()' function...")
time.sleep(0.4)
print("[ ok ] Defining variables...")
time.sleep(0.5)
print("[ ok ] Setup intro...")
time.sleep(0.4)
print("[ ok ] Setup pillar one...")
time.sleep(0.2)
print("[ ok ] Setup pillar two...")
time.sleep(0.3)
print("[ ok ] Setup pillar three...")
time.sleep(0.6)
print("[ ok ] Setting up TUI menu...")
print("[ ok ] Done!")
time.sleep(1)
msg_success("--- Finished initalizing! Continuing... ---")
time.sleep(2)

### Display menu
clear_screen()
while True:
    # Print menu options
    print(f"{Colors.bold}--- Please choose an option: ---{Colors.reset}")
    print(f"1.{Colors.blue} Intro {Colors.reset}")
    print(f"2.{Colors.yellow} Pillar one:{Colors.reset} College and career ready")
    print(f"3.{Colors.purple} Pillar two:{Colors.reset} ")
    print(f"4.{Colors.cyan} Pillar three:{Colors.reset} ")
    print()
    print(f"0.{Colors.red}{Colors.bold} Exit program{Colors.reset}")
    print(f"")
    print(f"Put your desired number here: ")

    # Get user input
    choice = input()

    # Process user input
    if choice == '1':
        msg_info("User chose: Intro\n")
        intro()
        
    elif choice == '2':
        msg_info("User chose: College and career ready\n")
        college_career()
        
    elif choice == '3':
        msg_info("You chose option 3")
        
    elif choice == '0' or 'q':
        msg_error("User quited...")
        msg_error("Goodbye!")
        break
    else:
        msg_error("Invalid choice, please try again.")

