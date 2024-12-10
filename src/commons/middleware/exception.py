import logging
from django.http import JsonResponse
from django.core.exceptions import ImproperlyConfigured
from utilities.constant import HttpStatus

logger = logging.getLogger(__name__)




class ExceptionHandlerMiddleware:
    """
    Middleware for handling exceptions and returning appropriate JSON responses.

    Args:
        get_response (callable): The next middleware in the chain or the view if this middleware is last.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    @staticmethod
    def process_exception(request, exception):
        # Log the original exception
        logger.error('Exception occurred: %s', str(exception), exc_info=True)
        # Default error status and message
        error_status = HttpStatus.UnexpectedError.value[0]
        error_message = HttpStatus.UnexpectedError.value[1]

        # Handle different types of exceptions and set appropriate status and message
        if isinstance(exception, ImproperlyConfigured):
            error_status = HttpStatus.InternalServerError.value[0]
            error_message = HttpStatus.InternalServerError.value[1]

        # If no specific exception is caught, set a generic error status and message
        if error_status is None:
            error_status = HttpStatus.UnexpectedError.value[0]
            error_message = HttpStatus.UnexpectedError.value[1]

        # Construct JSON response with error message
        error_response = {
            'error': {
                'message': error_message
            }
        }

        # Return JSON response
        return JsonResponse(error_response, status=error_status)