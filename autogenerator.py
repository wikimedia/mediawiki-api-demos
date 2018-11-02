#!/usr/bin/python3

"""
    autogenerator.py

    MediaWiki Action API Code Samples
    Generates python files for all demos of MediaWiki API supported
    actions that support GET Requests only and can be easily built
    from a JSON Schema.

    MIT License
"""
import pathlib
import json

class CodeGeneratorBackend:
    """ A python code generator backend. Code borrowed from
    http://effbot.org/zone/python-code-generator.htm """

    def __init__(self, tab="\t"):
        """ Declare variables """
        self.code = []
        self.tab = tab
        self.level = 0

    def end(self):
        """ Get the complete code string """
        return "".join(self.code)

    def write(self, string):
        """ Append code line to a string """
        self.code.append(self.tab * self.level + string)

    def indent(self):
        """ Indent a line of code """
        self.level = self.level + 1

    def dedent(self):
        """ Dedent a line of code """
        self.level = self.level - 1

def make_file():
    """ Generate a file... """
    code = CodeGeneratorBackend(tab="    ")

    file = open('modules.json', 'r')
    modules = json.load(file)
    file.close()

    for module in modules:
        file = pathlib.Path(module['filename'])

        if file.exists():
            print('`' + module['filename'] + "`: already exists, cannot re-write!")
        else:
            code.code = []
            code.write('#This file is partly auto-generated\n\n')
            code.write('#!/usr/bin/python3\n\n')
            code.write('"""\n')
            code.indent()
            code.write(module['filename'] + '\n\n')
            code.write('MediaWiki Action API Code Samples\n')
            code.write(module['docstring'] + '\n\n')
            code.write('MIT License\n')
            code.dedent()
            code.write('"""\n\n')
            code.write('import requests\n\n')
            code.write('S = requests.Session()\n\n')
            code.write('URL = "' + module['endpoint'] + '"\n\n')
            code.write('PARAMS = {\n')
            code.indent()

            for i, param in enumerate(module['params']):
                param_str = '"' + param + '": "' + module['params'][param]
                if i < (len(module['params'])-1):
                    code.write(param_str + '",\n')
                else:
                    code.write(param_str + '"\n')

            code.dedent()
            code.write('}\n\n')
            code.write('R = S.get(url=URL, params=PARAMS)\n')
            code.write('DATA = R.json()\n\n')
            code.write('print(DATA)\n')

            file = open(module['filename'], 'w')
            file.write(code.end())
            file.close()

            print('`' + module['filename'] + "`: generated")

if __name__ == '__main__':
    make_file()
