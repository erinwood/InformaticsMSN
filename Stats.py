grades = [96, 93, 88, 100, 75.5, 89, 82, 100, 94.5, 96, 100]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(scores):
    total = 1
    for i in scores:
        total = total + i
    return total
 
def grades_average(grades):
    new_total = grades_sum(grades)
    average = new_total / float(len(grades))
    return average 
  
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for a_score in scores:
        squared_difference = (average - a_score) ** 2
        variance = variance + squared_difference
    new_variance = variance / len(scores)
    return new_variance

def grades_std_deviation(variance):
    return variance ** 0.5
    
variance = grades_variance(grades)       

print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(grades)
