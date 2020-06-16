

# import_test.py  Learning/Informatica_Power_center/Learning/Dataset_retail_db/
import cx_Oracle
import csv

con = cx_Oracle.connect('SYSTEM/Bharat@89@localhost:1521/xe')
cur = con.cursor()
########################## Table Department Load  ########################## 

# with open('F:///Learning/Informatica_Power_center/Learning/Dataset_retail_db/Department.csv', "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for lines in csv_reader:
#         #print(lines)
#         cur.execute("insert into Departments (Dept_ID,Dept_Name) values (:1, :2)",(lines[0], lines[1]))
# print(f"Table Department Load completed")

########################## Table Categories.dat load   ########################## 

# with open('F:///Learning/Informatica_Power_center/Learning/Dataset_retail_db/Categories.dat', "r") as csv_file_cat:
#     csv_reader_Cat = csv.reader(csv_file_cat, delimiter=',')
#     for lines in csv_reader_Cat:
#         #print(lines)
#         cur.execute("insert into Categoried(Category_ID,Category_Dept_ID,Category_Name) values (:1, :2, :3)",(lines[0], lines[1], lines[2]))
# print(f"Table Categories Load completed")


# ########################## Table Customer.dat load   ########################## 

# with open('F:///Learning/Informatica_Power_center/Learning/Dataset_retail_db/Customer.dat', "r") as csv_file_cus:
#     csv_reader_Cus = csv.reader(csv_file_cus, delimiter=',')
#     for lines in csv_reader_Cus:
#         #print(lines)
#         cur.execute("insert into Customers(Customer_ID,Customer_Fname,Customer_Lname,Customer_Email,Customer_password,Customer_Street,Customer_City,Customer_State,Customer_Zipcode) values (:1, :2, :3, :4, :5, :6, :7, :8, :9)"
#         ,(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7], lines[8]))
# print(f"Table Customer.dat Load completed")



########################## Table Order_Item.dat load   ########################## 

# with open('F:///Learning/Informatica_Power_center/Learning/Dataset_retail_db/Order_Item.dat', "r") as csv_file_oi:
#     csv_reader_oi = csv.reader(csv_file_oi, delimiter=',')
#     for lines in csv_reader_oi:
#         #print(lines)
#         cur.execute("insert into (Order_Item_ID,Order_Item_order_id,Order_Item_product_ID,Order_Item_Quantity,Order_Item_subtotal,Order_Item_product_price) values (:1, :2, :3, :4, :5, :6)"
#         ,(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5]))
# print(f"Table Order_Item.dat Load completed")


########################## Table Product.dat load   ########################## 

# with open('F:///Learning/Informatica_Power_center/Learning/Dataset_retail_db/Order_Item.dat', "r") as csv_file_Pr:
#     csv_reader_Pr = csv.reader(csv_file_Pr, delimiter=',')
#     for lines in csv_reader_Pr:
#         #print(lines)
#         cur.execute("insert into Products(Product_ID,Product_Category_ID,Product_Name,Product_description,Product_Price,Product_Image) values (:1, :2, :3, :4, :5, :6)"
#         ,(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5]))
# print(f"Table Products.dat Load completed")


########################## Table Orders.dat load   ########################## 

with open('F:///Learning/Informatica_Power_center/Learning/Dataset_retail_db/orders.dat', "r") as csv_file_OR:
    csv_reader_OR = csv.reader(csv_file_OR, delimiter=',')
    for lines in csv_reader_OR:
        #print(lines)
        cur.execute("insert into Orders(Order_ID,Order_date,Order_customer,Order_status) values(:1, :2, :3, :4)"
        ,(lines[0], lines[1], lines[2], lines[3]))
print(f"Table Orders.dat Load completed")


cur.close()
con.commit()
con.close()
