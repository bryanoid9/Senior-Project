Project Report: NutriBot Flask Application

Overview:
NutriBot is a web-based application designed to provide users with an interactive platform for nutrition and fitness advice. Utilizing a chatbot powered by GPT-3.5, NutriBot engages users in conversation about their health goals, providing personalized recommendations for diet and exercise. The application also features a calorie tracker that allows users to log their food intake and monitor their nutritional data. 

Roles & Responsibilities:
Eduardo Castro Becerra - Full Stack Developer for website; handled frontend and backend responsibilities.
Bryan Martinez Ramirez - Full Stack Developer for website; handled frontend and backend responsibilities.

Objective:
The primary objective of NutriBot is to make nutritional guidance accessible and engaging. By integrating advanced AI through OpenAI's GPT-3.5 turbo model, NutriBot offers an interactive experience that goes beyond traditional calorie counting apps. It aims to be a companion for users looking to make informed decisions about their diet and exercise routines.

Technical Overview:
NutriBot is built using the Flask framework, a Python web framework known for its simplicity and flexibility. The backend structure is organized into several components, including user authentication, chatbot interaction, and calorie tracking. Here are the key technical features:

Flask: Serves as the backbone of the web application, handling HTTP requests, routing, and rendering templates.
Flask-SQLAlchemy: Manages database interactions, providing an ORM layer for SQL operations.
Flask-Bcrypt: Ensures secure password hashing for user authentication.
OpenAI API: Powers the intelligent chatbot, using the gpt-3.5-turbo model for generating human-like text responses.
SQLite/MySQL: SQLite is used for development, with MySQL as the production database for storing user data and food logs.
HTML/CSS/JS: Frontend technologies used to create a responsive and interactive user interface.
Key Features
User Authentication: Secure signup and login functionality.
Chatbot Interaction: Real-time conversation with the NutriBot for nutrition and fitness advice.
Calorie Tracker: Logging and analysis of daily food intake with nutritional breakdown.

Challenges and Solutions:
Throughout the development of NutriBot, several challenges were encountered and overcome:
Integration of GPT-3.5: Ensuring seamless communication between the Flask backend and the OpenAI API was crucial. This was achieved by creating robust API request handlers within Flask. One of the problems we faced was when putting the code into github our API was published as well, therefore making the api key unusable. 
User Session Management: Flask's built-in session management was utilized, and Flask-Bcrypt was used for password hashing to maintain user security. One issue we had was the routing within Flask.
AWS hosting: While exploring options for hosting our website, we initially considered AWS for its robust infrastructure and scalability. However, we encountered several complexities and challenges with AWS's technical documentation and setup process. Given these difficulties and the steep learning curve, we decided to pivot towards local hosting. This decision was made to ensure a more manageable and straightforward deployment, allowing us to focus on the core functionalities of our project without getting overwhelmed by the intricacies of AWS hosting.

Future Enhancements:
Features that could be added upon working on the website more:
Advanced Analytics: Implement machine learning to provide trend analysis and predictive suggestions.
Community Features: Add forums or groups for users to share experiences and motivate each other.
AWS website hosting.

Conclusion:
NutriBot stands at the intersection of technology and wellness, embodying a tool that harnesses the power of AI to foster healthier lifestyle choices. As the project grows, it will continue to embrace new technologies and feedback from its user base to improve and expand its capabilities.

