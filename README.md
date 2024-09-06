# SnippyShare
A simple website to share snippets of code *(work in progress)*.

![Website preview](/image.png?raw=true "Screenshot")

## Features
-Generating URL to store code snippets<br>
-Syntax highlighting<br>
*expect more features soon!*

## Running locally

### Cloning the repo
```bash
git clone https://github.com/Kavoyaa/SnippyShare.git
```

### Changing directory
```bash
cd SnippyShare
```

### Installing required packages
```bash
pip install -r requirements.txt
```

### Setting up database using Python prompt
```bash
python3
>>> from SnippyShare import app, db
>>> app.app_context().push()
>>> db.create_all()
>>> exit()
```
*alternatively, if `python3` doesn't work, try using `python` instead.*

### Running the application
```bash
flask run
```
