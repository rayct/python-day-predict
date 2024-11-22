# Date Calculator

## Description

The **Date Calculator** is a simple Python-based GUI application built using `tkinter` that allows users to calculate:

1. **Days Difference** between two dates.
2. **Future Date** by adding a specified number of days to a given date.

This application features a modern dark-themed interface and includes **Clear** buttons to reset the input fields and results for each function.

## Features

- **Days Difference**: Calculate the number of days between two dates.
- **Future Date**: Calculate a future date by adding a specified number of days to a given start date.
- **Clear Buttons**: Reset the input fields and result labels for both calculations.
- **Dark UI**: Modern dark mode design for a clean and user-friendly experience.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/<username>/date-calculator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd date-calculator
    ```

3. Install any dependencies (if needed):

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the application, simply execute the Python script:

```bash
python date_calculator.py
```

### How It Works:

1. **Days Difference**:
   - Enter the **Start Date** and **End Date** in the format `DD-MM-YYYY`.
   - Click the "Calculate Days Difference" button to get the number of days between the two dates.
   - Use the "Clear" button to reset the inputs and results.

2. **Future Date**:
   - Enter the **Start Date** in the format `DD-MM-YYYY`.
   - Enter the number of **Days to Add**.
   - Click the "Calculate Future Date" button to get the future date.
   - Use the "Clear" button to reset the inputs and results.

### Example:
- **Days Difference**:
  - Start Date: `20-08-2024`
  - End Date: `19-11-2024`
  - Output: `Days Difference: 91`

- **Future Date**:
  - Start Date: `20-08-2024`
  - Days to Add: `100`
  - Output: `Future Date: 29-11-2024`

## About

Created by **Raymond C. Turner**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Summary of Updates - v0.1.4
- Added "Clear" buttons for each section (`Days Difference` and `Future Date`).
- Each "Clear" button resets the input fields and the result labels to allow for fresh calculations.