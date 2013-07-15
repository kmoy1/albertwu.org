from utils import utils

exam = 'Midterm 2'

contents = [
    ('Dictionaries', 'dictionaries'),
    ('Map, filter, and friends', 'functions'),
    ('Identity vs. Equality', 'identity'),
    ('Nonlocal', 'nonlocal'),
    ('OOP', 'oop'),
]

notes = ''

contents = utils.table(
    ids = 'topics',
    classes='highlight',
    headers=('Topic', 'Basic', 'Exam'),
    contents=list(map(
        lambda x: (
            x[0],
            utils.a(x[1] + '/basic/question.html', 'Questions',
                internal=False),
            utils.a(x[1] + '/exam/question.html', 'Questions',
                internal=False)
        ), contents))
)


attrs = globals()
