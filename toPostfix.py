# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:57:58 2020

@author: USER
"""

from Stack import STACK

# This method converts mathematical equation to postfix notation from infix
# infix notation
def convert_to_postfix(str1):
    
    i = 0
    flag = True
    postfix = []
    
    stack1 = STACK()
    
    while i < len(str1) and flag:
        if str1[i] == "=":
            flag = False
        else:
            if str1[i] =="(":
                stack1.pushElement(str1[i])
            elif str1[i] == ")":
                temp = stack1.popElement()
                while temp != "(":
                    postfix.append(temp)
                    temp = stack1.popElement()
            elif str1[i] == "+" or str1[i] == "-":
                if stack1.isEmpty():
                    stack1.pushElement(str1[i])
                else:
                    temp = stack1.popElement()
                    if temp == "(":
                        stack1.pushElement(temp)
                        stack1.pushElement(str1[i])
                    elif temp == "/":
                        postfix.append(temp)
                        while (not stack1.isEmpty()) and (temp != "("):
                            temp = stack1.popElement()
                            if temp!= "(":    
                                postfix.append(temp)
                        stack1.pushElement(str1[i])
                    elif temp == "*":
                        postfix.append(temp)
                        while not stack1.isEmpty() and (temp!="("):
                            temp = stack1.popElement()
                            if temp!="(":
                                postfix.append(temp)
                        stack1.pushElement(str1[i])
                    elif temp != str1[i]:
                        postfix.append(temp)
                        stack1.pushElement(str1[i])
                    else:
                        postfix.append(temp)
                        stack1.pushElement(str1[i])
            elif str1[i] == "/" or str1[i] == "*":
                if stack1.isEmpty():
                    stack1.pushElement(str1[i])
                else:
                    temp = stack1.popElement()
                    if temp == "(":
                        stack1.pushElement(temp)
                        stack1.pushElement(str1[i])
                    elif temp == "+" or temp== "-":
                        stack1.pushElement(temp)
                        stack1.pushElement(str1[i])
                    elif temp != str1[i]:
                        postfix.append(temp)
                        stack1.pushElement(str1[i])
            elif str1[i].isdigit() or str1[i].isalpha():
                postfix.append(str1[i])
                 
        i += 1
    
    while not stack1.isEmpty():
        postfix.append(stack1.popElement())
        
    return postfix

###############################################################################
# Solve Equatio by using Postfix Notation
###############################################################################




# This method solves mathematical equation by using given postfix notation
# and numbers
# For example
# dict1 = {"a":1,"b":1,"c":1}
# if infix is a * (b+c) = 20
# postfix will be a b c + *
def solve_given_equation(dict1,postfix):

    stack2 = STACK()
    i = 0
        
    while i < len(postfix):
        
        if postfix[i].isdigit():
            stack2.pushElement(int(postfix[i]))
        elif postfix[i].isalpha():
            value = dict1[postfix[i]]
            stack2.pushElement(value)
        elif postfix[i] == "+":
            value1 = stack2.popElement()
            value2 = stack2.popElement()
            val = value1 + value2
            stack2.pushElement(val)
        elif postfix[i] == "-":
            value1 = stack2.popElement()
            value2 = stack2.popElement()
            val = value2 - value1
            stack2.pushElement(val)      
        elif postfix[i] == "*":
            value1 = stack2.popElement()
            value2 = stack2.popElement()
            val = value1 * value2
            stack2.pushElement(val)         
        elif postfix[i] == "/":
            value1 = stack2.popElement()
            value2 = stack2.popElement()
            val = value2 / value1
            stack2.pushElement(val)  
    
        i += 1
    
    result = stack2.popElement()
    
    while not stack2.isEmpty():
        result = stack2.popElement()
        
    return result

