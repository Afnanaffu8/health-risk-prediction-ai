def get_answer(query):
    query = query.lower()

    if "diabetes" in query:
        return "Diabetes is caused by high blood sugar levels. Maintain diet and exercise."

    elif "bp" in query or "blood pressure" in query:
        return "Normal BP is around 120/80. Reduce salt and stress."

    else:
        return "Limited info available. Please consult a doctor."