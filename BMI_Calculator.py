class bmicalc:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calculator(self):
        i= 0
        print("\nBMI Score for the given JSON Input:")
        for h, w in zip(self.height, self.weight):
            i +=1
            bmi = w/((h/100)**2)
            if ( bmi < 18.4):
                condition = "severely underweight."
                hrisk = "Malnutrition Risk"
            elif ( bmi >= 18.5 and bmi < 24.9):
                condition ="in normal weight."
                hrisk = "Low risk"
            elif ( bmi >= 25 and bmi < 29.9):
                condition ="overweight"
                hrisk = "Enhanced risk"
            elif ( bmi >= 30 and bmi < 34.9):
                condition ="moderately obese"
                hrisk = "Medium risk"
            elif ( bmi >=35 and bmi < 39.9 ):
                condition ="severely obese"
                hrisk = "High risk"
            else:
                condition ="very Severely obese"
                hrisk = "Very High risk"
            print("\nPerson {2} has BMI Score :{0}, and the person is  {1}\nHealth Risk: {3}\n".format(bmi,condition,i,hrisk))
