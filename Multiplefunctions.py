class multiplefunction:
    def Subfields():
        Lists= ["Machine learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language processing"]
        print("Sub-fields in AI are:")
        for subfield in Lists:
            print(subfield)
    def OddEven():
        num= int(input("Enter a number:"))
        if(num%2==0):
            print(num,"is Even number")
        else:
            print(num,"is Odd number")
    def Elegible():
        Gender= input("Your Gender:")
        Age= int(input("Your Age:"))
        if (Gender=="Male" and Age>=21):
            print("Elegible")
        elif(Gender=="Female" and Age>=18):
            print("Elegible")
        else:
            print("Not Elegible")
    def percentage():
        sub1= int(input("Subject1="))
        sub2= int(input("Subject2="))
        sub3= int(input("Subject3="))
        sub4= int(input("Subject4="))
        sub5= int(input("Subject5="))
        totalmarks= sub1+sub2+sub3+sub4+sub5
        print("Total:",totalmarks)
        per= (totalmarks / 500)*100
        print("Percentage:",per)
    def triangle():
        height= int(input("Height:"))
        base= int(input("Base:"))
        print("Area formula: (Height*Base)/2")
        Area= (height*base)/2
        print("Area of triangle:",Area)
        side1=int(input("Side1:"))
        side2=int(input("Side2:"))
        base=int(input("Base:"))
        print("Perimeter formula: Side1+Side2+Base")
        Perimeter= side1+side2+base
        print("Perimeter of Triangle:",Perimeter)