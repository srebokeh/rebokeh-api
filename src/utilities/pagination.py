from rest_framework import viewsets, pagination


class CustomPagination(pagination.PageNumberPagination):
    page_size = 4  # Adjust the number of items per page here
    page_size_query_param = 'page_size'
    max_page_size = 1000