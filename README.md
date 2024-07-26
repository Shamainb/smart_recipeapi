Smart Recipe api

## Overview

The Smart Recipe API allows users to search for recipes, manage their favorite recipes, and generate grocery lists based on selected recipes. This API leverages FastAPI for the backend framework and Firebase for user authentication and data storage. It uses the Spoonacular API to fetch recipe data.

## Features

- **User Authentication:**
  - Sign up and log in using Firebase Authentication.
  - Secure endpoints using JWT tokens.

- **Recipe Management:**
  - Search for recipes by ingredients, cuisine, or dietary restrictions.
  - Retrieve detailed recipe information.

- **Favorites:**
  - Allow users to save their favorite recipes.
  - Retrieve a list of favorite recipes.

- **Grocery List Generator:**
  - Generate a grocery list based on selected recipes.
  - Allow users to mark items as purchased.

- **User Profiles:**
- Store user preferences, dietary restrictions, and favorite ingredients in Firebase Firestore.
  - Customize recipe recommendations based on user profiles.

## Technology Stack

- **Backend Framework:** FastAPI
- **Database:** Firebase Firestore
- **Authentication:** Firebase Authentication
- **Recipe Data:** Spoonacular API

## Setup Instructions

1. Clone the repository.
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
