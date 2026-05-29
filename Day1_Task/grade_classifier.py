# List of 5 students to claasify their grades based on their scores
students = [
    {"name": "Ashok",   "score": 92},
    {"name": "Bob",     "score": 81},
    {"name": "Rahul", "score": 74},
    {"name": "Diya",   "score": 65},
    {"name": "Divy",   "score": 48},
]

# Grade classifier
def classify(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Print results
print(f"{'Name':<10} {'Score':>5}  {'Grade':>5}")
print("-" * 25)
for student in students:
    grade = classify(student["score"])
    print(f"{student['name']:<10} {student['score']:>5}  {grade:>5}")