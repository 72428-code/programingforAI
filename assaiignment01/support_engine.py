def read_float(prompt, minimum, maximum):
    """Read and return a valid floating-point value."""

    while True:
        try:
            value = float(input(prompt))

            if minimum <= value <= maximum:
                return value 

            print(f"Please enter a value between {minimum} and {maximum}.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def read_int(prompt, minimum):
    """Read and return a valid integer value."""

    while True:
        try:
            value = int(input(prompt))

            if value >= minimum:
                return value

            print(f"Please enter a value of {minimum} or greater.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def classify_support(attendance, assignment_average, missed_submissions):
    """Return the student support-priority category."""

    if attendance < 60 or missed_submissions >= 4:
        return "High priority"

    if attendance < 75 or assignment_average < 60 or missed_submissions >= 2:
        return "Moderate priority"

    return "Routine monitoring"


def format_message(category):
    """Return an advisory message for the category."""

    if category == "High priority":
        return "Immediate academic support is recommended."

    if category == "Moderate priority":
        return "Monitor progress and provide targeted guidance."

    return "Continue routine monitoring."


def main():
    """Run the student support rule engine."""

    attendance = read_float(
        "Attendance percentage: ", 0, 100
    )

    assignment_average = read_float(
        "Assignment average: ", 0, 100
    )

    missed_submissions = read_int(
        "Missed submissions: ", 0
    )

    category = classify_support(
        attendance,
        assignment_average,
        missed_submissions
    )

    message = format_message(category)

    print("Support category:", category)
    print("Advisory:", message)


if __name__ == "__main__":
    main()