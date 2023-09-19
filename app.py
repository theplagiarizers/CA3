from flask import Flask
from calculate_bmi import calculate_bmi
from get_bmi_category import get_bmi_category
from hello import hello


app = Flask(__name__)

@app.route ('/')

@app.route('/bmi', methods=['POST'])
# def calculate_bmi():
#     data = request.get_json()
#     weight = data['weight']
#     height = data['height']

#     bmi = weight / (height ** 2)
#     category = get_bmi_category(bmi)

#     result = {
#         'bmi': bmi,
#         'category': category
#     }

#     return result


# def get_bmi_category(bmi):
#     if bmi < 18.5:
#         return 'Underweight'
#     elif bmi < 25:
#         return 'Normal weight'
#     elif bmi < 30:
#         return 'Overweight'
#     else:
#         return 'Obese'
def empty():
    print('working')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)