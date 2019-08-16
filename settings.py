# API_KEY: Google Maps with Geocoding API Key
# Google Maps API is used to Geocode a Postcode to a logitude and latitude
# To use the API a private API key is required.
# Open the following URL (https://developers.google.com/maps/documentation/embed/get-api-key) to obtain a private API key
# Ensure you have enabled the "Geocoding API"

# The API_KEY is not needed as much anymore. It is only needed if you do not have a stores.json file where your script
# is running from. But it should be automatically downloaded on first run anyway. The stores.json file is used to
# determine the location of a 7Eleven stores and lock in around that area.

API_KEY=""

# BASE_URL: 7-11 Mobile Application API End Point
BASE_URL="https://711-goodcall.api.tigerspike.com/api/v1/"

# PRICE_URL: 11-Seven Price API
PRICE_URL="https://projectzerothree.info/api.php?format=json"

# Device name - Samsung Galaxy S10. You can change this to any device you want.
DEVICE_NAME="SM-G973FZKAXSA"

# Device name - Samsung Galaxy S10. You can change this to any device you want.
OS_VERSION="Android 9.0.0"

# App version
APP_VERSION="1.8.0.2027"
