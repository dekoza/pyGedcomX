import pytest

from gedcomx.date import DateFormat

# Let's test that no example from original specs throws an error.
# https://github.com/FamilySearch/gedcomx/blob/master/specifications/date-format-specification.md


@pytest.mark.parametrize(
    "value",
    [
        "+1752-01-18T22:14:3Z",  # this is the example that does not follow own specs!
        "+1964-11-14T10-07:00",
        "+1889-05-17T14:23",
        "+1492-07-27",
        "+0186-03",
        "-1321",
    ],
)
def test_parse_simple_date(value):
    assert DateFormat.validate(value)


@pytest.mark.parametrize(
    "value",
    [
        # These needed to be prepended with minimal simple date
        # because doesn't allow duration being alone.
        "+1964/P17Y6M2D",
        "+1964/P186D",
        "+1964/PT5H17M",
        "+1964/P1000Y18M72DT56H10M1S",
    ],
)
def test_parse_duration(value):
    assert DateFormat.validate(value)


@pytest.mark.parametrize(
    "value",
    [
        "+1752/+1823",
        "+1825-04-13/+1825-11-26",
        "+1933-02-19/P74Y",
    ],
)
def test_closed_date_range(value):
    assert DateFormat.validate(value)


@pytest.mark.parametrize(
    "value",
    [
        "/+1887-03",
        "+1976-07-11/",
        "/-1287",
        "/+0000",
        "-0001-04/",
    ],
)
def test_open_date_range(value):
    assert DateFormat.validate(value)


@pytest.mark.parametrize(
    "value",
    [
        "R4/+1776-04-02/+1776-04-09",
        "R/+2000/P12Y",
        "R100/+1830/+1840",
    ],
)
def test_recurring(value):
    assert DateFormat.validate(value)


@pytest.mark.parametrize(
    "value",
    [
        "A+1680",
        "A-1400",
        "A+1980-05-18T18:53Z",
        "A+2014-08-19",
    ],
)
def test_approx_date(value):
    assert DateFormat.validate(value)


@pytest.mark.parametrize(
    "value",
    [
        "A+1752/+1823",
        "A+1825-04-13/+1825-11-26",
        "A+1633-02-19/P74Y",
        "A/+1887-03",
        "A+1976-07-11/",
        "A/-1287",
        "A/+0000",
        "A-0001-04/",
    ],
)
def test_approx_date_range(value):
    assert DateFormat.validate(value)
