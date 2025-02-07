from faker import Faker
from termcolor import colored
import time 
from tqdm import tqdm

fake = Faker()

for i in tqdm(range(10)):
    time.sleep(0.1)

print(colored("Fake Information Generator\n", "red"))

# Personal Information
print(colored("Personal Information:", "cyan"))
print(colored("Name: ", "yellow") + colored(fake.name(), "green"))  # Fake name
print(colored("Date of Birth: ", "yellow") + colored(fake.date_of_birth(), "green"))  # Fake date of birth
print(colored("SSN: ", "yellow") + colored(fake.ssn(), "green"))  # Fake social security number

# Contact Information
print(colored("\nContact Information:", "cyan"))
print(colored("Address: ", "yellow") + colored(fake.address(), "green"))  # Fake address
print(colored("Email: ", "yellow") + colored(fake.email(), "green"))  # Fake email
print(colored("Phone Number: ", "yellow") + colored(fake.phone_number(), "green"))  # Fake phone number

# Professional Information
print(colored("\nProfessional Information:", "cyan"))
print(colored("Job: ", "yellow") + colored(fake.job(), "green"))  # Fake job title
print(colored("Company: ", "yellow") + colored(fake.company(), "green"))  # Fake company name

# Internet Information
print(colored("\nInternet Information:", "cyan"))
print(colored("URL: ", "yellow") + colored(fake.url(), "green"))  # Fake URL
print(colored("IPv4: ", "yellow") + colored(fake.ipv4(), "green"))  # Fake IPv4 address
print(colored("IPv6: ", "yellow") + colored(fake.ipv6(), "green"))  # Fake IPv6 address
print(colored("User Agent: ", "yellow") + colored(fake.user_agent(), "green"))
print(colored("Password: ", "yellow") + colored(fake.password(), "green"))

# Financial Information
print(colored("\nFinancial Information:", "cyan"))
print(colored("Credit Card Number: ", "yellow") + colored(fake.credit_card_number(), "green"))
print(colored("Currency Code: ", "yellow") + colored(fake.currency_code(), "green"))
print(colored("Currency Name: ", "yellow") + colored(fake.currency_name(), "green"))
print(colored("Currency Symbol: ", "yellow") + colored(fake.currency_symbol(), "green"))

# Location Information
print(colored("\nLocation Information:", "cyan"))
print(colored("Country: ", "yellow") + colored(fake.country(), "green"))
print(colored("City: ", "yellow") + colored(fake.city(), "green"))
print(colored("Street Name: ", "yellow") + colored(fake.street_name(), "green"))
print(colored("Street Address: ", "yellow") + colored(fake.street_address(), "green"))
print(colored("Building Number: ", "yellow") + colored(fake.building_number(), "green"))
print(colored("Postcode: ", "yellow") + colored(fake.postcode(), "green"))
print(colored("Latitude: ", "yellow") + colored(fake.latitude(), "green"))
print(colored("Longitude: ", "yellow") + colored(fake.longitude(), "green"))
print(colored("Coordinate: ", "yellow") + colored(fake.coordinate(), "green"))
print(colored("Timezone: ", "yellow") + colored(fake.timezone(), "green"))

# File Information
print(colored("\nFile Information:", "cyan"))
print(colored("File Extension: ", "yellow") + colored(fake.file_extension(), "green"))
print(colored("File Name: ", "yellow") + colored(fake.file_name(), "green"))
print(colored("File Path: ", "yellow") + colored(fake.file_path(), "green"))
print(colored("MIME Type: ", "yellow") + colored(fake.mime_type(), "green"))

# Miscellaneous
print(colored("\nMiscellaneous:", "cyan"))
print(colored("Color Name: ", "yellow") + colored(fake.color_name(), "green"))
print(colored("Language Code: ", "yellow") + colored(fake.language_code(), "green"))
print(colored("Language Name: ", "yellow") + colored(fake.language_name(), "green"))
print(colored("Country Code: ", "yellow") + colored(fake.country_code(), "green"))
print(colored("Word: ", "yellow") + colored(fake.word(), "green"))
print(colored("Sentence: ", "yellow") + colored(fake.sentence(), "green"))
print(colored("Paragraph: ", "yellow") + colored(fake.paragraph(), "green"))
print(colored("Text: ", "yellow") + colored(fake.text(), "green"))