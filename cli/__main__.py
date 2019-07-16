# Bot driver

import click
import yaml

import json
import logging
import pathlib
import subprocess
import sys


def bots():
    result = []
    logging.debug("Loading bots from %s", CALLIOPE_BOT_DIR)
    for path in pathlib.Path(CALLIOPE_BOT_DIR).iterdir():
        with open(path) as f:
            bot = yaml.safe_load(f)
        result.append(bot)
    return result


@click.command()
@click.option('--debug/--no-debug', help="Enable debug output to stderr")
@click.option('--frequency', type=click.Choice(['weekly', 'daily', 'hourly']),
              default='daily', help="Recommendation frequency")
# FIXME: this should really be a user profile document, which contains
# usernames for different platforms.
@click.option('--seed', help="Random seed to use", default=0)
@click.option('--tick', help="Tick value", default=0)
@click.option('--user', help="Username to pass to recommender bots")
def main(debug, frequency, seed, tick, user):
    if debug:
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    else:
        logging.basicConfig(stream=sys.stderr, level=logging.WARNING)

    bot_list = bots()
    logging.debug("Found bots: %s", bot_list)
    for bot in bot_list:
        logging.info("Running bot %s", bot)
        query = {
            'user': user,
            'seed': seed,
            'tick': tick,
        }

        query_encoded = json.dumps(query).encode('utf-8')

        logging.debug("Query: %s", query)
        command = bot['command']
        if debug:
            command += ['--debug']

        result = subprocess.run(command, input=query_encoded, stdout=subprocess.PIPE)

        print(result.stdout.decode('utf-8'))


main()
