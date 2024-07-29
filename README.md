Smart Recipe API

Features
Recipe Search: Allows users to search for recipes based on various criteria.
Recipe Details: Provides detailed information about each recipe, including ingredients and preparation steps.
Responsive Design: Ensures a user-friendly interface across different devices.

Technology Stack
Backend Framework: Django
Frontend Technologies: HTML, CSS
API Integration: Spoonacular API

Installation

To run the Smart Recipe API locally, follow these steps:

Clone the Repository:
git clone https://github.com/yourusername/smart-recipe-api.git
cd smart-recipe-api

Create a Virtual Environment:
python -m venv venv
source venv/bin/activate

Install Dependencies:
pip install -r requirements.txt

Configure Environment Variables:
SPOONACULAR_API_KEY=your_spoonacular_api_key

Run Migrations:
python manage.py migrate

Start the Development Server:
python manage.py runserver

Open Your Browser:
Visit http://127.0.0.1:8000 to access the application.

API Endpoints

Search Recipes
Endpoint: /api/recipes/search/
Method: GET
Parameters:
query (string): Search term for recipes
Response:
json
{
  "recipes": [
    {
      "id": "recipe_id",
      "title": "Recipe Title",
      "summary": "Brief description",
      "image": "URL to image"
    }
  ]
}

Recipe Details
Endpoint: /api/recipes/{id}/
Method: GET
Parameters:
id (string): Recipe ID
Response:
json
{
  "id": "recipe_id",
  "title": "Recipe Title",
  "ingredients": [
    "Ingredient 1",
    "Ingredient 2"
  ],
  "instructions": "Cooking instructions here",
  "image": "URL to image"
}

Development
Code Style: Follow PEP 8 guidelines.
Testing: Add and run tests in the tests directory.
Contributing: Open issues or submit pull requests for improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Spoonacular API: For providing the recipe data.
Django: For the robust backend framework.
