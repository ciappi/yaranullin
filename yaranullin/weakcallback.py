# yaranullin/weakcallback.py
#
# Copyright (c) 2012 Marco Scopesi <marco.scopesi@gmail.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

''' Provide weak references to bound methods.

This is needed because it is impossible to directly save a weak reference to
a bound method (i.e. using weakref.ref).

'''

import inspect
import weakref


class WeakCallback(object):

    ''' Store a weak reference to a method or function 
    
    For a given callback returns always the same instance of WeakCallback.
    
    '''

    _map = weakref.WeakValueDictionary()

    def __new__(cls, callback):
        cb_id = id(callback)
        if cb_id in cls._map:
            return cls._map[cb_id]
        else:
            obj = object.__new__(cls, callback)
            cls._map[cb_id] = obj
            return obj

    def __init__(self, callback):
        if inspect.ismethod(callback):
            self.weak_obj = weakref.ref(callback.im_self)
            self.weak_func = callback.im_func
        elif inspect.isfunction(callback):
            self.weak_obj = None
            self.weak_func = callback
        else:
            raise TypeError("'%s' is not a method or callback" %
                    str(type(callback)))

    def __call__(self):
        ''' Return a reference to the callback or None '''
        if self.weak_obj is None:
            # It is a function
            return self.weak_func
        else:
            # It is a bound method
            obj = self.weak_obj()
            if obj is None:
                return None
            else:
                return getattr(obj, self.weak_func.__name__)
