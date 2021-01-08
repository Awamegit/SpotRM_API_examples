# SpotRM API Manual and examples
A manuual/tutorial as Python Jupyter notebook.
Also alternative plain Python scripts & a Knime Workflow file.  
Explains the use of the API to access to [SportRM Web](https://spotrm.com/).

# Prerequisits
* A valid account to SpotRM.
* Windows PC or Linux. Not tested on Mac OS, though it should work there as well, as long as dependencies are supported.
* Written in Python 3 (tested with Python 2). 
* A chemistry kit such as RDKit is not explicitly required for these particular examples, but if you eventually want to use structures, a 'Conda' installation is recommended over a "plain" Python install.
* The Knime example does not require Python. Version 4.x is preferred, though V3.x should work as well (not tested).

# Installation
For a regular Python installation, use
```
python -m pip install requests
```

In case of Conda, use 
```
conda install -c anaconda requests
```

Should you want to use Jupyter notebook, please see [Jupyter homepage for installation](https://jupyter.org/install)


Knime Version 4.x ([dowloadable here](https://www.knime.com/downloads/download-knime)) will automatically detect any missing nodes and suggest to download those.

# Description of available examples

**API_Manual_and_examples.ipynb** Jupyter notebook (iPython) explaining authentication & get/post request including the examples available here as separate python files (which in themselves are less descriptive than this notebook). Can be viewed directly on GitHub.

**basicExample.knwf** example workflows for graphical data science platform Knime.
Download this file and use "File->Import" in Knime. Knime will notify of any missing nodes and offer to download them. Written for Knime V4.1 and greater. Should work in versions 3.7.x.

**basicExample.py ** Python based code examples.

**getImage.py** Python script illustrating how to retrieve a image of your
query smiles highlighted with the alert substructure. The image is retrieved as file. In the Jupyter notebook the image file is also displayed within the notebook.

**useToken.py** Python script illustrating how to get an authorisation token
and use it to search for alerts and retrieve the drug information on the alerts
found.

# Contributers
* [@DocMinus](https://www.github.com/DocMinus)
* [@kebp](https://www.github.com/kebp)

# License
The software is licensed under the BSD3-Clause License (see LICENSE file), and is free and provided as-is.

# Questions and Feedback
For questions or suggestions, please use the GIT feedback channels or mail to Awametox support (found on the homepage).
