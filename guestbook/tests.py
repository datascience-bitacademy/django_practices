# from django.test import TestCase  (Django TDD)
import guestbook.models as guestbookmodel


def test_guestbookmodel_fetchlist():
    results = guestbookmodel.fetchlist()
    print(results)


test_guestbookmodel_fetchlist()


