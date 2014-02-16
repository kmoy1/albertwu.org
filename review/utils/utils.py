from utils.utils import *
from urllib.parse import quote_plus
from cgi import escape

#-------------------#
# Utility functions #
#-------------------#

PROMPT='>>> '

def has_keys(keys, d):
    if type(keys) != list:
        keys = [keys]
    for key in keys:
        assert key in d, 'No key {}'.format(key)

def contents_li(contents):
    has_keys(['name', 'id'], contents)
    name, hash_id = contents['name'], contents['id']
    return a(hash_id, name)

def make_section(sec, maker):
    if 'notes' in sec:
        notes = p(sec['notes']())
    else:
        notes = ''
    maker, questions = sec[maker], sec['questions']()
    q_id = sec['id']
    assert callable(maker), 'Not a valid maker'
    assert type(questions) == list, 'Not a valid question list'
    section = h(2, sec['name'], ids=sec['id'],
                classes=['subtopic', 'anchor'])
    section += notes
    for i, question in enumerate(questions):
        section += maker(i+1, question, q_id) + '\n'
    return section

def make_question_section(sec):
    return make_section(sec, 'maker')

def make_section_dropdown(sec):
    name, questions = sec['name'], sec['questions']()
    q_id = sec['id']
    assert type(questions) == list, 'Not a valid question list'
    menu = h(3, name)
    links = [a(q_id + str(i+1), 'Q{}'.format(i+1))
             for i in range(len(questions))]
    menu += div(ul(links))
    return menu

def make_reference_link(link):
    if type(link) in (tuple, list):
        return a(link[1], link[0], internal=False)
    return link


#--------------------#
# QUESTION COMPILERS #
#--------------------#


def toggle_button(tag):
    return "<button id='{}' class='toggleButton'>Toggle Solution<noscript> (enable JavaScript)</noscript></button>".format(tag)

def make_counter():
    i = 0
    def counter():
        nonlocal i
        result = i
        i += 1
        return result
    return counter

counter = make_counter()

def make_concept_question(num, question, q_id):
    has_keys(['description', 'solution'], question)
    text = h(3, 'Q' + str(num), ids=q_id + str(num),
             classes=['question', 'anchor'])
    text += p(question['description'])
    if 'code' in question:
        text += prettify(escape(question['code'].strip('\n')))
    if 'hint' in question:
        text += p(b('Hint') + ': ' + question['hint'], classes='hint')

    tag = '{}'.format(counter())
    text += toggle_button(tag)
    solution = p(b('Answer: ') + question['solution'])
    if 'explanation' in question:
        solution += p(b('Explanation: ') + question['explanation'])
    text += div(solution, classes=['solution', tag])
    return text

def make_code_question(num, question, q_id):
    has_keys(['description', 'solution'], question)
    text = h(3, 'Q' + str(num), ids=q_id + str(num),
             classes=['question', 'anchor'])
    text += p(question['description'])
    if 'code' in question:
        text += prettify(escape(question['code'].strip('\n')))
    if 'hint' in question:
        text += p(b('Hint') + ': ' + question['hint'], classes='hint')

    tag = '{}'.format(counter())
    text += toggle_button(tag)
    solution = prettify(escape(question['solution'].strip('\n')))
    if 'explanation' in question:
        solution += p(b('Explanation: ') + question['explanation'])
    text += div(solution, classes=['solution', tag])
    return text

def make_print_question(num, question, q_id):
    has_keys('prompts', question)
    prompts = question['prompts']
    text = h(3, 'Q' + str(num), ids=q_id + str(num),
             classes=['question', 'anchor'])
    if 'description' in question:
        text += p(question['description'])
    symbol = question.get('symbol', PROMPT)

    tag = '{}'.format(counter())
    prints = []
    for line in prompts:
        prints.append(escape(symbol + line[0]))
        if len(line) == 2:
            prints.append(span('______', classes='blank'+tag) + \
                          span(escape(line[1]),
                               classes=['hidden', 'solution', tag]))
    text += prettify('\n'.join(prints))
    text += toggle_button(tag)
    return text

def make_env_question(num, question, q_id):
    has_keys('code', question)
    text = h(3, 'Q' + str(num), ids=q_id + str(num),
             classes=['question', 'anchor'])
    text += prettify(escape(question['code']))

    # tutor_url = 'http://www.pythontutor.com/visualize.html'
    tutor_url = 'http://www.pythontutor.com/iframe-embed.html'
    # tutor_url = 'http://tutor.composingprograms.com/visualize.html'
    param = '#mode=display&cumulative=true&py=3&code='
    param += quote_plus(question['code'])
    iframe = '<iframe width="900" height="500" frameborder="0" src="{}"></iframe>'.format(tutor_url + param)

    tag = '{}'.format(counter())
    text += toggle_button(tag)
    # text += div(p(a(tutor_url + param, 'Link to Online Python Tutor', internal=False)),
            # classes=['solution', tag])
    text += div(p(iframe),
            classes=['solution', tag])
    return text

def make_eval_print_question(num, question, q_id):
    has_keys('prompts', question)
    prompts = question['prompts']
    text = h(3, 'Q' + str(num), ids=q_id + str(num),
             classes=['question', 'anchor'])
    text += p("""Determine what each of the following expressions will
    evaluate to, as well as what would be displayed if each
    expression were entered into the interpreter. Special cases:""")
    text += ul((
        'Function objects: write <b>FUNCTION</b>',
        'Errors: write <b>ERROR</b>',
        'Infinite loops: write <b>FOREVER</b>',
        ))
    if 'description' in question:
        text += p(question['description'])

    tag = '{}'.format(counter())
    prints = []
    for line in prompts:
        prints.append((
            prettify(line[0]),
            div(prettify(line[1]),
                 classes=['hidden', 'solution', tag]),
            div(prettify(line[2]),
                 classes=['hidden','solution', tag]),
        ))
    text += table(prints, headers=('', 'Evaluates', 'Displays'),
                  classes='eval-print')
    text += toggle_button(tag)
    return text

