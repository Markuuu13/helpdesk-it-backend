from rest_framework.pagination import PageNumberPagination
class TicketsPagination(PageNumberPagination):
    page_size = 10
    pag_size_query_param = 'page_size'
    max_page_size = 100
    