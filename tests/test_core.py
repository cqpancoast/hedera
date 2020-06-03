"""Testing for core.py."""

import unittest
from ..src.core import Vine
from ..src.core import Serializer
from networkx import Digraph


# TESTING IDEAS
# - Self loops
# - Not fully connected graphs
# - NODES HAVE HASHES THAT STAY WITH THEM FOR ALL TIME


# EXAMPLES

# Serialized Vines
path_empty_vine_ser = "empty_ser.hd"
path_basic_vine_ser = "basic_ser.hd"
path_complex_vine_ser = "complex_ser.hd"
path_cycle_vine_ser = "cycle_ser.hd"

# A serialization of a vine with no nodes.
with open(path_empty_vine_ser, "r") as f:
    empty_vine_ser = f.readlines()

# A serialization of a vine with a few nodes.
with open(path_basic_vine_ser, "r") as f:
    basic_vine_ser = f.readlines()

# A serialization of a vine with many nodes
# which includes the basic vine ser as a subset.
with open(path_complex_vine_ser, "r") as f:
    complex_vine_ser = f.readlines()

# An serialization with the correct serialization form,
# but with a cycle.
with open(path_cycle_vine_ser, "r") as f:
    ycle_vine_ser = f.readlines()

# Vines
empty_vine = Vine(path_empty_vine_ser)
also_empty_vine = Vine()
basic_vine = Vine(path_basic_vine_ser)
complex_vine = Vine(path_complex_vine_ser)

# Serializers
ser = Serializer()

# TESTS

class TestVineMethods(unittest.TestCase):

    pass


