import logging

logging.basicConfig(filename="tuple.log", level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(message)s')

class TupleAssignment() :


    # Task 1

    def extractonlytuple(self):
        try:
            logging.info("first step of task 1")
            l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                 {'k1': "sudh", "k2": "ineuron", "k3":
                     "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]]
            for i in l:
                logging.info("second step of task 1")
                if type(i) == tuple:
                    print(i)
            return i
            logging.info("Executed succsessfully")
        except Exception as e:
            print(e)

dictobj= TupleAssignment()
dictobj.extractonlytuple()