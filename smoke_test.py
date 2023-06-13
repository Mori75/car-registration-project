import re
import requests

def extract_registration_numbers(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        # Using regex pattern to extract registration numbers
        pattern = r'[A-HJ-PR-Y]{2}\d{2}\s?[A-HJ-PR-Z]{3}'
        registration_numbers = re.findall(pattern, data)
        return registration_numbers

def fetch_car_value(registration_number):
    url = f"https://www.cazoo.co.uk/value-my-car/?reg={registration_number}"
    response = requests.get(url)
    # Assuming the returned value is in JSON format
    car_value = response.json()
    return car_value

def compare_output(file_path, output):
    with open(file_path, 'r') as file:
        expected_output = file.read().strip()
        return output == expected_output

def run_test_suite():
    input_file = "car_input_v2.txt"
    output_file = "car_output_v2.txt"

    # Step 1: Read input file and extract registration numbers
    registration_numbers = extract_registration_numbers(input_file)

    # Step 2: Process each registration number
    for number in registration_numbers:
        # Step 3: Fetch car value
        car_value = fetch_car_value(number)

        # Step 4: Compare the output
        if compare_output(output_file, car_value):
            print(f"Registration Number: {number} - Test Passed")
        else:
            print(f"Registration Number: {number} - Test Failed")

run_test_suite()
