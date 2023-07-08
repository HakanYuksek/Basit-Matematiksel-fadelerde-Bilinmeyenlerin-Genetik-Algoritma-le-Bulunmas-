# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:49:42 2020

@author: USER
"""

class STACK:
    
    def __init__(self):
        self.size = 0
        self.elements = []
    
    # This method provides to push an element to stack
    def pushElement(self,element):
        self.elements.append(element)
        self.size += 1
    
    # This method provides to pop an element from stack
    # First in Last Out Principle is used
    def popElement(self):
        if not self.isEmpty():
            self.size -= 1
            last_element = self.elements[self.size]
            self.elements.pop(self.size)
            return last_element
        else:
            return "Empty Stack"
    
    # We can check whether stack is empty or not by using this method
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    # This method prints all elements of the stack
    def writeStackElements(self):
        print("Stack Elements--->")
        for each in self.elements:
            print(each)
            