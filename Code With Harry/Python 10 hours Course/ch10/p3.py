class student:
    school = 'RKMVP'

armin = student()
print(armin.school) # Prints the class attribute because instance attribute is not present
armin.school = "AOT" # Instance attribute is set
print(armin.school) # Instance attribute, takes preference over class attribute during assignment & retrieval

# Correct answer will be:
# No, object attribute has changed, but class attribute has not changed.
print(student.school) # Prints the class attribute, which is unchanged