from enum import Enum

class HttpStatus(Enum):
    """
    Enum representing various HTTP status codes along with their default messages.

    Each member of this enumeration represents an HTTP status code along with its associated message.
    """
    NotImplemented = (501, "Service not available", ["The requested service or endpoint is currently not implemented. Our team is working on adding this feature. Please check back later or contact support for updates."])
    BadRequest = (400, "The server could not understand the request.", [])
    Unauthorized = (401, "Please provide valid credentials to access the requested resource. Ensure that you include the necessary authentication details in your request. If you continue to experience issues, contact the system administrator for assistance.", [])
    Forbidden = (403, "You do not have the necessary permissions to access the requested resource. Please ensure you have proper authorization and try again. If you believe this is an error, contact the system administrator for assistance.", [])
    NotFound = (404, "The requested resource could not be found on the server. Please verify the URL or endpoint you are trying to access and ensure it is correct. If you believe this is an error, contact the system administrator for assistance.", [])
    Conflict = (409, "An issue arose with the request due to a conflict; kindly address and attempt the request again. Additionally, a duplicate record was detected.", [])
    UnprocessableEntity = (422, "The server understands the content type but was unable to process the contained instructions.", [])
    TooManyRequests = (429, "You have exceeded the number of allowed requests. Please try again later.", [])
    InternalServerError = (500, "The server encountered an unexpected condition and cannot fulfill your request at the moment. Please try again later. If the issue persists, contact the system administrator for assistance.", [])
    BadGateway = (502, "The server, while working as a gateway to get a response needed to handle the request, got an invalid response.", [])
    ServiceUnavailable = (503, "The server is not ready to handle the request.", [])
    GatewayTimeout = (504, "The server, while acting as a gateway or proxy, did not receive a timely response from the upstream server.", [])
    UnexpectedError = (535, "An unexpected error occurred. Please try again later or contact support for assistance.", [])



"""
List of paths to be excluded from certain operations.
"""
excluded_paths = ['/user/login',
                  '/user/register/',
                  '/user/forgot-password/',
                  '/user/otp-verification/'
                 ]