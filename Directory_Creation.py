import os
import random
import pandas as pd
from faker import Faker

# Initialize Faker for generating random data
faker = Faker()

# Constants
BASE_DIR = r"C:\Data Projects\Fake KDrive"

# Function to generate random FOA number
def generate_foa_number():
    return f"FOA {random.randint(1000, 9999)}"

# Function to generate random control number
def generate_control_number(foa_number):
    return f"{foa_number.split()[1]}-{random.randint(1000, 9999)}"

# Function to generate random data for Concept Papers
def generate_concept_paper_data(foa_number, num_records):
    data = []
    for _ in range(num_records):
        control_number = generate_control_number(foa_number)
        tfr = random.randint(10000, 1000000)
        pcs = random.randint(1000, 500000)
        tpc = tfr + pcs
        data.append({
            "Status Name": faker.word(),
            "Control Number": control_number,
            "Topic Name": faker.sentence(),
            "Created Date": faker.date(),
            "Submitted Date": faker.date(),
            "Submitted By": faker.name(),
            "Project Title": faker.sentence(),
            "Abstract": faker.text(),
            "Lead Organization": faker.company(),
            "Other Organizations": faker.company(),
            "Total Funds Requested": tfr,
            "Proposed Cost Share": pcs,
            "Total Projected Costs": tpc,
            "Proposed Perf Period": faker.date(),
            "Location Of Work Primary Location": faker.word(),
            "Location Of Work Organization": faker.company(),
            "Location Of Work Address": faker.address(),
            "Location Of Work City": faker.city(),
            "Location Of Work State": faker.state(),
            "Location Of Work Zip": faker.zipcode(),
            "Location Of Work Percentage": random.randint(1, 100),
            "UEI Number": faker.ein(),
            "Lead Org Type": faker.job(),
            "Key Participants": faker.name(),
            "Admin POC Salutation": faker.prefix(),
            "Admin POC First Name": faker.first_name(),
            "Admin POC Last Name": faker.last_name(),
            "Admin POC Address": faker.address(),
            "Admin POC City": faker.city(),
            "Admin POC State Province Region": faker.state(),
            "Admin POC Zip": faker.zipcode(),
            "Admin POC Country": faker.country(),
            "Admin POC Email": faker.email(),
            "Project Lead PI Salutation": faker.prefix(),
            "Project Lead PI First Name": faker.first_name(),
            "Project Lead PI Last Name": faker.last_name(),
            "Project Lead PI Address": faker.address(),
            "Project Lead PI City": faker.city(),
            "Project Lead PI State Province Region": faker.state(),
            "Project Lead PI Zip": faker.zipcode(),
            "Project Lead PI Country": faker.country(),
            "Project Lead PI Email": faker.email(),
            "Is Minority Owned Business": faker.boolean(),
            "Is Women Owned Business": faker.boolean(),
            "Is HUB Zone Certified Business": faker.boolean(),
        })
    return pd.DataFrame(data)

# Function to generate Applications data
def generate_application_data(foa_number, concept_paper_data, num_records):
    # Extract control numbers from Concept Papers file
    concept_control_numbers = concept_paper_data["Control Number"].tolist()

    # Determine how many CNs to reuse (80-100%)
    reuse_count = max(int(num_records * 0.8), 1)
    reused_data = concept_paper_data.sample(n=reuse_count).copy()

    # Generate additional (random) control numbers (0-20%)
    additional_count = num_records - reuse_count
    additional_data = []
    for _ in range(additional_count):
        control_number = generate_control_number(foa_number)
        tfr = random.randint(10000, 1000000)
        pcs = random.randint(1000, 500000)
        tpc = tfr + pcs
        additional_data.append({
            "Foa Number": foa_number,
            "Status Name": faker.word(),
            "Control Number": control_number,
            "Topic Name": faker.sentence(),
            "Submitted Date": faker.date(),
            "Submitted By": faker.name(),
            "Project Title": faker.sentence(),
            "Abstract": faker.text(),
            "Lead Organization": faker.company(),
            "Other Organizations": faker.company(),
            "Proposed Cost Share": pcs,
            "Total Funds Requested": tfr,
            "Total Projected Costs": tpc,
            "Proposed Perf Period": faker.date(),
            "Lead Organization Locations": faker.address(),
            "Other Organization Locations": faker.address(),
            "Primary Location Of Work Address": faker.address(),
            "UEI Number": faker.ein(),
            "UEI Not Applicable": faker.boolean(),
            "Lead Org Type": faker.job(),
            "Key Participants": faker.name(),
            "Admin POC Salutation": faker.prefix(),
            "Admin POC First Name": faker.first_name(),
            "Admin POC Last Name": faker.last_name(),
            "Admin POC Address": faker.address(),
            "Admin POC City": faker.city(),
            "Admin POC State Province Region": faker.state(),
            "Admin POC Zip": faker.zipcode(),
            "Admin POC Country": faker.country(),
            "Admin POC Phone": faker.phone_number(),
            "Admin POC Email": faker.email(),
            "Project Lead PI Salutation": faker.prefix(),
            "Project Lead PI First Name": faker.first_name(),
            "Project Lead PI Last Name": faker.last_name(),
            "Project Lead PI Address": faker.address(),
            "Project Lead PI City": faker.city(),
            "Project Lead PI State Province Region": faker.state(),
            "Project Lead PI Zip": faker.zipcode(),
            "Project Lead PI Country": faker.country(),
            "Project Lead PI Phone": faker.phone_number(),
            "Project Lead PI Email": faker.email(),
            "Is Minority Owned Business": faker.boolean(),
            "Is Women Owned Business": faker.boolean(),
            "Is HUB Zone Certified Business": faker.boolean(),
        })

    # Combine reused and additional data
    additional_data_df = pd.DataFrame(additional_data)
    application_data = pd.concat([reused_data, additional_data_df], ignore_index=True)

    # Update Foa Number column for reused data
    application_data["Foa Number"] = foa_number

    return application_data

# Main function to generate the folder and files
def generate_folders_and_files(y):
    for _ in range(y):
        foa_number = generate_foa_number()
        master_folder = os.path.join(BASE_DIR, foa_number)
        os.makedirs(master_folder, exist_ok=True)

        # Create Applications and Concept Papers folders
        applications_folder = os.path.join(master_folder, "Applications")
        concept_papers_folder = os.path.join(master_folder, "Concept Papers")
        os.makedirs(applications_folder, exist_ok=True)
        os.makedirs(concept_papers_folder, exist_ok=True)

        # Generate Concept Papers data
        concept_paper_records = random.randint(30, 400)
        concept_paper_data = generate_concept_paper_data(foa_number, concept_paper_records)
        concept_paper_file = os.path.join(concept_papers_folder, f"{foa_number}_CP Data Capture.xlsx")
        with pd.ExcelWriter(concept_paper_file, engine="openpyxl") as writer:
            concept_paper_data.to_excel(writer, index=False, sheet_name="Original")

        # Generate Applications data
        application_records = random.randint(1, concept_paper_records)
        application_data = generate_application_data(foa_number, concept_paper_data, application_records)
        application_file = os.path.join(applications_folder, f"{foa_number}_Full App Data Capture.xlsx")
        with pd.ExcelWriter(application_file, engine="openpyxl") as writer:
            application_data.to_excel(writer, index=False, sheet_name="Original")

# Run the generator
y = int(input("Enter the number of FOA folders to generate: "))
generate_folders_and_files(y)
