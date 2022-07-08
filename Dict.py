import logging

logging.basicConfig(filename="dict.log", level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(message)s')

class DictAssignment() :


    # Task 1

    def extractonlydict(self):
        try:
            logging.info("first step of task 1")
            l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                 {'k1': "sudh", "k2": "ineuron", "k3":
                     "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]]
            for i in l:
                logging.info("second step of task 1")
                if type(i) == dict:
                    print(i)
            return i
            logging.info("Executed succsessfully")
        except Exception as e:
            print(e)


    # Task 2

    def extractdictkeyvalue(self):
        try:
            logging.info("first step of task 1")
            l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                 {'k1': "sudh", "k2": "ineuron", "k3":
                     "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]]
            l20 = []
            for i in l:
                if type(i) == dict:
                    print(i.items())
                    for g, h in i.items():
                        # print(g)
                        # print(h)
                        l20.append(g)
                        l20.append(h)
                    print(l20)
            logging.info("Executed succsessfully")
        except Exception as e:
            print(e)

 # Task 3

    def extractdictvalueonly(self):
        try:
            logging.info("first step of task 1")
            l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                 {'k1': "sudh", "k2": "ineuron", "k3":
                     "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]]
            for i in l:
                if type(i) == dict:
                    for k, v in i.items():
                        print(v)
                        # print(len(k))
            logging.info("Executed succsessfully")
        except Exception as e:
            print(e)

dictobj= DictAssignment()
dictobj.extractonlydict()
print(dictobj.extractdictkeyvalue())
dictobj.extractdictvalueonly()