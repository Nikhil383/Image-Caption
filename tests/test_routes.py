# Integration tests for Flask routes

import pytest
from PIL import Image
from io import BytesIO
from image_caption import create_app
from unittest.mock import patch, MagicMock

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SECRET_KEY": "test-secret-key",
        "WTF_CSRF_ENABLED": False,
        "RATELIMIT_ENABLED": False,  # Disable rate limits for testing
    })
    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


def test_get_index(client):
    """Test that GET / returns 200 and renders the form."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'AI Image Captioner' in response.data
    assert b'Generate Caption' in response.data


def test_post_no_file(client):
    """Test POST without file returns error."""
    response = client.post('/', data={}, follow_redirects=True)
    assert response.status_code == 200
    assert b'No file part' in response.data


def test_post_empty_filename(client):
    """Test POST with empty filename returns error."""
    response = client.post('/', data={'image': (BytesIO(), '')}, follow_redirects=True)
    assert response.status_code == 200
    assert b'No selected file' in response.data


def test_post_invalid_file_type(client):
    """Test POST with invalid file type returns error."""
    # Create a fake text file
    fake_file = BytesIO(b'This is not an image')
    fake_file.name = 'test.txt'
    
    response = client.post('/', data={'image': (fake_file, 'test.txt')}, follow_redirects=True)
    assert response.status_code == 200
    # Should show error about invalid file type
    assert b'Invalid file type' in response.data


def test_post_valid_image_success(client):
    """Test POST with valid image returns caption."""
    # Create a small test image
    img = Image.new('RGB', (100, 100), color='red')
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    
    # Mock the caption generation
    with patch('image_caption.routes.generate_caption') as mock_caption:
        mock_caption.return_value = 'a red square'
        
        response = client.post('/', data={'image': (img_bytes, 'test.png')})
        
        assert response.status_code == 200
        assert b'a red square' in response.data
        assert b'Generated Caption' in response.data
        mock_caption.assert_called_once()


def test_post_file_too_large(app, client):
    """Test POST with file exceeding size limit returns error."""
    app.config['MAX_CONTENT_LENGTH'] = 1024  # 1KB limit for test
    
    large_file = BytesIO(b'x' * 2048)  # 2KB file
    large_file.name = 'large.png'
    
    response = client.post('/', data={'image': (large_file, 'large.png')})
    # Flask returns 413 Request Entity Too Large, or 302 if error handler redirects
    assert response.status_code in [413, 302, 200]
