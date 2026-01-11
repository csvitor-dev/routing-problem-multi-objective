from pymoo.core.result import Result
import numpy as np


def knee_point(res: Result) -> list[list[float]]:
    f1, f2 = res.F[:, 0], res.F[:, 1]

    p1 = np.array([f1.min(), f2.max()])
    p2 = np.array([f1.max(), f2.min()])
    distances = []

    for i in range(len(res.F)):
        p = np.array([f1[i], f2[i]])
        dist = np.abs(np.cross(p2 - p1, p - p1)) / np.linalg.norm(p2 - p1)
        distances.append(dist)
    best_choice_index = np.argmax(distances)

    return res.X[best_choice_index]
