# Synthetic Dataset Generation (Paid Polyclinic)

This project is a synthetic dataset generator for analyzing a paid polyclinic system. The application allows generating data regarding patient visits to the polyclinic, including personal information, symptoms, doctor's choice, analysis details, payment details, etc.

## Setup

1. Install Python 3.x from the [official website](https://www.python.org/).
2. Download the source code of the project from the GitHub repository.
3. Open a terminal or command prompt and navigate to the directory with the downloaded project.
4. Run the script by executing the command `python main.py`.

## Usage

1. Before starting, choose the necessary settings by specifying the percentage shares for each property.
2. Enter the number of rows you want to generate in the dataset.
3. Click the "Create Table" button to generate the dataset.

## Specifications

1. Total number of rows in the dataset - minimum 50,000.
2. Full name - the dictionary should consist only of Slavic names.
3. Passport data - only Russian, Belarusian, and Kazakh passports should be included.
4. SNILS (insurance number) - unique, but tied to the patient (full name and passport data), which may be repeated for subsequent visits.
5. Symptoms - the dictionary should consist of a minimum of 5000 symptoms. Thus, there may be a combination of final symptoms (no more than 10).
6. Doctor's choice - the dictionary should consist of a minimum of 50 doctors.
7. Visit date to the doctor - during working hours and days of the week. A subsequent visit can be made to the doctor at least 24 hours after receiving the analysis.
8. Analysis - the dictionary should consist of a minimum of 250 analyses. Thus, there may be a combination of final symptoms (no more than 5).
9. Date of analysis receipt - during working hours and days (within 24-72 hours).
10. Cost of analysis - only in rubles.
11. Payment card - maximum number of repetitions - 5 times.
