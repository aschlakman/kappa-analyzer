from typing import List

from extract_results import get_aggregated_classification
from FleissKappa.fleiss import fleissKappa


def create_binary_scale(classification_matrix: List[List[int]]):
    binary_classification_matrix: List[List[int]] = list()

    for discrete_classification in classification_matrix:
        binary_classification = [0, 0]
        for i, value in enumerate(discrete_classification):
            if i + 1 <= len(discrete_classification) / 2:
                binary_classification[0] += value
            else:
                binary_classification[1] += value
        binary_classification_matrix.append(binary_classification)
    return binary_classification_matrix


if __name__ == '__main__':
    db_files = [
        r"C:\Code\seminar\results_db\storage_yaara.db",
        r"C:\Code\seminar\results_db\storageMerav.db",
        r"C:\Code\seminar\results_db\storageAri.db"
    ]
    classification_matrix = get_aggregated_classification(db_files)
    print(classification_matrix)
    binary_matrix = create_binary_scale(classification_matrix)
    print(binary_matrix)

    f = fleissKappa(classification_matrix, len(db_files))

    f_bin = fleissKappa(binary_matrix, len(db_files))
