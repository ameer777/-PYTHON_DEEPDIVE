import csv

with open('C:\\Users\\mdhsa\\OneDrive\\שולחן העבודה\\Cust.csv', mode='w') as Cust:
    Cust_writer = csv.writer(Cust)

    Cust_writer.writerow(['id', 'name', 'city'])
    Cust_writer.writerow(['10', 'eli', 'ashdod'])
    Cust_writer.writerow(['20', 'avi', 'haifa'])
    Cust_writer.writerow(['30', 'dani', 'tel aviv'])
    Cust_writer.writerow(['40', 'yosi', 'yafo'])


with open('C:\\Users\\mdhsa\\OneDrive\\שולחן העבודה\\Orders.csv', mode='w') as Orders:
    Orders_writer = csv.writer(Orders)

    Orders_writer.writerow(['id', 'cust_id', 'date' , 'sum'])
    Orders_writer.writerow(['1', '10', '1/1/17', '123'])
    Orders_writer.writerow(['2', '20', '2/4/16', '190'])
    Orders_writer.writerow(['3', '10', '2/3/17', '2455'])
    Orders_writer.writerow(['4', '30', '9/2/17', '240'])
    Orders_writer.writerow(['5', '40', '1/5/16', '200'])
    Orders_writer.writerow(['6', '30', '1/2/17', '1240'])
    Orders_writer.writerow(['7', '40', '14/5/16', '1200'])
