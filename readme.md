# ZipZap <small>Written by @synackable</small>

## Intro
This tool was written to use brute-force based attack methods against compressed files
such as ZIP, RAR, TAR, etc. in an effort to discover the correct password and decrypt
all the files within. You can give it a single word to create/test every variation of it,
or you can supply a massive database that I've assembled from [SecLists](https://github.com/danielmiessler/SecLists).

## Usage
This project requires Python 3.6+; if you have Py2 ([which you shouldn't](https://www.python.org/doc/sunset-python-2/)) installed, you'll wanna use `python3 ...` instead of `python`.
```
git clone https://github.com/synackable/ZipZap.git
cd ZipZap/
python -m pip install -r requirements.txt; chmod +x zipzap.py
./zipzap.py --help
```