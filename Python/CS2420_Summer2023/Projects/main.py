from slist import SList
from course import Course


def calculate_gpa(courseList):
    sumGrades = 0
    credits = 0
    for course in courseList:
        sumGrades += course.grade() * course.credit_hr()
        credits += course.credit_hr()
    if credits == 0:
        return 0
    return sumGrades / credits


def is_sorted(lyst):
    for i in range(len(lyst) - 1):
        if lyst[i] > lyst[i + 1]:
            return False
    return True


def main():
    # Create an SList of Course objects
    courses = SList()

    # Insert Course objects in ascending order of course number
    courses.insert(Course(101, "Math", 3.0, 3.5))
    courses.insert(Course(201, "Physics", 4.0, 3.7))
    courses.insert(Course(105, "English", 3.0, 3.2))
    courses.insert(Course(301, "Chemistry", 3.5, 3.9))

    # Print the list of courses
    print(courses)

    # Find a course by course number
    found_course = courses.find(105)
    if found_course:
        print(f"Found Course: {found_course}")
    else:
        print("Course not found")

    # Remove a course by course number
    removed = courses.remove(201)
    if removed:
        print("Course removed")
    else:
        print("Course not found")

    # Remove all occurrences of a course by course number
    courses.insert(Course(101, "Math", 3.0, 3.5))
    courses.insert(Course(201, "Physics", 4.0, 3.7))
    courses.insert(Course(105, "English", 3.0, 3.2))
    courses.insert(Course(301, "Chemistry", 3.5, 3.9))
    courses.insert(Course(201, "Physics", 4.0, 3.7))
    courses.remove_all(201)

    # Print the updated list of courses
    print(courses)

    # Calculate GPA
    gpa = calculate_gpa(courses)
    print(f"GPA: {gpa}")

    # Check if the list is sorted
    sorted_status = is_sorted(courses)
    print(f"Sorted: {sorted_status}")


if __name__ == "__main__":
    main()
