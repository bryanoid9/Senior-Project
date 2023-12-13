function fetchFoodForMeal(mealType) {
    // Assuming you have inputs with ids like 'breakfast-input', 'lunch-input', 'dinner-input'
    const inputId = `${mealType}-input`; 
    const foodItem = document.getElementById(inputId).value;

    console.log(foodItem); // This will log the food item to the console

    fetch(`/features/submit-food`, {
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
        foodElement.onclick = () => selectFoodOption(food, index, mealType);
        container.appendChild(foodElement);
    });
}

function selectFoodOption(food, index, mealType) {
    console.log(`Selected Food #${index + 1}:`, food);
    // Send the selected food to the backend for logging
    fetch(`/features/log-selected-food`, { // Adjust the endpoint as needed
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(food) // Send the entire selected food item
    })
    .then(response => response.json())
    .then(data => {
        if(data.success) {
            console.log('Food logged successfully:', data.foodLogged);

            //update the food table with the selected food's details 
            updateFoodTable(food, mealType);
            
            //clear the options container to signify seleciton 
            const containerId = `${mealType}-options-container`;
            document.getElementById(containerId).innerHTML = '';
        } else {
            console.error('Failed to log food:', data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });

}

function updateFoodTable(food, mealType) {
    const tableBodyId = `${mealType}-data`;
    const tableBody = document.getElementById(tableBodyId);

    // Create a new row
    const row = document.createElement('tr');

    // Add cells for food name, calories, protein, and fat
    const foodCell = document.createElement('td');
    foodCell.textContent = food.name;
    row.appendChild(foodCell);

    const caloriesCell = document.createElement('td');
    caloriesCell.textContent = food.nutrients.find(n => n.name === 'Energy')?.value || 'N/A';
    row.appendChild(caloriesCell);

    const proteinCell = document.createElement('td');
    proteinCell.textContent = food.nutrients.find(n => n.name === 'Protein')?.value || 'N/A';
    row.appendChild(proteinCell);

    const fatCell = document.createElement('td');
    fatCell.textContent = food.nutrients.find(n => n.name === 'Total lipid (fat)')?.value || 'N/A';
    row.appendChild(fatCell);

    // Append the row to the table body
    tableBody.appendChild(row);
}
