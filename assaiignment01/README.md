# ASSIGNMENT No. 1 – CLO1 – STUDENT SUPPORT RULE ENGINE

## Program Description

This program is a Student Support Rule Engine. It takes a student's attendance percentage, assignment average, and number of missed submissions as input. Based on these values, it classifies the student into a support-priority category and displays an appropriate advisory message.

## Support-Priority Rules

The program applies the rules in the following order:

1. **High priority**

   * Attendance is below 60%, **OR**
   * Missed submissions are 4 or more.

2. **Moderate priority**

   * Attendance is below 75%, **OR**
   * Assignment average is below 60%, **OR**
   * Missed submissions are 2 or more.

3. **Routine monitoring**

   * Used when neither the High priority nor Moderate priority rule is satisfied.

## Submitted Files

### `support_engine.py`

Contains the main student support rule engine. It includes input-validation functions, the support classification function, the advisory-message function, and the `main()` function.

### `test_support_engine.py`

Contains assertions that test the support-priority classification and advisory messages, including normal and boundary cases.

### `README.md`

Provides information about the assignment, support rules, submitted files, commands for running and testing the program, and known limitations.

## How to Run the Program

Run the following command from the project root:

```bash
uv run python Assignment_01/support_engine.py
```

## How to Run the Tests

Run:

```bash
uv run python Assignment_01/test_support_engine.py
```

A successful test run displays:

```text
All tests passed.
```

## Known Limitations

1. The program uses fixed support-priority rules and does not adapt the rules based on individual student circumstances.

2. The program only considers three indicators: attendance, assignment average, and missed submissions.

3. The program is command-line based and does not provide a graphical user interface.

4. The program does not permanently store student records or previous results.
