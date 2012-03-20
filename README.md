# Yaranullin

Copyright (c) 2012 Marco Scopesi <marco.scopesi@gmail.com>

Yaranullin is an interactive map for role-playing games. Basically it is
a piece of software that helps role players to track the position of their
heroes when fighting against monsters and other scary things, such as
skeletons and other derivatives.

## Dependencies

This is a list of all dependencies.

* python >= 2.7
* python-pygame >= 1.9.1
* python-bson (included in the sources)

## Server

To run a server for a Yaranullin game, open a terminal and type:

```bash
$ cd /path/to/yaranullin/sources
$ ./bin/yaranullin server --game test_1
```

The game to load (test_1 in the above example) should be a folder inside '/path/to/yaranullin/sources/data/saves/'.

## Client

To run a client for a Yaranullin game, open a terminal and type:

```bash
$ cd /path/to/yaranullin/sources
$ ./bin/yaranullin client --host 127.0.0.1
```

You can change the host if the server is on another machine on the network.

## Tokens

All pawn images are taken from http://www.immortalnights.com/tokensite/tokenpacks.html
