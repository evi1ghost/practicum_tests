"""
Фикстуры get_precod_and_capture_stdout, precode, student_output,
созданы в качестве локальной имплементации тестовой платформы.
"""
import sys
from io import StringIO

import pytest


@pytest.fixture(scope='session')
def get_precod_and_capture_stdout():
    """
    Capture stdout from precode and return tuple (precode, stdout).

    Pytest capsys can't be used with session scope and doesn't work
    properly in current case.
    """
    _stdout = sys.stdout
    sys.stdout = _stringio = StringIO()
    import precode # noqa
    output = _stringio.getvalue()
    sys.stdout = _stdout
    return (precode, output)


@pytest.fixture
def precode(get_precod_and_capture_stdout):
    """Return precode module."""
    return get_precod_and_capture_stdout[0]


@pytest.fixture
def student_output(get_precod_and_capture_stdout):
    """Return stdout of student code."""
    return get_precod_and_capture_stdout[1]


@pytest.fixture
def expected_output(capsys):
    """Return string with stdout of author solution."""
    import author # noqa
    return capsys.readouterr().out


@pytest.fixture
def missing_variables(precode):
    """Return list of items which were deleted from precode."""
    expected_variables = ('make_divider_of', 'div2', 'div5')
    missing_variables = []
    for var in expected_variables:
        if var not in precode.__dict__:
            missing_variables.append(var)
    return missing_variables
