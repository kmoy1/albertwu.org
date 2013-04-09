from template.utils import make_list, contents_li, \
        make_concept_question, make_print_question, make_env_question,\
        make_concept_solution, make_print_solution, make_env_solution,\
        make_code_solution, \
        make_question_section, make_solution_section

#---------#
# CONTENT #
#---------#

title = 'Orders of Growth'
level = 'basic'

references = [
    'Lecture: Recursive Data and Orders of Growth',
]

notes = ''

contents = [
        {'name': 'Conceptual',
         'id': 'conceptual',
         'maker q': make_concept_question,
         'maker s': make_concept_solution,
         'questions': lambda: concept_questions},
]

concept_questions = [
    {'description': """What is the time complexity of this function in big-Theta (&theta;) notation?""",
     'code': """
def one(n):
    for a in range(n):
        for b in range(n/2):
            for c in range(n/4):
                print(a + b + c)""",
    'solution': '&theta;(n<sup>3</sup>)'
    },
    {'description': """What is the time complexity of this function in big-Theta (&theta;) notation?""",
     'code': """
def two(n):
    for a in range(n):
        for b in range(1000000000):
            for c in range(n):
                print(a + b + c)""",
    'solution': '&theta;(n<sup>2</sup>)'
    },
    {'description': """What is the time complexity of this function in big-Theta (&theta;) notation?""",
     'code': """
def three(n):
    while n &gt; 1:
        result = n * n
        print(result)
        n = n / 10
    return False""",
    'solution': '&theta;(log<i>n</i>)'
    },
    {'description': """What is the time complexity of this function in big-Theta (&theta;) notation?""",
     'code': """
def four(lst):
    if len(lst) &lt; 12345:
        return lst[0]
    return four(lst[1:])""",
    'solution': '&theta;(n), where <i>n</i> is the length of the list.'
    },
    {'description': """What is the time complexity of this function in big-Theta (&theta;) notation?""",
     'code': """
def five(n):
    def helper(x):
        return x + n
    return helper(n/2)""",
    'solution': '&theta;(1)',
    },
    {'description': """What is the time complexity of this function in big-Theta (&theta;) notation?""",
     'code': """
def reverse(lst):
    if not lst:
        return []
    result = reverse(lst[1:])
    result.append(lst[0])
    return result""",
    'solution': '&theta;(n), where <i>n</i> is the size of the list.',
    },
]

#-------------------#
# COMPILING STRINGS #
#-------------------#

attrs = globals()
