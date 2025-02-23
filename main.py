import argparse

from lark import Lark

import formatters


def main():
    parser = argparse.ArgumentParser(
                    prog="Source Engine CFG Formatter",
                    description="Formats CFG files from source engine games.")

    parser.add_argument("input_file", help="input file to be formatted")
    parser.add_argument("-m", "--minify", help="minify instead of beutify",
                    action="store_true")

    args = parser.parse_args()

    with open("source_cfg.lark", "r") as file:
        cfg_grammar = file.read()
    cfg_parser = Lark(cfg_grammar, parser="earley")


    with open(args.input_file, "r") as file:
        input_content = file.read()

    result = ""
    if args.minify:
        result = formatters.minify_cfg(cfg_parser.parse(input_content))
    else:
        result = formatters.prettify_cfg(cfg_parser.parse(input_content))

    print(result)

if __name__ == "__main__":
    main()
