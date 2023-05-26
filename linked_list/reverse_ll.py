from typing import Optional
import copy


class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def build_ll(self, values):
        head = Node(val=values[0], next_node=None)
        head_ref = head

        for val in values[1:]:
            head.next = Node(val=val, next_node=None)
            head = head.next

        return head_ref

    def print_ll(self, head):
        head = copy.deepcopy(head)
        while head is not None:
            print(head.val)
            head = head.next

    def reverseList(self, head: Node) -> Node:
        prev_node = None
        current_node = head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node


def main():
    soln = Solution()
    ll = soln.build_ll(values=[1, 2, 3])
    soln.print_ll(ll)

    print("\n")

    new_head = soln.reverseList(head=ll)
    soln.print_ll(new_head)


if __name__ == '__main__':
    main()
