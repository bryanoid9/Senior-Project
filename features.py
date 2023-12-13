# features.py
from flask import Blueprint, request, jsonify, render_template, session
import requests
from models import db, FoodLog, User

feature_blueprint = Blueprint('feature', __name__, url_prefix='/features')

@feature_blueprint.route('/calorie-tracker')
def calorie_tracker():
    return render_template('CalorieTracker.html')

@feature_blueprint.route('/submit-food', methods=['POST'])
def submit_food():
    data = request.get_json()
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
                "nutrients": [],
                "fdcId": food_item.get('fdcId')  # or another unique identifier
            }

            nutrients_dict = {
                "Protein": 0, 
                "Total lipid (fat)": 0, 
                "Carbohydrate, by difference": 0, 
                "Energy": 0
            }

            for nutrient in food_item['foodNutrients']:
                if nutrient['nutrientName'] in nutrients_dict:
                    nutrients_dict[nutrient['nutrientName']] = nutrient['value']
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

@feature_blueprint.route('/log-selected-food', methods=['POST'])
def log_selected_food():
    data = request.get_json()
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "User not logged in"}), 401
    
    food_name = data.get ("name")
    calories = next((nutrient.get("value") for nutrient in data.get("nutrients", []) if nutrient.get("name") == "Energy"), 0)
    protein = next((nutrient.get("value") for nutrient in data.get("nutrients", []) if nutrient.get("name") == "Protein"), 0)
    fat = next((nutrient.get("value") for nutrient in data.get("nutrients", []) if nutrient.get("name") == "Total lipid (fat)"), 0)
    carbs = next((nutrient.get("value") for nutrient in data.get("nutrients", []) if nutrient.get("name") == "Carbohydrate, by difference"), 0)

    new_food_log = FoodLog(
        user_id=user_id,
        food_name=food_name,
        calories=calories,
        protein=protein,
        fat=fat,
        carbohydrate=carbs
    )

    db.session.add(new_food_log)
    try:
        db.session.commit()
        return jsonify({"success": True, "foodLogged": food_name})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500