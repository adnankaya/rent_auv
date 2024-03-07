from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


def paginate_objects(objects, page, per_page=10):
    """Returns paginated list of given objects
    Parameters:::
    objects: QuerySet
    page: int
    per_page: int
    ::: returns paginated object list
    """
    paginator = Paginator(objects, per_page=per_page)
    try:
        paginated_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        paginated_list = paginator.page(number=1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        paginated_list = paginator.page(number=paginator.num_pages)

    return paginated_list


class BasePageNumberPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "limit"
    max_page_size = 20

    def get_paginated_response(self, data):
        return Response(
            {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "current_page": self.page.number,
                "results": data,
            }
        )

    def paginate_queryset(self, queryset, request, view=None):
        if "noPage" in request.query_params:
            return None
        return super().paginate_queryset(queryset, request, view=view)

    def get_page_size(self, request):
        limit = request.query_params.get(self.page_size_query_param)
        if limit is not None:
            try:
                limit = int(limit)
            except ValueError:
                pass  # Ignore invalid integer values
            else:
                if limit == -1:
                    # we can return None to disable pagination but no need to write more frontend code :)
                    return 999_999
                return limit
        return self.page_size
