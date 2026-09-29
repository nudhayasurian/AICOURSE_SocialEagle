def main():
    try:
        mark = float(input("Enter a mark (0-100): "))

        # Check that the mark is within the valid range
        if mark < 0 or mark > 100:
            print("Invalid mark. Please enter a number between 0 and 100.")
            return

        # Determine the grade
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "E"

        print(f"Entered mark: {mark}")
        print(f"Grade: {grade}")

    except ValueError:
        print("Invalid input. Please enter a number between 0 and 100.")
