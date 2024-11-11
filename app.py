import re
import streamlit as st

def extract_numbers_from_urls(urls):
    number_pattern = re.compile(r'\d+')
    extracted_numbers = []
    for url in urls:
        numbers = number_pattern.findall(url)
        for number in numbers:
            extracted_numbers.append(number)
    return extracted_numbers

# Streamlit app
st.title("URL Numbers Extractor")

# Prompt the user to enter URLs
urls = st.text_area("Enter URLs (one per line):")

# Check if the user has provided any input
if urls:
    urls_list = urls.strip().split('\n')
    
    # Call the function to extract numbers
    extracted_numbers = extract_numbers_from_urls(urls_list)
    
    # Join the extracted numbers into a comma-separated string without spaces
    extracted_numbers_str = ','.join(extracted_numbers)
    
    # Print the extracted numbers
    st.write("Extracted Numbers:", extracted_numbers_str)
