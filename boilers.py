#!/usr/bin/env python3
from rich.traceback import install
from rich.console import Console
import requests
import argparse
install()
console = Console()

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

        console.print(f"Success. Imported as {filename}!", style="green")
    except FileExistsError:
        console.print(f"{filename} already exists.", style="red")
        filename = filename.split('.')[0]
        new_filename = f"{filename}-boiler.css"
        
        with open(new_filename, 'w') as f:
            f.write(content)
        console.print(f"Imported as {new_filename}!", style="green")

def main():
    parser = argparse.ArgumentParser( description="Stop worrying about boilerplate code!")  
    subparsers = parser.add_subparsers(dest='command')

    # Available commands
    html = subparsers.add_parser('html', help='HTML boilerplate.')    # noqa: F841
    css = subparsers.add_parser('css', help='CSS template with resets.')       # noqa: F841
    cppcmake = subparsers.add_parser('cmake-cpp', help='CMake boilerplate for C++.')   # noqa: F841


    args = vars(parser.parse_args())

    if args['command'] == 'html':
        console.print('Fetching HTML boilerplate...', style="yellow")
        content = get_template('https://raw.githubusercontent.com/bgevko/boilers/main/templates/html.html')
        write_file('index.html', content)

    elif args['command'] == 'css':
        console.print('Fetching CSS boilerplate...', style="yellow")
        content = get_template('https://raw.githubusercontent.com/bgevko/boilers/main/templates/css.css')
        write_file('styles.css', content)

    elif args['command'] == 'cmake-cpp':
        console.print('Fetching CMake boilerplate for C++...', style="yellow")
        content = get_template('https://raw.githubusercontent.com/bgevko/boilers/main/templates/cmake-cpp.txt')
        write_file('CMakeLists.txt', content)
    else:
        parser.print_help()
if __name__ == "__main__":
    main()

