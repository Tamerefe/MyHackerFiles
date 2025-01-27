from faker import Faker
from termcolor import colored

fake = Faker()

print(colored("Fake Information Generator\n", "red"))

# Personal Information
print(colored("Personal Information:", "cyan"))
print(colored(fake.name(), "green"))
print(colored(fake.date_of_birth(), "green"))
print(colored(fake.ssn(), "green"))

# Contact Information
print(colored("\nContact Information:", "cyan"))
print(colored(fake.address(), "green"))
print(colored(fake.email(), "green"))
print(colored(fake.phone_number(), "green"))

# Professional Information
print(colored("\nProfessional Information:", "cyan"))
print(colored(fake.job(), "green"))
print(colored(fake.company(), "green"))

# Internet Information
print(colored("\nInternet Information:", "cyan"))
print(colored(fake.url(), "green"))
print(colored(fake.ipv4(), "green"))
print(colored(fake.ipv6(), "green"))
print(colored(fake.user_agent(), "green"))
print(colored(fake.password(), "green"))

# Financial Information
print(colored("\nFinancial Information:", "cyan"))
print(colored(fake.credit_card_number(), "green"))
print(colored(fake.currency_code(), "green"))
print(colored(fake.currency_name(), "green"))
print(colored(fake.currency_symbol(), "green"))

# Location Information
print(colored("\nLocation Information:", "cyan"))
print(colored(fake.country(), "green"))
print(colored(fake.city(), "green"))
print(colored(fake.street_name(), "green"))
print(colored(fake.street_address(), "green"))
print(colored(fake.building_number(), "green"))
print(colored(fake.postcode(), "green"))
print(colored(fake.latitude(), "green"))
print(colored(fake.longitude(), "green"))
print(colored(fake.coordinate(), "green"))
print(colored(fake.timezone(), "green"))

# File Information
print(colored("\nFile Information:", "cyan"))
print(colored(fake.file_extension(), "green"))
print(colored(fake.file_name(), "green"))
print(colored(fake.file_path(), "green"))
print(colored(fake.mime_type(), "green"))

# Miscellaneous
print(colored("\nMiscellaneous:", "cyan"))
print(colored(fake.color_name(), "green"))
print(colored(fake.language_code(), "green"))
print(colored(fake.language_name(), "green"))
print(colored(fake.country_code(), "green"))
print(colored(fake.word(), "green"))
print(colored(fake.sentence(), "green"))
print(colored(fake.paragraph(), "green"))
print(colored(fake.text(), "green"))