# from django.test import TestCase  (Django TDD)
import guestbook.models as guestbookmodel


def test_guestbookmodel_insert():
    guestbookmodel.insert('안대혁', '1234', '안녕하세요~')


def test_guestbookmodel_fetchlist():
    results = guestbookmodel.fetchlist()
    print(results)


# test_guestbookmodel_insert()
test_guestbookmodel_fetchlist()


