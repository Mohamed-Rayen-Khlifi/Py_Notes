import csv
import random

# Define the class options
classes = ['IDL', 'IDISC', 'ISEOC'] 

# Generate the CSV data
data = []
for _ in range(25000):
    name = f"Student_{_ + 1}"
    class_name = random.choice(classes)
    # Math
    math_1 = random.randint(0, 20)
    math_2 = random.randint(0, 20)
    math = round((math_1 + math_2) / 2, 2) 
    
    # Physics
    physics_1 = random.randint(0, 20)
    physics_2 = random.randint(0, 20)
    physics = round((physics_1 + physics_2) / 2, 2)

    # Science
    science_1= random.randint(0, 20)
    science_2 = random.randint(0, 20)
    science = round((science_1 + science_2) / 2, 2)
    
    #Final score
    score = round((math + physics + science) / 3, 2)

        
    entry = [name, class_name, 
            math_1, math_2,
            physics_1, physics_2, 
            science_1, science_2,
            math, physics, science, 
            score]
    data.append(entry)

# Write the data to a CSV file
filename = 'student_scores.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Student', 'Class', 
        'Math_1', 'Math_2', 
        'Physics_1', 'Physics_2', 
        'Science_1', 'Science_2', 
        'Math', 'Physics', 'Science', 
        'Score'])
    writer.writerows(data)

print(f"CSV file '{filename}' generated successfully.")
