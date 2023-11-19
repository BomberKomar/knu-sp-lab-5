from pptree import Node, print_tree

from yacc_lex import parser
from accomplisher import Accomplisher

def build_pptree(ast, parent_node = None):
    if ast[0] == 'grouped':
        node = Node('()', parent_node)
        build_pptree(ast[1], node)
        return node
    elif ast[0] == 'binop':
        node = Node(ast[1], parent_node)
        build_pptree(ast[2], node)
        build_pptree(ast[3], node)
        return node
    elif ast[0] == 'unary':
        node = Node(ast[1], parent_node)
        build_pptree(ast[2], node)
        return node
    else:
        return Node(ast[1], parent_node)

expression_string = input('Enter your mathematical expression: ')

ast = parser.parse(expression_string)
accomplisher = Accomplisher(ast)

print('Result: ', accomplisher.accomplish()[1])
print('AST visual representation: ')
print_tree(build_pptree(ast))
