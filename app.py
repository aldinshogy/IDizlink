import re

def extract_numbers_from_urls(urls):
    number_pattern = re.compile(r'\d+')
    extracted_numbers = []
    for url in urls:
        numbers = number_pattern.findall(url)
        for number in numbers:
            extracted_numbers.append(number)
    return extracted_numbers

# Prompt the user to enter URLs
print("Enter URLs (one per line). Type 'done' when finished:")
user_input = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    user_input.append(line)

# List of URLs entered by the user
urls = user_input

# Call the function to extract numbers
extracted_numbers = extract_numbers_from_urls(urls)

# Print the extracted numbers
print("Extracted Numbers:",extracted_numbers)
