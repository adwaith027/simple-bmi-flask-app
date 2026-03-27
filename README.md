# BMI Flask Calculator

A simple Flask web application for calculating Body Mass Index (BMI) with support for multiple units of measurement.

## Description

This is a learning project built to understand how Flask works. The application allows users to calculate their BMI by entering their height and weight in various units (feet, meters, inches, centimeters for height and pounds, kilograms for weight). The app provides personalized feedback based on WHO health standards.

## Features

- **Multi-unit Support**: Calculate BMI using imperial (feet, inches, pounds) or metric (meters, centimeters, kilograms) units
- **Health Feedback**: Get personalized health feedback based on BMI categories (Underweight, Normal Weight, Overweight, Obese)
- **Input Validation**: Ensures valid numeric input before calculation
- **Responsive Design**: Clean and user-friendly interface

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd bmi_flask_app
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - **Windows**: `venv\Scripts\activate`
   - **macOS/Linux**: `source venv/bin/activate`
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python run.py
   ```
2. Open your web browser and navigate to `http://localhost:5000`
3. Enter your height and weight in your preferred units
4. Click "Calculate" to see your BMI and health feedback

### Debug Mode

To enable Flask debug mode, set the environment variable:
```bash
set DEBUG_VAL=True  # Windows
export DEBUG_VAL=True  # macOS/Linux
```

## Project Structure

```
bmi_flask_app/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── bmi.py               # BMI calculation logic
│   ├── routes.py            # Route handlers
│   ├── static/              # Static files (CSS, JS, images)
│   └── templates/           # HTML templates
│       └── index.html       # Main page
├── run.py                   # Application entry point
└── requirements.txt         # Python dependencies
```

## Technologies Used

- **Flask 3.1.3** - Lightweight Python web framework
- **HTML/CSS/JavaScript** - Frontend
- **Python 3** - Backend logic

## BMI Categories

The app classifies BMI according to WHO standards:

| BMI Range | Category | Recommendation |
|-----------|----------|-----------------|
| < 16.0 | Severe Underweight | Consult a doctor |
| 16.0 - 18.4 | Underweight | Gain weight gradually |
| 18.5 - 24.9 | Normal Weight | Maintain current weight |
| 25.0 - 29.9 | Overweight | Exercise and balanced diet |
| 30.0 - 34.9 | Obese Class I | Medical consultation recommended |
| 35.0 - 39.9 | Obese Class II | Medical supervision needed |
| ≥ 40.0 | Obese Class III | Seek urgent medical advice |

## Learning Objectives

This project demonstrates:
- Flask application structure and configuration
- Route handling with GET and POST requests
- Form data processing
- Template rendering with Jinja2
- Application factory pattern
- Unit conversion logic
- Input validation

## License

This project is open source and available under the MIT License.
