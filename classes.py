class SubfieldsInAI():
    def subfields():
        lst = ['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        return lst

    def OddEven():
        num=int(input('Enter an number:'))
        if num%2==0:
            return num,' is a Even number'
        else:
            return num,' is a Odd number'

    def Eligible():
        gender=input('Enter the gender:')
        age=int(input('Enter the age:'))
        if gender=='Male' and age>=21:
            msg='Eligible'
        elif gender=='Female' and age>=18:
            msg='Eligible'
        else:
            msg='Not Eligible'
        return msg

    def percentage():
        Sub1=int(input('Subject 1:'))
        Sub2=int(input('Subject 2:'))
        Sub3=int(input('Subject 3:'))
        Sub4=int(input('Subject 4:'))
        Sub5=int(input('Subject 5:'))
        Total = Sub1 + Sub2 + Sub3 + Sub4 + Sub5
        Percentage = Total / 5
        return 'Total:', Total, 'Percentage:', Percentage

    def triangle():
        height = 32
        breadth = 34
        # Area of Triangle
        area = (height* breadth)/2
        print('Height:',height)
        print('Breadth:',breadth)
        print("Area formula: (Height * Breadth) / 2")
        print("Area of Triangle:", area)

        #Perimeter of triangle
        height1 = 2
        height2 = 4
        breadth2=4
        perimeter=(height1+height2+breadth2)
        print('Height1:',height1)
        print('Height2:',height2)
        print('Breadth2:',breadth2)
        print("Perimeter formula: Height1 + Height2 + Breadth")
        print("Perimeter of Triangle:", perimeter)



