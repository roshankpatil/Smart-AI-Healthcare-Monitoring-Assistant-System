def chatbot_response(text):
    text = text.lower()

    if "heart disease" in text:
        return "Heart disease occurs due to reduced blood flow to the heart."
    elif "symptoms" in text:
        return "Common symptoms include chest pain, shortness of breath, fatigue."
    elif "prevention" in text:
        return "Exercise, healthy diet, stress control, and avoiding smoking help prevent heart disease."
    elif "emergency" in text:
        return "Please contact a doctor or emergency services immediately."
    elif "Is my heart rate normal?" in text:
        return "A normal resting heart rate for adults is usually between 60 and 100 beats per minute."
    elif "How much water should I drink daily?" in text:
        return "Most adults should aim for 2–3 liters per day, depending on activity level and climate."
    else:
        return "I am an AI healthcare assistant. Ask about heart disease, symptoms, or prevention."

