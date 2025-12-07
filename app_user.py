import streamlit as st
from storage import load_reviews, save_reviews
from llm_utils import call_llm

st.title("⭐ User Review Submission")

rating = st.slider("Select a Rating", 1, 5, 5)
review = st.text_area("Write your review")

if st.button("Submit"):
    if not review.strip():
        st.warning("Please enter a review.")
    else:

        # ----------- AI REPLY (short, natural, no email format) -----------
        ai_reply = call_llm(
            f"Write a short, friendly, conversational 2–3 sentence reply to a customer.\n"
            f"Do NOT write an email. Do NOT use placeholders. Do NOT ask for more details.\n"
            f"Tone: simple, warm, and human.\n\n"
            f"Rating: {rating}\n"
            f"Review: {review}\n\n"
            f"Reply:"
        )

        # ------------------------ SUMMARY ------------------------
        summary = call_llm(
            f"Summarize the customer's review in ONE short sentence.\n"
            f"Keep it simple.\n\n"
            f"Review: {review}\n"
            f"Summary:"
        )

        # -------------------- RECOMMENDED ACTION ---------------------
        action = call_llm(
            f"Suggest ONE very short, specific, actionable improvement based on this review.\n"
            f"No explanation. Just the action.\n\n"
            f"Rating: {rating}\n"
            f"Review: {review}\n"
            f"Action:"
        )

        # -------- Save to storage --------
        data = load_reviews()
        entry = {
            "id": len(data) + 1,
            "rating": rating,
            "review": review,
            "ai_reply": ai_reply,
            "summary": summary,
            "action": action
        }
        data.append(entry)
        save_reviews(data)

        st.success("Your review has been submitted!")
        st.subheader("AI Response")
        st.write(ai_reply)
