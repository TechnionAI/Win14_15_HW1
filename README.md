#Homework 1 - Heuristic Search

##Directory Structure

###[`/`](/)
Add your source files here, and insert calls for them in [`main.py`](main.py).

[`__init__.py`](__init__.py) A hint for the interpreter - ignore this file.

[`main.py`](main.py) Minimal interface to the command line: `$ python main.py [args]`

[`stats.py`](stats.py) Gather and print statistics: `$ python stats.py`

You can add any directory for 3rd party libraries. Remember to declare `dir any_other_directory` in [`docs/dependencies.txt`](docs/dependencies.txt)

___
###[`ways/`](ways/)
Primary library directory. Basic usage: 
```python
from ways import load_map_from_csv
````

[`ways/__init__.py`](ways/__init__.py) Defines the functions accessible using `import ways`

[`ways/graph.py`](ways/graph.py) Code to load the map from the database

[`ways/info.py`](ways/info.py) Constants

[`ways/tools.py`](ways/tools.py) Arbitrary, possibly useful tools

[`ways/draw.py`](ways/draw.py) Helper file for drawing paths using matplotlib
___

###[`docs/`](docs/)
Documentation

[`docs/AI_HW1.pdf`](docs/AI_HW1.pdf) Assignment file

[`docs/dependencies.txt`](docs/dependencies.txt) Declarations of dependencies in 3rd party libraries. For example:

> pip numpy
>

___
###[`db/`](db/)
Database. Do not change.

[`db/israel.csv`](db/israel.csv) Roads description. primary database file

[`db/lights.csv`](db/israel.csv) List of locations of traffic lights
___		
###[`results/`](results/)
Put your experiment results (text and images) here
