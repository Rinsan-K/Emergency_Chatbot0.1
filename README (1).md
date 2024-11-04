
# Emergency Preparedness Chatbot

This project is an AI-powered chatbot that provides emergency preparedness information. The bot is designed to answer user questions based on a specialized dataset, offering guidance in various emergency scenarios.

## Features
- **Real-time Q&A:** Responds to questions with relevant emergency preparedness information.
- **Retrieval-Augmented Generation (RAG):** Uses a semantic search system to find and deliver relevant information from a dataset.
- **User-Friendly Interface:** Accessible web interface built with HTML, CSS, and JavaScript.

## Technologies Used
- **Flask:** Backend framework to handle chatbot API requests.
- **FAISS:** Fast, efficient similarity search for retrieving relevant information.
- **Sentence Transformers:** For semantic embeddings of the dataset.
- **Gradio / HTML, CSS, JS:** Front-end interface for user interaction.

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone <repo_url>
   cd <repo_name>
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the Data:**
   - Make sure the dataset file (`emergency_preparedness.csv`) is in the project directory.
   - Run the indexing script to encode the dataset and build the FAISS index:
     ```bash
     python index_data.py
     ```

4. **Run the Application:**
   ```bash
   python app.py
   ```

5. **Access the Chatbot:**
   - Open a browser and navigate to `http://127.0.0.1:5000` to start chatting.

## Usage Guide
- Type any question related to emergency preparedness into the chatbox (e.g., “How do I prepare for childbirth during an emergency?”).
- The bot will respond with relevant guidance based on the dataset.

## Project Structure
- **app.py:** Main Flask application for handling chat requests.
- **index_data.py:** Script for encoding the dataset and building the FAISS index.
- **templates/index.html:** Front-end HTML template for the chatbot interface.
- **requirements.txt:** List of dependencies for easy setup.

## Example Interaction
User: "What supplies should I have in an emergency childbirth kit?"  
Bot: "For emergency childbirth, you should have large underpads, sterile gloves, alcohol, etc."

## License
This project is for educational purposes. Ensure proper attribution if you modify or distribute it.

---

Feel free to reach out with any questions or suggestions!
