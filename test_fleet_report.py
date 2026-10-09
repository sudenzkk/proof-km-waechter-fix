# test_fleet_report.py
from fleet_report import fleet_summary
from fleet_utils import km_to_miles

SAMPLE = [
    {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
    {"id": "VOS-2210", "odometer": 48400, "last_service_km": 45000},
]


def test_summary_counts_due_cars():
    # Only VOS-4471 is nearly worn, so exactly one car is due.
    assert fleet_summary(SAMPLE)["due"] == 1


def test_summary_handles_car_without_last_service_reading():
    fleet = SAMPLE + [{"id": "VOS-7788", "odometer": 92000}]

    assert fleet_summary(fleet) == {
        "count": 3,
        "due": 1,
        "average_wear": (14900 / 15000 * 100 + 3400 / 15000 * 100) / 2,
    }


def test_average_wear_preserves_fractional_values():
    fleet = [
        {"id": "A", "odometer": 14900, "last_service_km": 0},
        {"id": "B", "odometer": 3000, "last_service_km": 0},
    ]

    assert abs(fleet_summary(fleet)["average_wear"] - 59.67) < 0.01


def test_kilometres_convert_to_miles():
    assert abs(km_to_miles(100) - 62.14) < 0.01
