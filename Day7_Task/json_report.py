# Task 2: Extract a Small Report from a JSON File

import json

# Load the JSON file
with open(r"C:\Users\Ashok kumar\Desktop\Tasks\aiml-crash-Ashok_Kumar\Day7_Task\learner_data.json", "r") as file:
    data = json.load(file)

#List comprehension: uppercase all skill names
skills_upper = [skill.upper() for skill in data["skills"]]

# List comprehension: filter projects with more than one word
detailed_projects = [p for p in data["projects"] if len(p.split()) > 1]

# Print the report using f-strings
print(f"\n{'=' * 42}")
print(f"        LEARNER REPORT SUMMARY")
print(f"{'=' * 42}")
print(f"  Name        : {data['name']}")
print(f"  Age         : {data['age']}")
print(f"  Role        : {data['role']}")
print(f"  Department  : {data['department']}")
print(f"  Status      : {data['status']}")
print(f"  Score       : {data['score']} / 100")
print(f"  Skills      : {', '.join(skills_upper)}")
print(f"  Projects    : {', '.join(detailed_projects)}")
print(f"{'=' * 42}\n")