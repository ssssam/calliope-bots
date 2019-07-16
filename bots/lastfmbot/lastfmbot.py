#!/usr/bin/python3

import json
import logging
import random
import sys

import calliope.lastfm.history


def main():
    if '--debug' in sys.argv:
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    else:
        logging.basicConfig(stream=sys.stderr, level=logging.WARNING)

    logging.info("lastfmbot")

    query = json.load(sys.stdin)
    seed = query['seed']
    tick = query['tick']
    user = query['user']

    random.seed(seed)

    history = calliope.lastfm.history.load(user)

    sequence = list(history.artists())
    logging.debug("Got sequence of %i artists.", len(sequence))

    random.shuffle(sequence)
    value = sequence[tick]

    result = {
        'artist': value['artist'],
        'user': user,
    }
    json.dump(result, sys.stdout)


main()
