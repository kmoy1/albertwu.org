import os
import re
# Import various utilities from utils
# import templar.utils.html
# import templar.utils.filters

# Path of the current file -- best not to change this
FILEPATH = os.path.dirname(os.path.abspath(__file__))

configurations = {
    # List of directories in which to search for templates
    'TEMPLATE_DIRS': [
        FILEPATH,
        os.path.join(FILEPATH, 'cs61a'),
        os.path.join(FILEPATH, 'review'),
        os.path.join(FILEPATH, 'notes'),
        os.path.join(FILEPATH, 'blog'),
    ],

    # Variables that can be used in templates
    'VARIABLES': {
        # Add variables here, like the following
        'MASTER_DIR': '',
        'CS61A_DIR': '/cs61a',
        'REVIEW_DIR': '/cs61a/review',
        'NOTES_DIR': '/cs61a/notes',
        'BLOG_DIR': '/blog',
    },

    # Substitutions for the linker
    'SUBSTITUTIONS': [
        # Add substitutinos of the form
        # (regex, sub_function),
        # (regex, sub_function, condition),
    ],

    # Use the following to scrape "headers"
    # TOC_BUILDER should be a subclass of templar.utils.core.TocBuilder
    # 'TOC_BUILDER': templar.utils.htmlHeaderParser,
}