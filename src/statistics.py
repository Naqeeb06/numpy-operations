import numpy as np


def calculate_average(marks):
    average = np.mean(marks)
    return average


def standard_deviation(marks):
    return np.std(marks)


def calculate_percentile(marks, percentile):
    return np.percentile(marks, percentile)


def top_students(marks, percentile):
    threshold = calculate_percentile(marks, percentile)

    top = marks[marks >= threshold]
    return np.sort(top)


def calculate_grade_distribution(marks):
    grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    grades["A"] = np.count_nonzero(marks[(marks >= 90)])
    grades["B"] = np.count_nonzero(marks[(marks >= 80) & (marks < 90)])
    grades["C"] = np.count_nonzero(marks[(marks >= 70) & (marks < 80)])
    grades["D"] = np.count_nonzero(marks[(marks >= 60) & (marks < 70)])
    grades["F"] = np.count_nonzero(marks[(marks < 60)])

    return grades


def calculate_median(marks):
    return np.median(marks)


def calculate_minimum(marks):
    return np.min(marks)


def calculate_maximum(marks):
    return np.max(marks)
