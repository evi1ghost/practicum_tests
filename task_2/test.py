import inspect
import pytest


def test_precode_variables_exist(missing_variables):
    """Test if initial precode viriables exist."""
    pluralise = 'переменнyю' if len(missing_variables) <= 1 else 'переменные'
    assert not missing_variables, (
        f'Пожалуйста, используйте {pluralise} {", ".join(missing_variables)} '
        'из прекода.'
    )


def test_contact_init_not_changed(precode):
    """Test if the __init__ method of the Contact class has changed."""
    contact_parameters = set(
        inspect.signature(precode.Contact).parameters.keys()
    )
    expected_parameters = {'name', 'phone', 'birthday', 'address'}
    assert not expected_parameters.difference(contact_parameters), (
        'Метод __init__ класса Contact должен принимать на вход следующие '
        f'параметры: self, {", ".join(expected_parameters)}.'
    )


def test_contact_has_show_contact(precode):
    """Test if Contact class has show_contact method."""
    assert 'show_contact' in precode.Contact.__dict__, (
        'Необходимо реализовать метод show_contact().'
    )


def test_show_contact_is_used(not_called):
    """Test if show_contact method is used for 'mike' and 'vlad' objects."""
    pluralise = 'объекта' if len(not_called) <= 1 else 'объектов'
    assert not not_called, (
        f'Вызовите метод show_contact для {pluralise} '
        f'{", ".join(not_called)}.'
    )


def test_print_contact_is_deleted(precode):
    """Test if print_contact function was deleted."""
    assert 'print_contact' not in precode.__dict__, (
        'Удалите из кода функцию print_contact().'
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
