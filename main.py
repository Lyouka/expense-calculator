from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
import os


app = FastAPI()

# Mount the static directory (contains index.html)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


# Serve the HTML file at the root URL
@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html") as f:
        return f.read()


# Serve the HTML file at the root URL
@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html") as f:
        return f.read()


# Expense models
class Expense(BaseModel):
    category: str
    amount: float


class ExpensesRequest(BaseModel):
    expenses: List[Expense]


class ExpensesResponse(BaseModel):
    total: float
    averageDaily: float
    top3: List[Expense]


# API endpoint for calculations
@app.post("/expenses", response_model=ExpensesResponse)
def calculate_expenses(data: ExpensesRequest):
    expenses = data.expenses
    if not expenses:
        raise HTTPException(status_code=400, detail="Expenses list cannot be empty.")

    total = sum(e.amount for e in expenses)
    average_daily = round(total / 30, 2)
    top3 = sorted(expenses, key=lambda e: e.amount, reverse=True)[:3]

    return ExpensesResponse(total=total, averageDaily=average_daily, top3=top3)
