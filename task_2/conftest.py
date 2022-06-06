"""
Фикстуры get_precod_and_capture_stdout, precode, student_output, user_code
созданы в качестве локальной имплементации тестовой платформы.
"""

import os
import re
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


@pytest.fixture(scope='session')
def user_code():
    """Return precode as a string."""
    test_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(test_dir, 'precode.py'), 'r') as f:
        return f.read()


@pytest.fixture
def expected_output(capsys):
    """Return string with stdout of author solution."""
    import author # noqa
    return capsys.readouterr().out


@pytest.fixture
def missing_variables(precode):
    """Return list of items which were deleted from precode."""
    expected_variables = ('Contact', 'mike', 'vlad')
    missing_variables = []
    for var in expected_variables:
        if var not in precode.__dict__:
            missing_variables.append(var)
    return missing_variables


@pytest.fixture
def not_called(user_code):
    """
    Return list of Contact instance names which show_contact method
    wasn't colled.
    """
    objects_with_pattern = {
        'mike': re.compile(r'^mike.show_contact\(\)'),
        'vlad': re.compile(r'^vlad.show_contact\(\)')
    }
    for line in user_code.split('\n'):
        for key, pattern in objects_with_pattern.items():
            if re.search(pattern, line):
                objects_with_pattern.pop(key)
                break
    return objects_with_pattern.keys()
