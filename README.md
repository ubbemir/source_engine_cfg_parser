# Source Engine CFG Parser
A parser and formatter for the config files (.cfg) of your beloved source engine games. The parser takes comments and variable amount of whitespaces into account.

# Requirements
Python 3.2 and the python library *lark*.\
Install with `pip install lark`

# Example Usage:
Format *input.cfg* file to an easily readable format:
`python main.py input.cfg`

Format *input.cfg* file to a one line command:
`python main.py input.cfg -m`
