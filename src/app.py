from flask import Flask, render_template, jsonify
from models.visa_officer import VisaOfficer
from models.speech_handler import SpeechHandler  # Import the new model

app = Flask(__name__)
visa_officer = VisaOfficer()
speech_handler = SpeechHandler()  # Instantiate the new model

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_applicant')
def get_applicant():
    applicant = visa_officer.generate_applicant()
    applicant['script'] = speech_handler.get_script()  # Add script from new model
    return jsonify(applicant)

if __name__ == '__main__':
    app.run(debug=True)