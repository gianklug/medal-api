import requests  # Web requests
import logging  # Error logging
from secrets import token_hex as token  # Random UIDs


class MedalAPI:
    def __init__(self, token=None):
        # Headers required for contacting the Medal API
        self.headers = {
                    "Content-Type": "application/json",
                    "Medal-User-Agent": "Medal-web/1.0 (string_id; simplified_signup; no_upscale; markdown)"
                }
        if token is None:
            token = self.authenticate()
        # Append the Medal auth to the headers
        self.headers |= {"X-Authentication":token}

    def get_uid(self) -> str:
        # Sample UID: 088443fe-405b-4298-8d13-9fa24d44c96
        # Structure the string as f string:
        uid = f"{token(8)}-{token(4)}-{token(4)}-{token(4)}-{token(11)}"
        # Return the random UID
        return uid

    def authenticate(self) -> str | bool:
        # First we need a UID
        uid = self.get_uid()
        # Construct the function call body
        body = {"email": "guest", "userName": "guest", "password": uid}
        # Request a user token
        try:
            user = requests.post(
                "https://medal.tv/api/users",
                timeout=10,
                json=body,
                headers=self.headers
            ).json()
            # Return the user token
            return f"{user['user']['userId']},{user['auth']['key']}"
        except requests.exceptions.ConnectionError:
            logging.critical("Connection to medal.tv failed.")
            return False
        except requests.exceptions.JSONDecodeError:
            logging.critical("Medal did not return valid JSON data.")
            return False

    def get_user(self, username):
        try:
            # Get the user via api
            user = requests.get(
                f"https://medal.tv/api/users?username={username}",
                timeout=10,
                headers=self.headers
            ).json()
            # Return the user data
            return user
        except requests.exceptions.ConnectionError:
            logging.critical("Connection to medal.tv failed.")
            return []
        except requests.exceptions.JSONDecodeError:
            logging.critical("Medal did not return valid JSON data.")
            return []

    def get_category(self, category_id):
        try:
            # Get the category via api
            category = requests.get(
                f"https://medal.tv/api/categories/{category_id}",
                timeout=10,
                headers=self.headers
            ).json()
            # Return the user data
            return category
        # Handle connection error
        except requests.exceptions.ConnectionError:
            logging.critical("Connection to medal.tv failed.")
            return []
        # Handle json error
        except requests.exceptions.JSONDecodeError:
            logging.critical("Medal did not return valid JSON data.")
            return []

    def get_recent_games(self, user):
        # Get the user data
        user = self.get_user(user)
        # Get the recent activity
        activity = user[0]['gameSessions']
        # Initialize empty array for the result
        result = []
        # Loop over the recent activity
        # 'sessionId': '293FwVPjVSWMki', 'categoryId': 'fW3AZxHf_c', 'startTime': 1675363738000, 'expiresAt': 1675968538000
        for item in activity:
            result.append({
                    'sessionId': item['sessionId'],
                    'category': self.get_category(item['categoryId'])['categoryName'],
                    'startTime': item['startTime'],
                    'endTime': item['endTime'] if 'endTime' in item else "",
                    'expiresAt': item['expiresAt']
                })
        return result
