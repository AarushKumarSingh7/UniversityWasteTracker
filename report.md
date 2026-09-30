# University Waste Tracker - Project Report

## 1. Introduction

University Waste Tracker is a Python-based problem-solving project. It applies basic programming concepts to a real-world university waste-recording problem.

The project is designed for CSE1021 and uses basic algorithms, functions, conditional statements, loops, lists, sets and dictionaries.

## 2. Problem Statement

University waste is generated at multiple locations and in multiple categories. The quantity may be recorded manually, but calculating totals and comparing categories or locations repeatedly is time-consuming.

The proposed program provides a simple computational solution for recording and analysing waste.

## 3. Objectives

1. Record waste quantity.
2. Store each record using a Python dictionary.
3. Calculate total waste using summation.
4. Find the largest recorded quantity.
5. Group records by category.
6. Group records by university location.
7. Demonstrate problem-solving and algorithm design using Python.

## 4. Functional Requirements

### Module 1: Waste Entry
- Accept date.
- Accept university location.
- Accept waste category.
- Accept quantity.
- Add the record to the list.

### Module 2: Record Display
- Display all stored records.
- Display record number, date, location, category and quantity.

### Module 3: Waste Analysis and Reporting
- Calculate total waste.
- Find maximum single-record quantity.
- Produce category-wise totals.
- Produce location-wise totals.
- Produce date-wise totals.

## 5. Non-Functional Requirements

1. **Usability:** Menu-based interaction should be simple for a beginner.
2. **Reliability:** Invalid menu choices and invalid quantities are rejected.
3. **Maintainability:** Different tasks are placed in separate Python files and functions.
4. **Resource Efficiency:** The program uses simple lists and dictionaries and does not require external packages.

## 6. System Architecture

User
  |
  v
main.py
  |
  +--> tracker.py ----> data.py
  |
  +--> reports.py ----> algorithms.py
  |
  v
Console Output

## 7. Workflow

START
  |
Display Menu
  |
Read Choice
  |
  +-- 1 --> Enter Waste --> Validate --> Store Record --+
  |                                                     |
  +-- 2 --> Display Records ----------------------------+
  |                                                     |
  +-- 3 --> Total/Maximum Report -----------------------+
  |                                                     |
  +-- 4 --> Category Report ----------------------------+
  |                                                     |
  +-- 5 --> Location Report ----------------------------+
  |                                                     |
  +-- 6 --> Date Report -------------------------------+
  |                                                     |
  +-- 7 --> END
  |
  +-- Other --> Show Error --> Display Menu

## 8. Use Case Diagram

User
 |
 +-- Add waste record
 +-- View records
 +-- View total waste
 +-- View category report
 +-- View location report
 +-- View date report
 +-- Exit program

## 9. Sequence Diagram

User -> main.py: Select menu option
main.py -> tracker.py: Request input / record operation
tracker.py -> data.py: Read categories and locations
tracker.py -> main.py: Return updated records
main.py -> reports.py: Request report
reports.py -> algorithms.py: Perform summation/counting/max
algorithms.py -> reports.py: Return calculated result
reports.py -> main.py: Return report
main.py -> User: Display result

## 10. Component Diagram

+------------------+
|     main.py      |
| Menu / Workflow  |
+--------+---------+
         |
   +-----+------+
   |            |
   v            v
tracker.py   reports.py
   |            |
   v            v
data.py    algorithms.py

## 11. Data Design

A waste record is represented by a dictionary:

{
    "date": "30-09-2026",
    "location": "Canteen",
    "category": "Food",
    "quantity": 12.5
}

All records are stored in a Python list.

Categories are stored in a Python list.
University locations are stored in a Python list.
Unique dates/categories can be obtained using a Python set.

## 12. Algorithms

### Algorithm A: Total Waste

1. Set total = 0.
2. Traverse every record.
3. Add record quantity to total.
4. Return total.

### Algorithm B: Maximum Waste

1. If the list is empty, return 0.
2. Set first number as maximum.
3. Traverse all numbers.
4. If a number is greater than maximum, update maximum.
5. Return maximum.

### Algorithm C: Category Report

1. Select one category.
2. Traverse all records.
3. If the record category matches, add its quantity.
4. Repeat for each category.
5. Display the result.

## 13. Pseudocode

BEGIN

Create sample records

REPEAT
    Display menu
    Read choice

    IF choice = 1
        Read date, location, category and quantity
        Validate input
        Add record
    ELSE IF choice = 2
        Display records
    ELSE IF choice = 3
        Calculate total and maximum
    ELSE IF choice = 4
        Calculate category totals
    ELSE IF choice = 5
        Calculate location totals
    ELSE IF choice = 6
        Calculate date totals
    ELSE IF choice = 7
        Stop program
    ELSE
        Display invalid choice
    END IF
UNTIL choice = 7

END

## 14. Testing Approach

| Test | Input | Expected Result |
|---|---|---|
| 1 | Menu 2 | Existing records displayed |
| 2 | Valid waste record | Record added |
| 3 | Quantity 0 | Quantity rejected |
| 4 | Negative quantity | Quantity rejected |
| 5 | Invalid menu number | Error message displayed |
| 6 | Total report | Correct sum displayed |
| 7 | Category report | Category totals displayed |
| 8 | Location report | Location totals displayed |
| 9 | Date report | Date totals displayed |

## 15. Example Result

With the included sample records:

- Food: 12.5 kg
- Paper: 6.0 kg
- Plastic: 8.5 kg
- Total: 27.0 kg
- Largest single record: 12.5 kg

## 16. Design Decisions and Rationale

A list is used to store multiple records because Python list operations are part of the syllabus.

A dictionary is used for each record because it provides a simple way to associate fields such as date, location, category and quantity.

Functions divide the solution into smaller tasks and demonstrate modular programming.

Loops are used for repeated input and calculations.

No external library or database is used so that the implementation remains within the requested course scope.

## 17. Challenges Faced

1. Designing a useful real-world problem using basic programming only.
2. Organising records using lists and dictionaries.
3. Calculating multiple reports without advanced libraries.
4. Validating user input using basic Python statements.

## 18. Learnings and Key Takeaways

- A real-world problem can be converted into smaller programming tasks.
- Top-down design helps divide a program into functions.
- Lists and dictionaries can represent practical data.
- Loops can perform repeated calculations.
- Simple algorithms such as counting, summation and maximum finding are useful for data analysis.

## 19. Future Enhancements

Future versions could include permanent storage, graphical interface and more advanced analysis. These are intentionally outside the current implementation because the project is restricted to the CSE1021 syllabus.

## 20. References

1. CSE1021 Introduction to Problem Solving and Programming - provided course syllabus.
2. VITyarthi Build Your Own Project - provided project instructions.
