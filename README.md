# Python_example_pdfs
Python example project to showcase working with PDFs

# Installation
Install in virtual environment using following commands:
```shell
git clone https://github.com/CodeByAlejandro/Python_example_PDFs.git
cd Python_example_PDFs
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

# Usage
1. Run the `pdf.py` module to merge 2 or more PDFs given on the cmd line into a "merged.pdf". This module also contains code in comments to showcase some typical stuff we might wanna do with PDFs.
2. Run the `watermark.py` module to watermark one or more PDFs given on the cmd line with the "wtr.pdf" and save them as new files with a "_wtr.pdf" extension.

## Examples
```shell
python pdf.py dummy.pdf twopage.pdf my_pdf.pdf
```
```shell
python watermark.py merged.pdf
```

# Uninstall
Deactivate the virtual environment using the exported shell function `deactivate`:
```shell
deactivate
```
Remove the project:
```shell
cd ..
rm -rf Python_example_PDFs
```
