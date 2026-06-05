# Task 3: Create a Tiny Class with a Useful Method

class Learner:
    """Represents a learner in an intern workflow."""

    def __init__(self, name: str, role: str, skills: list, score: float):
        self.name = name
        self.role = role
        self.skills = skills
        self.score = score

    def get_profile(self) -> str:
        """Returns a formatted profile summary of the learner."""
        skills_str = ", ".join(self.skills)
        status = "Passing" if self.score >= 60 else "Needs Improvement"

        return (
           
            f" LEARNER PROFILE--\n"
         
            f"  Name   : {self.name}\n"
            f"  Role   : {self.role}\n"
            f"  Skills : {skills_str}\n"
            f"  Score  : {self.score} / 100  →  {status}\n"
          
        )

    


# Create objects and call methods
learner1 = Learner("Aarav ",  "Python Intern", ["Python", "Pandas", "Git"], 88.5)
learner2 = Learner("Priya",   "Data Intern",   ["SQL", "NumPy", "Excel"],   72.0)
learner3 = Learner("Rohan ",   "ML Intern",     ["Python", "TensorFlow"],    55.0)

for learner in [learner1, learner2, learner3]:
    print(learner.get_profile())
  