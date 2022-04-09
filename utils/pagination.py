import math

from django.core.paginator import Paginator


def make_pagination_range(page_range, qty_pages, current_page):
    middle_range = math.ceil(qty_pages / 2)
    total_pages = len(page_range)
    start_range = current_page - middle_range
    end_range = current_page + middle_range

    end_range_offset = abs(start_range) if start_range < 0 else 0
    start_range_offset = abs(end_range - total_pages) if end_range > total_pages else 0

    start_range -= start_range_offset
    end_range += end_range_offset

    start_range = start_range if start_range > 0 else 0
    end_range = end_range if end_range < total_pages else total_pages

    pagination = page_range[start_range:end_range]

    return {
        'pagination': pagination,
        'page_range': page_range,
        'qty_pages': qty_pages,
        'current_page': current_page,
        'total_pages': total_pages,
        'start_range': start_range,
        'end_range': end_range,
        'first_page_out_range': current_page > middle_range,
        'last_page_out_range': end_range < total_pages
    }


def make_pagination(request, queryset, per_page,qty_pages):
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1
    queryset_pages = Paginator(queryset, per_page)
    page = queryset_pages.get_page(current_page)

    pagination_range = make_pagination_range(
        page_range=queryset_pages.page_range,
        qty_pages=qty_pages,
        current_page=current_page,
    )

    return page, pagination_range
