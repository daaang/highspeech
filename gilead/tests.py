from django.test import TestCase

HASH_HELP_SUBSTR = \
        "the URL you entered\n      will only work in JavaScript"

class TestHashUrlView (TestCase):

    def test_get_hash_url_uses_js_redirect (self):
        response = self.client.get("/i")

        self.assertContains(response, HASH_HELP_SUBSTR)

    def test_post_hash_url_creates_ajax_page (self):
        response = self.client.post("/i",
                data = {"url": "/some/full/url"})

        self.assertNotContains(response, HASH_HELP_SUBSTR)
