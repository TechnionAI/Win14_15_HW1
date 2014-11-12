#`ways`
Library for handling road map.

##Functions

#####`load_map_from_csv(filename='israel.csv', start=0, count=sys.maxint) -> Roads`
The workhorse of the library. The basic usage is simple:
```python
from ways import load_map_from_csv
roads = load_map_from_csv()
# work with road
```

##Classes
`Link` and `Junction` are [`namdetuple`](https://docs.python.org/2/library/collections.html#collections.namedtuple) - which means they are tuple-like and immutable.

####`Link(source, target, distance, highway_type)`
    
`source` : `int` Junction index

`target` : `int` Junction index

`distance` : `float` Meters

`highway_type` : `int` See [`info.py`](info.py#7)

####`Junction(index, lat, lon, links)`

`index` : `int` Junction index

`lat` : `float` Latitude

`lon` : `float` Longitude

`links` :  `list(Link)`


####`Roads(generation)`
The graph is a dictionary mapping Junction_id to `Junction`, with some additional methods.

This is the return type of `load_map_from_csv`.

#####Fields

`generation` : `int`

#####Methods
All the methods for `dict` are avalaible here too. In particular, `__getitem__` (Python's `operator[]`).

######[`__init__`](graph.py)`(self, junction_list, lights)`
Don't construct this object yourself. Called by `load_map_from_csv`.

######[`iterlinks`](graph.py)`(self) -> iterable(Link)`
Chains all the links in the graph. 
use: 
```python
for link in road.iterlinks(): ...
```

######[`junctions`](graph.py)`(self) -> list(Junction)`
Iterate over the junctions in the road.
Simply returns the values in the dictionary.

######[`has_traffic_lights`](graph.py)`(self, junction) -> bool`
Check if `link` has a traffic lights, based on the file [`db/lights.txt`](../db/lights.txt).
    
######[`has_traffic_jam`](graph.py)`(self, link) -> bool`
Check if `link` has a traffic jam, based on `self.generation`. 

######[`link_speed`](graph.py)`(self, link)`
returns the speed for the link, based on  `self.generation`.

