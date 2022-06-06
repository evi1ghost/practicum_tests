import pytest


def test_precode_variables_exist(missing_variables):
    """Test if initial precode viriables exist."""
    pluralise = 'переменнyю' if len(missing_variables) <= 1 else 'переменные'
    assert not missing_variables, (
        f'Пожалуйста, используйте {pluralise} {", ".join(missing_variables)} '
        'из прекода.'
    )


def test_expected_imports_exist(missing_imports):
    """Test if expected modules were imported."""
    pluralise = 'модуль' if len(missing_imports) <= 1 else 'модули'
    assert not missing_imports, (
        f'Пожалуйста, импортируйте {pluralise} {", ".join(missing_imports)}.'
    )


def test_stdout(expected_output, student_output):
    """Test if student's output equal to expected."""
    if student_output:
        student_lines = student_output.strip().split('\n')
        expected_lines = expected_output.strip().split('\n')
        if len(expected_lines) == len(student_lines):
            for line_num, (expected_line, student_line) in enumerate(
                zip(expected_lines, student_lines), 1
            ):
                assert expected_line == student_line, (
                    'Результат не соответствует ожидаемому.\n'
                    f'Проверьте {line_num} строку результата '
                    'выполнения кода. Она должная выглядеть '
                    'следующим образом:\n'
                    f'{expected_line}'
                )
    assert expected_output == student_output, (
        'Результат не соответствует ожидаемому:\n'
        f'Ваш вывод:\n {student_output}\n'
        f'Ожидаемый вывод:\n {expected_output}'
    )
