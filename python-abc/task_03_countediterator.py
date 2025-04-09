#!/usr/bin/env python3

# CountedIterator class that extends the functionality of an iterator
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)  # Initialize the underlying iterator
        self.count = 0  # Initialize the counter to track the number of items iterated

    def __next__(self):
        try:
            # Get the next item from the iterator
            item = next(self.iterator)
            self.count += 1  # Increment the counter
            return item
        except StopIteration:
            # Raise StopIteration when the iterator is exhausted
            raise StopIteration

    def get_count(self):
        # Return the count of items that have been iterated
        return self.count
