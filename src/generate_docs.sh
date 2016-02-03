#!/bin/bash
#Generate python class API documentation
for item in *.py;
do
    filename=${item::-3}
    #The test file opens a window and shit when run
    if [ "$filename" = "test" ]
        then
            continue
    fi
    pydoc -w $filename
done
#Generate html from markdown files
for item in *.md;
do
    markdown_py $item > ${item::-3}".html"
    echo "wrote "${item::-3}".html"
done
#Move the generated files to their designated directory
for item in *.html;
do
   mv $item ../docs
done
