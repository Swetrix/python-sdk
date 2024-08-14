# Swetrix Python SDK


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The Swetrix Python SDK is a client library designed to interact with the Swetrix API. This SDK provides easy-to-use methods for tracking and analyzing various events, user interactions, and metrics within your Python applications.

## Features

- Simple integration with Swetrix API.
- Track various events and user interactions.
- Collect and analyze custom metrics.
- Lightweight and easy to use.

## Installation

You can install the SDK using pip:

```bash
pip install swetrix-sdk
```

## Usage

Below is a basic example of how to use the Swetrix Python SDK to send events to Swetrix.

### Environment Variables

```bash
# In your .env file or environment
SWETRIX_PROJECT_ID=your_project_id
SWETRIX_API_KEY=your_api_key
```

Alternatively, you can pass these values directly to the `Swetrix` instance.

## Basic Usage

### Initialization

Initialize the Swetrix client with your `PROJECT_ID` and `API_KEY`.

```python
from swetrix_sdk import Swetrix
from enums import CustomEventType, PageViewOption

# Initialize Swetrix instance
swetrix = Swetrix(
    project_id='your_project_id',
    api_key='your_api_key',
    enable_logging=True  # Enable logging for debugging
)
```

### Tracking Custom Events

Use the `track_event` method to track any custom event. Here's an example where we track a "signup" event:

```python
event_data = {
    PageViewOption.SOURCE: "homepage",
    PageViewOption.METHOD: "google"
}

swetrix.track_event(
    ip="192.168.0.1",
    user_agent="Mozilla/5.0",
    event_type=CustomEventType.SIGNUP,
    event_options=event_data
)
```

### Tracking Page Views

You can easily track page views by providing the necessary options like `URL` and `User ID`.

```python
page_view_data = {
    PageViewOption.URL: "/homepage",
    PageViewOption.USER_ID: "user123"
}

swetrix.track_page_view(
    ip="192.168.0.1",
    user_agent="Mozilla/5.0",
    page_view_options=page_view_data
)
```

## Using Decorators for Automatic Event Tracking

The SDK provides decorators that automatically track events or page views whenever a function is called. This is useful for tracking specific function executions, like API endpoints.

### Tracking Custom Events with a Decorator

To automatically track an event when a function is executed, use the `track_event_decorator`:

```python
@swetrix.track_event_decorator(
    ip="192.168.0.1",
    user_agent="Mozilla/5.0",
    event_type=CustomEventType.LOGIN,
    event_options={PageViewOption.SOURCE: "login_page"}
)
def user_login(username: str, password: str):
    return "User logged in"

# Call the decorated function
user_login("Yehor", "Python")
```

### Tracking Page Views with a Decorator

Similarly, you can use the `track_page_view_decorator` to track page views when a function is executed.

```python
@swetrix.track_page_view_decorator(
    ip="192.168.0.1",
    user_agent="Mozilla/5.0",
    page_view_options={PageViewOption.URL: "/profile", PageViewOption.USER_ID: "user123"}
)
def load_profile():
    return "Profile loaded"

load_profile()
```

## Configuration Options

- `project_id`: The project ID for Swetrix.
- `api_key`: The API key for Swetrix.
- `options`: Additional configuration options for custom API URLs.
- `enable_logging`: Boolean flag to enable or disable logging.


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Support

For any issues or support requests, please open an issue on the [GitHub Issues](https://github.com/Swetrix/python-sdk/issues) page.

