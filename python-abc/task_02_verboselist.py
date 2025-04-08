class VerboseList(list):
    # Overriding the append method
    def append(self, item):
        super().append(item)  # Call the original append method
        print(f"Added {item} to the list.")
    
    # Overriding the extend method
    def extend(self, iterable):
        super().extend(iterable)  # Call the original extend method
        print(f"Extended the list with {len(iterable)} items.")
    
    # Overriding the remove method
    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)  # Call the original remove method
    
    # Overriding the pop method
    def pop(self, index=-1):
        item = super().pop(index)  # Call the original pop method
        print(f"Popped {item} from the list.")
        return item

# Testing the VerboseList class
vl = VerboseList()

# Testing append method
vl.append(1)  # "Added 1 to the list."

# Testing extend method
vl.extend([2, 3, 4])  # "Extended the list with 3 items."

# Testing remove method
vl.remove(2)  # "Removed 2 from the list."

# Testing pop method
vl.pop()  # "Popped 4 from the list."
vl.pop(0)  # "Popped 1 from the list."
