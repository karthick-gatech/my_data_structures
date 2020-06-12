# support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key
#           if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
#           When the cache reached its capacity, it should invalidate the least
#           recently used item before inserting a new item.

# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

# Get the key / Check if the key exists
#
# Put the key
#
# Delete the first added key
#
# The first two operations in \mathcal{O}(1)O(1) time are
# provided by the standard hashmap, and the last one - by linked list.
# There is a structure called ordered dictionary, it combines behind both hashmap and linked list.

from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
param_1 = obj.get(2)
obj.put(1, 3)
