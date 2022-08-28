list_of_names=[]
list_of_DOB=[]
list_of_contact_num=[]
list_of_email=[]
list_of_password=[]
users_list=[list_of_names,list_of_DOB,list_of_contact_num,list_of_email,list_of_password]
list_of_food=[ "Tandoori Chicken (4 pieces) [INR 240]","Vegan Burger (1 piece)[INR 320]","Truffle Cake (500gm)[INR 900]"]
food_info={"101":{"Name":"Tandoori Chicken","Quantity": " 4 Pieces","Price":240,"Discount":0,"Stock Left":0},
            "102":{"Name":"Vegan Burger","Quantity":"1 piece","Price":320,"Discount":0,"Stock Left":0},
             "103":{"Name":"Traffle Cake","Quantity":"500 gram","Price":900,"Discount":0,"Stock Left":0}}

pos=0
class user:
    
    
    def __init__(self):
        pass

    def  register(self):
        name=self.NAME()
        dob=self.DOB()
        contact=self.contact_num()
        email_id=self.email()
        Password=self.password()
        print("\nYour account has been created! Login and order your delicious meal now\n")
        self.login_user()
    
   
    def NAME(self):
        print("Enter your Name :")
        name=input().split("-")
        self.name=name
        list_of_names.append(name)
    def DOB(self):

        print("Enter your date of birth in format dd-mm-yyyy : ")
        DOB=input().split("-")
        self.dob=DOB
        list_of_DOB.append(DOB)
    def contact_num(self):
        print("Enter contact number : ")
        num=input()
        import re
        if (re.search("[0-9]{10}",num)):
            self.contact=num
            list_of_contact_num.append(num)
            return
        else:
            print("Contact number is 10 digits number ,fill it again")
    def email(self):
        print("Enter E-mail address : ")
        email_add=input()
        import re
        if email_add in list_of_email:
            print("This email id is already registered ,please login")
            list_of_names.pop(len(list_of_names)-1)
            list_of_DOB.pop(len(list_of_DOB)-1)
            list_of_contact_num.pop(len(list_of_contact_num)-1)
        else:
            if( re.search("[a-zA-Z]+.*@gmail.com$",email_add)):
                list_of_email.append(email_add)
                self.email=email_add
                
            else:
                print("E-mail address must start with an alphabet should have a domain @gmail.com")
    def password(self):
        print("Enter your password : ")
        word=input()
        import re
        if(re.search("[a-zA-Z]+.[0-9]+.",word)):
            self.password=word
            list_of_password.append(word)
        else:
            print("\n***Warning***\nPassword must begin with an alphabet ,must contain one special character and one or more digits")
    

    def login_user(self):
        print("Enter your email address")
        x=input()
        if x in list_of_email:
            print("Enter password : ")
            y=input()
            if y in list_of_password:
                print("*****What You want to do*****\n1. Placing an order\n2.Checking order history\n3. Update profile")
                z=int(input("Choose option : "))
                if z==1:
                    print(list_of_food)
                    ordering=input("Want to order something,press Yes or No")
                    ordering.lower()
                    if ordering=="yes":
                        self.order()
                    else:
                        pass
                elif z==2:
                    self.show_order()
                    print("Please log in your account")
                    self.login_user()
                elif z==3:
                    self.update_profile()
                    print("Please log in your account see changes")
                    self.login_user()

            else:
                print("Password does not match with the email id")
        else:
            print("The email id is not registered,Kindly sign-in")
    
    def order(self):
        self.list_of_order=[]
        for i in range(len(list_of_food)):
            print("Enter",i+1,"for",list_of_food[i])
        z=list(map(int,input().split(",")))
        for i in z:
            print("You have selected ",list_of_food[i-1])
        print("Do you want to place your order? enter OK to place your order")
        if(input()=="ok"):
            for i in z:
                self.list_of_order.append(list_of_food[i-1])
            print("Your order has been placed,Enjoy your meal")
        else:
            return
        
        print("Do you want to go befores option?Enter yes")
        x=input()
        if x=="yes":
            print ("Please login to your account")
            self.login_user()
        else:
            return
        
       
    
    
    def show_order(self):
        print(self.list_of_order)
    
    
    def update_profile(self):
        print("NAME",self.name)
        print("DOB",self.dob)
        print("contact",self.contact)
        print("Email id",self.email)
        print("Password",self.password)
        x=input("What do you want to update : ")
        if(x=="NAME"):
            name= self.NAME()
            print("Profile updated susccessfully\n")
        elif(x=="DOB"):
            dob= self.DOB()
            print("Profile updated successfully\n")
        elif(x=="contact number"):
            contact=self.contact_num()
            print("Profile updated successfully\n")
        elif(x=="email Id"):
            email= self.email()
            print("Profile updated successfully\n")
        elif(x=="password"):
            Password=self.password()
            print("Profile updated successfully\n")
        else:
            print('You have not selected anythng to be updated')
class admin:
    def __init__(self):
        pass
    def admin_functions(self):
        print("*****What do you want to do*****\n1.View  the food item/related info \n2.To add more food items \n3.Edit information of food items")
        y=int(input())
        if y==1:
            self.show_food_list()
        elif y==2:
            self.add_more_food()
        elif y==3:
            self.edit_food_info()
        print("Do you want to be here more?Enter yes")
        x=input()
        x.lower()
        if x=="yes":
            self.admin_functions()
        else:
            return
    def login_admin(self):
        print("Enter your email id : ")
        admin_mail=input()
        print("Enter password :")
        admin_pass=input()
        print("\n*****Admin login successful*****\n")
        self.admin_functions()
    
    def show_food_list(self):
                   print(food_info)
    def add_more_food(self):
                   a={}
                   food_info[input("Enter food id : ")]=a
                   a["Name"]=input("Enter name of food item : ")
                   a["Quantity"]=input("Enter quantity per serving")
                   a["price"]=int(input("Enter price per serve : "))
                   a["discount"]=int(input("Offer customer some discount : "))
                   a["stocK_left"]=int(input("Enter stocks left :"))
    def edit_food_info(self):
        print("Enter id of food item you want to make changes on : ")
        x=input()
        if x not in food_info:
            print("There is no food item with this id")
        else:
            print(food_info[x])
            print("enter 1 to change the name \n enter 2 to change the quantity \n enter 3 to change the price \n enter 4 to change discount \n enter 5 to change the stock left \n enter 6 to delete the fod item from the menu")
            y=int(input())
            if y==1:
                food_info[x]["Name"]=input("Enter new name :")
            elif y==2:
                food_info[x]["Quantity"]=input("Enter new quantity :")
            elif y==3:
                food_info[x]["Pice"]=int(input("Enter new price : "))
            elif y==4:
                food_info[x]["Discount"]=int(input("Enter new discount : "))
            elif y==5:
                food_info[x]["stock left"]=int(input("Enter new stock left : "))
            elif y==6:
                del food_info[x]
            else:
                print("\n*****Data has been updated Successfully*****\n")
                return
print("Choose option\n1.User Login \n2.Admin Login")
x=int(input("Option : "))
if x==1:
    u=user()
    a=int(input("Are you already registered(0/1) : "))
    if a==1:
        u.login_user()
    elif a==0:
        u.register()
elif x==2:
    a=admin()
    a.login_admin()





