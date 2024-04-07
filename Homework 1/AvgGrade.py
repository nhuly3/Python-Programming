students = [
    {'name': 'Alice', 'age': 20, 'grades': [85, 90, 88]},
    {'name': 'Bob', 'age': 20, 'grades': [70, 75, 68]},
    {'name': 'Charlie', 'age': 21, 'grades': [80, 82, 84]},
    {'name': 'David', 'age': 21, 'grades': [90, 95, 92]}
]

def average_grade_by_age(students):
    # Your code here
    avg={}
    [avg.update({s['age']:{'sum':avg.get(s['age'],{'sum':0})['sum']+sum(s['grades']),'count':avg.get(s['age'],{'count':0})['count']+len(s['grades'])}}) for s in students]
    return{age:round(data['sum']/data['count'],1) for age,data in avg.items()}

print(average_grade_by_age(students))
