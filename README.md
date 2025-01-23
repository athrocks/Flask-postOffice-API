# Post Office Finder

![gif](https://github.com/athrocks/Flask-postOffice-API/blob/main/1.gif)

## Overview
A Flask-based web application to find post office details using an Indian postal code (pincode).

## Features
- Lookup post office details by 6-digit pincode
- Input validation
- Error handling for invalid pincodes
- Displays state, name, block, and district information

## Prerequisites
- Python 3.8+
- pip

## Setup

### 1. Clone the Repository

### 2. Create Virtual Environment
```bash
virtualenv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install flask requests
```

### 4. Run the Application
```bash
python app.py
```

## Usage
1. Open browser to `http://localhost:5000`
2. Enter 6-digit pincode
3. View post office details

## API
Uses [Postal Pincode API](https://api.postalpincode.in/)

## Error Handling
- Validates 6-digit numeric input
- Displays error for invalid pincodes

## License
MIT License
