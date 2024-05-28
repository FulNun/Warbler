import unittest
from app import app, db
from models import User, Message

class FlaskAppTests(unittest.TestCase):
    """Test cases for Flask app"""

    def setUp(self):
        """Set up test environment"""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.client = app.test_client()

        # Create database tables
        with app.app_context():
            db.create_all()

    def tearDown(self):
        """Clean up after each test"""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_homepage(self):
        """Test homepage route"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Warbler', response.data)

    def test_signup(self):
        """Test user signup"""
        response = self.client.post('/signup', data=dict(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Warbler', response.data)
        # Check if user was added to the database
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'test@example.com')

    def test_login(self):
        """Test user login"""
        # Create a test user
        user = User(username='testuser', email='test@example.com', password='testpassword')
        db.session.add(user)
        db.session.commit()

        response = self.client.post('/login', data=dict(
            username='testuser',
            password='testpassword'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome back, testuser!', response.data)

    # Add more test cases for other routes and functionality...

if __name__ == '__main__':
    unittest.main()
