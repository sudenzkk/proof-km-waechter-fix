# test_km_wachter.py
from km_wachter import needs_service, wear_percent


def test_wear_percent_preserves_fractional_progress():
    assert abs(wear_percent(14900, 15000) - 99.33) < 0.01


def test_almost_due_car_is_flagged():
    # A car at 14,900 of its 15,000 km window is about 99% worn and MUST be flagged.
    assert needs_service({"id": "VOS-4471", "odometer": 14900, "last_service_km": 0}) is True


def test_missing_reading_is_not_treated_as_zero():
    # A car with NO last-service reading must not be treated as fully worn.
    assert needs_service({"id": "VOS-7788", "odometer": 92000}) is False


def test_none_reading_is_not_treated_as_zero():
    assert needs_service({"id": "VOS-7788", "odometer": 92000, "last_service_km": None}) is False
