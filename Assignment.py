class Assignment:
    def SubFields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
        
    def OddEven():
        a = int(input("Enter a even number"))
        if a%2 == 0:
            print(a , " is even number")
        else:
            print(a, " is odd number")
            
    def Elegible():
        gender = input("Your gender : ")        
        age = int(input("Your age : "))
        
        
        if (gender == "Male" and age >= 21) or (gender == "Female" and age >= 18):
            print("Eligible")
        elif (gender == "Male" and age < 21) or (gender == "Female" and age < 18):
            print("Not Eligible")
        else:
            print("incorrect input")
            
    def Percentage():
        s1 = int(input("Subject1  "))
        s2 = int(input("Subject2  "))
        s3 = int(input("Subject3  "))
        s4 = int(input("Subject4  "))
        s5 = int(input("Subject5  "))
        
        total = s1+s2+s3+s4+s5
        percentage = total/5
        
        print("Total : ",total)
        print("Percentage :" , percentage)
    def area():
        h = int(input("Height: "))
        b = int(input("Breadth: "))
        area = (h*b)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of triangle = " , area)
    def perimeter():
        h1 = int(input("Height1: "))
        h2 = int(input("Height2: "))
        b = int(input("Breadth: "))        
        perimeter = h1+h2+b
        print("Perimeter formula: Height1+ Height2 + Breadth")
        print("Area oftri angle = " , perimeter)