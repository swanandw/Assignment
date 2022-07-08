import logging

class ListAssignment :


    logging.basicConfig(filename="listassignment.log",level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(message)s')

# 1 . Try to reverse a list

    def reverselist(self):
        try :
            logging.info("first step of task 1")
            l = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
                {"key1": "sudh", 234: [23, 45, 656]}]
            return l[::-1]
            logging.info("Executed succsessfully")
        except Exception as e :
            print(e)

# 2. try to access 234 out of this list

    def accesselement(self):
        try :
            logging.info("first step of task 2")
            l = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
                {"key1": "sudh", 234: [23, 45, 656]}]
            return l[7][0]
            logging.info("Executed succsessfully")
        except Exception as e :
            print(e)

# Task 3 try to access 456 out of this list

    def accesselement456(self):
        try :
            logging.info("first step of task 3")
            l = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
                {"key1": "sudh", 234: [23, 45, 656]}]
            return l[5][1]
            logging.info("Executed succsessfully")
        except Exception as e :
            print(e)

# Task 4 Try to extract only a list collection form list l

    def extractlist(self):
        try :
            logging.info("first step of task 4")
            l = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
                {"key1": "sudh", 234: [23, 45, 656]}]
            return l[5:7]
            logging.info("Executed succsessfully")
        except Exception as e :
            print(e)

# Task 5 Try to extract "sudh"

    def extractsudh(self):
        try :
            logging.info("first step of task 5")
            l = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
                {"key1": "sudh", 234: [23, 45, 656]}]
            return l[8]['key1']
            logging.info("Executed succsessfully")
        except Exception as e :
            print(e)

# Task 6 Try to list all the key in dict element avaible in list

    def extractallkey(self):
        try :
            logging.info("first step of task 6")
            l = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
                {"key1": "sudh", 234: [23, 45, 656]}]
            return l[8].keys()
            logging.info("Executed succsessfully")
        except Exception as e :
            print(e)

# Task 7 Try to extract all the value element form dict available in list

    def extractallvalue(self):
        try :
            logging.info("first step of task 7")
            l = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
                {"key1": "sudh", 234: [23, 45, 656]}]
            return l[8].values()
            logging.info("Executed succsessfully")
        except Exception as e :
            print(e)


# Task 8

    def extractfevalue(self):
        try :
            logging.info("first step of task 8")
            l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                 {'k1': "sudh", "k2": "ineuron", "k3":
                     "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]]
            return l[3]
            logging.info("Executed succsessfully")
        except Exception as e :
            print(e)

# Task 9

    def extractonlylist(self):
        try :
            logging.info("first step of task 9")
            l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                 {'k1': "sudh", "k2": "ineuron", "k3":
                     "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]]
            for i in l:
                if type(i) == list:
                    print(i)
            return i
            logging.info("Executed succsessfully")
        except Exception as e :
            print(e)

task = ListAssignment()
print(task.reverselist())
print(task.accesselement())
print(task.accesselement456())
print(task.extractlist())
print(task.extractsudh())
print(task.extractallkey())
print(task.extractallvalue())
print(task.extractfevalue())
print(task.extractonlylist())
