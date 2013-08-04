#-------------------#
# Utility functions #
#-------------------#

def make_id_class(kargs):
    """Makes the id and class attributes of a tag, if they are present
    in KARGS.

    KARGS -- a dictionary. It may or may not contain keys 'id' and/or
             'class'

    >>> make_id_class({'id': ['hi', 'bom'], 'class': 'boink'})
    ' id="hi bom" class="boink"'
    >>> make_id_class({})
    ''
    """
    if 'ids' not in kargs:
        ids = ''
    elif type(kargs['ids']) == str:
        ids = ' id="' + kargs['ids'].strip() + '"'
    else:
        ids = ' id="' + ' '.join(kargs['ids']) + '"'

    if 'classes' not in kargs:
        classes = ''
    elif type(kargs['classes']) == str:
        classes = ' class="' + kargs['classes'].strip() + '"'
    else:
        classes = ' class="' + ' '.join(kargs['classes']) + '"'
    return ids + classes


def a(href, contents, internal=True, **kargs):
    """Makes an <a> tag"""
    ids = make_id_class(kargs)
    if internal:
        href = '#' + href
    return '<a{} href="{}">{}</a>'.format(ids, href, contents)

def b(contents, **kargs):
    ids = make_id_class(kargs)
    return '<b{}>{}</b>'.format(ids, contents)

def h(num, title, **kargs):
    """Makes a header tag"""
    ids = make_id_class(kargs)
    return '<h{0}{1}>{2}</h{0}>\n'.format(num, ids, title)

def code(contents, **kargs):
    ids = make_id_class(kargs)
    return '<code{}>{}</code>'.format(ids, contents)

def div(contents, **kargs):
    ids = make_id_class(kargs)
    return '<div{}>{}</div>'.format(ids, contents)

def li(item, **kargs):
    ids = make_id_class(kargs)
    return '<li{}>{}</li>'.format(ids, item)

def ol(contents, **kargs):
    ids = make_id_class(kargs)
    result = '<ol{}>\n'.format(ids)
    for li in contents:
        result += '  <li>{}</li>\n'.format(li)
    return result + '</ol>'

def p(contents, **kargs):
    """Makes a <p> tag"""
    ids = make_id_class(kargs)
    return '<p{}>{}</p>\n'.format(ids, contents)

def pre(code, **kargs):
    """Makes a <pre> tag"""
    ids = make_id_class(kargs)
    return '<pre{}>{}</pre>\n'.format(ids, code)

def span(contents, **kargs):
    ids = make_id_class(kargs)
    return '<span{}>{}</span>'.format(ids, contents)

def table(contents, headers=None, **kargs):
    ids = make_id_class(kargs)
    width = max(map(len, contents))
    result = '<table{}>\n'.format(ids)
    if headers:
        result += '  <tr>\n'
        for cell in headers:
            result += '    <th>{}</th>\n'.format(cell)
        result += '  </tr>\n'
    for content in contents:
        result += '  <tr>\n'
        for cell in content:
            result += '    <td>{}</td>\n'.format(cell)
        result += '  </tr>\n'
    return result + '</table>'

def tt(contents, **kargs):
    ids = make_id_class(kargs)
    return '<tt{}>{}</tt>'.format(ids, contents)

def ul(contents, **kargs):
    ids = make_id_class(kargs)
    result = '<ul{}>\n'.format(ids)
    for li in contents:
        result += '  <li>{}</li>\n'.format(li)
    return result + '</ul>'

#####################
# Multi-Level Lists #
#####################

def insert_into_table(table, level, name, html_id=None, base_level=2):
    """Inserts a header name and its HTML id into TABLE.

    PARAMTERS:
    table      -- the table to modify (e.g. table of contents)
    level      -- the HTML header level (1 to 6)
    html_id    -- the header's id tag
    name       -- the contents of the header
    base_level -- what level should be the outer-most bullet point
                  level

    >>> table = []
    >>> insert_into_table(table, 2, 'test', 'Test')
    >>> table
    [('Test', 'test')]
    >>> insert_into_table(table, 2, 'foo', 'Foo')
    >>> table
    [('Test', 'test'), ('Foo', 'foo')]
    >>> insert_into_table(table, 3, 'bar', 'Bar')
    >>> table
    [('Test', 'test'), ('Foo', 'foo'), [('Bar', 'bar')]]
    >>> insert_into_table(table, 2, 'bop', 'Bop')
    >>> table
    [('Test', 'test'), ('Foo', 'foo'), [('Bar', 'bar')], ('Bop', 'bop')]
    """
    slot = table
    while level > base_level:
        if not slot or type(slot[-1]) != list:
            slot.append([])
        slot = slot[-1]
        level -= 1
    if html_id:
        slot.append((name, html_id))
    else:
        slot.append((name,))

def table_to_html(table, list_type='ul'):
    """Converts a table generated by insert_into_table into an HTML
    unordered list. Recursively deals with nested lists."""
    contents = '<{}>'.format(list_type)
    for elem in table:
        if type(elem) == tuple:
            assert 1 <= len(elem) <= 3, 'Invalid entry {}'.format(elem)
            if len(elem) == 3:
                name, html_id, internal = elem
                contents += li(a(html_id, name, internal))
            elif len(elem) == 2:
                name, html_id = elem
                contents += li(a(html_id, name))
            elif len(elem) == 1:
                name = elem[0]
                contents += li(name)
        elif type(elem) == list:
            contents += table_to_html(elem)
    contents += '</{}>'.format(list_type)
    return contents
