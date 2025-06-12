#Importing the celery task from tasks.py
from tasks import send_email_task
#jsonify to return JSON responses
from flask import Flask, request, jsonify

#name of the Flask app
app = Flask(__name__)
#Setting the app route to handle POST requests to '/send-email' 
@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json #get the JSON data from the POST request

    #Extract to, subject and body fields from the JSON data
    to = data.get('to')
    subject = data.get('subject')
    body = data.get('body')

    #Add this task to the Celery queue
    send_email_task.delay(to, subject, body)
    #If the task is successfully added to the queue, return a success message
    return jsonify({"message": "Email is being sent"})

if __name__ == '__main__':
    #Start the Flask development server, the '0.0.0.0' helps Docker expose this server
    app.run(debug=True, host='0.0.0.0')