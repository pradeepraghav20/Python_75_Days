# Write a Python program to insert space before every capital letter appears in a given word.
# Sample Data:
# ("PythonExercises") -> "Python Exercises"
# ("Python") -> "Python"
# # ("PythonExercisesPracticeSolution") -> "Python Exercises Practice Solution"

s='PythonExercises'
new_s=""
for i in s:
    if i.isupper():
        new_s+=" "+i
    else:
        new_s+=i
print(new_s)

