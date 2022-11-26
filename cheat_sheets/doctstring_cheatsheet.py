# docstring cheat sheet by cjteclab
#
# Resources:
#
# 1. PEP 257
#    https://peps.python.org/pep-0257/
# 2. numpy - style guide for docstrings
#    https://numpydoc.readthedocs.io/en/latest/format.html
# 3. pandas - docstring guide
#    https://pandas.pydata.org/docs/development/contributing_docstring.html
# 4. google - python style guide
#    https://google.github.io/styleguide/pyguide.html
#
# For discussion:
# - Text starts at the same line (PEP 257, numpy) or in the next line (pandas)
# after the opening quotes.
# - Where to documenting the class constructor? In class docstring (numpy,
# google) or in __init__ method docstring (PEP 257).
# - First word in functions: use infinitive (pandas) or use descriptive-style
# (google).

"""Docstring for the example.py script.

Note: license and author info do not belong in docstrings.
"""

"""Docstring for the example.py module.

Modules names should have short, all-lowercase names.  The module name may
have underscores if this improves readability.

Every module should have a docstring at the very top of the file.  The
module's docstring may extend over multiple lines.  If your docstring does
extend over multiple lines, the closing three quotation marks must be on
a line by itself, preferably preceded by a blank line.

Consist of:
    1. summary
    2. extended summary
    3. routine listings
    4. seel also
    5. notes
    6. references
    7. examples

Note: license and author info do not belong in docstrings.
"""
import os  # standard library imports first

# Do NOT import using *, e.g. from numpy import *
#
# Import the module using
#
#   import numpy
#
# instead or import individual functions as needed, e.g
#
#  from numpy import array, zeros
#
# If you prefer the use of abbreviated module names, we suggest the
# convention used by NumPy itself::

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# These abbreviated names are not to be used in docstrings; users must
# be able to paste and execute docstrings after importing only the
# numpy module itself, unabbreviated.


class Foo():
    """Use the same sections as outlined in function docstring (except
    Returns).
    The constructor __init__ should also be documented here.

    Parameters
    ----------
    Use this section to describe the constructor's parameters.

    Attributes
    ----------
    x : float
        This section bescribe non-method attributes of the class.

    Methods
    -------
    colorspace(c='rgb')
        Represent the photo in the given colorspace
    In general, it is not necesarry to list class methods. If a class may have
    a great many methods, of which only a few are relevant, they can be list
    here.
    Do not list private methods.
    """
    def __init__(self):
        pass


CONSTANT = 12
"""Consist of: Summary, extendet summary, see also, references, examples"""


def foo(var1, var2, *args, long_var_name="hi", only_seldom_used_keyword=0, **kwargs):
    r"""Summarize the function in one line. Do this, return that.
    (functions and methods must start with an infinitive verb: cast, get,
    calculate, transform, ).

    Several sentences providing an extended description - to clarify
    functionality, not to discuss impelmentation detail or background theory.
    Why the function is useful and their use cases, if it is not too generic.
    Refer to variables using back-ticks, e.g. `var`.

    Parameters
    ----------
    var1 : array_like
        Array_like means all those objects -- lists, nested lists, etc. --
        that can be converted to an array.  We can also refer to
        variables like `var1` (enclose variables in single backticks).
    var2 : int
        The type above can either refer to an actual Python type
        (e.g. ``int``), or describe the type of the variable in more
        detail, e.g. ``(N,) ndarray`` or ``array_like``.
    *args : iterable
        Other arguments.
    long_var_name : {'hi', 'ho'}, optional
        When a parameter can only assume one of a fixed set of values.
        Choices in brackets, default first when optional.
    more_var1 : int, default=True
        For default values
    more_var2 : x1, x2 : int
        When two or more parameter have exactly the same type, shape and
        description, they can be combined.

    Parameter types:
        int, float, str, bool
        list of int
        dict of {str : int}
        tuple of (str, int, int)
        tuple of (str,)
        set of str
    Multiple types:
        int or float
        str, list or float

    Returns
    -------
    type
        Explanation of anonymous return value of type ``type``.
    describe : type
        Explanation of return value named `describe`.
    out : type
        Explanation of `out`.
    type_without_description

    Other Parameters
    ----------------
    only_seldom_used_keyword : int, optional
        Infrequently used parameters can be described under this optional
        section to prevent cluttering the Parameters section.
    **kwargs : dict
        Other infrequently used keyword arguments. Note that all keyword
        arguments appearing after the first parameter specified under the
        Other Parameters section, should also be described under this
        section.

    Raises
    ------
    BadException
        Because you shouldn't have done that.

    See Also
    --------
    numpy.array : Relationship (optional).
    numpy.ndarray : Relationship (optional), which could be fairly long, in
                    which case the line wraps here.
    numpy.dot, numpy.linalg.norm, numpy.eye

    Notes
    -----
    Notes about the implementation algorithm (if needed).

    This can have multiple paragraphs.

    You may include some math:

    .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

    And even use a Greek symbol like :math:`\omega` inline.

    References
    ----------
    Cite the relevant literature, e.g. [1]_.  You may also cite these
    references in the notes section above.

    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
       expert systems and adaptive co-kriging for environmental habitat
       modelling of the Highland Haggis using object-oriented, fuzzy-logic
       and neural-network techniques," Computers & Geosciences, vol. 22,
       pp. 585-588, 1996.

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.
    All imports, including the demonstrated function, must be explicit.

    >>> a = [1, 2, 3]
    >>> print([x + 3 for x in a])
    [4, 5, 6]
    >>> print("a\nb")
    a
    b

    Comment explaining the second example -- note ... for continuing code

    >>> np.add([[1, 2], [3, 4]],
    ...        [[5, 6], [7, 8]])
    array([[ 6, 8],
           [10, 12]])
    """
    # After closing class docstring, there should be one blank line to
    # separate following codes (according to PEP257).
    # But for function, method and module, there should be no blank lines
    # after closing the docstring.
    pass
