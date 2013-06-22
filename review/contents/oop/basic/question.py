from utils import utils
from review.utils.utils import *

#---------#
# CONTENT #
#---------#

title = 'OOP'
level = 'basic'

references = [
        'Lecture: Object-Oriented Programming',
        'Lecture: Inheritance',
        'Discussion 7',
]

notes = ''

contents = [
        {'name': 'Variables: Conceptual',
         'id': 'var-conceptual',
         'maker': make_concept_question,
         'questions': lambda: var_concept_questions},
        {'name': 'Variables: What would Python print?',
         'id': 'var-print',
         'maker': make_print_question,
         'questions': lambda: var_print_questions},
        {'name': 'Methods: Conceptual',
         'id': 'method-conceptual',
         'maker': make_concept_question,
         'questions': lambda: meth_concept_questions},
        {'name': 'Methods: What would Python print?',
         'id': 'meth-print',
         'maker': make_print_question,
         'questions': lambda: meth_print_questions},
]

var_concept_questions = [
    {'description': """Define each of the following terms:""" + \
            ol(contents=(
                'Local variable',
                'Instance variable',
                'Class variable',
            )),
        'solution': ol(contents=(
            'Local variable: a variable that is only visible within the scope of a method. Once the method finishes executing, the local variable is erased.',
            'Instance variable: a variable that persists -- even after methods are done executing, these variables will still exist and retain their value.' + ul(contents=(
                '<b>Tip</b>: you can tell a variable is an instance variable if it has <tt>self.</tt> in front of it (e.g. <tt>self.name</tt>). Instance variable',
                'Instance variables can only be used within methods.',
                'Instance variables are unique to each instance of the class. They are not shared by instances.'
                )),
            'Class variable: like instance variables, class variables also persist. However, class variables ARE shared by all instances of the class.' + ul(contents=(
                'When initialized outside of methods (which is usually the case), the class variable has no "dot" modifier (e.g. just <tt>num_of_accounts</tt>',
                'When referenced in methods, the class variable must be referenced with the following syntax: <tt>class_name.variable</tt> (e.g. <tt>Account.num_of_accounts)</tt>',
                ))
            ))
    },
    {'description': """For the following code, determine whether each of these variables are local, instance, or class variables:""" + \
    ul(contents=list(map(lambda x: code(x, classes='prettyprint'), (
                'name',
                'self.name',
                'balance',
                'self.balance',
                'interest',
                'amt',
                'total',
            )))),
        'code': """
class Account:
    interest = 0.02
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        total = self.balance + amt
        self.balance = total""",

        'solution': ul(contents=(
            code('name', classes='prettyprint') + ': local',
            code('self.name', classes='prettyprint') + ': instance',
            code('balance', classes='prettyprint') + ': local',
            code('self.balance', classes='prettyprint') + ': instance',
            code('interest', classes='prettyprint') + ': class',
            code('amt', classes='prettyprint') + ': local',
            code('total', classes='prettyprint') + ': local',
        )),
    },
    {'description': """For the code following code, let's say we want
to have a variable that keeps track of all the Person
objects ever created.""" + ul(contents=(
    'What type of variable should this be? (local, instance, or class)',
    'Modify the code to initialize <tt>population</tt> to 0, and to increment it by 1 every time you create a new Person object.',
    )),
        'code': """
class Person:
    def __init__(self, name):
        self.name = name""",

        'solution': ul(contents=(
    'Class Variable',
    'New code:' + pre("""
class Person:
    <b>population = 0</b>
    def __init__(self, name):
        self.name = name
        <b>Person.population += 1</b>""",
        classes='prettyprint'),
        )),
    },
]

var_print_questions = [
    {'description': """For the following questions, use the following
    class definition:""" + pre("""
class Account:
    \"\"\"A class computer account. Each account has a two-letter ID
    and the name of the student who is registered to the account.
    \"\"\"
    num_of_accounts = 0
    def __init__(self, id):
        self.id = id
        Account.num_of_accounts += 1

    def register(self, student):
        self.student = student
        print('Registered!')

    @property
    def type(self):
        return type(self)""", classes='prettyprint'),

    'prompts': [
            ('self.id', 'NameError'),
            ('acc_aa = Account("aa")',),
            ('acc_aa.id', "'aa'"),
            ('acc_aa.student', "AttributeError (self.student not defined yet)"),
            ('acc_aa.register("Peter Perfect")', 'Registered!'),
            ('acc_aa.student', "'Peter Perfect'"),
            ('num_of_accounts', "NameError"),
            ('Account.num_of_accounts', "1"),
            ('acc_aa.num_of_accounts', "1"),
            ('acc_zz = Account("zz")',),
            ('Account.num_of_accounts', "2"),
            ('acc_aa.num_of_accounts', "2"),
            ('acc_zz.num_of_accounts', "2"),
            ('acc_aa.num_of_accounts = 100',),
            ('acc_aa.num_of_accounts', "100"),
            ('acc_zz.num_of_accounts', "2"),
            ('Account.num_of_accounts', "2"),
            ('Account.num_of_accounts = 9001',),
            ('acc_aa.num_of_accounts', "100"),
            ('acc_zz.num_of_accounts', "9001"),
        ]},
]

meth_concept_questions = [
    {'description': """Consider the <tt>Account</tt> class defined
    <a href='#var-print'>above</a>. Why is it that, when I call
    <tt>acc_aa.register('me')</tt> no errors will be raised, even
    though I didn't pass in an argument for <tt>self</tt>?""",

    'solution': """The dot notation will implicitly pass
    <tt>acc_aa</tt> into <tt>type</tt> as <tt>self</tt>. This is
    known as a <b>bound method</b>. Another way to think about it
    is that <tt>acc_aa.register</tt> acts like a curried function:
    """ + pre("""
>>> acc_aa.register = curry2(Account.register)(acc_aa)
>>> acc_aa.register('me')
Registered!""", classes='prettyprint'),
    },

    {'description': """Can a method have the same name as a
    variable?""",
    'solution': """No; in python, variables and methods share the same
    namespace, so variable and method names can collide if you aren't
    careful."""
    },

    {'description': """What does the
    <code class='prettyprint'>@property</code> decorator do?""",
    'solution': """The <code class='prettyprint'>@property</code>
    decorator allows you to use the affected method to be accessed
    like a variable. For example, the following method""" + pre("""
class Example:
    @property
    def foo(self):
        return 3""", classes='prettyprint') + """can be accessed like
        this:""" + pre("""
>>> a = Example()
>>> a.foo
3""", classes='prettyprint'),
    },
]

meth_print_questions = [
    {'description': """For the following questions, use the
    <tt>Account</tt> class defined <a href='#var-print'>above</a>.""",
    'prompts': [
        ('acc_aa = Account("aa")',),
        ('acc_aa.register', '<bound method Account.register ...>'),
        ('Account.register', '<function register at ...> # (not a bound method!)'),
        ('acc_aa.register(self, "Peter Perfect")', 'TypeError'),
        ('acc_aa.register("Peter Perfect")', 'Registered!'),
        ('acc_aa.type()', 'TypeError'),
        ('acc_aa.type', "<class '__main__.Account'>"),
        ('acc_aa.type = "Nothing"', 'AttributeError'),
    ]},
]


#-------------------#
# COMPILING STRINGS #
#-------------------#

questions = '\n'.join(map(make_question_section, contents))

attrs = globals()

