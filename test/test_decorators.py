import re
from src.decorators import log


def test_empty_log_decorator(capsys):
    @log()
    def func():
        pass

    func()
    captured = capsys.readouterr().out
    assert re.fullmatch(f'func - [2-5] с\\.\n', captured)


def test_log_decorator(capsys):
    @log('Test {} decorator')
    def func():
        pass

    func()
    captured = capsys.readouterr().out
    assert re.fullmatch(f'Test [2-5] decorator\n', captured)
