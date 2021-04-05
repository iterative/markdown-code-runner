# Markdown Code Runner

This repository contains a Python program to run code blocks in Markdown-formatted
files in Docker containers. The primary use case is running code samples of 
documentation in a controlled environment.

For installation, you may want to create a virtual environment after cloning:

```
python -m venv .env
. .env/bin/activate
```

Install the requirements as usual:

```
python -m pip install -r requirements.txt
```
## Directories

`bin`: Contains scripts to extract the code from Markdown files and executing
them in containers. Normally, you only need to use the scripts in this directory.

`mdcoderun`: A python package that can be used to import the parser and execute functionality.

`test`: Unit tests.

`test/test-files`: Various Markdown documents to test the package.

## Extract Code

`bin/extract-md-code.py` is used to extract the code from Markdown files. By
default, it extracts all `inline code` and code blocks enclosed by ```. There
are options to limit the extracted portions.

```
usage: extract-md-code.py [-h] [--katacoda-tag KATACODA_TAG] [--no-inline]
                          [--no-block] [--language LANGUAGE] [--debug]
                          files [files ...]
```

`-l, --language lang`: Used to limit the extracted code to a particular language
specified like

````
```lang
code
 ..
```
````

`-k, --katacoda-tag`: Used to limit the extracted code to a Katacoda tag
like `{{execute}}`. For code blocks in Katacoda Markdown documents, you can
specify the trailing tag with this option. 

```
python extract-md-code.py -k execute katacoda-file.md 
```

extracts only the code blocks that have ``{{execute}}`` at the end, e.g., 

````
```
code 
...
```{{execute}}
````

`--no-inline`: Skips `inline code` elements within the text.

`--no-blocks`: Skips code blocks enclosed by ```.

## Run in Container

`bin/run-in-container.py` sends the extracted code to a Docker container specified by its tag. 

```
usage: run-in-container.py [-h] --container CONTAINER
                           [--katacoda-tag KATACODA_TAG] [--no-inline]
                           [--no-block] [--no-fix-initial-dollar] [--no-stop]
                           [--language LANGUAGE] [--debug]
                           files [files ...]
```

Extracts code blocks from .md files and runs these code in specified container

### Options

`--container CONTAINER, -c CONTAINER`: (Required) Docker image id to run the code. 

`--katacoda-tag KATACODA_TAG, -k KATACODA_TAG`: The Katacoda tag that will be
searched in .md code blocks, e.g., for {{execute}}, specify 'execute'

`--language LANGUAGE, -l LANGUAGE`: Filter the code blocks by ```language ```.
Implies --no-inline, as inline code elements cannot specify language

`--no-inline`: Skip `inline code elements` while parsing

`--no-block`: Skip ``` code blocks ``` while parsing

`--no-fix-initial-dollar`: Code blocks in Markdown documents may contain `$`
signs as prompt. By default these are removed before sending them to the
container. Setting this option keeps them intact. 

`--no-stop`:  By default, the container is stopped at the end. This options
tells to keep it running, e.g., for debugging purposes. 

`--debug`               Show debug output
