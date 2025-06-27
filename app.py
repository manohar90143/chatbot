from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = generate_response(user_input)
    return jsonify({"reply": response})

def generate_response(message):
    message = message.lower().strip()

    if message in ["gm", "good morning"]:
        return "🌞 Good Morning! How can I assist you today?"
    elif message in ["gn", "good night"]:
        return "🌙 Good night! Take care and rest well."
    elif "hi" in message or "hello" in message or "hai" in message:
        return "Welcome to Prediction App Assistant 👨‍⚕️ How can I assist you today?"
    elif message in ["yes", "yeah", "yup", "ya", "sure", "of course"]:
        return "Great! 👍 Let me know the details or what you'd like to proceed with."
    elif message in ["no", "nope", "nah", "not now"]:
        return "No problem 😊 Let me know whenever you're ready."
    elif "appointment" in message:
        return "Sure, do you want to book an appointment with a General Physician, Dentist, or Pediatrician?"
    elif "general" in message or "physician" in message:
        return "Dr. Anil Kumar (General Physician) is available from 10 AM to 1 PM. Would you like to book a slot?"
    elif "dentist" in message:
        return "Dr. Rekha Sharma (Dentist) is available from 2 PM to 5 PM. Would you like to book an appointment?"
    elif "pediatrician" in message:
        return "Dr. Neha Joshi (Pediatrician) is available from 9 AM to 12 PM. Shall I book your visit?"
    elif "cardiologist" in message:
        return "Dr. Ramesh Varma (Cardiologist) is available on Mon, Wed, Fri from 10 AM to 12 PM."
    elif "orthopedic" in message or "bone doctor" in message:
        return "Dr. Sudheer Reddy (Orthopedic Surgeon) is available on Tue, Thu, Sat from 11 AM to 1 PM."
    elif "ambulance" in message:
        return "Yes, we provide 24x7 ambulance services. Call 📞 1800-123-456 for immediate help."
    elif "emergency" in message:
        return "For emergencies, please call our 24x7 helpline: 📞 1800-123-456 or rush to the ER immediately!"
    elif "services" in message:
        return "We offer General Medicine, Dental, Pediatrics, Cardiology, Orthopedics, Lab Tests, Vaccination, and more."
    elif "vaccination" in message or "vaccine" in message:
        return "Yes, we offer COVID-19, Hepatitis, Typhoid, and Flu vaccines for all age groups."
    elif "insurance" in message:
        return "Yes, we accept major health insurances like Star Health, Niva Bupa, ICICI Lombard, and others."
    elif "blood test" in message or "lab" in message:
        return "Yes, we have a full lab testing facility open from 8 AM to 6 PM. No appointment needed."
    elif "opd" in message or "outpatient" in message:
        return "OPD timings are 8 AM to 8 PM, Monday to Saturday."
    elif "hours" in message or "timing" in message or "open" in message:
        return "City Hospital is open Monday to Saturday from 8 AM to 8 PM. Emergency service: 24/7."
    elif "location" in message or "address" in message:
        return "Predication Creators is located at 📍 Vasavi College, Tadepalligudem."
    elif "date" in message:
        today = datetime.datetime.today()
        return f"Today's date is {today.strftime('%B %d, %Y')}."
    elif "time" in message:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}."
    elif "bmi" in message or "body mass index" in message:
        return "BMI (Body Mass Index) is a number calculated from your height and weight. A BMI of 18.5–24.9 is considered healthy."
    elif "glucose" in message or "sugar level" in message:
        return "Normal blood glucose level (fasting) is between 70–99 mg/dL. Levels above 126 mg/dL may indicate diabetes."
    elif "heartbeat" in message or "heart rate" in message:
        return "A normal resting heart rate for adults ranges from 60 to 100 beats per minute (bpm)."
    elif "pulse" in message:
        return "Pulse is the number of heartbeats per minute. It's the same as heart rate and can be felt on your wrist or neck."
    elif "blood pressure" in message or "bp" in message:
        return "Normal blood pressure is around 120/80 mmHg. High BP is over 140/90, and low is below 90/60."
    elif "oxygen" in message or "spo2" in message:
        return "A normal oxygen (SpO2) level is between 95% and 100%. Below 92% may require attention."
    elif "fever" in message or "temperature" in message:
        return "A body temperature above 100.4°F (38°C) is generally considered a fever."
    elif message in ["ok", "okay", "fine", "cool", "nice", "great", "good", "hmm"]:
        return "Alright! Let me know if you have any more questions. 😊"
    elif "thank" in message:
        return "You're most welcome! 🙏 Stay safe and healthy."
    elif "bye" in message:
        return "Goodbye! 👋 Wishing you good health. Come back if you need anything."

    # (All disease cases remain unchanged...)
    
    else:
        return "🤖 I'm here to help with appointments, doctors, hours, insurance, and emergencies. Ask me anything!"

if __name__ == "__main__":
    app.run(debug=True)
