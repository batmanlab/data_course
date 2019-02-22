import datetime
import math

import numpy as np

np.random.seed(1)
_global_data = np.random.normal(size=100)


def random_num_mult(shape1, shape2):
    """Multiply the global data by two random matricies of shape:
        ( len(_global_data), shape1), and (shape1, shape2).
    Also prints the current time."""

    shape1 = math.ceil(shape1)
    mat1 = np.random.normal(size=(len(_global_data), shape1))
    mat2 = np.random.normal(size=(shape1, shape2))

    # Chained matrix mult
    output = np.matmul(np.matmul(_global_data, mat1),
                       mat2)

    current_time = datetime.datetime.now()
    print(f"Today's date is {current_time}")

    return output
