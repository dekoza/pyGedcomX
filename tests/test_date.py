from gedcomx.date import DateFormat


def test_simple():
    date = DateFormat("+1000")
    assert date.year == 1000
    assert date.month is None
    assert date.to_formal_string() == "+1000"


def test_approximate():
    date = DateFormat("A+1900")
    assert date.is_approximate
    assert date.month is None
    assert date.to_formal_string() == "A+1900"


def test_range():
    date_range = DateFormat("+1900/1910")
    assert date_range.to_formal_string() == "+1900/1910"
    start = date_range.start
    assert start.to_formal_string() == "+1900"
    end = date_range.end
    assert end.to_formal_string() == "+1910"


def test_duration():
    duration = DateFormat("P1Y35D")


def test_recurring():
    recurring = DateFormat("R3/+1900/P1Y")
