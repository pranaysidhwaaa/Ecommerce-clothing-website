from abc import ABC, abstractmethod
from tkinter import *


class LinkedListNode:
    def _init_(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def _init_(self):
        self.head = None

    def add_node(self, value):
        new_node = LinkedListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def delete_node(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next and current_node.next.value != value:
                current_node = current_node.next
            if current_node.next:
                current_node.next = current_node.next.next

    def length(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count


class PolynomialLinkedList(LinkedList):
    def _init_(self):
        super()._init_()

    def add_polynomial(self, polynomial):
        self.add_node(polynomial)

    def evaluate_polynomial(self, x):
        current_node = self.head
        result = 0
        while current_node:
            result += current_node.value * (x ** current_node.index)
            current_node = current_node.next
        return result

    def add(self, other):
        result = PolynomialLinkedList()
        current_node_self = self.head
        current_node_other = other.head
        while current_node_self or current_node_other:
            if not current_node_self:
                result.add_node(current_node_other.value)
                current_node_other = current_node_other.next
            elif not current_node_other:
                result.add_node(current_node_self.value)
                current_node_self = current_node_self.next
            else:
                if current_node_self.index < current_node_other.index:
                    result.add_node(current_node_self.value)
                    current_node_self = current_node_self.next
                elif current_node_self.index > current_node_other.index:
                    result.add_node(current_node_other.value)
                    current_node_other = current_node_other.next
                else:
                    result.add_node(current_node_self.value + current_node_other.value)
                    current_node_self = current_node_self.next
                    current_node_other = current_node_other.next
        return result


class MatrixNode:
    def _init_(self, value):
        self.value = value
        self.right = None
        self.down = None


class MatrixLinkedList:
    def _init_(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.head = None

    def add_row(self, row):
        if len(row) != self.cols:
            raise ValueError("Row must have length equal to number of columns.")
        new_node = MatrixNode(row[0])
        current_node = new_node
        for value in row[1:]:
            new_node = MatrixNode(value)
            current_node.right = new_node
            current_node = new_node
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.down:
                self.new_method()

    def new_method(self):
        current