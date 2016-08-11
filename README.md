Pave Subway Challenge
====================

The task was to model the New York subway system in Python. Some key observations:
+ Subway system can be modelled as an undirected, unweighted/weighted (for Challenge 2) sparse graph
+ BFS is sufficient for finding the shortest path from an origin to destination for an unweighted graph. With weights, the problem needs to be re-approached with a more versatile algorithm (e.g. Dijkstra's)

The core logic is contained in the SubwaySystem class found in `subway.py`. This project uses Python -v3.5.1.

To run challenge examples:
`python examples.py`

To run tests:
`python tests.py`
