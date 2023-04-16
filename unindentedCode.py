import ast

__author__ = 'Gabriel Mendes'
__repo__ = 'https://github.com/Gabrielm3/PyJSTranspiler'


def transpile_expr(node):
    if isinstance(node, ast.Num):
        return str(node.n)
    elif isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.BinOp):
        left = transpile_expr(node.left)
        right = transpile_expr(node.right)
        op = transpile_expr(node.op)
        return f"({left} {op} {right})"
    elif isinstance(node, ast.Add):
        return "+"
    elif isinstance(node, ast.Sub):
        return "-"
    elif isinstance(node, ast.Call):
        func = transpile_expr(node.func)
        args = ", ".join(transpile_expr(arg) for arg in node.args)
        return f"{func}({args})"
    elif isinstance(node, ast.JoinedStr):
        values = [transpile_expr(val) for val in node.values]
        return f"`{''.join(values)}`"
    elif isinstance(node, ast.Constant):
        if isinstance(node.value, str):
            return f'"{node.value}"'
        else:
            raise NotImplementedError(
                f"Unhandled constant type: {type(node.value)}")
    elif isinstance(node, ast.FormattedValue):
        value = transpile_expr(node.value)
        return f"${{{value}}}"
    elif isinstance(node, ast.List):
        elements = [transpile_expr(el) for el in node.elts]
        return f"[{', '.join(elements)}]"
    else:
        raise NotImplementedError(
            f"Não foi implementado o suporte para o nó {type(node)}") # exit


def transpile_stmt(node):
    if isinstance(node, ast.Assign):
        target = transpile_expr(node.targets[0])
        value = transpile_expr(node.value)
        return f"let {target} = {value};"
    elif isinstance(node, ast.Expr):
        value = transpile_expr(node.value)
        return f"{value};"
    elif isinstance(node, ast.FunctionDef):
        name = node.name
        args = ", ".join(arg.arg for arg in node.args.args)
        body = "\n".join(transpile_stmt(stmt) for stmt in node.body)
        return f"function {name}({args}) {{\n{body}\n}}"
    elif isinstance(node, ast.For):
        target = transpile_expr(node.target)
        iter_ = transpile_expr(node.iter)
        body = "\n".join(transpile_stmt(stmt) for stmt in node.body)
        return f"for (let {target} of {iter_}) {{\n{body}\n}}"
    else:
        raise NotImplementedError(
            f"Não foi implementado o suporte para o nó {type(node)}") # exit


def transpile(code):
    tree = ast.parse(code)
    output = []

    for node in tree.body:
        output.append(transpile_stmt(node))

    return "\n".join(output)

python_code = """
def greet(name):
   print(f"Hello, {name}!")

names = ["Alice", "Bob", "Charlie"]

for name in names:
   greet(name)
"""

js_code = transpile(python_code)

with open("output.js", "w") as output_file:
    output_file.write(js_code)

print("Código gerado em output.js")
# [Código não Indentado]
