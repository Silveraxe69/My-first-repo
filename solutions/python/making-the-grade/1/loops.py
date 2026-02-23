"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores."""
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """Count the number of failing students (score <= 40)."""
    return sum(1 for score in student_scores if score <= 40)


def above_threshold(student_scores, threshold):
    """Return scores that are at or above the given threshold."""
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Create a list of grade thresholds for D, C, B, A."""
    # Total range from just above failing (41) to highest
    step = (highest - 40) // 4
    return [
        41,
        41 + step,
        41 + step * 2,
        41 + step * 3,
    ]


def student_ranking(student_scores, student_names):
    """Return student rankings with names and scores."""
    rankings = []
    for index, (name, score) in enumerate(zip(student_names, student_scores), start=1):
        rankings.append(f"{index}. {name}: {score}")
    return rankings


def perfect_score(student_info):
    """Return the first student with a perfect score of 100."""
    for student in student_info:
        if student[1] == 100:
            return student
    return []