#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Common Utilities
================

Defines common utilities objects that don't fall in any specific category.
"""

from __future__ import unicode_literals

__author__ = "Colour Developers"
__copyright__ = "Copyright (C) 2013 - 2014 - Colour Developers"
__license__ = "New BSD License - http://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-science@googlegroups.com"
__status__ = "Production"

__all__ = ["is_scipy_installed",
           "is_string"]


def is_scipy_installed(raise_exception=False):
    """
    Returns if *scipy* is installed and available.

    Parameters
    ----------
    raise_exception : bool
        Raise exception if *scipy* is unavailable.

    Returns
    -------
    bool
        Is *scipy* installed.
    """

    try:
        # Importing *scipy* Api features used in *Colour*.
        import scipy.interpolate
        import scipy.ndimage
        import scipy.spatial

        return True
    except ImportError as error:
        if raise_exception:
            raise ImportError(
                "'scipy' or specific 'scipy' Api features are not available: '{1}'.".format(
                    error))
        return False


def is_string(data):
    """
    Returns if given data is a *string_like* variable

    Parameters
    ----------
    data : object
        Data to test.

    Returns
    -------
    bool
        Is *string_like* variable.

    Examples
    --------
    >>> colour.utilities.is_string("I'm a string!")
    True
    >>> colour.utilities.is_string(["I'm a string!"])
    False
    """

    return True if isinstance(data, basestring) else False