#!/usr/bin/python3

import json
import logging
import pathlib
import random
import sys


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

    datadir = pathlib.Path(__file__).resolve().parent
    with open(datadir.joinpath('peel-artists-rateyourmusic.json')) as f:
        sequence = json.load(f)
    logging.debug("Got sequence of %i artists.", len(sequence))

    random.shuffle(sequence)
    value = sequence[tick]

    result = {
        'artist': value['artist'],
        'user': user,
    }
    json.dump(result, sys.stdout)


main()
