# Monthly Expense Calculator

A simple web application to help users calculate and analyze their monthly expenses. Enter your expenses by category and amount, and instantly see your total spending, average daily expense, and the top 3 largest expenses.

## Features
- Add expenses by category and amount (supports decimals)
- View all entered expenses in a table
- Calculate:
  - Total amount of expenses
  - Average daily expense (over 30 days)
  - Top 3 largest expenses
- Responsive, user-friendly interface
- Backend API built with FastAPI (Python)
- Unit tests for backend logic

## Project Structure
```
.
├── main.py              # FastAPI backend (serves API and static files)
├── requirements.txt     # Python dependencies
├── static/
│   └── index.html       # Frontend (HTML, CSS, JS)
├── test_main.py         # Backend unit tests
└── README.md            # Project documentation
```

## Getting Started

### 1. Clone the repository
```bash
git clone <repo-url>
cd <repo-directory>
```

### 2. Set up a virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
uvicorn main:app --reload
```
- The app will be available at [http://localhost:8000](http://localhost:8000)

## Usage
1. Open the app in your browser.
2. Enter expense categories and amounts (decimals allowed).
3. Click "Add Expense" to add each item to the table.
4. When ready, click "Calculate" to see:
   - Total expenses
   - Average daily expense
   - Top 3 largest expenses

## API
### POST `/expenses`
- **Request Body:**
  ```json
  {
    "expenses": [
      { "category": "Groceries", "amount": 15000.50 },
      { "category": "Rent", "amount": 40000 }
    ]
  }
  ```
- **Response:**
  ```json
  {
    "total": 55000.5,
    "averageDaily": 1833.35,
    "top3": [
      { "category": "Rent", "amount": 40000 },
      { "category": "Groceries", "amount": 15000.5 }
    ]
  }
  ```
- **Error (empty list):**
  ```json
  { "detail": "Expenses list cannot be empty." }
  ```

## Testing
Run backend unit tests with:
```bash
pytest test_main.py
```

## License
MIT (or specify your license)
