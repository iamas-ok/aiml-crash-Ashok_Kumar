# prints skills with numbering and total count.

skills = ["Python", "SQL", "Machine Learning", "Communication", "Problem Solving"]

for index, skill in enumerate(skills, start=1):
    print(f"{index}. {skill}")

print(f"\nTotal Skills: {len(skills)}")