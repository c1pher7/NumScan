import phonenumbers
from phonenumbers import geocoder, carrier, timezone                                                                                         from phonenumbers import *
import os
import time
from colorama import *

time.sleep(0.10)
os.system("clear")
init(autoreset=True)

creator = (Style.DIM + Fore.WHITE + "https://github.com/c1pher7")
ascii_art = f"""
  _   _                  _____
 | \ | |                / ____|
 |  \| |_   _ _ __ ___ | (___   ___ __ _ _ __
 | . ` | | | | '_ ` _ \ \___ \ / __/ _` | '_ \
 | |\  | |_| | | | | | |____) | (__ (_| | | | |
 |_| \_|\__,_|_| |_| |_|_____/ \___\__,_|_| |_|
           {creator}
"""
colorascii = (Fore.BLUE + Style.BRIGHT + ascii_art)

print(colorascii)
run = input("Enter the target number: ")

time.sleep(0.15)

print()

num = phonenumbers.parse(run)

numformat = format_number(num, PhoneNumberFormat.NATIONAL)
intformat = format_number(num, PhoneNumberFormat.INTERNATIONAL)
country = region_code_for_number(num)
region = geocoder.description_for_number(num, "en")
carrier = carrier.name_for_number(num, "en")
valid = is_valid_number(num)
time = timezone.time_zones_for_number(num)

reset = (Style.RESET_ALL)
simbol = (Style.BRIGHT + Fore.RED + f"+{reset}]")
print(f" [{simbol} International format number   : {intformat}")
print(f" [{simbol} Number in national format     : {numformat}")
print(f" [{simbol} Country of number (code)      : {country}")
print(f" [{simbol} Region of the number          : {region}")
print(f" [{simbol} Number carrier                : {carrier}")
if valid == True:
    corvalid1 = (Style.BRIGHT + Fore.GREEN + f"{valid}")
    print(f" [{simbol} Is number valid?              : {corvalid1}")
else:
    corvalid2 = (Fore.RED + f"{valid}")
    print(f" [{simbol} Is number valid?              : {corvalid2}")
print(f" [{simbol} Timezone                      : {time}")

print()
q = input(Style.DIM + Fore.WHITE + "press enter to exit ")
