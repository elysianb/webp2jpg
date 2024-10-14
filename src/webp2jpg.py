import sys
import glob
import PIL
from PIL import Image

version = "24.10.14.0"

try:
    arg_searchPattern = sys.argv[1]
except IndexError:
    arg_searchPattern = ""
 
if arg_searchPattern=="" or arg_searchPattern=="-h" or arg_searchPattern=="--help":
  print('NAME')
  print('        webp2jpg - convert webp images to jpeg images')
  print('')
  print('SYNOPSIS')
  print('        python webp2jpg.py [options / FILE]')
  print('')
  print('DESCRIPTION')
  print('        Find files that matches the pattern FILE from the working')
  print('        directory. Then convert files endings by .webp or .WEBP to')
  print('        jpg files. Other files are skipped.')
  print('')
  print('FILE')
  print('        Can be a filename or a search pattern like *file.webp or')
  print('        just *')
  print('')
  print('        Examples:')
  print('          python webp2jpg.py image.webp')
  print('          python webp2jpg.py *')
  print('          python webp2jpg.py *suffix.webp')
  print('')
  print('OPTIONS')
  print('        -h, --help')
  print('                Display this manual page')
  print('')
  print('        -v, --version')
  print('                Display the current version number')
  print('')  
  exit()

if arg_searchPattern=="-v" or arg_searchPattern=="--version":
  print(version)
  exit()
  
print('# search pattern : ' + arg_searchPattern)  
mylist = [f for f in glob.glob(arg_searchPattern)]
print('#', len(mylist), 'file(s) found')
counter = 0
for file in mylist:
  if file.endswith('.webp') or file.endswith('.WEBP'):
    im = Image.open(file).convert('RGB')
    jpgFilename = file.replace('.webp', '.jpg').replace('.WEBP', '.JPG')
    im.save(jpgFilename, 'jpeg')
    counter += 1
    print(jpgFilename)
  else:
    print('# skipped:', file)
 
print('#', counter,'file(s) converted')