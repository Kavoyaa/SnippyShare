# SnippyShare
A simple website to share snippets of code.

![Website preview](/image.png?raw=true "Screenshot")

## Features
-Syntax highlighting<br>
*and uh yeah thats it*

## Running locally
### Cloning the repo
```bash
git clone https://github.com/Kavoyaa/SnippyShare.git
```

### Setting up database using Python prompt
```bash
cd SnippyShare
```

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
