
# Health Care Assistant 👨‍⚕️ 🩺 🏥

### Overview
The Health Care Assistant is a web application designed to assist with the analysis of medical reports. Leveraging advanced generative AI models, the app allows users to upload medical images and receive detailed analysis, including identification of anomalies, diseases, conditions, and health issues based on the uploaded report.

#### Preview-link
https://karan-kr-451-health-care-with-gemini-app-wjajal.streamlit.app/

### Features
- Report Upload: Users can upload medical reports in PNG, JPG, or JPEG formats.
- AI-Powered Analysis: Utilizes the Gemini 1.5 Flash model to generate a comprehensive analysis report based on the uploaded medical report.
- User-Friendly Interface: Clean and intuitive UI built with Streamlit for ease of use.

### Installation
#### Prerequisites
- Python 3.9+
- Streamlit
- google-generativeai
- python-dotenv
## Installation
#### Clone the Repository

```cmd
  git clone https://github.com/karan-kr-451/Health-Care-With-Gemini.git
  cd Health-Care-With-Gemini
```

#### Install Dependencies
```cmd
pip install -r requirements.txt

```
#### Set Up Environment Variables
Create a .env file in the root directory of the project and add your API key:

```plaintext
API_KEY=your_google_generative_ai_api_key
```

#### Run the Application
```cmd
streamlit run app.py
```

#### Usage
1. Open the web application in your browser.
2. Upload a medical report using the file uploader.
3. Click the "Generate Analysis" button to receive a detailed analysis report.