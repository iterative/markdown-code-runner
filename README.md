This repository contains a Python program to run code blocks in Markdown formatted
files in Docker containers. It is meant to be used for checking code samples in
documentation. 

For installation, you may want to create a virtual environment after cloning:

```
python -m venv .env
. .env/bin/activate
```

Install the requirements as usual:

```
python -m pip install -r requirements.txt
```

`bin`: Contains scripts to extract code from MD files and executing them in
containers. Normally you only need to use scripts in this directory. 

`mdcoderun`: A python package that can be used to import the functionality.

`test`: Unit tests.

`test/test-files`: Various markdown documents that contains code. 

## Extract Code

`bin/extract-md-code.py` can be used to extract code from Markdown files. By
default, it extracts all `inline code` and code blocks enclosed by ```. There
are options to limit what is extracted from the markdown file. 

`-l, --language lang`: Used to limit the extracted code to a particular language
specified like

````
```lang
code
 ..
```
````

`-k, --katacoda`: Used to limit the extracted code to a particular katacoda tag
like `{{execute}}`. For code blocks in Katacoda Markdown documents,you can
specify the trailing tag with this option. 

```
python extract-md-code.py -k execute katacoda-file.md 
```

extracts only the code blocks that has ``{{execute}}`` at the end, e.g., 

````
```
code 
...
```{{execute}}
````

`--no-inline`: Skips `inline code` elements within the text. 

`--no-blocks`: Skips code blocks enclosed by ```. 
