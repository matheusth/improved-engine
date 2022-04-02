import math


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
