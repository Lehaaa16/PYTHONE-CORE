class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


t = False
if t:
    print(f"{Colors.HEADER}Це HEADER текст{Colors.RESET}")
    print(f"{Colors.BLUE}Це BLUE текст{Colors.RESET}")
    print(f"{Colors.CYAN}Це CYAN текст{Colors.RESET}")
    print(f"{Colors.GREEN}Це GREEN текст{Colors.RESET}")
    print(f"{Colors.YELLOW}Це YELLOW текст{Colors.RESET}")
    print(f"{Colors.RED}Це RED текст{Colors.RESET}")
    print(f"{Colors.BOLD}Це BOLD (жирний) текст{Colors.RESET}")
    print(f"{Colors.UNDERLINE}Це UNDERLINE (підкреслений) текст{Colors.RESET}")
