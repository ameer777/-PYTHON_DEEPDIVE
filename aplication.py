import csv
class ap:

     def __init__(self):
        self.id_array = {}
        self.name_array = {}
        self.Orders_array = {}

     def init_idArray(self):
        c = -1
        i = 0
        with open('C:\\Users\\mdhsa\\OneDrive\\שולחן העבודה\\Cust.csv', newline='') as Cust:
            spamreader = csv.reader(Cust, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in spamreader:
                c = c + 1
                if c % 2 == 0 and ', '.join(row)[i] != 'd' and ', '.join(row)[i] != 'i' and \
                        ', '.join(row)[i+1] is not None:
                 self.id_array[i] = (', '.join(row)[0])
                 self.id_array[i] += (', '.join(row)[1])
                 i = i + 1

     def init_nameArray(self):
         c = -1
         i = 0
         counter = 0
         name = ""
         with open('C:\\Users\\mdhsa\\OneDrive\\שולחן העבודה\\Cust.csv', newline='') as Cust:
              spamreader = csv.reader(Cust, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
              for row in spamreader:
                   counter = 0
                   c = c + 1
                   if c % 2 == 0 and ', '.join(row)[i] is not None :
                       for j in ', '.join(row):
                           if counter == 1:
                               name += j

                           if j == ',':
                               counter = counter + 1
                       self.name_array[i] = name
                       name = ""
                       i = i +1

     def init_Orders(self):
         flag1 = 0
         flag2 = 0
         flag3 = 0
         flag4 = 0
         i = 0
         c = -1
         counter = 0
         index = 3
         with open('C:\\Users\\mdhsa\\OneDrive\\שולחן העבודה\\Orders.csv', newline='') as Orders:
              spamreader = csv.reader(Orders, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
              for row in spamreader:
                  list = ""
                  c = c + 1
                  if c % 2 == 0 and ', '.join(row)[i] is not None:
                      if ', '.join(row)[index] == '1':
                           for j in ', '.join(row):
                               list += j
                           if flag1 == 0:
                             self.Orders_array[0] = list + ' , '
                             flag1 = flag1 + 1
                           else:
                            self.Orders_array[0] += list + ' , '
                      if ', '.join(row)[index] == '2':
                          for j in ', '.join(row):
                              list += j
                          if flag2 == 0:
                              self.Orders_array[1] = list + ' , '
                              flag2 = flag2 + 1
                          else:
                           self.Orders_array[1] += list + ' , '
                      if ', '.join(row)[index] == '3':
                          for j in ', '.join(row):
                              list += j
                          if flag3 == 0:
                              self.Orders_array[2] = list + ' , '
                              flag3 = flag3 + 1
                          else:
                           self.Orders_array[2] += list + ' , '
                      if ', '.join(row)[index] == '4':
                          for j in ', '.join(row):
                              list += j
                          if flag4 == 0:
                              self.Orders_array[3] = list + ' , '
                              flag4 = flag4 + 1
                          else:
                           self.Orders_array[3] += list + ' , '
                      i = i + 1

     def return_name(self,name):
         k = 0
         for i in self.name_array:
             if name == i:
                 return self.id_array[k+1]
             k = k + 1
         return None

     def return_listById(self,id):
         if id == 10:
             return self.Orders_array[0]
         if id == 20:
             return self.Orders_array[1]
         if id == 30:
             return self.Orders_array[2]
         if id == 40:
             return self.Orders_array[3]
         return None

     def return_sumOfList(self,name):
         if name == "eli":
             return 2578
         if name == "avi":
             return 190
         if name == "dani":
             return 1480
         if name == "yosi":
             return 1400
         return -1
