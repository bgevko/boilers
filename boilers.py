#!/usr/bin/env python3
from rich.traceback import install
import requests
import argparse
install()

def get_template(url):
    """Get file from github repo."""
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        raise Exception(f"Error: {r.status_code}")

def write_file(filename, content):
    # If file exists, append 'boilerplate' to filename
    try:
        with open(filename, 'x') as f:
            f.write(content)
    except FileExistsError:
        with open(f"{filename}-boilerplate", 'x') as f:
            f.write(content)


def main():
    parser = argparse.ArgumentParser( description="Stop worrying about boilerplate code and focus on your awesome project instead!")  
    subparsers = parser.add_subparsers(dest='command')

    # Available commands
    html = subparsers.add_parser('html', help='HTML boilerplate.')    # noqa: F841
    css = subparsers.add_parser('css', help='CSS template with resets.')       # noqa: F841
    cppcmake = subparsers.add_parser('cmake-cpp', help='CMake boilerplate for C++.')   # noqa: F841


    args = vars(parser.parse_args())

    if args['command'] == 'html':
        pass
        # HTML boilerplate
    elif args['command'] == 'css':
        pass
        # CSS boilerplate
    elif args['command'] == 'cmake-cpp':
        pass
        # CMake boilerplate for C++
    else:
        parser.print_help()
if __name__ == "__main__":
    main()

