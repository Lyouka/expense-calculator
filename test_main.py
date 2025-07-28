import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_calculate_expenses_normal(client):
    """Test calculation with a typical list of expenses."""
    data = {
        "expenses": [
            {"category": "Groceries", "amount": 15000},
            {"category": "Rent", "amount": 40000},
            {"category": "Transportation", "amount": 5000},
            {"category": "Entertainment", "amount": 10000},
            {"category": "Communication", "amount": 2000},
            {"category": "Gym", "amount": 3000},
        ]
    }
    response = client.post("/expenses", json=data)
    assert response.status_code == 200
    result = response.json()
    assert result["total"] == 75000
    assert result["averageDaily"] == 2500.0
    assert [e["category"] for e in result["top3"]] == [
        "Rent",
        "Groceries",
        "Entertainment",
    ]
    assert [e["amount"] for e in result["top3"]] == [40000, 15000, 10000]


def test_calculate_expenses_empty(client):
    """Test that an empty expenses list returns a 400 error."""
    data = {"expenses": []}
    response = client.post("/expenses", json=data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Expenses list cannot be empty."


@pytest.mark.parametrize(
    "expenses,expected_top3",
    [
        (
            [{"category": "A", "amount": 100}, {"category": "B", "amount": 200}],
            ["B", "A"],
        ),
        ([{"category": "A", "amount": 100}], ["A"]),
    ],
)
def test_calculate_expenses_top3_various(client, expenses, expected_top3):
    """Test top3 logic with less than 3 expenses."""
    data = {"expenses": expenses}
    response = client.post("/expenses", json=data)
    assert response.status_code == 200
    result = response.json()
    assert [e["category"] for e in result["top3"]] == expected_top3


@pytest.mark.parametrize(
    "expenses",
    [
        ([{"category": "A", "amount": 0}, {"category": "B", "amount": 0}]),
        ([{"category": "A", "amount": 0}]),
    ],
)
def test_calculate_expenses_zero_amount(client, expenses):
    """Test calculation when all amounts are zero."""
    data = {"expenses": expenses}
    response = client.post("/expenses", json=data)
    assert response.status_code == 200
    result = response.json()
    assert result["total"] == 0
    assert result["averageDaily"] == 0.0
    assert len(result["top3"]) == len(expenses)
