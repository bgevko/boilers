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
    buildscript = subparsers.add_parser('buildscript', help='Template for a build bash script')   # noqa: F841
    express = subparsers.add_parser('express', help='Template for an express server')   # noqa: F841
    simple_react = subparsers.add_parser('simple-react', help='Create a minimal React project with just two pages, index.html and app.jsx')   # noqa: F841


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
    elif args['command'] == 'buildscript':
        console.print('Fetching build script template...', style="yellow")
        content = get_template('https://raw.githubusercontent.com/bgevko/boilers/main/templates/rebuild.sh')
        write_file('build.sh', content)
    elif args['command'] == 'simple-react':
        console.print('Fetching HTML file...', style="yellow")
        content = get_template('https://raw.githubusercontent.com/bgevko/boilers/main/templates/simple-react.html')
        write_file('index.html', content)
        console.print('Fetching app.jsx...', style="yellow")
        content = get_template('https://raw.githubusercontent.com/bgevko/boilers/main/templates/simple-react-app.jsx')
        write_file('app.jsx', content)
    elif args['command'] == 'express':
        console.print('Fetching express server template...', style="yellow")
        content = get_template('https://raw.githubusercontent.com/bgevko/boilers/main/templates/express.js')
        write_file('server.js', content)
        console.print('Fetching package.json template...', style="yellow")
        content = get_template('https://raw.githubusercontent.com/bgevko/boilers/main/templates/express-package.json')
        write_file('package.json', content)
        console.print("Run 'npm install' to install dependencies.", style="yellow")
    else:
        parser.print_help()
if __name__ == "__main__":
    main()

