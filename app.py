from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('CalorieTracker.html')

@app.route('/submit-food', methods=['POST'])
def submit_food():
    data = request.json
    food_item = data.get('foodItem')

    # API endpoint and key
    url = "https://api.nal.usda.gov/fdc/v1/foods/search"
    api_key = 'ysek0LUZ15TNFpE5YGLGUtTUz89egzsCwV6QpUt6'

    # Define the parameters for the USDA API request
    params = {
        'api_key': api_key,
        'query': food_item,
        'dataType': ["Survey (FNDDS)"],
        'pageSize': 5,
    }

    # Make the request to the USDA API
    response = requests.get(url, params=params)

    # Process the response
    if response.status_code == 200:
        data = response.json()
        foods_data = []
        for food_item in data['foods']:
            food_info = {
                "name": food_item['description'],
                "nutrients": []
            }
            for nutrient in food_item['foodNutrients']:
                if nutrient['nutrientName'] in ["Protein", "Total lipid (fat)", "Carbohydrate, by difference", "Energy"]:
                    food_info["nutrients"].append({
                        "name": nutrient['nutrientName'],
                        "value": nutrient['value'],
                        "unit": nutrient['unitName']
                    })
            foods_data.append(food_info)
        return jsonify(foods_data)
    else:
        print("Failed to retrieve data:", response.status_code)
        return jsonify({"error": "Failed to retrieve data"}), response.status_code
        '''
        data = response.json()
        for food_item in data['foods']:
            print(f"Name of the food item: {food_item['description']}")
            for nutrient in food_item['foodNutrients']:
                if nutrient['nutrientName'] in ["Protein", "Total lipid (fat)", "Carbohydrate, by difference", "Energy"]:
                    print(f"  {nutrient['nutrientName']}: {nutrient['value']} {nutrient['unitName']}")
            print()
        return "Food data printed to the terminal"
    else:
        print("Failed to retrieve data:", response.status_code)
        return "Failed to retrieve data"
        '''

if __name__ == '__main__':
    app.run(debug=True)
