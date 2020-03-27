from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If at capacity,
        if len(self.storage) == self.capacity:
            # if nothing is selected, move to the tail
            if self.current is None:
                self.current = self.storage.tail

            # set a current value to the item that is pased in
            self.current.value = item

            # if we have a prev state, set the current to a prev state
            if self.current.prev:
                self.current = self.current.prev
            # assign it to the tail
            else:
                self.current = self.storage.tail

        # if not at capacity just add to the head of the list
        elif self.capacity > len(self.storage):
            self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        selected_node = self.storage.tail

        while selected_node:
            if selected_node.value is not None:
                list_buffer_contents.append(selected_node.value)

            selected_node = selected_node.prev

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # The storage takes up the amount of space that the capacitycontains
        self.storage = [None] * capacity
        self.current = 0

    def append(self, item):
        # if the current is less than the capacity, sets the item and returns 
        if self.current < self.capacity:
            self.storage[self.current] = item
            self.current += 1
            return

        # Else, resets the current number
        else:
            self.current = 0
            self.storage[self.current] = item
            self.current += 1

    def get(self):
        return [x for x in self.storage if x]