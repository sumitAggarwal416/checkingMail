''' I, Sumit Aggarwal, student number:000793607, certify that all code submitted
is my own code, that I have not copied it from any other source. I also certify
that, I have not allowed anyone else to copy my code.
'''
import re
address= input("Enter your full street address ")
add=address.split()
length=len(add)
x=False
while x==False:
    if not re.match("^[0-9]+$",add[0]) or length>3:
        print("Invalid Address")
        address= input("Enter your full street address ")
        x=False
    else:
        x=True
    x=False
    while x==False:
        city=input("Enter your city ")
        if city.isalpha()==False:
            print("Invalid City")
            x=False
        else:
            x=True
        city=city.capitalize()
                        
        x=False
        while x==False:
            prov= input("Enter your province ")
            if len(prov)!=2:
                print("Inavlid province")
                x=False
            else:
                x=True
                prov=prov.upper()
                if prov.isalpha()==True:
                    x=False
                    while x==False:
                        postal= input("Enter your postal code ")
                        if len(postal)>7:
                            print("Enter a valid postal code")
                            x=False
                        else:
                            postal=postal.upper()
                            post=list(postal)
                            if post[0].isalpha()==False and post[1].isdecimal()==False and post[2].isalpha()==False and post[4].isdecimal()==False and post[5].isalpha()==False and post[6].isdecimal()==False:
                                print("Invalid Postal Code")
                                x=False
                            else:
                                if (prov=='AB' and postal.startswith('T')) or (prov=='BC' and postal.startswith('V')) or (prov=='MB' and postal.startswith('R')) or (prov=='SK' and postal.startswith('S')):
                                    shippingcost=12
                                    print("Shipping to",add[0],add[1].title(),add[2].title(),", ",city,", ",prov," - ",postal[0:3]+" "+postal[3:7]," will cost $",shippingcost)
                                elif (prov=='NB' and postal.startswith('E')) or (prov=='NL' and postal.startswith('A')) or (prov=='NS' and postal.startswith('B')) or (prov=='PE' and postal.startswith('C')):
                                    shippingcost=15
                                    print("Shipping to",add[0],add[1].title(),add[2].title(),", ",city,", ",prov," - ",postal[0:3]+" "+postal[3:7]," will cost $",shippingcost)
                                elif (prov=='NT' and postal.startswith('X')) or (prov=='NU' and postal.startswith('X')) or (prov=='YK' and postal.startswith('Y')):
                                    shippingcost=20
                                    print("Shipping to",add[0],add[1].title(),add[2].title(),", ",city,", ",prov," - ",postal[0:3]+" "+postal[3:7]," will cost $",shippingcost)
                                elif (prov=='ON' and (postal.startswith('K') or postal.startswith('L') or postal.startswith('M') or postal.startswith('N') or postal.startswith('P'))) or (prov=='QC' and (postal.startswith('G') or postal.startswith('H') or postal.startswith('J'))):
                                    shippingcost=8
                                    print("Shipping to",add[0],add[1].title(),add[2].title(),", ",city,", ",prov," - ",postal[0:3]+" "+postal[3:7]," will cost $",shippingcost)
                                x=True
                     
