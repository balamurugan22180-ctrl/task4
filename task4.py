facts = {
    "HighCGPA",
    "GoodAttendance",
    "CompletedProjects",
    "CompletedInternship",
    "ScoredWellInAptitude",
}

rules = [
    ("R1", ["HighCGPA", "GoodAttendance"], "GoodAcademicPerformance"),
    ("R2", ["CompletedProjects", "CompletedInternship"], "PracticalExperience"),
    ("R3", ["ScoredWellInAptitude"], "AptitudeReady"),
    ("R4", ["GoodAcademicPerformance", "PracticalExperience", "AptitudeReady"], "EligibleForPlacement"),
    ("R5", ["LowAptitudeScore"], "NeedsExtraPractice"),
]


def prove(goal, depth=0):
    indent = "  " * depth
    print(f"{indent}Goal: {goal}")

    if goal in facts:
        print(f"{indent}-> '{goal}' is a known fact")
        return True

    for name, conditions, conclusion in rules:
        if conclusion == goal:
            print(f"{indent}-> Trying {name}: IF {' AND '.join(conditions)} THEN {conclusion}")
            if all(prove(condition, depth + 1) for condition in conditions):
                print(f"{indent}-> {name} succeeded, '{goal}' is proved")
                return True
            print(f"{indent}-> {name} failed")

    print(f"{indent}-> '{goal}' cannot be proved")
    return False


goal = "EligibleForPlacement"

print("Facts:", ", ".join(sorted(facts)))
print("Goal to prove:", goal)
print("-" * 70)

result = prove(goal)

print("-" * 70)
if result:
    print(f"Conclusion: {goal} is TRUE for this student")
else:
    print(f"Conclusion: {goal} cannot be proved for this student")