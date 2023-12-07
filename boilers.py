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

        parts = filename.rsplit('.', 1)

        if len(parts) == 2:
            base_name, file_ext = parts
            new_filename = f"{base_name}-boilerplate.{file_ext}"
        else:
            base_name = parts[0]
            new_filename = f"{base_name}-boilerplate"
        
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
    tailwind_html = subparsers.add_parser('tailwind-html', help='Blank index.html with tailwind cdn.')   # noqa: F841
    python = subparsers.add_parser('python', help='Python boilerplate.')   # noqa: F841
    makefile = subparsers.add_parser('makefile', help='Makefile boilerplate.')   # noqa: F841
    devnote = subparsers.add_parser('devnote', help='Template for a devnote')   # noqa: F841
    devnote.add_argument('-f', '--filename', type=str, help='Filename for devnote', default='devnote.md')   # noqa: F841

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

    elif args['command'] == 'express':
        console.print('Fetching express server template...', style="yellow")
        content = get_template('https://raw.githubusercontent.com/bgevko/boilers/main/templates/express.js')
        write_file('server.js', content)
        console.print('Fetching package.json template...', style="yellow")
        content = get_template('https://raw.githubusercontent.com/bgevko/boilers/main/templates/express-package.json')
        write_file('package.json', content)
        console.print("Run 'npm install' to install dependencies.", style="yellow")

    elif args['command'] == 'tailwind-html':
        console.print('Fetching tailwind index.html template...', style="yellow")
        content = get_template('https://raw.githubusercontent.com/bgevko/boilers/main/templates/tailwind-html.html')
        write_file('index.html', content)

    elif args['command'] == 'python':
        console.print('Fetching python boilerplate...', style="yellow")
        content = get_template('https://raw.githubusercontent.com/bgevko/boilers/main/templates/python.py')
        write_file('main.py', content)

    elif args['command'] == 'makefile':
        console.print('Fetching makefile boilerplate...', style="yellow")
        content = get_template('https://raw.githubusercontent.com/bgevko/boilers/main/templates/makefile')
        write_file('makefile', content)

    elif args['command'] == 'devnote':
        console.print('Fetching devnote template...', style="yellow")
        content = get_template('https://raw.githubusercontent.com/bgevko/boilers/main/templates/devnote.mdx')
        write_file(args['filename'], content)

    else:
        parser.print_help()
if __name__ == "__main__":
    main()

