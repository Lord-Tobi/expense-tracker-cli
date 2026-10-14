# Python Expense Tracker

A simple command-line Expense Tracker built with Python. This project helps users record their expenses, view spending history, and understand where their money goes.

I built this project as part of my journey to learn Python programming, practise problem-solving, and improve my understanding of lists, dictionaries, loops, functions, and input validation.

## Features

- **Add Expenses:** Record an expense with a description, category, and amount.
- **Input Validation:** Reject invalid amounts and require the amount to be greater than zero.
- **View All Expenses:** Display all recorded expenses.
- **Calculate Total Spending:** Calculate the total amount spent.
- **Category Summary:** Calculate how much was spent in each category.
- **Most Expensive Expense:** Identify the expense with the highest amount.
- **Interactive Menu:** Navigate the application through a menu that repeats until you choose to quit.
- **In-Memory Storage:** Store expenses while the application is running.

## Technologies Used

- Python 3
- Git
- GitHub

## Getting Started

### Prerequisites

You need Python 3 installed on your computer.

Check your Python version by running:

```bash
python3 --version
```

### Installation

1. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate into the project directory:

   ```bash
   cd expense-tracker
   ```

3. (Optional) Create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

4. Activate the virtual environment on Linux:

   ```bash
   source .venv/bin/activate
   ```

### Running the Application

Run the main program:

```bash
python3 main.py
```

Follow the on-screen menu to add expenses, view your expenses, view your summary, or quit the application.

## Example

An expense might look like this:

```text
Description: Groceries
Category: Food
Amount: 2500.00
```

The summary displays the total amount spent, spending by category, and the most expensive expense.

## Project Structure

```text
expense-tracker/
├── main.py
├── level_1.py
├── level_2-3.py
├── .gitignore
└── README.md
```

- `main.py` — Main Expense Tracker application.
- `level_1.py` — Python practice exercises.
- `level_2-3.py` — Additional Python practice exercises.
- `.gitignore` — Specifies files and folders Git should ignore.
- `README.md` — Project documentation.

## Current Limitations

- Expenses are stored in memory and are lost when the program exits.
- The application runs in the terminal rather than a graphical interface.
- There is no database or file-based persistence yet.

## Future Improvements

- Save expenses to a file or database.
- Add dates to expenses.
- Allow users to edit and delete expenses.
- Add monthly spending reports.
- Improve error handling and input validation.
- Add automated tests.

## Learning Goals

This project helps me practise:

- Variables and data types
- Lists and dictionaries
- Conditional statements
- Loops
- Exception handling with `try` and `except`
- User input validation
- Basic data processing
- Git and GitHub version control

## Author

A Python learner building practical projects to develop programming and problem-solving skills.

## License

This project is currently available for learning and personal practice. A formal license can be added later if the project is shared for reuse.