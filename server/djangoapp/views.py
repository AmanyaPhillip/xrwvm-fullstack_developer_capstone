from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import JsonResponse
from django.db import models # F401: This seems unused. If not used, remove.

# F401: Remove unused imports: HttpResponseRedirect, HttpResponse, get_object_or_404, messages, datetime
# F811: Remove redefinition of render
# F401: 'django.shortcuts.render' imported but unused
# F401: 'django.shortcuts.get_object_or_404' imported but unused
# F401: 'django.shortcuts.redirect' imported but unused
# F401: 'django.contrib.messages' imported but unused
# F401: 'datetime.datetime' imported but unused

from .restapis import get_dealers_from_api, get_dealer_reviews_from_api, analyze_review_sentiments, post_request

# Create a `login_request` view function
# E302: Add 2 blank lines.
def login_user(request): # E275: Missing whitespace after keyword.
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['userName']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"userName": username, "status": "Logged in"})
        else:
            return JsonResponse({"userName": username, "status": "Login failed"})
    return JsonResponse({"message": "Invalid request method"}, status=405) # Add default for GET or other methods

# E302: Add 2 blank lines.
def logout_request(request):
    logout(request)
    return JsonResponse({"userName": ""})

# E302: Add 2 blank lines.
def registration_request(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['userName']
        password = data['password']
        first_name = data['firstName']
        last_name = data['lastName']
        email = data['email']

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({"userName": username, "error": "Already Registered"})

        # Check if email already exists
        # F841: 'email_exist' variable is assigned but never used.
        # email_exist = User.objects.filter(email=email).exists() # If not used, remove this line.

        try:
            User.objects.create_user(username=username, password=password,
                                     first_name=first_name, last_name=last_name, email=email) # E501: Line too long.
            login(request, authenticate(username=username, password=password))
            return JsonResponse({"userName": username, "status": "Registered"})
        except Exception as e: # E722: Do not use bare 'except'. Be more specific if possible.
            print(f"Error during registration: {e}")
            return JsonResponse({"userName": username, "error": "Registration failed. Try again."})
    return JsonResponse({"message": "Invalid request method"}, status=405)

# E302: Add 2 blank lines.
def get_dealerships(request): # E275: Missing whitespace after keyword.
    if request.method == "GET":
        endpoint = "/fetchDealers"
        dealerships = get_dealers_from_api(endpoint)
        return JsonResponse({"status": 200, "dealers": dealerships})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})

# E302: Add 2 blank lines.
def get_dealer_reviews(request, dealer_id): # E275: Missing whitespace after keyword.
    # print("heyye") # Debugging print, remove in production
    endpoint = "/fetchReviews/dealer/" + str(dealer_id)
    reviews = get_request(endpoint)
    # print(reviews) # Debugging print, remove in production

    # Check if reviews is not None and is iterable
    if reviews:
        for review_detail in reviews:
            # print(review_detail['review']) # Debugging print
            # Ensure review_detail['review'] exists and is a string
            if 'review' in review_detail and isinstance(review_detail['review'], str):
                sentiment_response = analyze_review_sentiments(review_detail['review'])
                # print(sentiment_response) # Debugging print
                if sentiment_response and 'sentiment' in sentiment_response:
                    review_detail['sentiment'] = sentiment_response['sentiment']
                else:
                    review_detail['sentiment'] = 'unknown' # Default sentiment on failure
                    print(f"WARNING: Sentiment not found for review: {review_detail.get('review', 'N/A')}")
            else:
                review_detail['sentiment'] = 'missing_review_text' # Default if review text is missing/invalid
                print(f"WARNING: 'review' key missing or not a string in: {review_detail}")
        return JsonResponse({"status": 200, "reviews": reviews})
    else:
        return JsonResponse({"status": 404, "message": "No reviews found or API error"})

# E302: Add 2 blank lines.
def get_dealer_details(request, dealer_id): # E275: Missing whitespace after keyword.
    if request.method == "GET":
        if dealer_id: # E712: Use 'if dealer_id:' instead of 'if dealer_id is not False:'
            endpoint = "/fetchDealer/" + str(dealer_id)
            dealership = get_request(endpoint)
            # F841: 'response' variable assigned but never used.
            # response = JsonResponse({"status": 200, "dealer": dealership}) # This line can be removed if not used
            return JsonResponse({"status": 200, "dealer": dealership}) # Return directly.
        else:
            return JsonResponse({"status": 400, "message": "Bad Request"})
    else:
        return JsonResponse({"status": 405, "message": "Method Not Allowed"})

# E302: Add 2 blank lines.
def add_review(request): # E275: Missing whitespace after keyword.
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            post_request("/insert_review", data)
            return JsonResponse({"status": 200, "message": "Review added successfully"})
        except Exception as e: # E722: Do not use bare 'except'. Be specific (e.g., requests.exceptions.RequestException).
            print(f"Error adding review: {e}")
            return JsonResponse({"status": 400, "message": f"Failed to add review: {e}"}) # E501: Line too long.
    return JsonResponse({"status": 405, "message": "Method Not Allowed"}) # E501: Line too long.

# E302: Add 2 blank lines.
def about(request):
    return render(request, 'djangoapp/about.html')

# E302: Add 2 blank lines.
def contact(request):
    return render(request, 'djangoapp/contact.html')
