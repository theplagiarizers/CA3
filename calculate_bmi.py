from get_bmi_category import get_bmi_category 
from flask import request


def calculate_bmi():
    data = request.get_json()
    weight = data['weight']
    height = data['height']

    bmi = weight / (height ** 2)
    category = get_bmi_category(bmi)

    result = {
        'bmi': bmi,
        'category': category
    }

    return result

def main():
    
    print(get_bmi_category(20))
    
    
main()    