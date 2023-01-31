from SublimeLinter.lint import PythonLinter


class ruff(PythonLinter):
    cmd = ('ruff', '-')
    regex = (
        r'^(?P<filename>.+?):(?P<line>\d+):(?P<col>\d+): '
        r'(?P<code>.+?) (?P<message>.+)$'
    )
    multiline = False
    defaults = {
        'selector': 'source.python'
    }
