import os
f = open("images_markdown.txt", "w+")
for file in os.listdir():
    if file.lower().endswith(".png"):
      f.write('![' + file + ']' + '(/screenshots/' + file + ')\n')
f.close()