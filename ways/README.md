#`ways`
Library for handling road map.

##Functions

#####[`load_map_from_csv(filename='israel.csv', start=0, count=sys.maxint) -> Roads`](graph.py#L73)
The workhorse of the library. Returns a [`Roads`](#roads) object; see below for details.

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
[`Link`](graph.py#12) and [`Junction`](graph.py#L12) are [`namdetuple`](https://docs.python.org/2/library/collections.html#collections.namedtuple) - which means they are tuple-like and immutable.

####`Link(source, target, distance, highway_type)`
    
`source` : `int` Junction index

`target` : `int` Junction index

`distance` : `float` Meters

`highway_type` : `int` See [`info.py`](info.py#L7)

####`Junction(index, lat, lon, links)`

`index` : `int` Junction index

`lat` : `float` Latitude

`lon` : `float` Longitude

`links` :  `list(Link)`


####[`Roads`](graph.py#L27)
The graph is a dictionary mapping Junction_id to `Junction`, with some additional methods.

This is the return type of `load_map_from_csv`.

#####Fields

`generation` : `int`

#####Methods
All the methods for `dict` are avalaible here too. In particular, `__getitem__` (Python's `operator[]`).

######[`iterlinks`](graph.py#L55)`(self) -> iterable(Link)`
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

######[`link_speed`](graph.py#L50)`(self, link)`
returns the speed for the link, based on  `self.generation`.

