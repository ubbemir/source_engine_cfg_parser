from lark import Lark, Transformer, v_args
import formatters

with open("source_cfg.lark", "r") as file:
    cfg_grammar = file.read()

cfg_parser = Lark(cfg_grammar, parser='earley')


with open("input2.cfg", "r") as file:
    cfg_input = file.read()


parse_tree = cfg_parser.parse(cfg_input)

print(formatters.prettify_cfg(parse_tree))