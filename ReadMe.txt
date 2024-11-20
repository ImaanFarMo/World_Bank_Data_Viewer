Project Name: World Bank Data Viewer​
Developer Name: Imaan Jaffer

Please view PPT for example video of website
Git Repo URL: 


File Structure: 

Backend :
    database.py: Manages MongoDB connection and operations.
    main.py: Defines the FastAPI application and routes.
    model.py: Defines data models for MongoDB.

Frontend:
    src
        App.js: Main React component managing application state and routing.
        components/ChoroplethMap.js: makes a choropleth map visualization of country data.
        components/WorldBank.js: Contains the delete and update country handler 
        components/WorldBankView.js: Displays a list of countries and their corresponding data.



Tech Stack:
    Backend:
        FastAPI
        MongoDB
    Frontend:
        React.js
        


Setup Instructions:

Backend Setup

    In Terminal:
    cd backend

    Create and activate a virtual environment: python -m venv env
    Install the required dependencies: pip install -r requirements.txt
    Run: pipenv shell

    On a new terminal run: uvicorn main:app --reload

    The backend will be running on http://127.0.0.1:8000.

    The database is connected to yyour local MongoDB compass, which can be installed on your device

Frontend Setup:

    In Terminal:    
    cd frontend

    Install the required dependencies: npm install axios 

    Run: npm start

    The frontend will be running on http://localhost:3000.



How to Use:

    Start the backend and frontend servers.
    Open the application in your browser at http://localhost:3000.
    Use the form to:
        Add a new country by entering details manually or fetching data from the World Bank API.
        View existing countries in a list or on a map.
        Delete a country from the database.


Future Enhancements:

    Better user interface
    A working edit function 
    Add more World Bank indicators for richer data visualization.
    Integrating some sort of World API

