import pytest
from io import StringIO
import sys
from script_tools.handlers.input_handler import InputHandler


# A fixture to initialize an InputHandler instance
@pytest.fixture
def init_handler():
    return InputHandler({
        'menu_options': {
            'validator': InputHandler._is_option,
            'actions': {
                '1': lambda: print("Option 1 selected!"),
                '2': lambda: print("Option 2 selected!")
            },
            'error_message': 'Please select a valid option or hit Enter to exit.'
        }
    })


def test_handler_initialization(init_handler):
    assert isinstance(init_handler, InputHandler)
    assert 'menu_options' in init_handler.input_map


def test_is_option_valid(init_handler):
    input_details = init_handler.input_map['menu_options']
    assert InputHandler._is_option('1', input_details)
    assert InputHandler._is_option('2', input_details)


def test_is_option_invalid(init_handler):
    input_details = init_handler.input_map['menu_options']
    assert not InputHandler._is_option('3', input_details)
    assert not InputHandler._is_option('hello', input_details)


def test_handle_input_valid_option_1(monkeypatch, init_handler):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    sys.stdout = StringIO()  # Capture the printed output
    init_handler.handle_input('menu_options', 'Choose an option (1-2): ')
    output = sys.stdout.getvalue().strip()
    sys.stdout = sys.__stdout__  # Reset stdout
    assert output == "Option 1 selected!"


def test_handle_input_valid_option_2(monkeypatch, init_handler):
    monkeypatch.setattr('builtins.input', lambda _: '2')
    sys.stdout = StringIO()
    init_handler.handle_input('menu_options', 'Choose an option (1-2): ')
    output = sys.stdout.getvalue().strip()
    sys.stdout = sys.__stdout__
    assert output == "Option 2 selected!"


def mock_input_sequence(*args):
    """Generator to simulate multiple successive user inputs."""
    for item in args:
        yield item


def test_handle_input_invalid(monkeypatch, init_handler):
    mock_inputs = mock_input_sequence('3', '1')  # first input is invalid, second is valid
    monkeypatch.setattr('builtins.input', lambda _: next(mock_inputs))

    sys.stdout = StringIO()
    init_handler.handle_input('menu_options', 'Choose an option (1-2): ')
    output = sys.stdout.getvalue().strip().split('\n')
    sys.stdout = sys.__stdout__

    assert "Please select a valid option or hit Enter to exit." in output[0]
    assert "Option 1 selected!" in output[1]


def test_handle_input_exit(monkeypatch, init_handler):
    monkeypatch.setattr('builtins.input', lambda _: '')
    sys.stdout = StringIO()
    init_handler.handle_input('menu_options', 'Choose an option (1-2): ')
    output = sys.stdout.getvalue().strip()
    sys.stdout = sys.__stdout__
    assert output == "Console exit condition triggered."
