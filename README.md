# 🌤️ Simple Weather Agent using Python

A beginner-friendly Python Weather Agent that takes a city name from the user, connects to the OpenWeatherMap API, collects live weather data, and displays the weather report.

---

## 📌 Project Name

**Simple Weather Agent using Python**

---

## 🎯 Goal

Create an AI agent that takes a city name from the user and shows weather information.

---

## 🔄 Weather Agent Workflow

```text
User enters city name
        ↓
Weather Agent receives city
        ↓
Agent calls Weather API
        ↓
API sends weather data
        ↓
Agent displays result
```

---

## 🛠️ Tools & Technologies

- Python
- OpenWeatherMap API
- Requests
- python-dotenv
- JSON
- VS Code
- Internet

---

## 📁 Project Structure

```text
Weather-Agent/
│
├── weather_agent.py
├── README.md
├── requirements.txt
├── .env
└── .gitignore
```

---

## 📦 Installation

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install requests python-dotenv
```

---

## 🔑 OpenWeatherMap API Key

Create a free account and get your API key from:

https://openweathermap.org/api

**Do not put your API key directly inside `weather_agent.py`.**

Create a `.env` file:

```env
OPENWEATHER_API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual OpenWeatherMap API key.

---

## 🔐 API Key Security

The API key is loaded from the `.env` file using `python-dotenv`.

Example:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")
```

The `.env` file should **not** be uploaded to GitHub.

Add this to `.gitignore`:

```text
.env
__pycache__/
```

---

## ▶️ How to Run

Open the terminal inside the project folder and run:

```bash
python weather_agent.py
```

Then enter a city name:

```text
Enter city name or type exit: Udaipur
```

---

## 🌦️ Sample Output

```text
Weather Report
City: Udaipur
Temperature: 32.5 °C
Feels Like: 33.0 °C
Humidity: 45 %
Weather: clear sky
Wind Speed: 3.2 m/s
```

---

## 🚪 Exit the Program

Type:

```text
exit
```

The program will display:

```text
Thank you for using Weather Agent.
```

---

## 🤖 Agentic AI Workflow

### User Goal

```text
"What is the weather in Udaipur?"
```

### Agent Process

1. Identify city
2. Call weather API
3. Get temperature, humidity, and wind
4. Format answer
5. Give final response

---

## 📊 Weather Information

The Weather Agent displays:

- City
- Temperature
- Feels Like Temperature
- Humidity
- Weather Condition
- Wind Speed

---

## 🧠 Concepts Learned

This project helps beginners understand:

- Python input
- API integration
- HTTP requests
- JSON data
- Dictionary data access
- Conditions
- Environment variables
- API key security
- Basic AI agent workflow

---

## 🚀 Future Extensions

The project can be extended with:

1. Streamlit interface
2. Voice input
3. Weather forecast
4. Rain alert
5. WhatsApp weather bot
6. Email weather report
7. Travel suggestion
8. Agentic AI planning

---

## 📚 Project Description

A Weather Agent is a beginner-friendly AI project that takes a city name, connects to a weather API, collects live weather data, and displays temperature, humidity, weather condition, and wind speed.

This project helps beginners understand API, JSON, Python input, conditions, and real-world AI agent workflow.

---

## ⚠️ Important Security Note

**Never upload your real API key to a public GitHub repository.**

Keep your API key inside:

```text
.env
```

and make sure `.env` is included in:

```text
.gitignore
```

---

## 👨‍💻 Author

**AMARCHAND TIGAYA PUSHKAR**

GitHub:  
`https://github.com/amarchand-tigaya-pushkar`