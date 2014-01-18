albertwu.org
============

This repo was originally created to generate my TA materials for CS
61A, an introductory CS course offered at UC Berkeley. In addition,
it now also generates code for the rest of my website at
[albertwu.org](albertwu.org)

Main Directory Makefile Commands
================================

* `make pub-all`: publishes all apps listed in the variable `APPS`,
  public assets, and index.html
* `make pub-assets`: publishes public assets (like CSS and JS)
* `make pub-index`: publishes index.html
* `make pub-404`: publishes 404.html
* `make app-%`: creates a directory structure for a new app
* `make local_config.py`: create a `local_config.py`

Contents
========

* `.example_app`: Directory housing skeletons for new apps
* `public`: Directory for public assets (CSS, JS, etc.)
* `templates`: Directory for templates (usually HTML)
* `utils`: Python utilities for compiler
* `local_config.py`: local configurations for compiler. Not included
  in git.
* `Makefile`: user interface for compiler
* `compile.py`: the compiler

Apps
----

* `cs61a`: houses the index and general assets for cs61a-related pages
* `review`: exam practice problems
* `notes`: miscellaneous notes

Compiler
========

I wrote the compiler (`compile.py`) specifically for this repo. The
compiler acts as a static templating engine that publishes plain text
files (usually HTML). Its templating language is inspired by
[Django](https://www.djangoproject.com/).

Dependencies
------------

* [Python3.2](http://www.python.org/download/releases/3.2.4/)
* [argparse module](http://docs.python.org/3.2/library/argparse.html)

Basic Usage
-----------

Usually you won't be running `compile.py` directly -- the `Makefile`s
are designed to provide a simpler interface. In the event that you
need to run `compile.py` (or want to write new `Makefile`s), you can
use the `-h` flag:

    $ python3 compile.py -h
    usage: compile.py [-h] [-c CONTENT] template dest

    positional arguments:
      template              The template's filename
      dest                  The destination directory

    optional arguments:
      -h, --help            show this help message and exit
      -c CONTENT, --content CONTENT
                            A Python file with controller logic.

* `content`: optional argument. A Python file containing content.
  Content is expressed as strings that are assigned to variables --
  these variables will be directly substituted into the template to
  generate the result.
* `template`: the name of the template, without a filepath (e.g. just
  `index.html`, not `templates/index.html`). Templates can be defined
  locally for apps, and should be housed in a local `templates`
  directory.
* `dest`: filepath of the destination. Relative paths are okay, but
  to avoid unexpectated behavior it is recommended to use absolute
  paths.

Local Configuration
-------------------

`local_config.py` should be located in the home directory of the repo.
It specifies some settings for the compiler. It must contain the
following variables:

* `BASE_PATH`: the filepath of the repo directory
* `TEMPLATE_DIRS`: a list of directories containing `templates`
  directories (do not include `templates` in the actual filepath)
* `CONFIGS`: a dictionary of variables used by templates (usually for
  resource path configuration).

Here is an example:

    import os

    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_DIRS = [
        BASE_PATH,
        os.path.join(BASE_PATH, 'review'),
        os.path.join(BASE_PATH,'notes'),
    ]
    CONFIGS = {
        'MASTER_DIR': '/',
        'REVIEW_DIR': '/review',
    }

`CONFIGS` is usually used for path configuration -- any apps you
create should be added to `CONFIGS` with their published paths (where
they will be published) as string.

Content
-------

Content files must be Python files, designed for
[Python3.2](http://www.python.org/download/releases/3.2.4/). Anything
can go in these files (subroutines, variables, etc.), but there
**must** be a variable called `attrs` that contains all the variables
you want to use when compiling. Standard procedure is to include this
line at the end:

    attrs = globals()

There are utilities provided in a directory called `utils`, so you can
import them with this line at the top

    from utils import utils

Templates
---------

Templates can be any type of plain-text file (usually but not limited
to HTML). They must be housed in a directory called `templates`. The
syntax for templates is based partially off of [Embedded
JS](http://embeddedjs.com/) and Django.

### Inheritance ###

The following line must be the **very first line** in the template:

    <% extends template_name %>

where `template_name` is any template from which you wish to inherit.
**Note the spaces**: there must be exactly one space in each of the
specified positions above, or else the parser will not work.

The order of template search is determined by the `TEMPLATE_DIRS`
config variable in `local_config.py`. If you want to specify a
particular app's template directory, you can use the following syntax:

    <% extends app:template_name %>

**Note**: there is no "multiple inheritance" -- each template can only
inherit from one parent (the parent itself can inherit).

Once the template inheritance list is determined, inheritance is
resolved from top down (i.e. starting with the super-template and
ending with the sub-template).

### Sub tags ###

To specify a block that a sub-template can inherit:

    {% tag_name %}

where `tag_name` is the name of the tag. Sub-templates will reference
the tag by that name. **Note the spaces**.


### Super tags ###

To poplate an inherited tag, you will need both an opening tag and a
closing tag:

    <% tag_name %>
    contents...
    </% tag_name %>

where `tag_name` is the name of the inherited tag, and `contents` is
anything. Note the spaces, as before. Also, **the open and close tags
must be on their own lines**. The following is invalid:

    <% tag_name %>contents</% tag_name %>

The parser will treat that literally, without marking it for
inheritance.

### Expression tags ###

You can execute Python expressions by using this tag:

    {{ expression }}

As always, note the spaces. `expression` can be any Python expression,
but it cannot be a Python statement. The tag will be replaced with the
`str` of the final expression.
