#!/usr/bin/env python3
# Creator: Host1let
# https://github.com
"""
Aresx is a Hash Creator
"""

import os 
import hashlib
import random

os.system('')

# This Function I Pasted from https://github.com/Zrexer/BrupRocket

hashlist = ['sha1', 'sha256', 'sha224', 'sha512', 'sha384', 'sha3_256', 'sha3_224', 'sha3_512', 'sha3_384']

def createHasher(text : str, type_of_encrypt : str):
        """
        Hash Creator
        ~~~~~~~~~~~~~
        ```
        from BrupRocket import BrupRocket as br
        
        app = br()
        data = app.createHasher(text="Hello world", type_of_encrypt="md5")
        print(data)
        ```
        
        Available Type of hash: 
        
        `md5`
        `sha1`
        `sha256`
        `sha224`
        `sha512`
        `sha384`
        `sha3_256`
        
        or you can select a random type , just use "random" on parameter.
        
        """
        
        t = type_of_encrypt
        
        if t == "md5":
            md5 = hashlib.md5()
            md5.update(text.encode())
            return md5.hexdigest()
        
        elif (
            t == "sha1"
            ):
            sha1 = hashlib.sha1()
            sha1.update(
                text.encode()
                )
            return (
                sha1.hexdigest()
                )
        
        elif (
            t == "sha256"
            ):
            sha256 = hashlib.sha256()
            sha256.update(
                text.encode()
                )
            return (
                sha256.hexdigest()
                )
        
        elif (
            t == "sha224"
            ):
            sha224 = hashlib.sha224()
            sha224.update(
                text.encode()
                )
            return (
                sha224.hexdigest()
                )
        
        elif (
            t == "sha512"
            ):
            sha512 = hashlib.sha512()
            sha512.update(
                text.encode()
                )
            return (
                sha512.hexdigest()
                )
        
        elif (
            t == "sha384"
            ):
            sha384 = hashlib.sha384()
            sha384.update(
                text.encode()
                )
            return (
                sha384.hexdigest()
                )
        
        elif (
            t == "sha3_256"
            ):
            sha3_256 = hashlib.sha3_256()
            sha3_256.update(
                text.encode()
                )
            return (
                sha3_256.hexdigest()
                )
        
        elif (
            t == "sha3_224"
            ):
            sha3_224 = hashlib.sha3_224()
            sha3_224.update(
                text.encode()
                )
            return (
                sha3_224.hexdigest()
                )
        
        elif (
            t == "sha3_512"
            ):
            sha3_512 = hashlib.sha3_512()
            sha3_512.update(
                text.encode()
            )
            return (
                sha3_512.hexdigest()
            )
            
        elif (
            t == "sha3_384"
        ):
            sha3_384 = hashlib.sha3_384()
            sha3_384.update(
                text.encode()
            )
            return (
                sha3_384.hexdigest()
            )
            
        elif (
            t == "random"
        ):
            result = (
                random.choice(hashlist)
            )
            
            return createHasher(text=text, type_of_encrypt=result)

class colors:
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    yellow = '\033[93m'
    magenta = '\033[95m'
    cyan = '\033[96m'
    white = '\033[97m'
    bold = '\033[1m'
    underline = '\033[4m'
    black='\033[30m'
    Backsilver='\033[100m'
    silver='\033[90m'
    Backwhite='\033[3m'
    Backgreen='\033[42m'
    Backyellow='\033[43m'
    BackBlue='\033[44m'
    Backpink='\033[45m'
    Backcyan='\033[46m'
    BackRed='\033[41m'
    green = '\033[32m' 
    red = '\033[31m' 
    blue = '\033[36m' 
    pink = '\033[35m' 
    yellow = '\033[93m' 
    darkblue = '\033[34m' 
    white = '\033[00m'
    bluo = '\033[34m'
    red_p = '\033[41m'
    green_p = '\033[42m'
    bluo_p = '\033[44m'
    pink_p = '\033[45m'
    blue_p = '\033[46m'
    white_p = '\033[47m'
    rd = '\033[91m'
    black='\033[30m'
    bold = '\033[1m'
    underline = '\033[4m'
    magenta = '\033[95m'

class handler:
    a = "{"
    b = "}"
    
    def banner():
        return f"""
{colors.red}
        |     '||''|.   '||''''|   .|'''.|  '||' '|'     {colors.yellow}({colors.white}{colors.BackRed}A{colors.white}{colors.yellow}){colors.red}
       |||     ||   ||   ||  .     ||..  '    || |       {colors.yellow}({colors.white}{colors.BackRed}R{colors.white}{colors.yellow}){colors.red}
      |  ||    ||''|'    ||''|      ''|||.     ||        {colors.yellow}({colors.white}{colors.BackRed}E{colors.white}{colors.yellow}){colors.red}
     .''''|.   ||   |.   ||       .     '||   | ||       {colors.yellow}({colors.white}{colors.BackRed}S{colors.white}{colors.yellow}){colors.red}
    .|.  .||. .||.  '|' .||.....| |'....|'  .|   ||.     {colors.yellow}({colors.white}{colors.BackRed}X{colors.white}{colors.yellow}){colors.red}
                                                 
                                        
                                        
"""+f"                 {colors.white}{handler.a}{colors.yellow}3.2.3#Host1let{colors.white}{handler.b}\n"

    def UsageDictionary(numberCommand : int):
        dictX = {
            'commands': [
                {
                    '1' : 'help',
                    'info' : 'Its Show this message',
                    'usage' : 'help',
                    'switch/argument' : 'help'
                },
                {
                    '1' : 'random hash',
                    'info' : 'create hashes with randomly type',
                    'usage' : 'hash #<text to encrypt> : hash Im_Host1let_from_localPC',
                    'switch/argument' : 'hash #<text to encrypt>'
                },
                {
                    '1' : 'hash with selected type',
                    'info' : 'create hashes with selected type',
                    'usage' : 'hash #<text to encrypt> --type #<type> : hash Im_Host1let_from_localPC sha256',
                    'switch/argument' : 'hash #<text to encrypt> #<type>'
                },
                {
                    '1' : 'random hash and save it in local system',
                    'info' : 'create hashes randomly and save in a file, you can select a name for your file [optical], if you not write a name for that, save it on hashesCreated.txt',
                    'usage' : 'hash #<text to encrypt> -s / --save || hash #<text to encrypt> -s / --save #<file name> ===> hash Im_ali -s hashSaves.txt || hash Im_ali -s',
                    'switch/argument' : 'hash #<text to encrypt> -s / --save || hash #<text to encrypt> -s / --save #<file name>'
                },
                {
                    '1' : 'hash with selected type and save it in local system',
                    'info' : 'create hashes with selected type and save it in a file , like 4 number command',
                    'usage' : 'hash #<text to encrypt> --type #<type> -s / --save ===> hash Im_Host1let_from_localPC sha256 -s hashSaves.txt',
                    'switch/argument' : 'hash #<text to encrypt> #<type> -s / --save #<file name> -> [optical]'
                },
                {
                    '1' : 'available hashes',
                    'info' : 'show available hashes to encrypting',
                    'usage' : 'hash-type / hash-types : and print a list hashes for you',
                    'switch/argument' : 'hash-type / hash-types'
                },
                         ]
        }
        
        return dictX['commands'][numberCommand]

    def activity():
        while 1:
            user = str(input(f'\n{colors.white}{colors.underline}Ares{colors.white} > '))
            if user == "help":
                numbers = [0, 1, 2, 3, 4, 5]
                for nums in numbers:   
                    print(f"""
{colors.blue}[{colors.pink}{colors.BackRed}+{colors.white}{colors.blue}] {colors.white}command info : {colors.yellow}{handler.UsageDictionary(nums).get('1')}
{colors.blue}[{colors.pink}{colors.BackRed}+{colors.white}{colors.blue}] {colors.white}info : {colors.yellow}{handler.UsageDictionary(nums).get('info')}
{colors.blue}[{colors.pink}{colors.BackRed}+{colors.white}{colors.blue}] {colors.white}usage : {colors.yellow}{handler.UsageDictionary(nums).get('usage')}
{colors.blue}[{colors.pink}{colors.BackRed}+{colors.white}{colors.blue}] {colors.white}switch or argument : {colors.yellow}{handler.UsageDictionary(nums).get('switch/argument')}

""")
                
            elif "hash" in user.split():
                
                # Save Without Name 
                if "-s" == user.split()[-1] or "--save" == user.split()[-1]:
                    if "--type" == user.split()[-3]:
                        typeHash = user.split()[-2]
                        text = user.split()[user.index('hash')+1]
                        hashToCreateAndSave = createHasher(text=text, type_of_encrypt=typeHash)
                        print(f'{colors.blue}[{colors.pink}{colors.BackRed}+{colors.white}{colors.blue}] {colors.yellow}{hashToCreateAndSave}')
                        with open('hashesCreated.txt', 'a') as fhtcas:
                            fhtcas.write(f'\n{hashToCreateAndSave}')
                            fhtcas.close()
                    else:
                        text = user.split()[user.index('hash')+1]
                        hashToCreateRandomAndSave = createHasher(text=text, type_of_encrypt='random')
                        print(f'{colors.blue}[{colors.pink}{colors.BackRed}+{colors.white}{colors.blue}] {colors.yellow}{hashToCreateRandomAndSave}')
                        with open('hashesCreated.txt', 'a') as fhtcas:
                            fhtcas.write(f'\n{hashToCreateRandomAndSave}')
                            fhtcas.close()
                
                # Save With Name     
                elif "-s" == user.split()[-2] or "--save" == user.split()[-2]:
                    if "--type" == user.split()[-4]:
                        fileName = user.split()[-1]
                        typeHash = user.split()[-3]
                        text = user.split()[user.index('hash')+1]
                        hashToCreateAndSave2 = createHasher(text=text, type_of_encrypt=typeHash)
                        print(f'{colors.blue}[{colors.pink}{colors.BackRed}+{colors.white}{colors.blue}] {colors.yellow}{hashToCreateAndSave2}')
                        with open(fileName, 'a') as fhtcas:
                            fhtcas.write(f'\n{hashToCreateAndSave2}')
                            fhtcas.close()
                            
                    else:
                        fileName = user.split()[-1]
                        text = user.split()[user.index('hash')+1]
                        hashToCreateInName = createHasher(text=text, type_of_encrypt='random')
                        print(f'{colors.blue}[{colors.pink}{colors.BackRed}+{colors.white}{colors.blue}] {colors.yellow}{hashToCreateInName}')
                        with open(fileName, 'a') as frasd: 
                            frasd.write(f'\n{hashToCreateInName}')
                            frasd.close()
                            
            elif "hash-type" in user.split() or "hash-types" in user.split():
                print(f'{colors.blue}[{colors.pink}{colors.BackRed}+{colors.white}{colors.blue}] {colors.yellow}{hashlist}')
                
            elif user == "exit":
                print(f'{colors.blue}[{colors.pink}{colors.Backsilver}<_>{colors.white}{colors.blue}]{colors.yellow} Thanks to use{colors.white}')
                exit()
        
print(handler.banner())
handler.activity()