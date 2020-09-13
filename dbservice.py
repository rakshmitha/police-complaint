# Import necessary modules
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy import update
from sqlalchemy import and_, or_

engine = create_engine('sqlite:///police.db', echo = True)

Base = declarative_base() 

class User_Details(Base):
   __tablename__ = 'user_details'
   
   id = Column(Integer, primary_key=True)
   name = Column(String)
   email = Column(String)
   password = Column(String)



Session = sessionmaker(bind = engine)
session = Session()

class complaint_details():
    __tablename__='compalint_details'

    id = Column(Integer, primary_key=True)
    cname = Column(String)
    cgender=Column(String)
    cdob=Column(Integer)
    caddress=Column(String)
    ccontactno=Column(Integer)
    cemail=Column(String)
    Subject=Column(String)
    date_of_occurance=Column(Integer)
    place_of_occurance=Column(String)
    description=Column(String)

def add_user(name, email, password):
    user=User_Details(name = name, email = email, password= password)

    session.add(user)
    session.commit()

    result = session.query(User_Details).filter(User_Details.email == email).first()
    return result.id

def login(email, password):
    result = session.query(User_Details).filter(User_Details.email == email).first()
    if result.password==password:
        return result.id
    else:
        return -1

def incident_registration(name, gender, dob, address, contactno, email, Subject, date_of_occurance, place_of_occurance, description):
    user=complaint_details(cname=name, cgender=gender, cdob=dob, caddress=address, ccontactno=contactno, cemail=email, Subject=Subject, date_of_occurance=date_of_occurance, place_of_occurance=place_of_occurance, description=description)

    session.add(user)
    session.commit()

    result = session.query(complaint_details).filter(complaint_details.cemail == email).first()
    return result.id
# def add_multiple_customers():

#     session.add_all([
#         Customers(name = 'Komal Pande', address = 'Koti, Hyderabad', email = 'komal@gmail.com'), 
#         Customers(name = 'Rajender Nath', address = 'Sector 40, Gurgaon', email = 'nath@gmail.com'), 
#         Customers(name = 'S.M.Krishna', address = 'Budhwar Peth, Pune', email = 'smk@gmail.com')]
#     )

#     session.commit()

# def add_customer(c_name, c_address, c_email):
    
#     c1 = Customers(name = c_name, address = c_address, email = c_email)

#     session.add(c1)
#     session.commit()

# def get_customers():

#     result = session.query(Customers).all()

#     for row in result:
#         print ("Name: ",row.name, "Address:",row.address, "Email:",row.email)

# # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_updating_objects.htm
# def get_customer_by_id(c_id):

#     result = session.query(Customers).get(c_id)

#     print ("Name: ",result.name, "Address:",result.address, "Email:",result.email)

#     return result

# def update_customer(c_id, addresss):

#     result = session.query(Customers).get(c_id)

#     result.address = addresss
#     session.commit()

#     print('address updated')

# def get_first_customer():

#     result = session.query(Customers).first()

#     print ("Name: ",result.name, "Address:",result.address, "Email:",result.email)

# def update_multi_rows():

#     session.query(Customers).filter(Customers.id != 2).update({Customers.address: Customers.address + ', Canada'}, synchronize_session = False)

#     session.commit()

#     print('address updated')

# '''
#     https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_filter_operators.htm
# '''
# # customer id equal
# def get_customer_id_equal(c_id):

#     result = session.query(Customers).filter(Customers.id == c_id)

#     for row in result:
#         print ("ID:", row.id, "Name: ",row.name, "Address:",row.address, "Email:",row.email)


# def get_customer_by_name(customer_name):

#     result = session.query(Customers).filter(Customers.name == customer_name).first()

#     # for row in result:
#     #     print ("ID:", row.id, "Name: ",row.name, "Address:",row.address, "Email:",row.email)
#     #     return row

#     print(result.name, result.address)

#     return result

# '''
#     https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_filter_operators.htm
# '''
# # customer name like
# def get_customer_like(like_string):

#     result = session.query(Customers).filter(Customers.name.like(like_string))

#     for row in result:
#         print ("ID:", row.id, "Name: ",row.name, "Address:",row.address, "Email:",row.email)

# def get_customer_in(id_list):

#     result = session.query(Customers).filter(Customers.id.in_(id_list))

#     for row in result:
#         print ("ID:", row.id, "Name: ", row.name, "Address:", row.address, "Email:",row.email)

# def get_customer_where_and():

#     result = session.query(Customers).filter(Customers.id > 2, Customers.name.like('A%'))
#     for row in result:
#         print ("ID:", row.id, "Name: ",row.name, "Address:",row.address, "Email:",row.email)

# def get_customer_where_and_2():

#     result = session.query(Customers).filter(and_(Customers.id > 2, Customers.name.like('A%')))

#     for row in result:
#         print ("ID:", row.id, "Name: ",row.name, "Address:",row.address, "Email:",row.email)

# def get_customer_where_or():
    
#     result = session.query(Customers).filter(or_(Customers.id > 2, Customers.name.like('A%')))

#     for row in result:
#         print ("ID:", row.id, "Name: ",row.name, "Address:",row.address, "Email:",row.email)


# def add_customer_with_invoice():

#     customer1 = Customers(name = "Justin", address = "67, Wall Street", email = "justin@gmail.com")

#     customer1.invoices = [Invoice(invno = 10, amount = 120), Invoice(invno = 14, amount = 340)]

#     session.add(customer1)
#     session.commit()

# def add_customer_with_user_point():

#     customer1 = Customers(name = "Vyshnavi", address = "67, Villivakkam", email = "vysh@gmail.com")

#     # custid, point, comment
#     customer1.user_point = [UserPoint(point = 20, comment = 'Daily attendance')]

#     session.add(customer1)
#     session.commit()


# def add_user_point_by_customer_id(customer_id):

#     customer1 = get_customer_by_id(customer_id)

#     # customer1 = Customers(name = "Vyshnavi", address = "67, Villivakkam", email = "vysh@gmail.com")

#     # custid, point, comment
#     customer1.user_point = [UserPoint(point = 20, comment = 'Daily attendance')]

#     session.add(customer1)
#     session.commit()


# def add_user_point_by_customer_name(customer_name):

#     customer1 = get_customer_by_name(customer_name)

#     print('customer1 : ', customer1)

#     userPoint = UserPoint(custid = customer1.id, point = 30, comment = 'Quiz Winner')

#     session.add(userPoint)
#     session.commit()


# '''
#     https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_working_with_joins.htm
# '''
# def get_customer_invoices():

#     for c, i in session.query(Customers, Invoice).filter(Customers.id == Invoice.custid).all():
#         print ("ID: {} Name: {} Invoice No: {} Amount: {}".format(c.id,c.name, i.invno, i.amount))

# def get_customer_points():

#     for c, p in session.query(Customers, UserPoint).filter(Customers.id == UserPoint.custid).all():
#         print ("ID: {} Name: {} UserPoint No: {} Point: {}".format(c.id,c.name, p.id, p.point))

# def get_customer_points_by_customer_name(customer_name):

#     for c, p in session.query(Customers, UserPoint).filter(and_(Customers.id == UserPoint.custid, Customers.name == customer_name)).all():
#         print ("ID: {} Name: {} UserPoint No: {} Point: {}".format(c.id,c.name, p.id, p.point))

# '''
#     https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_working_with_joins.htm
# '''
# def get_customer_invoices_with_filter():

#     result = session.query(Customers).join(Invoice).filter(Invoice.amount > 2700)
#     for row in result:
#         for inv in row.invoices:
#             print (row.id, row.name, inv.invno, inv.amount)

# def startpy():

#     pass

#     # Add customer
#     # add_customer('Sameena', '22, Thambaram', 'sam@gmail.com')

#     # add_multiple_customers()

#     # get_customers()

#     # get_customer_by_id(2)

#     # update_customer(2, '256, Brahms Avenue')

#     # get first customer
#     # get_first_customer()

#     # Add Toronto in address
#     update_multi_rows()

#     # get_customer_id_equal(2)

#     # Get Customer Like
#     # get_customer_like('A%')

#     # get_customer_in([1, 4])

#     # get_customer_where_and()

#     # get_customer_where_and_2()

#     # get_customer_where_or()

#     # Add customer with invoices
#     # add_customer_with_invoice()

#     # get_customer_invoices()

#     # get_customer_invoices_with_filter()

#     # Add user point
#     # add_customer_with_user_point()

#     # add_user_point(8)

#     # add_user_point_by_customer_name('Sameena')

#     # get_customer_by_name('Sameena')

#     # get_customer_points()

#     # get_customer_points_by_customer_name('Sameena')

#     # get_customer_points_by_customer_name('Vyshnavi')

# if __name__ == '__main__':
#     startpy()