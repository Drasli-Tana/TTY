"""
Created on 29 avr. 2022

@author: Thomas
"""

class Cell:
    def __init__(self, value, lastCell=None):
        self.value = value
        self.lastCell = lastCell
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
    
    def getLastCell(self):
        return self.lastCell
    
class Stack:
    def __init__(self):
        self.cell = None
    
    def append(self, value):
        self.cell = Cell(value, lastCell=self.cell)
    
    def pop(self):
        if self.cell is None:
            raise IndexError("Stack is empty.")
        value = self.cell.get_value()
        self.cell = self.cell.get_last_cell()
        return value
        
    def isEmpty(self):
        return self.cell is None
        
class Queue:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()
    
    def append(self, value):
        self.inStack.append(value)
    
    def pop(self):
        if self.outStack.isEmpty():
            while not self.inStack.isEmpty():
                self.outStack.append(self.inStack.pop())
                
            else:
                raise IndexError("Queue is empty.")
        
        else:
            return self.outStack.pop()
    
    def isEmpty(self):
        return self.inStack.isEmpty() and self.outStack.isEmpty()
    
