import json
# Data to be written
def my_function():
    dictionary = {
	    "name": "sadsad",
	    "rollno": 22,
	    "cgpa": 8.6,
	    "phonenumber": "9976770500"
    }

# Serializing json

    json_object = json.dumps(dictionary, indent=4)
    # Writing to sample.json
    with open("static/sample.json", "w") as outfile:
	    outfile.write(json_object)
