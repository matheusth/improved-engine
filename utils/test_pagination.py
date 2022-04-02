import unittest
from utils.pagination import make_pagination_range


class MyTestCase(unittest.TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )["pagination"]
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_half(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=2,
        )["pagination"]
        self.assertEqual([1, 2, 3, 4], pagination)
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=3,
        )["pagination"]
        self.assertEqual([2, 3, 4, 5], pagination)
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=4,
        )["pagination"]
        self.assertEqual([3, 4, 5, 6], pagination)

    def test_make_pagination_is_unchanged_if_last_page_is_next(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=20,
        )["pagination"]
        self.assertEqual([17, 18, 19, 20], pagination)
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=21,
        )["pagination"]
        self.assertEqual([17, 18, 19, 20], pagination)

    def test_if_total_pages_is_less_than_stop_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 3)),
            qty_pages=4,
            current_page=2,
        )["pagination"]
        self.assertEqual([1, 2], pagination)
