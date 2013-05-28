from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'Orders of Growth'
level = 'exam'

references = [
        'Lecture: Recursive Data and Orders of Growth',
]

notes = 'This <a href="http://www-inst.eecs.berkeley.edu/~cs61a/su12/lab/lab04/lab04.php">link</a> (from the summer version of 61A) has some practice problems for orders of growth. Take a look!'

contents = [
        {'name': 'Conceptual',
         'id': 'conceptual',
         'maker q': make_concept_question,
         'maker s': make_concept_solution,
         'questions': lambda: concept_questions},
]

concept_questions = [
        {'description': """Find the time complexity of <tt>main</tt> in big-Theta (&theta;) notation.""",
     'code': """
def helper(x):
    for i in range(x):
        print(i)

def main(n):
    if n == 2:
        return 0
    else:
        return helper(n - 1) + helper(n - 2)""",
    'solution': '&theta;(n)'
    },
        {'description': """Find the time complexity of <tt>bar</tt> in big-Theta (&theta;) notation.""",
     'code': """
def foo(x):
    for i in range(x):
        for j in range(x):
            print(x)

def bar(n):
    while n &gt; 0:
        foo(100000)
        n -= 1""",
    'solution': '&theta;(n)'
    },
        {'description': """Find the time complexity of <tt>funny</tt> in big-Theta (&theta;) notation.""",
     'code': """
def joke(n):
    for i in range(n**2):
        print(i)

def funny(n):
    for i in range(n**2):
        print(joke(100))
    return 'haha'""",
    'solution': '&theta;(n<sup>2</sup>)'
    },
#        {'description': """Find the time complexity of <tt>subsets</tt> in big-Theta (&theta;) notation.""",
#     'code': """
#def subsets(n):
#    if n == 0:
#        return [[]]
#    else:
#        result = subsets(n - 1)
#        for subset in result[:]:
#            result.append([n] + subset)
#        return result""",
#    'solution': '&theta;(2<sup>n</sup>)'
#    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))
solutions = '\n'.join(map(make_solution_section, contents))

attrs = globals()
