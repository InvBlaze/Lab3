import pyrebase
import random
import time

# Create new Firebase config and database object
config = {
    "apiKey": "AIzaSyAN7J9VoDoj6H1vBn2XfHAh5iopG3k6BTY",
    "authDomain": "lab3-sample-project-jasons.firebaseapp.com",
    "databaseURL": "https://lab3-sample-project-jasons-default-rtdb.firebaseio.com/",
    "storageBucket": "lab3-sample-project-jasons.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
dataset = "sensor1"


def writeData():
    while True:
        # Assuming you are replacing this with real sensor data
        sensorData = random.random()  # Replace with sensor data retrieval logic
        timestamp = int(time.time())  # Use current timestamp as key

        # Writing sensor data with timestamp as key
        db.child(dataset).child(timestamp).set(sensorData)

        time.sleep(1)  # Data writing frequency


def readData():
    # Fetching the last few entries from the database
    mySensorData = db.child(dataset).order_by_key().limit_to_last(10).get()

    for data in mySensorData.each():
        print(f"Timestamp: {data.key()}, Value: {data.val()}")


if __name__ == "__main__":
    # Example function call
    writeData()
    readData()

