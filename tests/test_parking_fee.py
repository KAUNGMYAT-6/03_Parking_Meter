# Unit tests for calculate_parking_fee() in parking_fee.py
# Test IDs follow the Test Case Specification (PKM-FEE-TC-xxx)

import pytest
from parking_fee import calculate_parking_fee


# Valid minutes: 200 cents for every started hour, 0 minutes is free
@pytest.mark.parametrize(
    "minutes, expected_fee",
    [
        pytest.param(0, 0, id="PKM-FEE-TC-001"),
        pytest.param(1, 200, id="PKM-FEE-TC-002"),
        pytest.param(59, 200, id="PKM-FEE-TC-003"),
        pytest.param(60, 200, id="PKM-FEE-TC-004"),
        pytest.param(61, 400, id="PKM-FEE-TC-005"),
        pytest.param(120, 400, id="PKM-FEE-TC-006"),
        pytest.param(121, 600, id="PKM-FEE-TC-007"),
    ],
)
def test_fee_for_valid_minutes(minutes, expected_fee):
    assert calculate_parking_fee(minutes) == expected_fee


# Negative minutes is the right type but out of range
@pytest.mark.parametrize(
    "minutes",
    [
        pytest.param(-1, id="PKM-FEE-TC-008"),
    ],
)
def test_fee_negative_minutes_raises_value_error(minutes):
    with pytest.raises(ValueError):
        calculate_parking_fee(minutes)


# Anything that is not a real int should raise TypeError (bool included)
@pytest.mark.parametrize(
    "minutes",
    [
        pytest.param(60.0, id="PKM-FEE-TC-009"),
        pytest.param("60", id="PKM-FEE-TC-010"),
        pytest.param(None, id="PKM-FEE-TC-011"),
        pytest.param(True, id="PKM-FEE-TC-012"),
    ],
)
def test_fee_wrong_type_raises_type_error(minutes):
    with pytest.raises(TypeError):
        calculate_parking_fee(minutes)
