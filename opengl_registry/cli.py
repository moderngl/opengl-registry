from typing import List

import argparse
import logging
import sys

from opengl_registry.reader import RegistryReader


def execute_from_command_line():
    """Command line entrypoints.


    """
    values = parse_args(sys.argv[1:])
    if values is None:
        return

    configure_logging(getattr(logging, values.log_level))

    reader = None
    if values.file:
        reader = RegistryReader.from_file(values.file)
    elif values.url:
        reader = RegistryReader.from_url(values.url)
    else:
        reader = RegistryReader.from_url()

    registry = reader.read()
    print('Registry:', registry)


def parse_args(args: List[str]):
    """Parses command line arguments.

    Args:
        args (List[str]): list of string arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file', '-f',
        help="Path to",
    )
    parser.add_argument(
        '--url', '-u',
        help="Url location for the gl.xml file",
    )
    parser.add_argument(
        '--default-url', '-d',
        action="store_true",
        help="Read the registry from the default url",
    )
    parser.add_argument(
        '--log-level', '-l',
        help="Set the log level",
        choices=['INFO', 'DEBUG', 'WARNING', 'ERROR'],
        default='INFO',
    )

    values = parser.parse_args(args)
    if not values.url and not values.file and not values.default_url:
        print("A --file or an --url needs to be supplied")
        parser.print_help()
        return None

    return values


def configure_logging(level):
    pkg_logger = logging.getLogger('opengl_registry')
    pkg_logger.setLevel(level)
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    pkg_logger.addHandler(ch)
