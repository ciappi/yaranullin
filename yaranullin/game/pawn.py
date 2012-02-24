# yaranullin/game/pawn.py
#
# Copyright (c) 2011 Marco Scopesi <marco.scopesi@gmail.com>
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

from cell_content import CellContent
from ..event_system import Event


class Pawn(CellContent):

    """A PG, an NPG or a monster."""

    def __init__(self, board, name, initiative, x, y, width, height,
                 rotated):
        CellContent.__init__(self, board, x, y, width, height, rotated)
        self.name = name
        self.initiative = initiative

    def handle_game_request_pawn_move(self, ev_type, pawn_id, dx, dy, rotate):
        """Try to move the Pawn."""
        if pawn_id != id(self):
            return
        moved = self.move(dx, dy, rotate)
        if moved:
            event = Event('game-event-pawn-updated', x=self.x, y=self.y,
                          rotated=self.rotated, pawn_id=pawn_id)
            self.post(event)

    def handle_game_request_pawn_place(self, ev_type, pawn_id, x, y, rotate):
        """Try to place the Pawn."""
        if pawn_id != id(self):
            return
        placed = self.place(x, y, rotate)
        if placed:
            event = Event('game-event-pawn-updated', x=self.x, y=self.y,
                          rotated=self.rotated, pawn_id=pawn_id)
            self.post(event)
