"""
Feel free to modify the content of the `CustomEventType` class if you require any specific custom events for your project.
"""

from enum import Enum


class CustomEventType(Enum):
    """
    Enum for different types of events that can be tracked.

    Here, you can define your custom events as needed for your specific project.
    As well it is like a base class, you can create your own hierarchy of ``CustomEventType`` classes

    Attributes:
        USER_SIGNUP: Event type for user signup.
        PURCHASE_COMPLETED: Event type for completed purchase.
        BUTTON_CLICK: Event type for button click.
    """

    USER_SIGNUP = "USER_SIGNUP"
    PURCHASE_COMPLETED = "PURCHASE_COMPLETED"
    BUTTON_CLICK = "BUTTON_CLICK"


class PageViewOption(Enum):
    """
    Enum for different options related to page view tracking.

    This will be extended by the Swetrix Core Team in case Swetrix starts tracking any other events.

    PAGE: The current page being viewed.
    PREVIOUS_PAGE: The previous page the user was on.
    LOCALE: The locale of the user.
    REFERRER: The referrer URL.
    SOURCE: The source of the traffic (e.g., ref, source, or utm_source GET parameter).
    MEDIUM: The medium of the traffic (e.g., utm_medium GET parameter).
    CAMPAIGN: The campaign of the traffic (e.g., utm_campaign GET parameter).
    UNIQUE: If set to true, only unique visits will be saved.
    PERFORMANCE: An object with performance metrics related to the page load.
    """

    PAGE = "pg"
    PREVIOUS_PAGE = "prev"
    LOCALE = "lc"
    REFERRER = "ref"
    SOURCE = "so"
    MEDIUM = "me"
    CAMPAIGN = "ca"
    UNIQUE = "unique"
    PERFORMANCE = "perf"
