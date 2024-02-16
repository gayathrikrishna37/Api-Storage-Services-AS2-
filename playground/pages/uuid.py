from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
import uuid

# Function for generating UUID
def generate_uuid():
    # Generate a random UUID
    random_id = uuid.uuid4()

    # Convert UUID to string
    random_id_str = str(random_id)

    # Extract a portion of the UUID if needed
    user_id = random_id_str[:8]  # for example, you can take the first 8 characters

    return user_id

# Function for generating bucket ID
def generate_bucket_id(user_id):
    # Generate a UUID for the bucket ID
    bucket_id = str(uuid.uuid4())

    # Concatenate user_id to make it unique per user
    bucket_id = f"{user_id}_{bucket_id}"

    return bucket_id

# Dashboard view function
@login_required
def dashboard(request):
    # Get the logged-in user
    user = request.user

    # Check if the user has an 'as2' user ID already
    if not user.profile.as2_user_id:
        # Generate a new 'as2' user ID
        user_id = generate_uuid()

        # Update the user's profile with the 'as2' user ID
        user.profile.as2_user_id = user_id
        user.profile.save()

    # Generate a bucket ID for the user
    bucket_id = generate_bucket_id(user_id)

    # Render the dashboard template with bucket ID
    return render(request, 'dashboard.html', {'bucket_id': bucket_id})
