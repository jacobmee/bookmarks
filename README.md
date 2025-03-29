# Flask Bookmark App

This project is a simple Flask application that serves as a personal bookmark page. It allows users to access multiple hyperlinks to various HTTP addresses.

## Project Structure

```
flask-bookmark-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── templates
│   │   └── index.html
│   └── static
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-bookmark-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```
   flask run
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

The main page will display a list of hyperlinks that you can click to navigate to your favorite websites. You can customize the links in the `index.html` file located in the `app/templates` directory. 

## License

This project is open-source and available under the MIT License.