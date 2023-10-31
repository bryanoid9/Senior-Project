from flask import Flask, Response, request, jsonify
import requests

app = Flask(__name__)

USDA_API_ENDPOINT = "https://api.nal.usda.gov/fdc/v1/foods/search"
API_KEY = "ysek0LUZ15TNFpE5YGLGUtTUz89egzsCwV6QpUt6"

@app.route('/fetch-food-data')
def fetch_food_data():
    food = request.args.get('food')
    
    params = {
        "query": food,
        "apiKey": API_KEY,
    }

    response = requests.get(USDA_API_ENDPOINT, params=params)
    print(response.text)

    
    if response.status_code == 200:
        data = response.json()
        if data['totalHits'] > 0:
            # Take the first item as an example
            food_data = data['foods'][0]
            nutrients = {
                "calories": None,
                "protein": None,
                "fat": None
            }
            for nutrient in food_data['foodNutrients']:
                if nutrient['nutrientName'] == "Energy":
                    nutrients["calories"] = nutrient["value"]
                elif nutrient['nutrientName'] == "Protein":
                    nutrients["protein"] = nutrient["value"]
                elif nutrient['nutrientName'] == "Total lipid (fat)":
                    nutrients["fat"] = nutrient["value"]

            return jsonify({
                "success": True,
                "name": food_data["description"],
                **nutrients
            })
    return jsonify({"success": False})

if __name__ == '__main__':
    app.run(debug=True)


