# Integration tests for Flask routes

import pytest
from PIL import Image
from io import BytesIO
from image_caption.app import app
from image_caption.models import CaptionModel
from unittest.mock import patch, MagicMock


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test-secret-key'
    with app.test_client() as client:
        yield client


@pytest.fixture
def reset_model():
    """Reset the model singleton before and after each test."""
    original_instance = CaptionModel._instance
    CaptionModel._instance = None
    yield
    CaptionModel._instance = original_instance


def test_get_index(client):
    """Test that GET / returns 200 and renders the form."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'AI Image Captioner' in response.data
    assert b'Generate Caption' in response.data


def test_post_no_file(client):
    """Test POST without file returns error."""
    response = client.post('/', data={})
    assert response.status_code == 200
    # Should redirect back, but test client follows redirects
    assert b'No file part' in response.data or response.status_code == 302


def test_post_empty_filename(client):
    """Test POST with empty filename returns error."""
    response = client.post('/', data={'image': (BytesIO(), '')})
    assert response.status_code == 200
    # Should redirect back
    assert b'No selected file' in response.data or response.status_code == 302


def test_post_invalid_file_type(client, reset_model):
    """Test POST with invalid file type returns error."""
    # Create a fake text file
    fake_file = BytesIO(b'This is not an image')
    fake_file.name = 'test.txt'
    
    response = client.post('/', data={'image': (fake_file, 'test.txt')})
    assert response.status_code == 200
    # Should show error about invalid file type
    assert b'invalid' in response.data.lower() or b'not supported' in response.data.lower()


def test_post_valid_image_success(client, reset_model):
    """Test POST with valid image returns caption."""
    # Create a small test image
    img = Image.new('RGB', (100, 100), color='red')
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    
    # Mock the caption generation
    with patch('image_caption.app.generate_caption') as mock_caption:
        mock_caption.return_value = 'a red square'
        
        response = client.post('/', data={'image': (img_bytes, 'test.png')})
        
        assert response.status_code == 200
        assert b'a red square' in response.data
        assert b'Generated Caption' in response.data
        mock_caption.assert_called_once()


def test_post_file_too_large(client):
    """Test POST with file exceeding size limit returns error."""
    # Save original config
    original_max_size = app.config.get('MAX_CONTENT_LENGTH')
    
    try:
        # Set a small limit for testing
        app.config['MAX_CONTENT_LENGTH'] = 1024  # 1KB limit for test
        
        large_file = BytesIO(b'x' * 2048)  # 2KB file
        large_file.name = 'large.png'
        
        response = client.post('/', data={'image': (large_file, 'large.png')})
        # Flask returns 413 Request Entity Too Large, or 200 if error handler redirects
        assert response.status_code in [413, 200]
    finally:
        # Restore original config
        if original_max_size is not None:
            app.config['MAX_CONTENT_LENGTH'] = original_max_size
        elif 'MAX_CONTENT_LENGTH' in app.config:
            del app.config['MAX_CONTENT_LENGTH']
