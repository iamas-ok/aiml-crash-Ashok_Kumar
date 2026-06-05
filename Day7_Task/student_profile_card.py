# Task 1: Student Profile Card using F-Strings and Type Hints

# Learner profile stored in variables and a dictionary 
learner: dict = {
    "name": "Ashok Kumar",
    "age": 21,
    "role": "Python Intern",
    "skills": ["Python", "Git", "Pandas", "NumPy"],
    "progress": 78.5,  
}


def build_profile_card(profile: dict) -> str:
    """Return a formatted 4-line profile card for a learner."""
    skills_str: str = ", ".join(profile["skills"])

    line1: str = f" Name     : {profile['name']} (Age: {profile['age']})"
    line2: str = f" Role     : {profile['role']}"
    line3: str = f"  Skills   : {skills_str}"
    line4: str = f" Progress : {profile['progress']}% completed"

    card: str = (
        f"\n{'=' * 45}\n"
        f"        LEARNER PROFILE CARD\n"
        f"{'=' * 45}\n"
        f"{line1}\n"
        f"{line2}\n"
        f"{line3}\n"
        f"{line4}\n"
        f"{'=' * 45}"
    )
    return card


# Main execution to build and print the profile card
if __name__ == "__main__":
    card = build_profile_card(learner)
    print(card)