# coding: utf-8


from django.core.urlresolvers import reverse
from django.test import TestCase  # Flush the database after each test
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


def build_list(list_raw, base_pattern, dict_name={}):
    ret = []
    for el in list_raw:
        url = base_pattern + el
        try:
            url = url % dict_name
        except Exception, e:
            print 'Url failing: ', url, Exception, e
        ret.append(url)
    return ret


def get_list_basic_urls():
    base_pattern = ""
    dict_name = {}
    list_raw = [
        # While no content is created, the / page cannot
        # be accessed. Those tests are handles by the
        # django-cms test suite anyway

        ## reverse('pages-root'),  # Landing page
        '/admin/',  # admin  section
    ]
    return build_list(list_raw, base_pattern, dict_name)


def get_all_list():
    global_list = []

    global_list += get_list_basic_urls()

    return global_list


###
# Test for unauthenticated users
###


class BaseTest(TestCase):

    def setUp(self):
        self.c = Client()

    def assert_get_404(self, url):
        response = self.c.get(url)
        self.assertEqual(response.status_code, 404)

    def get_302_or_200(self, url):
        response = self.c.get(url)
        self.assertIn(response.status_code, [200, 302])


class AppTestAuth(BaseTest):

    def test_urls_response_200_or_302(self):
        """
        Tests that the following urls can be accessed
        """
        for url in get_all_list():
            print url
            self.get_302_or_200(url)

