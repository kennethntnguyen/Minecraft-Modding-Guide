import os
import argparse

parser = argparse.ArgumentParser(description='This script will convert specified image extensions and change them to lowercase. It will also make a textfile with markdown syntax for images with alt attribute as the file name including the extension. A path to the directory of the image(s) can be specified as well.')
parser.add_argument('-p','--path',type=str,default='',metavar='',help='The path to files relative to location of this script file.')
parser.add_argument('-e','--extension',type=str,default='',metavar='',help='The name of the image extension you want to convert to lower case and add to markdown textfile in markdown inline image syntax.')
parser.add_argument('-f','--filename',type=str,default='images_markdown_syntax.txt',metavar='',help='The name of the text file ouputed.')
args = parser.parse_args()

def makeMarkdownTextFile(extension,path,filename):
  valid_image_extensions = ['.tif','.tiff','.gif','.jpeg','.jpg','.jif','.jfif','.jp2','.jpx','.j2k','.j2c','.fpx','.pcd','.png','.pdf']
  script_name = os.path.basename(__file__)
  f = open(filename, 'w+')
  image_names = os.listdir('.' + path)
  for i in range(len(image_names)):
    if image_names[i] != script_name: # This is so that if the script is ran inside that directory
      if image_names[i].endswith(extension):
        base_name,extension_name = os.path.splitext(image_names[i])
        if extension_name.lower() in valid_image_extensions:
          extension_name = extension_name.lower()
          os.rename('.' + path + '/' + image_names[i], '.' + path + '/' + base_name + extension_name)
          image_names[i] = base_name + extension_name
          f.write('![' + image_names[i] + ']' + '(' + path + '/' + image_names[i] + ')\n')
  f.close()


if __name__ == '__main__':
  makeMarkdownTextFile(args.extension,args.path,args.filename)