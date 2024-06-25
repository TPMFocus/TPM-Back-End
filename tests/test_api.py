import unittest
import requests
import uuid
import os
from flask import jsonify
import logging

class TestFlaskAPI(unittest.TestCase):
    # Base URL for the API. Can be overridden with an environment variable.
    BASE_URL = os.getenv('API_URL', 'http://localhost:5000')

    def setUp(self):
        # This method runs before each test
        # Generate a unique user ID and session ID for each test
        self.user_id = str(uuid.uuid4())
        self.session_id = str(uuid.uuid4())

    def test_start_session(self):
        """Test the /start-session endpoint"""
        # Prepare the data for the request
        data = {
            "user_id": self.user_id,
            "session_id": self.session_id
        }

        try:
            # Send a POST request to the start-session endpoint
            response = requests.post(f"{self.BASE_URL}/start-session", json=data)

            # Check if the request was successful (status code 200)
            self.assertEqual(response.status_code, 200, "Expected status code 200")

            # Parse the JSON response
            response_data = response.json()

            # Check if the response contains a session_id
            self.assertIn("session_id", response_data, "Response should contain a session_id")

            # Check if the returned session_id matches the one we sent
            self.assertEqual(response_data["session_id"], self.session_id, 
                             "Returned session_id should match the one sent")
            pass

        except Exception as e:
            logging.error(f"Error in start_session: {str(e)}")
            return jsonify({"error": "Internal server error"}), 500

    def test_generate_text(self):
        """Test the /generate-text endpoint"""
        # Prepare the data for the request
        data = {
            "session_id": self.session_id,
            "prompt": "Test prompt"
        }

        try:
            # Send a POST request to the generate-text endpoint
            response = requests.post(f"{self.BASE_URL}/generate-text", json=data)

            # Check if the request was successful (status code 200)
            self.assertEqual(response.status_code, 200, "Expected status code 200")

            # Parse the JSON response
            response_data = response.json()

            # Check if the response contains generated_text
            self.assertIn("generated_text", response_data, "Response should contain generated_text")

            # Check if generated_text is a non-empty string
            self.assertIsInstance(response_data["generated_text"], str, "generated_text should be a string")
            self.assertTrue(len(response_data["generated_text"]) > 0, "generated_text should not be empty")

            # Check if the response contains chatId and createdDate
            self.assertIn("chatId", response_data, "Response should contain chatId")
            self.assertIn("createdDate", response_data, "Response should contain createdDate")
            pass

        except Exception as e:
            logging.error(f"Error in start_session: {str(e)}")
            return jsonify({"error": "Internal server error"}), 500

    def test_clear_chat(self):
        """Test the /clear-chat endpoint"""
        # Prepare the data for the request
        data = {
            "session_id": self.session_id
        }

        try:
            # Send a POST request to the clear-chat endpoint
            response = requests.post(f"{self.BASE_URL}/clear-chat", json=data)

            # Check if the request was successful (status code 200)
            self.assertEqual(response.status_code, 200, "Expected status code 200")

            # Parse the JSON response
            response_data = response.json()

            # Check if the response contains the expected message
            self.assertIn("message", response_data, "Response should contain a message")
            self.assertEqual(response_data["message"], "Chat history has been cleared", 
                             "Unexpected message in response")
            pass
        except Exception as e:
            logging.error(f"Error in start_session: {str(e)}")
            return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    unittest.main()