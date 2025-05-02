from fastapi import FastAPI, Request
from pydantic import BaseModel
from sqlalchemy import create_engine, text

class DialogflowRequest(BaseModel):
    queryResult: dict

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my chatbot API!"}

# PostgreSQL connection string from Railway
DATABASE_URL = "postgresql://postgres:gJGOGUrxkVLPMVGLopEYbkXaqpItQUXs@caboose.proxy.rlwy.net:40581/railway"

engine = create_engine(DATABASE_URL)

@app.post("/find-farmer")
async def find_farmer(req: DialogflowRequest):
    try:
        produce = req.queryResult["parameters"]["Farm-Produce"]

        with engine.connect() as connection:
            query = text("""
                SELECT "FarmerName", "Product", "Location", "PricePerUnit", "Unit"
                FROM "farmers"
                WHERE LOWER("Product") = LOWER(:produce)
            """)
            result = connection.execute(query, {"produce": produce})
            rows = result.fetchall()

        if rows:
            response_text = f"Here are farmers selling {produce.title()}:\n"
            for idx, row in enumerate(rows):
                response_text += (
                    f"{idx+1}. 👨‍🌾 {row.FarmerName} ({row.Location})\n"
                    f"📦 Product: {row.Product}\n"
                    f"💰 Price: ₦{row.PricePerUnit:.2f} per {row.Unit}\n"
                )
        else:
            response_text = f"Sorry, no farmer is currently selling {produce.title()}."

        return {"fulfillmentText": response_text}

    except Exception as e:
        return {"fulfillmentText": f"Something went wrong: {str(e)}"}
