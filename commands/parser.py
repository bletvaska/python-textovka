def parse(line: str, context: dict) -> tuple:
    for cmd in context['commands']:
        for alias in cmd['aliases'] + (cmd['name'],):
            if line.startswith(alias):
                param = line.split(alias)[1].strip()
                return cmd, param

    return (None, None)
