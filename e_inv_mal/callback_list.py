class ObservableList:
    def __init__(self, initial_list=None):
        self._list = initial_list or []
        self.on_append = None  # Callback for append only
        print("initial_list ################## ",initial_list)
    def set_callback(self, callback):
        self.on_append = callback

    def append(self, item):
        self._list.append(item)
        if self.on_append:  # Trigger only for append
            self.on_append(item, self._list)

    # Access to the underlying list
    def __getitem__(self, index):
        return self._list[index]

    def __repr__(self):
        return repr(self._list)

# Example usage
def on_append_callback(item, updated_list):
    print(f"Appended {item} to the list. New list: {updated_list}")

global_list = ObservableList([])
global_list.set_callback(on_append_callback)

global_list.append(4)  # Prints: Appended 4 to the list. New list: [1, 2, 3, 4]
global_list.append(5)  # Prints: Appended 5 to the list. New list: [1, 2, 3, 4, 5]
global_list.append(4)

from collections import Counter
# List_of_invoices_and_count = []
counts = Counter(global_list)  # > Counter({4: 3, 1: 1, 5: 1})
print(counts)