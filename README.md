# Emergency_Chatbot0.1
Emergency Preparedness Chatbot Project:- This project will create a chatbot application that helps users find emergency preparedness information specifically related to childbirth. It’s designed to be user-friendly and provide relevant information from a CSV data file when users ask questions.


Project Goals:-
Flask API: Set up a backend to handle user queries and respond with answers from the dataset.
Data Processing: Use pandas to process and retrieve data from a CSV file.
Gradio Interface: Provide a simple web-based interface where users can ask questions.
Deployment: Package and organize the project for easy setup and usage.


Project Structure:-
emergency_chatbot_env/
├── app.py                    # Main Flask application
├── index_data.py          #file prepares and saves a searchable FAISS index of text embeddings, enabling fast similarity search in the chatbot by loading the index in app.py.
├── emergency_preparedness.csv   # CSV file containing emergency data
├── requirements.txt          # List of required libraries
└── README.md                 # Project description and setup guide
├── templates ├── index.html # frontent page code
