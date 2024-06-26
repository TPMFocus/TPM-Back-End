import unittest
from unittest.mock import patch, MagicMock
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

    @patch('requests.post')
    def test_start_session(self, mock_post):
        """Test the /start-session endpoint"""
        # Mock response data
        mock_response_data = {
            "session_id": self.session_id
        }

        # Configure the mock to return a response with your mock data
        mock_post.return_value = requests.Response()
        mock_post.return_value.status_code = 200
        mock_post.return_value.json = lambda: mock_response_data

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
        except requests.exceptions.RequestException as e:
            self.fail(f"Request to the /start-session endpoint failed: {e}")
        except ValueError as e:
            self.fail(f"Response is not valid JSON: {e}")


    @patch('requests.post')
    @patch('app.main.models.chat_flow.query.filter_by')
    @patch('app.main.models.chat_message.query.filter_by')
    def test_generate_text(self, mock_chat_message_query, mock_chat_flow_query, mock_post):
        """Test the /generate-text endpoint"""
        
        # Mock chat flow data
        mock_chat_flow_entry = MagicMock()
        mock_chat_flow_entry.flowData = '{"context": "sample context"}'
        mock_chat_flow_query.return_value.first.return_value = mock_chat_flow_entry

        # Mock chat messages data
        mock_chat_message = MagicMock()
        mock_chat_message.role = 'userMessage'
        mock_chat_message.content = 'sample message'
        mock_chat_message_query.return_value.all.return_value = [mock_chat_message]

        # Mock response data from OpenAI API
        mock_response_data = {
            "generated_text": "This is a mock generated text.",
            "chatId": "mockChatId123",
            "createdDate": "2023-01-01T00:00:00Z"
        }
        mock_post.return_value = requests.Response()
        mock_post.return_value.status_code = 200
        mock_post.return_value.json = lambda: mock_response_data

        # Prepare the data for the request
        data = {
            "session_id": self.session_id,
            "prompt": "Generate me an empty note node."
        }

        try:
            # Send a POST request to the generate-text endpoint
            response = requests.post(f"{self.BASE_URL}/generate-text", json=data)

            # Assertions
            self.assertEqual(response.status_code, 200, "Expected status code 200")

            try:
                response_data = response.json()
            except ValueError as e:
                self.fail(f"Response is not valid JSON: {e}")

            self.assertIn("generated_text", response_data, "Response should contain generated_text")
            self.assertIsInstance(response_data["generated_text"], str, "generated_text should be a string")
            self.assertTrue(len(response_data["generated_text"]) > 0, "generated_text should not be empty")
            self.assertIn("chatId", response_data, "Response should contain chatId")
            self.assertIn("createdDate", response_data, "Response should contain createdDate")

            # Additional checks for database interactions
            mock_chat_flow_query.assert_called_once_with(id=self.session_id)
            mock_chat_message_query.assert_called_once_with(chatflowid=self.session_id)
        except requests.exceptions.RequestException as e:
            self.fail(f"Request to the /generate-text endpoint failed: {e}")

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
        except requests.exceptions.RequestException as e:
            self.fail(f"Request to the /clear-chat endpoint failed: {e}")
        except ValueError as e:
            self.fail(f"Response is not valid JSON: {e}")

if __name__ == "__main__":
    unittest.main()
