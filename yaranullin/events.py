# yaranullin/events.py
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

''' The events of Yaranullin ''' 

# Basic
ANY = 0
QUIT = 1
TICK = 2

# Network
JOIN = 10

# Game
PAWN-NEW = 20
PAWN-DEL = 21
PAWN-UPDATED = 22
PAWN-MOVE = 23
PAWN-PLACE = 24
PAWN-NEXT = 25
BOARD-NEW = 26
BOARD-DEL = 27
BOARD-CHANGE = 28
STATE-UPDATE = 29
