import logging

import logging


class StringAssignment :


    # Task 1: Try to extract data from index one to index 300 with a jump of 3
    logging.basicConfig(filename="stringassignment.log",level=logging.DEBUG,format= '%(asctime)s %(levelname)s %(name)s %(message)s')
    def extract_string_one_hundred(self):

        try:
            logging.info("First step of task 1")
            s = "this is My First Python programming class and i am learNING python string and its function"
            return s[1:300:3]
            logging.info("first task executed successfully")

        except Exception as e:
            logging.exception("Error occured while performing operation ")

# Task 2 Try to reverse a string without using reverse function

    def reversestring(self):

        try:
            logging.info("First step of task 2")
            s = "this is My First Python programming class and i am learNING python string and its function"
            return s[::-1]
            logging.info("second task executed successfully")

        except Exception as e:
            logging.exception("Error occured while performing operation ")

# Task 3  Try to split a string after conversion of entire string in uppercase

    def splitstring(self):

        try:
            logging.info("First step of task 3")
            s = "this is My First Python programming class and i am learNING python string and its function"
            return s.upper().split(" ")
            logging.info("third task executed successfully")

        except Exception as e:
            logging.exception("Error occured while performing operation ")

# Task 4  Task 4 try to convert the whole string into lower case

    def splitstringlower(self):

        try:
            logging.info("First step of task 4")
            s = "this is My First Python programming class and i am learNING python string and its function"
            return s.lower().split(" ")
            logging.info("fourth task executed successfully")

        except Exception as e:
            logging.exception("Error occured while performing operation ")

# Task 5 Try to capitalize the whole string

    def capetalizestring(self):

        try:
            logging.info("First step of task 5")
            s = "this is My First Python programming class and i am learNING python string and its function"
            return s.capitalize().split(" ")
            logging.info("Fifth task executed successfully")

        except Exception as e:
            logging.exception("Error occured while performing operation ")

# Task 7 Try to give an example of expand tab

    def expand_tab(self):

        try:
            logging.info("First step of task 7")
            s = 'Swanand\tGajanan\tWalke'
            return s.expandtabs()
            logging.info("7th task executed successfully")

        except Exception as e:
            logging.exception("Error occured while performing operation ")

# Task 8 Give an example of strip.

    def strip(self):

        try:
            logging.info("First step of task 8")
            sw = "  Swanand   "
            return sw.strip()
            logging.info("8th task executed successfully")

        except Exception as e:
            logging.exception("Error occured while performing operation ")


# Task 9 Give an example of lstrip.

    def lstrip(self):

        try:
            logging.info("First step of task 9")
            sw = "  Swanand   "
            return sw.lstrip()
            logging.info("9th task executed successfully")

        except Exception as e:
            logging.exception("Error occured while performing operation ")


# Task 10 Give an example of rstrip.

    def rstrip(self):

        try:
            logging.info("First step of task 10")
            sw = "  Swanand   "
            return sw.rstrip()
            logging.info("10th task executed successfully")

        except Exception as e:
            logging.exception("Error occured while performing operation ")

# Task 11 Replace a string charecter by another charector by taking your own example

    def replace_string(self):

        try:
            logging.info("First step of task 11")
            s1 = 'Swanand'
            return s1.replace('a', '@')
            logging.info("11th task executed successfully")

        except Exception as e:
            logging.exception("Error occured while performing operation ")


task1 =StringAssignment()
print(task1.extract_string_one_hundred())
print(task1.reversestring())
print(task1.splitstring())
print(task1.splitstringlower())
print(task1.capetalizestring())
print(task1.expand_tab())
print(task1.strip())
print(task1.lstrip())
print(task1.rstrip())
print(task1.replace_string())

# Task 2 Try to reverse a string without using reverse function

