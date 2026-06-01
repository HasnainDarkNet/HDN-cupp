#!/usr/bin/env python3
"""
CUPP Style Wordlist Generator with Progress Bar
Generate custom wordlist based on target information
Author: HasnainDarkNet
"""

import os
import sys
import time
import itertools
import datetime
import threading

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
║                    WORDLIST GENERATOR WITH PROGRESS BAR                      ║
║                         [🐺] HasnainDarkNet [🐺]                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝{RESET}
    """)

class ProgressBar:
    def __init__(self, total, prefix='Progress', suffix='Complete', length=50):
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.current = 0
        self.lock = threading.Lock()
        self.start_time = time.time()
        
    def update(self, current=None):
        with self.lock:
            if current is not None:
                self.current = current
            else:
                self.current += 1
            
            percent = (self.current / self.total) * 100
            filled = int(self.length * self.current // self.total)
            bar = '█' * filled + '░' * (self.length - filled)
            
            elapsed = time.time() - self.start_time
            if self.current > 0:
                eta = (elapsed / self.current) * (self.total - self.current)
                eta_str = f"ETA: {eta:.1f}s"
            else:
                eta_str = "ETA: ?"
            
            sys.stdout.write(f'\r{self.prefix} |{bar}| {percent:.1f}% {self.current}/{self.total} {eta_str}')
            sys.stdout.flush()
            
            if self.current >= self.total:
                print()

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
            parts.extend([f"{yyyy}", f"{yy}"])
    
    return list(set(parts))

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
        'user', 'test', '12345', '123456789', '111111', 'password1',
        'letmein', 'iloveyou', 'princess', 'dragon', 'sunshine', 'master'
    ]
    return common

def leet_convert(word):
    """Convert word to leet speak"""
    leet_map = {
        'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5',
        'b': '8', 'g': '9', 't': '7', 'z': '2', 'l': '1'
    }
    leet_word = ''
    for char in word.lower():
        leet_word += leet_map.get(char, char)
    return leet_word

def generate_wordlist_with_progress(info):
    """Generate complete wordlist with progress bar"""
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
    
    word_list = list(words)
    
    # Progress bar for combinations
    total_combos = len(word_list) * len(word_list) + len(word_list)
    progress = ProgressBar(total_combos, prefix='Generating', suffix='Complete', length=40)
    
    combos = set()
    combo_count = 0
    
    # Single words
    for w in word_list:
        if w:
            combos.add(w)
            combo_count += 1
            progress.update(combo_count)
    
    # Two word combinations
    for w1 in word_list:
        for w2 in word_list:
            if w1 and w2 and w1 != w2:
                combos.add(f"{w1}{w2}")
                combos.add(f"{w1}.{w2}")
                combos.add(f"{w1}_{w2}")
                combos.add(f"{w1}@{w2}")
                combos.add(f"{w1}{w2}{w2}")
                combo_count += 5
                if combo_count % 50 == 0:
                    progress.update(combo_count)
    
    progress.update(total_combos)
    print()
    
    # Progress bar for final list
    all_passwords = list(combos)
    suffixes = ['123', '1234', '12345', '!', '@', '#', '$', '%', '2020', '2021', '2022', '2023', '2024', '2025']
    
    total_final = len(all_passwords) * (1 + len(suffixes))
    final_progress = ProgressBar(total_final, prefix='Processing', suffix='Complete', length=40)
    
    final_list = set()
    final_count = 0
    
    for pwd in all_passwords:
        if pwd and len(pwd) > 2:
            final_list.add(pwd)
            final_count += 1
            final_progress.update(final_count)
            
            for suffix in suffixes:
                final_list.add(f"{pwd}{suffix}")
                final_list.add(f"{pwd}{suffix}{suffix}")
                final_list.add(f"{pwd}{suffix}!")
                final_count += 3
                if final_count % 100 == 0:
                    final_progress.update(final_count)
    
    final_progress.update(total_final)
    print()
    
    # Add leet variants with progress
    print(f"{BLUE}[*] Adding leet speak variants...{RESET}")
    leet_list = list(final_list)
    leet_progress = ProgressBar(len(leet_list), prefix='Leet', suffix='Complete', length=40)
    
    leet_passwords = []
    for i, pwd in enumerate(leet_list):
        leet = leet_convert(pwd)
        if leet != pwd and len(leet) > 3:
            leet_passwords.append(leet)
        leet_progress.update(i + 1)
    
    final_list.update(leet_passwords)
    print()
    
    return sorted(list(final_list))

def save_wordlist_with_progress(passwords, filename):
    """Save wordlist to file with progress bar"""
    print(f"{BLUE}[*] Saving wordlist to file...{RESET}\n")
    
    save_progress = ProgressBar(len(passwords), prefix='Saving', suffix='Complete', length=40)
    
    with open(filename, 'w') as f:
        for i, pwd in enumerate(passwords):
            f.write(pwd + '\n')
            if i % 1000 == 0:
                save_progress.update(i)
    
    save_progress.update(len(passwords))
    print()
    
    print(f"{GREEN}[✓] Wordlist saved to: {filename}{RESET}")
    print(f"{GREEN}[✓] Total passwords: {len(passwords):,}{RESET}")

def main():
    banner()
    
    print(f"{CYAN}════════════════════════════════════════════════════════════{RESET}")
    print(f"{GREEN}              WORDLIST GENERATION{RESET}")
    print(f"{CYAN}════════════════════════════════════════════════════════════{RESET}\n")
    
    # Get information
    info = get_user_info()
    
    # Generate wordlist with progress bar
    start_time = time.time()
    passwords = generate_wordlist_with_progress(info)
    
    # Save wordlist
    filename = f"wordlist_{info['first_name'] or 'target'}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    save_wordlist_with_progress(passwords, filename)
    
    elapsed = time.time() - start_time
    
    # Show sample
    print(f"\n{CYAN}════════════════════════════════════════════════════════════{RESET}")
    print(f"{GREEN}              SAMPLE PASSWORDS (First 20){RESET}")
    print(f"{CYAN}════════════════════════════════════════════════════════════{RESET}")
    
    sample_count = min(20, len(passwords))
    for i in range(sample_count):
        print(f"{WHITE}{passwords[i]}{RESET}")
    
    if len(passwords) > sample_count:
        print(f"{YELLOW}... and {len(passwords) - sample_count:,} more{RESET}")
    
    print(f"\n{CYAN}════════════════════════════════════════════════════════════{RESET}")
    print(f"{GREEN}[✓] Generation complete!{RESET}")
    print(f"{WHITE}⏱️  Time taken: {elapsed:.2f} seconds{RESET}")
    print(f"{WHITE}📊 Total passwords: {len(passwords):,}{RESET}")
    print(f"{WHITE}📁 File: {filename}{RESET}")
    print(f"{CYAN}════════════════════════════════════════════════════════════{RESET}")
    
    print(f"\n{YELLOW}[*] Use with: hydra -L users.txt -P {filename} <target>{RESET}")
    print(f"{YELLOW}[*] Use with: aircrack-ng -w {filename} capture.cap{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Interrupted by user{RESET}")
        sys.exit(0)
