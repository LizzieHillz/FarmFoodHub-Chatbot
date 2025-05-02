# 🌾 FarmFoodHub-Chatbot

**FarmFoodHub Chatbot** is a server-side application that connects to a PostgreSQL database and responds to user queries about farm produce via a chatbot interface. It is built using **FastAPI** and designed to work with **Dialogflow**, providing real-time data on farmers, their products, prices, and locations.

This backend is part of the larger **FarmFoodHub** project — an AI-powered platform tackling food insecurity, waste management, and fair pricing for farmers.

---

## 🚀 Features

- 🔎 **Find Farmers**: Accepts POST requests at `/find-farmer` to search for farmers based on produce.
- 🧠 **Dialogflow Integration**: Integrates seamlessly with Dialogflow to handle chatbot interactions.
- 💃 **Database Integration**: Connects to a PostgreSQL database (hosted on Railway) containing up-to-date farmer and produce information.
- 🌐 **Scalable Backend**: Built using FastAPI and Uvicorn for fast, asynchronous performance.

---

## 🛠️ Technologies Used

- **FastAPI** – Python web framework for building fast APIs.
- **PostgreSQL** – Relational database for storing farmer and produce data.
- **PyODBC** – Library to connect Python with SQL databases.
- **Uvicorn** – ASGI server to run FastAPI apps.
- **Dialogflow** – Google’s NLP service for building intelligent chatbots.

---

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL (or a cloud-hosted alternative like [Railway](https://railway.app))
- [FastAPI](https://fastapi.tiangolo.com/) and [Uvicorn](https://www.uvicorn.org/)

---

## ⚙️ Getting Started

1. **Navigate to your project folder**  
   ```bash
   cd FarmFoodHub-Backend
   ```

2. **Create a virtual environment**  
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**

   - On PowerShell (after setting execution policy):  
     ```bash
     .\.venv\Scripts\activate
     ```

   - On CMD:  
     ```cmd
     .venv\Scripts\activate.bat
     ```

4. **Install required packages**  
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```

6. **Test the Endpoint**
   - URL: `http://localhost:8000/find-farmer`
   - Method: `POST`
   - JSON body:
     ```json
     {
       "queryResult": {
         "parameters": {
           "produce": "tomatoes"
         }
       }
     }
     ```

---

## 🧪 Sample Response
```json
{
  "fulfillmentText": "Here are farmers selling Tomatoes:\n1. 👨‍🌾 John Agric (Jos)📦 Product: Tomatoes💰 Price: ₦300.00 per kg\n2. 👨‍🌾 Jadsfam (Jos)📦 Product: Tomatoes💰 Price: ₦280.00 per kg\n3. 👨‍🌾 Jyna Produce (Jos)📦 Product: Tomatoes💰 Price: ₦285.00 per kg"
}
```

---

## 📌 Future Plans

- 🔒 **User Authentication**: Add secure login/signup for farmers and customers.
- 🏥 **Order Placement**: Enable customers to place and track orders directly from the chatbot.
- 📊 **Analytics Dashboard**: Provide farmers with insights about demand trends.
- 📍 **Geo-mapping**: Show nearest farmers based on user location.
- 💬 **Multilingual Support**: Make the chatbot multilingual to serve diverse regions.
- ☁️ **Deploy to Hugging Face Spaces or Vercel** for public accessibility.

---

## 🤝 Contributing

Interested in contributing or suggesting features? Feel free to fork the repo, create a new branch, and submit a pull request.

---

## 🧑‍💻 Author

**Chisom Elizabeth Omegor**  
AI/ML Enthusiast | Data Analyst  
📧: omegorchisom25@gmail.com.com
LinkedIn (http://www.linkedin.com/in/chisom-elizabeth-omegor-a21906233)

