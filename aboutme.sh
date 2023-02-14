#!/usr/bin/env bash

#* Script to do everything

# shellcheck disable=2145,2034,2317

# --- Initalization function ---
function init() {

    # - Set colors -
    # Normal text
    reset='\e[0m'
    # Bold text
    bold='\e[1m'
    # Red
    red='\e[31m'
    redbg='\e[41m'
    # Green
    green='\e[32m'
    greenbg='\e[42m'
    # Yellow
    yellow='\e[33m'
    yellowbg='\e[43m'
    # Blue
    blue='\e[34m'
    bluebg='\e[44m'
    # Purple
    purple='\e[35m'
    purplebg='\e[45m'
    # Cyan
    cyan='\e[36m'
    cyanbg='\e[46m'

    # - Set 'info', 'error', 'note', 'success' message functions -
    msg_info() {
        echo -e "${yellow}${bold}[INFO]${reset} $@ ${reset}"
    }

    msg_question() {
        echo -e "${red}${bold}[QUESTION]${reset} >> $@ ${reset}"
    }

    msg_success() {
        echo -e "${green}${bold}[SUCCESS]${reset} $@ ${reset}"
    }

    msg_answer() {
        echo -e "${blue}${bold}[ANSWER]${reset} >> $@ ${reset}"
    }
    
    echo ""
}

intro() {
    msg_info "This is my very creative Senior project."
    msg_info "I don't know how to fill up the rest of this space."
    msg_info "So I'll just do this."
    msg_info "A bit awkward but at least it's something."
    msg_success "--- Finished intro. ---"
    echo ""

}

college_career() {
    msg_question "What challenges do you think you will face in the next phase of life?" 
    msg_question "Are you prepared for those challenges? \n"
    
    msg_answer "Most of my challenges will probably be getting a job and living independantly."
    msg_answer "I have mental disorders/disabilities, so being independant will be a challenge for me,"
    msg_answer "as I have difficulty remembering to do tasks."
    echo ""
}





case $1 in
    intro) init; intro ;;
    college-career-ready) init; college_career ;;
esac