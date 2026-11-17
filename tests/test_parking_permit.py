# Unit tests for is_permit_valid() in parking_permit.py
# Test IDs follow the Test Case Specification (PKM-PMT-TC-xxx)

import pytest
from parking_permit import is_permit_valid


# Valid inputs. "is" is used on purpose because the spec says the
# function must return the real True/False, not 1 or 0 (and 1 == True in Python).
@pytest.mark.parametrize(
    "permit_active, parked_minutes, expected",
    [
        pytest.param(True, 0, True, id="PKM-PMT-TC-001"),
        pytest.param(True, 60, True, id="PKM-PMT-TC-002"),
        pytest.param(True, 120, True, id="PKM-PMT-TC-003"),
        pytest.param(True, 121, False, id="PKM-PMT-TC-004"),
        pytest.param(False, 60, False, id="PKM-PMT-TC-005"),
    ],
)
def test_permit_valid_inputs(permit_active, parked_minutes, expected):
    assert is_permit_valid(permit_active, parked_minutes) is expected


# Negative minutes is the right type but out of range
@pytest.mark.parametrize(
    "permit_active, parked_minutes",
    [
        pytest.param(True, -1, id="PKM-PMT-TC-006"),
    ],
)
def test_permit_negative_minutes_raises_value_error(permit_active, parked_minutes):
    with pytest.raises(ValueError):
        is_permit_valid(permit_active, parked_minutes)


# Wrong data types for either argument should raise TypeError
@pytest.mark.parametrize(
    "permit_active, parked_minutes",
    [
        pytest.param(1, 60, id="PKM-PMT-TC-007"),
        pytest.param("True", 60, id="PKM-PMT-TC-008"),
        pytest.param(True, 60.0, id="PKM-PMT-TC-009"),
        pytest.param(True, True, id="PKM-PMT-TC-010"),
        pytest.param(True, None, id="PKM-PMT-TC-011"),
    ],
)
def test_permit_wrong_type_raises_type_error(permit_active, parked_minutes):
    with pytest.raises(TypeError):
        is_permit_valid(permit_active, parked_minutes)
