"""CORE: Core functionality for Hedera."""

import networkx as nx


class Vine(object):
    """A Vine is a collection of tasks, their tags, and their
    dependency structure.

    Vines manage creating and editing "task graphs", in which tasks are
    represented as nodes in a graph and a directed edge between tasks
    indicates a dependency of the source task on the destination.

    A task can be any task - destroy Earth, write paper, make Hedera
    project. A task is a dictionary with two required fields, or "tags":
        "keyword": a keyword with no spaces (e.g., "destroy" or
            "write-paper").
        "short": a git-commit-style summary of your task. (e.g.,
            "destroy earth for mom", "write paper for CS 101").
    A task can have other tags as well. These tags are used by plugins.

    A Vine is created from a serialized vine by  initializing the vine
    with the path of the serialized vine. Vines themselves can be
    stored, but this is not common - generally, a Vine expires when an
    interface session is over, serializing its contents into a vine
    serialization at some path before it goes. Vines can also serialize
    themselves in the middle of their existence.

    Attributes:
        ???
    """

    def __init__(self):
        """Initializes an empty Vine with no tasks."""

        self._graph() = nx.DiGraph()

    def __init__(self, path):
        """Initializes a Vine from a serialization at the given path.
        For details on serialization, see the Serializer class. Also
        stores the path of this Vine.

        Args:
            path: A valid, accessible path.

        Raises:
            IOError: if the path is inaccessible or invalid.
        """

        self._graph = self._deserialize(path)
        self._path = path

    def get_path(self):
        """Returns the path of this Vine's most recent serialization,
        including the one it was loaded from."""

        return self._path

    def _deserialize(self, path):
        """Deserializes the serialized vine at the given path and
        returns it.

        Returns:
            A networkx DiGraph.

        Raises:
            IOError: if the path is inaccessible or invalid.
            ValueError: if the file at the path doesn't conform to the
                serialization scheme.
        """

        with f as open(path, "r"):
            try:
                serialization = f.readlines()
            except:
                raise IOError("The file at the path {} either does not exist "
                        "or could not be read from.".format(path))

        return Serializer().deserialize(serialization)

    def _serialize(self):
        """Serializes this Vine and writes it to its path."""

        self.serialize(self.path)

    def _serialize(self, path):
        """Serializes this Vine and stores it at the given path."""

        return Serializer().serialize(self._graph)


class Serializer(object):
    """Can turn a serialized vine into a networkx DiGraph, and vice
    versa."""

    def __init__(self):
        """Initializes this object, which may or may not be necessary.
        Hmm."""

        pass

    def serialize(self):
        """Turns a networkx Digraph into a serialized vine, a list of
        strings following the vine serialization scheme. Returns the
        result."""

        return []

    def deserialize(self):
        """Turns a serialized vine, a list of strings following the
        serialization scheme, into a networkx DiGraph. Returns the
        result."""

        return nx.Digraph()

