# medal-api

Unofficial API Client for [medal.tv](https://medal.tv)

# Usage
```py
# Don't know if this can be done any better
from medal_api.MedalAPI import MedalAPI

# Create the API object
api = MedalAPI()

# Query user info
print(api.get_user("Test"))

# Get a category
print(api.get_category(0))

# Get recent games
print(api.get_recent_games("Test"))

```
