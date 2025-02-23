from lark import Token, Tree


def minify_cfg(tree) -> str:
    final_str = ""
    for statement in tree.children:
        
        if isinstance(statement, Tree):
            for s_child in statement.children:
                if isinstance(s_child, Tree):
                    if s_child.data == "cmd":
                        result = ""
                        for c in s_child.children:
                            if isinstance(c, Token) and c.type == "CVAR":
                                result += c.value
                            elif isinstance(c, Tree):
                                for param in c.children:
                                    result += " " + param.value
                                

                        final_str += result + ";"

    return final_str[:-1]

def prettify_cfg(tree) -> str:
    final_str = ""
    for statement in tree.children:
        
        if isinstance(statement, Tree):
            for s_child in statement.children:
                if isinstance(s_child, Tree):
                    if s_child.data == "cmd":
                        result = ""
                        for c in s_child.children:
                            if isinstance(c, Token) and c.type == "CVAR":
                                result += c.value
                            elif isinstance(c, Tree):
                                for param in c.children:
                                    result += " " + param.value
                                

                        final_str += result + "\n"

    return final_str[:-1]