import statistics

import load_data

target_percentile = 90

marks = load_data.load_student_data("data/students.csv")

average_marks = statistics.calculate_average(marks)

std_dev = statistics.standard_deviation(marks)

percentile = statistics.calculate_percentile(marks, target_percentile)

top_students = statistics.top_students(marks, target_percentile)

grades = statistics.calculate_grade_distribution(marks)

median = statistics.calculate_median(marks)

minimum_marks = statistics.calculate_minimum(marks)

maximum_marks = statistics.calculate_maximum(marks)

print(f"""\n
        Average Marks: {average_marks}
        Standard Deviation : {std_dev}
        Percentile: {percentile}
        Top Students: {top_students}
        Grades: {grades}
        Median: {median}
        Minimum Marks: {minimum_marks}
        Maximum Marks: {maximum_marks}""")
