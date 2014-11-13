#`ways`
Library for handling road map.

##Functions

#####[`load_map_from_csv(filename='israel.csv', start=0, count=sys.maxint)`](graph.py#L74)` -> `[`Roads`](#roads)
The workhorse of the library.

The basic usage is simple:
```python
from ways import load_map_from_csv
roads = load_map_from_csv()
# work with road
```
This function takes some time to finish. To test your code on smaller maps, use `count`:
```python
roads = load_map_from_csv(count=10000)
```

And you can add `start` argument to work in more "interesting" regions:
```python
roads = load_map_from_csv(start=100000, count=10000)
```

##Classes
[`Link`](graph.py#L12) and [`Junction`](graph.py#L12) are [`namdetuple`](https://docs.python.org/2/library/collections.html#collections.namedtuple) - which means they are tuple-like and immutable.

####`Link`

| Field | `source`       |  `target`   | `distance` | `highway_type` |
| -------:|:-------------:|:---------:|:--------:|:------------:|
| Type    | `int`        |  `int`    | `float`  | `int`        |
| Meaning |  Junction index | Junction index | Meters | See [`info.py`](info.py#L7) |

####`Junction`

| Field   | `index`       |  `lat`   | `lon` | `highway_type` |
| -------:|:-------------:|:---------:|:--------:|:------------:|
| Type    | `int`        |  `float`    | `float`  | `int`        |
| Meaning |  Junction index | Latitude | Longitude | `list(Link)` |

####[`Roads`](graph.py#L27)
The graph is a dictionary mapping Junction index to `Junction`, with some additional methods.

This is the return type of [`load_map_from_csv`](#functions).

#####Fields

`generation` : `int`

#####Methods
All the methods for `dict` are avalaible here too. In particular, `__getitem__` (Python's `operator[]`).

######[`iterlinks`](graph.py#L56)`(self) -> iterable(Link)`
Chains all the links in the graph. 
use: 
```python
for link in road.iterlinks(): ...
```

######[`junctions`](graph.py#L32)`(self) -> list(Junction)`
Iterate over the junctions in the road.
Simply returns the values in the dictionary.

######[`has_traffic_lights`](graph.py#L41)`(self, junction) -> bool`
Check if `link` has a traffic lights, based on the file [`db/lights.txt`](../db/lights.txt).

######[`link_speed`](graph.py#L46)`(self, link)`
Returns the speed for the link (in km/h), based on  `self.generation`.

