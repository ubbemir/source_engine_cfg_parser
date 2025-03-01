# Source Engine CFG Parser
A parser and formatter for the config files (.cfg) of your beloved source engine games. The parser takes comments and variable amount of whitespaces into account.

# Requirements
Python 3.2 and the python library *lark*.\
Install with `pip install lark`

# Example Usage:
Make sure your current working directory is in the project root.

Format *input.cfg* file to an easily readable format:
`python -m src.main input.cfg`

Format *input.cfg* file to a one line command:
`python -m src.main input.cfg -m`

Run tests with:
`python -m unittest discover tests`