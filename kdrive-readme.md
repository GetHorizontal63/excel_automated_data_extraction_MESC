# Fake KDrive Generator

## Overview
This system generates a mock directory structure with realistic sample data that mimics a funding opportunity announcement (FOA) system. It creates a structured set of folders containing applications and concept papers with randomized but realistic data.

## Features
- Generates multiple FOA folders with randomized FOA numbers
- Creates hierarchical directory structure for each FOA
- Generates realistic sample data for both concept papers and applications
- Maintains data relationships between concept papers and applications
- Produces Excel files with comprehensive mock data
- Includes cleanup utility for easy system reset

## Directory Structure
The system creates the following structure:
```
C:\Data Projects\Fake KDrive\
└── FOA XXXX\
    ├── Applications\
    │   └── FOA XXXX_Full App Data Capture.xlsx
    └── Concept Papers\
        └── FOA XXXX_CP Data Capture.xlsx
```

## Components

### 1. Directory_Creation.py
Main data generation script that:
- Creates the directory structure
- Generates randomized FOA numbers
- Produces mock data for concept papers and applications
- Creates Excel files with realistic sample data
- Maintains data relationships between concept papers and applications

Features:
- Random FOA number generation
- Realistic data generation using Faker library
- Configurable number of records
- Maintained relationship between concept papers and applications (80-100% correlation)

### 2. Directory_Removal.py
Cleanup utility that:
- Safely removes the entire fake KDrive structure
- Includes confirmation prompt
- Handles errors gracefully

## Generated Data Fields

### Concept Papers
- Control Number
- Topic Name
- Created/Submitted Dates
- Project Details (Title, Abstract)
- Organization Information
- Financial Data (Funds Requested, Cost Share)
- Location Information
- Contact Information (Admin POC, Project Lead)
- Business Classification Data

### Applications
- FOA Number
- Control Number (linked to Concept Papers)
- Project Information
- Organization Details
- Financial Information
- Location Data
- Contact Information
- Business Classification Data

## System Requirements
- Python 3.x
- Required Python packages:
  - pandas
  - faker
  - openpyxl

## Installation

1. Install required Python packages:
```bash
pip install pandas faker openpyxl
```

2. Ensure you have write permissions for the `C:\Data Projects` directory

## Usage

### Generating Data
1. Run the creation script:
```bash
python Directory_Creation.py
```
2. Enter the number of FOA folders you want to generate when prompted
3. Wait for the system to complete the generation process

### Cleaning Up
To remove all generated data:
```bash
python Directory_Removal.py
```

## Data Relationships
- Each FOA contains both Applications and Concept Papers folders
- 80-100% of applications are linked to existing concept papers
- 0-20% of applications are new entries
- Financial calculations maintain realistic relationships:
  - Total Projected Costs = Total Funds Requested + Proposed Cost Share

## Notes
- The system uses the Faker library to generate realistic mock data
- All generated data is fictional and should not be used for real applications
- Financial data is generated within realistic ranges
- The system maintains data consistency across related files

## Best Practices
- Generate a reasonable number of FOAs to avoid system memory issues
- Verify generated data for testing scenarios
- Use the cleanup utility before regenerating data
- Back up any important data before running the cleanup utility

## Error Handling
- Directory existence checks
- User confirmation for destructive operations
- Exception handling for file operations
- Graceful cleanup process
