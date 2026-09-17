import numpy as np


def load_student_data(file_path):
    data = np.genfromtxt(file_path, dtype=np.int32, delimiter=",", skip_header=1)

    marks = data[:, 1]
    return marks


