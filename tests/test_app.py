# Unit tests for image captioning model

import pytest
from PIL import Image
from image_caption.models import generate_caption
from unittest.mock import MagicMock, patch

def test_generate_caption_success():
    """Test generating a caption successfully."""
    mock_model = MagicMock()
    mock_model.generate_content.return_value.text = "a cute cat"
    
    with patch('google.generativeai.GenerativeModel', return_value=mock_model):
        with patch('image_caption.models.API_KEY', 'fake_key'):
            # Dummy image
            img = Image.new('RGB', (100, 100))
            result = generate_caption(img)
            
            assert result == 'a cute cat'

def test_generate_caption_no_api_key():
    """Test handling of missing API key."""
    with patch('image_caption.models.API_KEY', None):
        img = Image.new('RGB', (100, 100))
        result = generate_caption(img)
        assert "Error" in result
        assert "GOOGLE_API_KEY is not configured" in result

def test_generate_caption_error():
    """Test handling of API errors."""
    mock_model = MagicMock()
    mock_model.generate_content.side_effect = Exception("API failed")
    
    with patch('google.generativeai.GenerativeModel', return_value=mock_model):
        with patch('image_caption.models.API_KEY', 'fake_key'):
            img = Image.new('RGB', (100, 100))
            result = generate_caption(img)
            
            assert "Error" in result
            assert "API failed" in result
