
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ----- CONFIG -----
FULL_NAME = "sneh_pratap"
DOB = "15042003"
EMAIL = "pratapsneh.sp@gmail.com"
ROLL_NUMBER = "22BCE2965"

class InputData(BaseModel):
    data: List[str]

@app.get("/")
def read_root():
    return {"message": "API is running. Use /bfhl POST endpoint for array processing."}

@app.post("/bfhl")
async def process_data(request: InputData):
    try:
        data = request.data
        even_numbers, odd_numbers, alphabets, specials = [], [], [], []
        total_sum = 0

        for item in data:
            if item.isdigit():
                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
            elif item.isalpha():
                alphabets.append(item.upper())
            else:
                specials.append(item)

        # concat_string = alphabets reversed + alternating caps
        concat_raw = "".join(alphabets)[::-1]
        concat_final = "".join(
            ch.lower() if i % 2 else ch.upper()
            for i, ch in enumerate(concat_raw)
        )

        return {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": specials,
            "sum": str(total_sum),
            "concat_string": concat_final
        }

    except Exception as e:
        return {"is_success": False, "error": str(e)}

