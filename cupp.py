#!/usr/bin/env python3
"""
CUPP Style Wordlist Generator - Common User Passwords Profiler
Generate custom wordlist based on target information
Author: HasnainDarkNet
"""

import os
import sys
import itertools
import datetime

# ============ COLORS ============
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
WHITE = '\033[97m'
PURPLE = '\033[95m'
RESET = '\033[0m'

def banner():
    print(f"""{CYAN}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║      ██████╗██╗   ██╗██████╗ ██████╗                                         ║
║     ██╔════╝██║   ██║██╔══██╗██╔══██╗                                        ║
║     ██║     ██║   ██║██████╔╝██████╔╝                                        ║
║     ██║     ██║   ██║██╔═══╝ ██╔═══╝                                         ║
║     ╚██████╗╚██████╔╝██║     ██║                                             ║
║      ╚═════╝ ╚═════╝ ╚═╝     ╚═╝                                             ║
║                                                                              ║
║                    WORDLIST GENERATOR (CUPP STYLE)                           ║
║                    Generate Custom Password Lists                            ║
║                         [🐺] HasnainDarkNet [🐺]                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝{RESET}
    """)

def get_user_info():
    """Get target information"""
    print(f"\n{CYAN}════════════════════════════════════════════════════════════{RESET}")
    print(f"{GREEN}              ENTER TARGET INFORMATION{RESET}")
    print(f"{CYAN}════════════════════════════════════════════════════════════{RESET}\n")
    
    info = {}
    
    info['first_name'] = input(f"{YELLOW}[?] First Name: {RESET}").strip().lower()
    info['last_name'] = input(f"{YELLOW}[?] Last Name: {RESET}").strip().lower()
    info['nickname'] = input(f"{YELLOW}[?] Nickname (optional): {RESET}").strip().lower()
    info['birth_date'] = input(f"{YELLOW}[?] Birth Date (DDMMYYYY or DD-MM-YYYY): {RESET}").strip()
    info['pet_name'] = input(f"{YELLOW}[?] Pet Name (optional): {RESET}").strip().lower()
    info['partner_name'] = input(f"{YELLOW}[?] Partner Name (optional): {RESET}").strip().lower()
    info['child_name'] = input(f"{YELLOW}[?] Child Name (optional): {RESET}").strip().lower()
    info['company'] = input(f"{YELLOW}[?] Company/School (optional): {RESET}").strip().lower()
    info['hobby'] = input(f"{YELLOW}[?] Hobby (optional): {RESET}").strip().lower()
    info['favorite_number'] = input(f"{YELLOW}[?] Favorite Number (optional): {RESET}").strip()
    
    return info

def extract_date_parts(date_str):
    """Extract different date formats"""
    parts = []
    if date_str:
        # Remove separators
        clean = date_str.replace('-', '').replace('/', '').replace(' ', '')
        
        if len(clean) == 8:
            dd = clean[0:2]
            mm = clean[2:4]
            yyyy = clean[4:8]
            yy = yyyy[2:4]
            
            parts.extend([dd, mm, yyyy, yy])
            parts.extend([f"{dd}{mm}", f"{mm}{dd}"])
            parts.extend([f"{dd}{mm}{yyyy}", f"{yyyy}{mm}{dd}"])
            parts.extend([f"{dd}{mm}{yy}", f"{yy}{mm}{dd}"])
    
    return list(set(parts))

def generate_combinations(words, max_len=20):
    """Generate combinations of words"""
    combos = set()
    
    # Single words
    for w in words:
        if w:
            combos.add(w)
    
    # Two word combinations
    for w1 in words:
        for w2 in words:
            if w1 and w2 and w1 != w2:
                combos.add(f"{w1}{w2}")
                combos.add(f"{w1}.{w2}")
                combos.add(f"{w1}_{w2}")
                combos.add(f"{w1}@{w2}")
    
    return [c for c in combos if len(c) <= max_len]

def generate_years():
    """Generate years from 1950 to current"""
    current_year = datetime.datetime.now().year
    years = []
    for year in range(1950, current_year + 1):
        years.append(str(year))
        years.append(str(year)[2:4])
    return years

def generate_common_passwords():
    """Generate common password patterns"""
    common = [
        'password', '123456', '12345678', '1234', 'qwerty', 'abc123',
        'admin', 'welcome', 'login', 'password123', 'admin123', 'root',
        'user', 'test', '12345', '123456789', '111111', 'password1'
    ]
    return common

def generate_wordlist(info):
    """Generate complete wordlist"""
    print(f"\n{BLUE}[*] Generating wordlist...{RESET}\n")
    
    words = set()
    
    # Basic info
    if info['first_name']:
        words.add(info['first_name'])
        words.add(info['first_name'].capitalize())
        words.add(info['first_name'].upper())
    
    if info['last_name']:
        words.add(info['last_name'])
        words.add(info['last_name'].capitalize())
        words.add(info['last_name'].upper())
    
    if info['nickname']:
        words.add(info['nickname'])
        words.add(info['nickname'].capitalize())
    
    if info['pet_name']:
        words.add(info['pet_name'])
        words.add(info['pet_name'].capitalize())
    
    if info['partner_name']:
        words.add(info['partner_name'])
        words.add(info['partner_name'].capitalize())
    
    if info['child_name']:
        words.add(info['child_name'])
        words.add(info['child_name'].capitalize())
    
    if info['company']:
        words.add(info['company'])
        words.add(info['company'].capitalize())
    
    if info['hobby']:
        words.add(info['hobby'])
        words.add(info['hobby'].capitalize())
    
    # Date combinations
    date_parts = extract_date_parts(info['birth_date'])
    for part in date_parts:
        words.add(part)
    
    # Favorite number
    if info['favorite_number']:
        words.add(info['favorite_number'])
    
    # Years
    for year in generate_years():
        words.add(year)
    
    # Common passwords
    for common in generate_common_passwords():
        words.add(common)
    
    # Generate combinations
    word_list = list(words)
    combos = generate_combinations(word_list)
    
    all_passwords = list(words) + combos
    
    # Add with common suffixes
    suffixes = ['123', '1234', '12345', '!', '@', '#', '$', '2020', '2021', '2022', '2023', '2024', '2025']
    
    final_list = set()
    for pwd in all_passwords:
        if pwd and len(pwd) > 2:
            final_list.add(pwd)
            for suffix in suffixes:
                final_list.add(f"{pwd}{suffix}")
                final_list.add(f"{pwd}{suffix}{suffix}")
    
    return sorted(list(final_list))

def save_wordlist(passwords, filename):
    """Save wordlist to file"""
    with open(filename, 'w') as f:
        for pwd in passwords:
            f.write(pwd + '\n')
    print(f"{GREEN}[✓] Wordlist saved to: {filename}{RESET}")
    print(f"{GREEN}[✓] Total passwords: {len(passwords)}{RESET}")

def interactive_mode():
    """Interactive mode - ask questions"""
    print(f"{CYAN}\n[?] Do you want to enter information interactively? (y/n): {RESET}", end='')
    choice = input().strip().lower()
    
    if choice == 'y':
        return get_user_info()
    else:
        # Quick mode
        print(f"\n{CYAN}════════════════════════════════════════════════════════════{RESET}")
        print(f"{GREEN}              QUICK MODE{RESET}")
        print(f"{CYAN}════════════════════════════════════════════════════════════{RESET}\n")
        
        info = {}
        info['first_name'] = input(f"{YELLOW}[?] First Name: {RESET}").strip().lower()
        info['last_name'] = input(f"{YELLOW}[?] Last Name: {RESET}").strip().lower()
        info['nickname'] = input(f"{YELLOW}[?] Nickname: {RESET}").strip().lower()
        info['birth_date'] = input(f"{YELLOW}[?] Birth Date (DDMMYYYY): {RESET}").strip()
        info['pet_name'] = input(f"{YELLOW}[?] Pet Name: {RESET}").strip().lower()
        info['partner_name'] = input(f"{YELLOW}[?] Partner Name: {RESET}").strip().lower()
        info['child_name'] = input(f"{YELLOW}[?] Child Name: {RESET}").strip().lower()
        info['company'] = input(f"{YELLOW}[?] Company: {RESET}").strip().lower()
        info['hobby'] = input(f"{YELLOW}[?] Hobby: {RESET}").strip().lower()
        info['favorite_number'] = input(f"{YELLOW}[?] Favorite Number: {RESET}").strip()
        
        return info

def leet_convert(word):
    """Convert word to leet speak"""
    leet_map = {
        'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5',
        'b': '8', 'g': '9', 't': '7', 'z': '2'
    }
    leet_word = ''
    for char in word.lower():
        leet_word += leet_map.get(char, char)
    return leet_word

def add_leet_variants(passwords):
    """Add leet speak variants"""
    new_passwords = []
    for pwd in passwords:
        leet = leet_convert(pwd)
        if leet != pwd:
            new_passwords.append(leet)
    return new_passwords

def main():
    banner()
    
    print(f"{CYAN}════════════════════════════════════════════════════════════{RESET}")
    print(f"{GREEN}              WORDLIST GENERATION{RESET}")
    print(f"{CYAN}════════════════════════════════════════════════════════════{RESET}")
    
    # Get information
    info = interactive_mode()
    
    # Generate wordlist
    passwords = generate_wordlist(info)
    
    # Add leet variants
    leet_passwords = add_leet_variants(passwords)
    passwords.extend(leet_passwords)
    
    # Remove duplicates and sort
    passwords = sorted(list(set(passwords)))
    
    # Save wordlist
    filename = f"wordlist_{info['first_name'] or 'target'}.txt"
    save_wordlist(passwords, filename)
    
    # Show sample
    print(f"\n{CYAN}════════════════════════════════════════════════════════════{RESET}")
    print(f"{GREEN}              SAMPLE PASSWORDS{RESET}")
    print(f"{CYAN}════════════════════════════════════════════════════════════{RESET}")
    sample_count = min(20, len(passwords))
    for i in range(sample_count):
        print(f"{WHITE}{passwords[i]}{RESET}")
    
    if len(passwords) > sample_count:
        print(f"{YELLOW}... and {len(passwords) - sample_count} more{RESET}")
    
    print(f"\n{GREEN}[✓] Wordlist generation complete!{RESET}")
    print(f"{YELLOW}[*] Use with: hydra -L users.txt -P {filename} <target>{RESET}")

if __name__ == "__main__":
    main()
