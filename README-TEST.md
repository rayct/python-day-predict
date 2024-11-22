# Date Calculator

A simple Python-based application that provides two date-related features:
1. **Days Difference Calculation**: Calculate the number of days between two dates.
2. **Future Date Calculation**: Calculate a future date after adding a specified number of days to a given start date.

This application uses Python's `Tkinter` library to provide a modern dark-themed user interface.

## Features

- **Days Difference**: Calculate the difference in days between two dates.
- **Future Date**: Calculate a future date by adding a specified number of days to a given start date.
- **Dark Mode UI**: The user interface is styled with a modern dark theme for ease of use.

## Requirements

- Python 3.6 or higher
- Tkinter (pre-installed with Python)

## Installation and Setup

Follow the steps below to set up the project on your local machine:

### 1. Clone the repository
Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/date-calculator.git
cd date-calculator
```

### 2. Create a Virtual Environment

#### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### For macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install any required dependencies (if applicable, such as `tkinter` or others):

```bash
pip install -r requirements.txt
```

Note: Tkinter is included by default with Python, so you may not need to install anything extra.

### 4. Run the Program

To run the program, execute the following command:

```bash
python date_calculator.py
```

This will open the application window where you can use the **Days Difference** and **Future Date** features.

## Usage

### Days Difference Calculation
1. Enter a **Start Date** and **End Date** in the format `DD-MM-YYYY`.
2. Click **Calculate Days Difference** to get the number of days between the two dates.

### Future Date Calculation
1. Enter a **Start Date** in the format `DD-MM-YYYY`.
2. Enter the number of **Days to Add**.
3. Click **Calculate Future Date** to calculate the future date.

## Screenshot

![Screenshot of the app](screenshot.png)

## About

Created by **Raymond C. Turner**.

Feel free to reach out for feedback, questions, or contributions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```

---

### Key Sections:

- **Project Title**: "Date Calculator"
- **Description**: Explains the functionality of the program.
- **Features**: Lists the two primary features (Days Difference and Future Date calculation).
- **Requirements**: Specifies that Python 3.6 or higher is required, and mentions Tkinter.
- **Installation & Setup**: Detailed instructions for cloning the repo, setting up a virtual environment, installing dependencies, and running the program.
- **Usage**: Explains how to use both the Days Difference and Future Date calculation features.
- **Screenshot**: Placeholder for a screenshot image (`screenshot.png`).
- **About**: Mentions the author and encourages feedback.
- **License**: Placeholder for project license (MIT License).

### Notes:
- Ensure you have a screenshot image (`screenshot.png`) in your project folder, or update the `README.md` if you prefer a different image name.
- If there are any specific dependencies in the future (like a library that is not part of the Python standard library), list them in the `requirements.txt` and update the installation instructions accordingly.