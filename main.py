#   Source code for my seinor presentation.
#   Wrote it in python to be interactive and portable
#   Have fun looking around!
#   I've put comments in case you are curious on what the code does. :)
#   - Michael
#
# Written by: michaelScopic (https://github.com/michaelScopic)


#### Import modules here
import time
import os
import getpass


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
        f"{Colors.red}{Colors.bold}[QUESTION]{Colors.reset} ?? {Colors.yellow}{' '.join(args)} {Colors.reset}"
    )
    
# Answer msg
def msg_answer(*args):
    print(
        f"{Colors.blue}{Colors.bold}[ANSWER]{Colors.reset} >> {Colors.bold}{' '.join(args)} {Colors.reset}"
    )

# An 'ok' msg when faking intializing
def ok_stat(*args):
    print(
        f"[  {Colors.green}OK{Colors.reset}  ] {' '.join(args)}"
    )


### Clear the screen with this
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


### (Pretend to) initalize, just intentionally wastes some time
def init():
    clear_screen()
    print("==> Initalizing... <==")
    print("=> STAGE 1/4")
    ok_stat("Started systemd.")
    time.sleep(1)
    ok_stat("Found mount points.")
    ok_stat(f"Reached target: {Colors.bold}Basic system{Colors.reset}")
    time.sleep(1)
    print(f"         Starting {Colors.bold}Network{Colors.reset}...")
    time.sleep(0.6)
    print(f"         Starting {Colors.bold}Bluetooth daemon{Colors.reset}...")
    time.sleep(0.8)
    print(f"         Started {Colors.bold}D-Bus message bus{Colors.reset}...")
    time.sleep(0.4)
    print(f"         Starting {Colors.bold}NTP client/server{Colors.reset}...")
    time.sleep(0.3)
    print(f"         Started {Colors.bold}Virtualization daemon{Colors.reset}.")
    time.sleep(0.3)
    print(f"         Starting {Colors.bold}CUPS Scheduler{Colors.reset}...")
    time.sleep(0.7)
    print(f"         Scanning {Colors.bold}iSCSI devices{Colors.reset}...")
    time.sleep(0.2)
    print(f"         Scanning {Colors.bold}Serial ATA drives{Colors.reset}...")
    time.sleep(0.5)
    ok_stat(f"Started {Colors.bold}System Logging Service{Colors.reset}.")
    time.sleep(0.7)
    print(f"         Starting {Colors.bold}Network Manager Script Dispatcher Service{Colors.reset}...")
    time.sleep(0.6)
    ok_stat(f"Starting {Colors.bold}Virtual Machine{Colors.reset}...")
    time.sleep(0.2)
    ok_stat(f"Started {Colors.bold}X11 Display Server{Colors.reset}.")
    ok_stat("Waiting on Network...")
    time.sleep(5)
    for x in range(10):
        time.sleep(1.5)
        print(f"{Colors.red}         Network timed out.{Colors.reset}")
    else:
        print(f"         Network established on {Colors.bold}eth0{Colors.reset}.")
    time.sleep(2)
    print(f"{Colors.bold}=> STAGE 2/4{Colors.reset}")
    ok_stat("Set colors...")
    time.sleep(0.6)
    ok_stat("Setting up message functions. This can take a bit...")
    time.sleep(0.5)
    ok_stat(f"{Colors.bold}msg_info(){Colors.reset} -- Finished.")
    time.sleep(0.4)
    ok_stat(f"{Colors.bold}msg_success(){Colors.reset} -- Finished.")
    time.sleep(0.3)
    ok_stat(f"{Colors.bold}msg_error(){Colors.reset} -- Finished.")
    time.sleep(0.6)
    ok_stat(f"{Colors.bold}msg_question(){Colors.reset} -- Finished.")
    time.sleep(0.5)
    ok_stat(f"{Colors.bold}msg_answer(){Colors.reset} -- Finished.")
    time.sleep(0.7)
    time.sleep(0.2)
    print(f"{Colors.bold}=> STAGE 3/4{Colors.reset}")
    ok_stat("Set 'clear_screen()' function...")
    time.sleep(0.4)
    ok_stat("Defining variables...")
    time.sleep(0.5)
    ok_stat("Setup intro...")
    time.sleep(0.4)
    ok_stat("Setup life resume...")
    time.sleep(0.7)
    ok_stat("Setup pillar one...")
    time.sleep(0.2)
    ok_stat("Setup pillar two...")
    time.sleep(0.3)
    ok_stat("Setup pillar three...")
    time.sleep(0.6)
    ok_stat("Setup self reflection...")
    time.sleep(2)
    print(f"{Colors.bold}=> STAGE 4/4{Colors.reset}") 
    time.sleep(0.5)
    ok_stat("Setting up TUI menu...")
    time.sleep(1)
    ok_stat("Cracking nuclear launch codes...")
    time.sleep(0.4)
    ok_stat("Hacking into Russian satelllites....")
    time.sleep(0.3)
    ok_stat("Sending balistic missiles to: 40.41736° N, 82.90771° W ...")
    time.sleep(1)
    time.sleep(1)
    msg_success("==> Finished initalizing! <==\n")
    time.sleep(2)


#### Display intro
def intro():
    clear_screen()
    print(f"{Colors.bold}-------- [         INTRO        ] --------{Colors.reset}\n")
    print(f"{Colors.bold}{Colors.underline}Hey hey, I'm Michael.{Colors.reset}")
    print(f"{Colors.green}I'm a Linux enthusiast, computer/hardware nerd, and Minecraft veteran.\n")

    print("I do karate and kickboxing with my best friend Jonathan.")
    print("I write automation for Linux systems, and aspiring to get a job in DevOps or becomming a sysadmin.")
    print("I mostly write scripts with Bash, but I'm learning more Python, which this presentation is written in.\n")

    print(f"\n{Colors.bold}You can view this script's source code at:{Colors.reset}")
    print(f"{Colors.blue}{Colors.underline}https://github.com/michaelScopic/senior-project{Colors.reset}\n")
    print("- Note: Because this repository is public, I cannot disclose my full name or the name of my school.\n")
    print(f"{Colors.bold}------------------------------------------{Colors.reset}\n")
    getpass.getpass(f"Press {Colors.bold}{Colors.blue}[ENTER]{Colors.reset} to return to main menu... ")
    
    
#### Display life resume
def life_resume():
    clear_screen()
    print(f"{Colors.bold}-------- [     LIFE RESUME     ] --------{Colors.reset}\n")
    print(f"{Colors.red}My favorate numbers are 5 and multipules of 2 (eg: 2, 4, 8, 16, 32, 64, ...).{Colors.reset}\n")
    print(f"{Colors.cyan}Favorate anime: The Disastrous Life of Saiki K.{Colors.reset}\n")
    print(f"{Colors.yellow}Favorate music genre: Phonk (both agressive and chill){Colors.reset}\n")
    print(f"{Colors.blue}If I could go back in history, I would go to the Civil War and make them fight with grenades.{Colors.reset}\n")
    
    print(f"{Colors.bold}-----------------------------------------{Colors.reset}\n")
    getpass.getpass(f"Press {Colors.bold}{Colors.blue}[ENTER]{Colors.reset} to return to main menu... ")


#### Display pillar one
def pillar_one():
    clear_screen()
    print(f"{Colors.bold}-------- [     PILLAR ONE     ] --------{Colors.reset}\n")
    msg_question("What challenges do you think you will face in the next phase of life?")
    msg_answer("I have mental disorders, so getting a job and being independent will be a challenge, as I have difficulty remembering to do tasks.\n")

    msg_question("How has this school supported you in terms of life readiness?")
    msg_answer("This school has shown that I can’t just work on my own interests, and that I need to do things even though I don’t want to.")
    msg_answer("They provided me with an IEP to cater to my needs, like for my ADHD and social anxiety. \n")
    
    msg_question("Prove to us that you are ready for the next step in life.")
    msg_answer("Am I ready for the real world? Probably not.")
    msg_answer("I have problems remembering to do stuff, I’m anxious all the time, and I’ll even get a panic attack under certain conditions.")
    msg_answer("For now, I’m just going to live with my dad, get a decent job, and down the line I’ll go to college.\n")
    
    print(f"{Colors.bold}-----------------------------------------{Colors.reset}\n")
    getpass.getpass(f"Press {Colors.bold}{Colors.blue}[ENTER]{Colors.reset} to return to main menu... ")


#### Display pillar two
def pillar_two():
    clear_screen()
    print(f"{Colors.bold}-------- [     PILLAR TWO     ] --------{Colors.reset}\n")
    msg_question("How big is your globe? What is the scope of your knowledge and daily interaction?")
    msg_answer("My globe/scope is limited to my immediate environment and who I interact with.")
    msg_answer("Expanding my scope for the world outside brings a lot more confusion and worry for me.\n")
    
    msg_question("What is the most impactful learning you have done about something outside of your own life?")
    msg_answer("Honestly, I haven’t really done anything outside of what I’m supposed to do. I can’t have empathy towards something because my brain is unable to “walk in their shoes”.") 
    msg_answer("I can’t process other people’s feelings because emotions are unpredictable and unstable to me. For example: Bob is happy today. What do you think he would feel the next day? To me, it’s impossible to answer that because so many things can affect how someone feels.")
    print(f"{Colors.bold}-----------------------------------------{Colors.reset}\n")
    getpass.getpass(f"Press {Colors.bold}{Colors.blue}[ENTER]{Colors.reset} to return to main menu... ")   
    
### Display pillar three
def pillar_three():
    clear_screen()
    print(f"{Colors.bold}-------- [     PILLAR THREE     ] --------{Colors.reset}\n")
    msg_question("What is your definition of a future focused individual?")
    msg_answer("Someone who is future focused is someone who has laid the foundation for what they will do in the future.")
    msg_answer("Like deciding what college to go to, what career they want to purse, where they will live, who they will live with, etc.\n")
    
    msg_question("Discuss how, if in any way, your time at this school has supported that.")
    msg_answer("After being more exposed to computers (mostly thanks to my dad) and taking AP computer science, I want to get a career in the IT department.")
    msg_answer("I know that I don't want to web development now, and I want to teach myself more about automation and being a sysadmin.")
    print(f"{Colors.bold}------------------------------------------{Colors.reset}\n")
    getpass.getpass(f"Press {Colors.bold}{Colors.blue}[ENTER]{Colors.reset} to return to main menu... ")


### Display self reflection
def self_reflection():
    clear_screen()
    print(f"{Colors.bold}-------- [     SELF REFLECTION     ] --------{Colors.reset}\n")
    msg_question("Do you think you represented your best self in your time in high school?")
    msg_answer("Honestly, I have no idea what my “best self” would look like.")
    msg_answer("I think I’ve done a decent job under all the weight of school, my parents, my friends, and even myself. Because of how restrictive school is, I probably wouldn’t be able to represent my “best self”.\n")
    
    msg_question("Where do you see yourself progressing from here and how did high school influence that path?")
    msg_answer("After I leave high school, I will learn more about scripting/programming by myself and then go to a tech college down the line.")
    msg_answer("School influenced this path because it made me realize that web development is not for me.")
    msg_answer("My CS teacher also assisted me with the DevOps/sysadmin side as well, which encourages me to continue down the path I want.")
    print(f"{Colors.bold}---------------------------------------------{Colors.reset}\n")
    getpass.getpass(f"Press {Colors.bold}[ENTER]{Colors.reset} to return to main menu... ")   



#### --> Start here <--
init()

## Display menu
while True:
    clear_screen()
    print(f'''{Colors.bold}{Colors.green}
 ____             _              ____            _           _   
/ ___|  ___ _ __ (_) ___  _ __  |  _ \ _ __ ___ (_) ___  ___| |_ 
\___ \ / _ \ '_ \| |/ _ \| '__| | |_) | '__/ _ \| |/ _ \/ __| __|
 ___) |  __/ | | | | (_) | |    |  __/| | | (_) | |  __/ (__| |_ 
|____/ \___|_| |_|_|\___/|_|    |_|   |_|  \___// |\___|\___|\__|
                                              |__/{Colors.reset}\n''')
    # Print menu options
    print(f"{Colors.bold}--- Please choose an option: ---{Colors.reset}")
    
    print(f"1. {Colors.blue}Intro {Colors.reset}")
    print(f"2. {Colors.yellow}Life resume {Colors.reset}")
    print(f"3. {Colors.purple}Pillar one: College/career ready {Colors.reset}")
    print(f"4. {Colors.cyan}Pillar two: Future focused {Colors.reset}")
    print(f"5. {Colors.green}Pillar three: Globally aware{Colors.reset}")
    print(f"6. {Colors.red}Self reflection {Colors.reset}\n")
    
    print(f"0. {Colors.underline}{Colors.bold}Exit program{Colors.reset}\n")
    
    # Get user input
    choice = input("Put your desired number here: ")


    # Process user input
    if choice == "1":
        msg_info("User chose: Intro \n")
        time.sleep(1)
        intro()

    elif choice == "2":
        msg_info("User chose: Life resume \n")
        time.sleep(1)
        life_resume()

    elif choice == "3":
        msg_info("User chose: Pillar one - College and career ready \n")
        time.sleep(1)
        pillar_one()

    elif choice == "4":
        msg_info("User chose: Pillar two - Future focused \n")
        time.sleep(1)
        pillar_two()
        
    elif choice == "5":
        msg_info("User chose: Pillar three - Globally aware \n")
        time.sleep(1)
        pillar_three()
    
    elif choice == "6":
        msg_info("User chose: Self reflection \n")
        time.sleep(1)
        self_reflection()
        
    elif choice == "0" or choice == "q":
        msg_error("User quited...")
        print(f"{Colors.bluebg}Goodbye!{Colors.reset}")
        break
        
    else:
        msg_error("'%s' is invalid, please try again." % choice )
        time.sleep(2)
