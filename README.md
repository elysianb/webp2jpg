# Installation

- Install python

https://www.python.org/downloads/

- Install pip

https://pip.pypa.io/en/stable/installation/

- Install pillow, for image management

`pip install pillow` 

- Extract binaries from a release into a local directory. Then, use it

`webp2jpg --help` 

# Documentation

NAME

        webp2jpg - convert webp images to jpeg images

SYNOPSIS

        python webp2jpg.py [options / FILE]

DESCRIPTION

        Find files that matches the pattern FILE from the working
        directory. Then convert files endings by .webp or .WEBP to
        jpg files. Other files are skipped.

FILE

        Can be a filename or a search pattern like *file.webp or
        just *

        Examples:
          python webp2jpg.py image.webp
          python webp2jpg.py *
          python webp2jpg.py *suffix.webp

OPTIONS

        -h, --help
                Display this manual page
		
        -v, --version
                Display the current version number
