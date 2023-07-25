class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class ArrayStack:

    def __init__(self) -> None:
        self._data = []
    
    def __len__(self) -> int:
        return len(self._data)
    
    def is_empty(self) -> bool:
        return len(self._data) == 0
    
    def push(self, element) -> None:
        self._data.append(element)
    
    def pop(self) -> type:

        if self.is_empty():
            raise Empty
        else:
            return self._data.pop()
    
    def top(self) -> type:

        if self.is_empty():
            raise Empty
        else:
            return self._data[-1]