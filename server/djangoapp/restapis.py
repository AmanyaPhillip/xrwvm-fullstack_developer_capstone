import requests
import json
import os # Make sure os is imported to get environment variables
from .models import CarDealer, DealerReview

# E302: Add 1 blank line here.

# Get environment variables (ensure they are loaded e.g., using python-dotenv in manage.py/wsgi.py)
backend_url = os.environ.get('backend_url')
sentiment_analyzer_url = os.environ.get('sentiment_analyzer_url')

# E302: Add 1 blank line here.

def get_request(endpoint, **kwargs): # E275: Add space after keyword 'def' and before arguments.
    params = ""
<<<<<<< HEAD
    if kwargs:
        for key, value in kwargs.items(): # E231: Missing whitespace after ','.
            params = params + key + "=" + value + "&" # E225: Missing whitespace around operator.
    request_url = backend_url + endpoint + "?" + params # W293: Blank line contains whitespace.

    # W293, E303: Remove blank lines containing whitespace, reduce multiple blank lines.
    # W293: Remove blank lines with whitespace.
    print(f"GET from {request_url}")
=======
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except:
        # If any error occurs
        print("Network exception occurred")

def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
>>>>>>> parent of 749909e (Module 4)
    try:
        response = requests.get(request_url)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        print(f"Response Status: {response.status_code}")
        json_data = json.loads(response.text)
        return json_data
    except requests.exceptions.RequestException as e: # E722: Don't use bare 'except'. Be specific.
        # Handle exceptions gracefully
        print(f"Network exception occurred: {e}")
        return {} # Return an empty dictionary or appropriate error indicator

# E302: Add 1 blank line here.

def post_request(endpoint, payload, **kwargs):
    # This function needs more robust error handling and structure
    print(f"POST to {endpoint} with payload: {payload}")
    try:
<<<<<<< HEAD
        response = requests.post(endpoint, json=payload, params=kwargs)
        response.raise_for_status()
        print(f"Response Status: {response.status_code}")
        json_data = response.json() # requests.post with json=payload directly returns JSON
        return json_data
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return {} # Return an empty dictionary or appropriate error indicator


# E302: Add 1 blank line here.

def get_dealers_from_api(url, **kwargs):
    results = []
    # Call a get method to get all dealers in the Cloudant database
    json_result = get_request(url, **kwargs)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["dealers"] # E231: Missing whitespace after ','.
        # For each dealer object
        for dealer_doc in dealers:
            # Create a CarDealer object from a dealer dictionary
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"],
                                   full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)
    return results

def get_dealer_reviews_from_api(url, dealerId): # Add blank line
    results = []
    json_result = get_request(url, dealerId=dealerId)
    if json_result:
        reviews = json_result["reviews"] # E231: Missing whitespace after ','.
        for review_doc in reviews:
            review_obj = DealerReview(
                dealership=review_doc["dealership"],
                name=review_doc["name"],
                purchase=review_doc["purchase"],
                review=review_doc["review"],
                purchase_date=review_doc.get("purchase_date"), # Use .get() for optional fields
                car_make=review_doc.get("car_make"),
                car_model=review_doc.get("car_model"),
                car_year=review_doc.get("car_year"),
                sentiment="neutral" # Default sentiment, will be updated by analyzer
            )
            # Make a call to the sentiment analyzer service to get the sentiment for the review
            sentiment_response = analyze_review_sentiments(review_obj.review)
            if sentiment_response and 'sentiment' in sentiment_response:
                review_obj.sentiment = sentiment_response['sentiment']
            else:
                print(f"WARNING: Could not get sentiment for review: {review_obj.review}")
                review_obj.sentiment = 'unknown' # Set a default if sentiment analysis fails
            results.append(review_obj)
    return results


def analyze_review_sentiments(review_text):
    # Ensure sentiment_analyzer_url is properly loaded from environment variables
    # This should be done once at the module level or configured in Django settings.
    # For now, let's assume it's correctly available from os.environ.get() as above.

    url = f"{sentiment_analyzer_url}/analyze" # Assuming an /analyze endpoint
    payload = json.dumps({"text": review_text})
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        sentiment_data = response.json()
        return sentiment_data
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with sentiment analyzer: {e}")
        return None # Return None or a default error dict if sentiment analysis fails
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from sentiment analyzer: {e}")
        print(f"Raw response text: {response.text if 'response' in locals() else 'No response received'}")
        return None # Return None or a default error dict if JSON is invalid
=======
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
>>>>>>> parent of 749909e (Module 4)
