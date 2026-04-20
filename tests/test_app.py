import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Introduction to Python', response.data)
        self.assertIn(b'Web Development with Flask', response.data)
        self.assertIn(b'Data Science Fundamentals', response.data)
        self.assertIn(b'Go Programming Language', response.data)

    def test_index_hero_section(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'hero', response.data)
        self.assertIn(b'Master Programming', response.data)
        self.assertIn(b'Explore Courses', response.data)

    def test_index_stats_bar(self):
        response = self.app.get('/')
        self.assertIn(b'stats-bar', response.data)
        self.assertIn(b'Expert Instructors', response.data)
        self.assertIn(b'Weeks of Content', response.data)

    def test_index_course_cards(self):
        response = self.app.get('/')
        self.assertIn(b'course-card', response.data)
        self.assertIn(b'View Course', response.data)
        self.assertIn(b'John Doe', response.data)
        self.assertIn(b'Jane Smith', response.data)

    def test_index_topic_tags(self):
        response = self.app.get('/')
        self.assertIn(b'topic-tag', response.data)
        self.assertIn(b'Variables and Data Types', response.data)

    def test_golang_course(self):
        response = self.app.get('/course/4')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Go Programming Language', response.data)

    def test_course(self):
        response = self.app.get('/course/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Introduction to Python', response.data)
        self.assertIn(b'cd-hero', response.data)

    def test_videos(self):
        response = self.app.get('/videos')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Videos', response.data)

    def test_contact_page_loads(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_content(self):
        response = self.app.get('/contact')
        self.assertIn(b'CodeLearn Academy', response.data)
        self.assertIn(b'hello@codelearnacademy.com', response.data)
        self.assertIn(b'123 Dev Street', response.data)

    def test_contact_social_links(self):
        response = self.app.get('/contact')
        self.assertIn(b'twitter.com/codelearnacademy', response.data)
        self.assertIn(b'github.com/codelearnacademy', response.data)
        self.assertIn(b'linkedin.com/company/codelearnacademy', response.data)

    def test_contact_mailto_link(self):
        response = self.app.get('/contact')
        self.assertIn(b'mailto:hello@codelearnacademy.com', response.data)

    def test_contact_form_renders(self):
        response = self.app.get('/contact')
        self.assertIn(b'Send Us a Message', response.data)
        self.assertIn(b'message_title', response.data)
        self.assertIn(b'message_body', response.data)

    def test_contact_form_post_redirects(self):
        response = self.app.post('/contact', data={"message_title": "Hello", "message_body": "Test body"})
        self.assertEqual(response.status_code, 302)
        self.assertIn('/contact', response.headers['Location'])

    def test_contact_form_post_flash(self):
        response = self.app.post('/contact', data={"message_title": "Hello", "message_body": "Test body"}, follow_redirects=True)
        self.assertIn(b"Your message has been sent", response.data)

    def test_contact_form_get_no_flash(self):
        response = self.app.get('/contact')
        self.assertNotIn(b"Your message has been sent", response.data)

if __name__ == '__main__':
    unittest.main()