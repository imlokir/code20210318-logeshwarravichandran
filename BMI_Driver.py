import json
from BMI_Calculator import bmicalc

bmi_ip = input("Enter JSON Data here:")

try:
    data = json.loads(bmi_ip)
except:
    print("Please enter a vaild JSON format")

try:
    height = [li['HeightCm'] for li in data]
    weight = [li['WeightKg'] for li in data]
    if len(data) > 0:
        BMI_value = bmicalc(height,weight)
        op =BMI_value.calculator()
except:
    print("Error during calculation of BMI")
