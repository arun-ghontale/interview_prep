class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node


class LL:
    def __init__(self):
        self.head = None

    def push(self, val):
        if self.head is None:
            self.head = Node(val=val)
            return

        head = self.head
        while head.next_node is not None:
            head = head.next_node

        head.next_node = Node(val=val)

    def pop_last(self):
        if self.head is None:
            return None

        if self.head.next_node is None:
            node = self.head
            self.head = None
            return node

        prev = self.head
        current = self.head.next_node

        while current.next_node is not None:
            prev = current
            current = current.next_node

        prev.next_node = None
        return current

    def pop(self, val=None):
        # if no value given pop last
        if not val:
            return self.pop_last()

        # if a value is given remove the first occurrence of that value
        if self.head is None:
            return None

        current_node = self.head
        next_node = current_node.next_node

        if current_node.val == val:
            if next_node is None:
                self.head = None
                return current_node
            else:
                self.head = next_node
                return current_node

        while next_node is not None:
            if next_node.val == val:
                current_node.next_node = next_node.next_node
                return next_node

            current_node = next_node
            next_node = next_node.next_node

        return

    def print_ll(self):
        head = self.head
        while head is not None:
            print(head.val, end=",")
            head = head.next_node

    def reverse_recursive(self, head):
        if head.next_node is None:
            return head, head

        current = head
        rest, new_head = self.reverse_recursive(current.next_node)

        rest.next_node = current
        current.next_node = None

        return current, new_head

    def reverse_iterative(self, head):
        prev_node = None
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = prev_node

            prev_node = current_node
            current_node = next_node

        return prev_node

    def reverse_ll(self, recursive=False):
        if recursive:
            old_head, new_head = self.reverse_recursive(head=self.head)
            self.head = new_head

        else:
            new_head = self.reverse_iterative(head=self.head)
            self.head = new_head


def main():
    ll = LL()

    values = [1, 2, 4, 6, 8, 10, 11, 12, 14, 21]
    for val in values:
        ll.push(val=val)

    print("pushing to ll")
    ll.print_ll()
    print("\n")

    print("popping ll last")
    for _ in range(15):
        popped_node = ll.pop()
        ll.print_ll()
        print("\n")

    print("pushing to ll")
    values = [1, 2, 4, 6, 8, 10, 11, 12, 14, 21]
    for val in values:
        ll.push(val=val)
    ll.print_ll()
    print("\n")

    print("reversing ll recursively")
    ll.reverse_ll(recursive=True)
    ll.print_ll()
    print("\n")

    print("pushing to ll")
    values = [1, 2, 4, 6, 8, 10, 11, 12, 14, 21]
    for val in values:
        ll.push(val=val)
    ll.print_ll()
    print("\n")

    print("popping last ll")
    ll.pop()
    ll.print_ll()
    print("\n")

    print("popping first occurrence of 4 in ll")
    ll.pop(val=4)
    ll.print_ll()
    print("\n")

    print("popping first occurrence of 21 in ll")
    ll.pop(val=21)
    ll.print_ll()
    print("\n")

    print("popping first occurrence of 14 in ll")
    ll.pop(val=14)
    ll.print_ll()
    print("\n")

    print("popping first occurrence of 14 in ll")
    ll.pop(val=14)
    ll.print_ll()
    print("\n")

    print("popping first occurrence of 12 in ll")
    ll.pop(val=12)
    ll.print_ll()
    print("\n")

    print("reversing ll iteratively")
    ll.reverse_ll(recursive=False)
    ll.print_ll()
    print("\n")


if __name__ == '__main__':
    main()



