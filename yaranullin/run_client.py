# yaranullin/run_client.py
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

import asyncore

from yaranullin.config import CONFIG
from yaranullin.event_system import post, process_queue
from yaranullin.network.client import ClientEndPoint

# Initialize network
ClientEndPoint()
HOST = CONFIG.get('network', 'host')
PORT = CONFIG.getint('network', 'port')

def run(args):
    ''' Main loop for the client '''
    stop = False
    post('join', host=HOST, port=PORT)
    while not stop:
        post('tick')
        stop = process_queue()
        asyncore.poll(0.01)
