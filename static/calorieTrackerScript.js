function fetchFoodForMeal(mealType) {
    // Assuming you have inputs with ids like 'breakfast-input', 'lunch-input', 'dinner-input'
    const inputId = `${mealType}-input`; 
    const foodItem = document.getElementById(inputId).value;

    console.log(foodItem); // This will log the food item to the console

    fetch(`/submit-food`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ foodItem: foodItem })
    })
    .then(response => response.json())
    .then(data => {
        //console.log(data); // For now, just log the result to the console
        displayFoodOptions(data, mealType); //Call with fetched dat and meal type
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

//function to display food options
function displayFoodOptions(foodsData, mealType) {
    const containerId = `${mealType}-options-container`;
    const container = document.getElementById(containerId);
    container.innerHTML = ''; // Clear existing options

    foodsData.forEach((food, index) => {
        const foodElement = document.createElement('button');
        foodElement.innerText = food.name;
        foodElement.onclick = () => selectFoodOption(food, index);
        container.appendChild(foodElement);
    });
}

function selectFoodOption(food, index) {
    console.log(`Selected Food #${index + 1}:`, food);
}