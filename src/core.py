"""CORE: Core functionality for Hedera."""

from typing import List
from networkx import DiGraph


class Vine(object):
    """A Vine is a collection of tasks, their tags, and their
    dependency structure.

    Vines manage creating and editing "task graphs", in which tasks are
    represented as nodes in a graph (or "leaves") and a directed edge
    between tasks (or a "tendril") indicates a dependency of the source
    task on the destination.

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
    """

    def __init__(self) -> None:
        """Initializes an empty Vine with no tasks."""

        self._graph() = nx.DiGraph()

    def __init__(self, path: str) -> None:
        """Initializes a Vine from a serialization at the given path.
        For details on serialization, see the Serializer class. Also
        stores the path of this Vine.

        Args:
            path: A valid, accessible path.

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

        self._graph = Serializer().deserialize(serialization)
        self._path = path

    def get_path(self) -> str:
        """Returns the path of this Vine's most recent serialization,
        including the one it was loaded from."""

        return self._path

    def is_serializable(self) -> bool:
        """Determine whether this Vine's graph is serializable. To be
        serializable, the Vine must have no circular dependencies and
        be fully connected."""

        return True  # TODO

    def save(self) -> None:
        """Serializes this Vine and writes it to its file path.

        Raises:
            IOError: if the serializaton cannot be written to the file
                path.
            ValueError: if this Vine is not serializable.
        """

        self.serialize(self.path)

    def save(self, path: str) -> None:
        """Serializes this Vine and writes it to the given file path.

        Raises:
            IOError: if the serializaton cannot be written to the file
                path.
            ValueError: if this Vine is not serializable.
        """

        if not self.is_serializable():
            raise ValueError("Attempted serialization of a non-serializable "
                    "Vine.")

        Serializer().serialize(self._graph)


class Serializer(object):
    """Can turn a serialized vine into a networkx DiGraph, and vice
    versa."""

    def __init__(self):
        """Initializes this object, which may or may not be necessary.
        Hmm."""

        pass

    def serialize(self, graph: nx.Digraph) -> List[str]:
        """Turns a networkx Digraph into a serialized vine, a list of
        strings following the vine serialization scheme. Returns the
        result."""

        return []

    def deserialize(self, ser_vine: List[str]) -> nx.DiGraph:
        """Turns a serialized vine, a list of strings following the
        serialization scheme, into a networkx DiGraph. Returns the
        result."""

        return nx.Digraph()

