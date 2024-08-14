import os
import requests
import logging
from typing import Optional, Any, Callable
from dotenv import load_dotenv
from enums import CustomEventType, PageViewOption

load_dotenv()


class Swetrix:
    """
    Swetrix Python Library for server-side tracking.

    Provides methods to track events, page views, and heartbeats.
    """

    DEFAULT_API_HOST = "https://api.swetrix.com/log"

    def __init__(
        self,
        project_id: Optional[str] = None,
        api_key: Optional[str] = None,
        options: Optional[dict[str, Any]] = None,
        enable_logging: bool = True,
    ):
        """
        Initialize the Swetrix object.

        project_id: The project ID for Swetrix.
        api_key: The API key for Swetrix.
        options: Additional options for Swetrix.
        enable_logging: Flag to enable or disable logging.
        """
        self.project_id = project_id or os.getenv("SWETRIX_PROJECT_ID")
        self.api_key = api_key or os.getenv("SWETRIX_API_KEY")
        self.options = options if options else {}
        self.api_url = self.options.get("apiURL", self.DEFAULT_API_HOST)
        self.enable_logging = enable_logging

        self.logger = logging.getLogger(__name__)
        if self.enable_logging:
            logging.basicConfig(level=logging.INFO)

        if not self.project_id or not self.api_key:
            raise ValueError("Project ID and API key must be provided")

    def _log_info(self, message: str) -> None:
        """Log an info message if a logger is provided."""
        if self.logger:
            self.logger.info(message)

    def _log_error(self, message: str) -> None:
        """Log an error message if a logger is provided."""
        if self.logger:
            self.logger.error(message)

    def _send_event(
        self, path: str, ip: str, user_agent: str, data: dict[str, Any]
    ) -> None:
        """
        Send an event to the Swetrix API.

        path: The API path for the event.
        ip: The IP address of the client.
        user_agent: The user agent string of the client.
        data: The data to be sent in the event.
        """
        url = f"{self.api_url}/{path}" if path else self.api_url
        headers = {
            "Content-Type": "application/json",
            "X-Client-IP-Address": ip,
            "User-Agent": user_agent,
            "X-Api-Key": self.api_key,
        }
        payload = {"pid": self.project_id, **data}
        self._log_info(f"Sending request to URL: {url}")
        self._log_info(f"Payload: {payload}")
        self._log_info(f"Headers: {headers}")
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            self._log_info(f"Response: {response.status_code} {response.text}")
        except requests.exceptions.RequestException as e:
            self._log_error(f"Error sending event to Swetrix: {e}")
            raise

    def track_event(
        self,
        ip: str,
        user_agent: str,
        event_type: CustomEventType,
        event_options: dict[PageViewOption, Any],
    ) -> None:
        """
        Track a custom event.

        ip: The IP address of the client.
        user_agent: The user agent string of the client.
        event_type: The type of event to track.
        event_options: The event options.
        """
        event_data = {
            option.value: value for option, value in event_options.items()
        }
        event_data["ev"] = event_type.value
        self._log_info(f"Tracking event data: {event_data}")
        self._send_event("custom", ip, user_agent, event_data)

    def track_page_view(
        self,
        ip: str,
        user_agent: str,
        page_view_options: dict[PageViewOption, Any],
    ) -> None:
        """
        Track a page view.

        ip: The IP address of the client.
        user_agent: The user agent string of the client.
        page_view_options: The page view options.
        """
        page_view_data = {
            option.value: value for option, value in page_view_options.items()
        }
        self._log_info(f"Tracking page view data: {page_view_data}")
        self._send_event("", ip, user_agent, page_view_data)

    def track_event_decorator(
        self,
        ip: str,
        user_agent: str,
        event_type: CustomEventType,
        event_options: dict[str, Any],
    ) -> Callable:
        """
        Decorator to track a page view when the decorated function is called.

        ip: The IP address of the client.
        user_agent: The user agent string of the client.
        event_options: The page view options.
        """

        def decorator(func: Callable) -> Callable:
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                self.track_event(ip, user_agent, event_type, event_options)
                return result

            return wrapper

        return decorator

    def track_page_view_decorator(
        self,
        ip: str,
        user_agent: str,
        page_view_options: dict[PageViewOption, Any],
    ) -> Callable:
        """
        Decorator to track a page view when the decorated function is called.

        ip: The IP address of the client.
        user_agent: The user agent string of the client.
        page_view_options: The page view options.
        """

        def decorator(func: Callable) -> Callable:
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                self.track_page_view(ip, user_agent, page_view_options)
                return result

            return wrapper

        return decorator

