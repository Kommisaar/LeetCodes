class EmptyLinkedListError(Exception):
    def __init__(self, message="Linked list is empty!"):
        self.message = message
        super().__init__(self.message)


class ValueNotFoundInLinkedListError(Exception):
    def __init__(self, value, message="Value not found in the linked list"):
        self.value = value
        self.message = f"{message}: {self.value}"
        super().__init__(self.message)


class OutOfLinkedListIndexError(Exception):
    def __init__(self, value, message="Position is out of range"):
        self.value = value
        self.message = f"{message}:{self.value}"
        super().__init__(self.message)


class LinkedListHasCycleError(Exception):
    def __init__(self, message="Linked list has Cycle"):
        self.message = message
        super().__init__(self.message)


class LinkedListDontExistsCycleError(Exception):
    def __init__(self, message="Linked list does not exists Cycle"):
        self.message = message
        super().__init__(self.message)
