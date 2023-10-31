const API_KEY = "ysek0LUZ15TNFpE5YGLGUtTUz89egzsCwV6QpUt6";
const BASE_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"; // Replace with the actual API domain

document.addEventListener('DOMContentLoaded', function() {
    const mealTypes = ['breakfast', 'lunch', 'dinner'];
    
    mealTypes.forEach(mealType => {
        document.querySelector(`#${mealType}-button`).addEventListener('click', function() {
            fetchFoodForMeal(mealType);
        });
    });
});

function fetchFoodForMeal(mealType) {
    let inputField;
    
    switch(mealType) {
        case 'breakfast':
            inputField = document.querySelector(".meal-col:nth-child(1) input");
            break;
        case 'lunch':
            inputField = document.querySelector(".meal-col:nth-child(2) input");
            break;
        case 'dinner':
            inputField = document.querySelector(".meal-col:nth-child(3) input");
            break;
    }

    if(inputField) {
        searchForFood(inputField, inputField.value, mealType);
    }
}

function searchForFood(inputField, foodItem, mealType) {
    fetch(`${BASE_URL}/foods/search?query=${foodItem}`, {
        headers: {
            'Authorization': `Bearer ${API_KEY}`
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data && data.length) {
            const fdcId = data[0].fdcId; 
            fetchFoodData(inputField, fdcId, mealType);
        } else {
            alert("No results found for the entered food item.");
        }
    })
    .catch(error => {
        console.error("Error searching for food:", error);
    });
}

function fetchFoodData(inputField, fdcId, mealType) {
    fetch(`${BASE_URL}/food/${fdcId}`, {
        headers: {
            'Authorization': `Bearer ${API_KEY}`
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data) {
            let tableBody = document.querySelector(`#${mealType}-data`);
            let newRow = tableBody.insertRow();
            
            let foodCell = newRow.insertCell(0);
            let calorieCell = newRow.insertCell(1);
            let proteinCell = newRow.insertCell(2);
            let fatCell = newRow.insertCell(3);
            
            foodCell.textContent = data.description; 
            calorieCell.textContent = data.calories;  
            proteinCell.textContent = data.protein;
            fatCell.textContent = data.fat;

            inputField.value = ""; 
        } else {
            alert("Failed to fetch food data.");
        }
    })
    .catch(error => {
        console.error("Error fetching food data:", error);
    });
}