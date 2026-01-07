import random

def get_live_vitals():
    return {
        "Heart Rate": random.randint(60, 120),
        "Blood Pressure": f"{random.randint(100,140)}/{random.randint(60,90)}",
        "Oxygen Level": random.randint(92, 100),
        "Body Temperature": round(random.uniform(97, 101), 1)
    }
