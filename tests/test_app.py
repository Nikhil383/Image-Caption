# Unit tests for image captioning model

import pytest
from PIL import Image
from image_caption.models import CaptionModel, generate_caption
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_pipeline():
    with patch('image_caption.models.pipeline') as mock:
        yield mock

def test_model_singleton(mock_pipeline):
    """Test that the model is only initialized once."""
    # Reset singleton
    CaptionModel._instance = None
    
    # First call
    model1 = CaptionModel.get_pipeline()
    # Second call
    model2 = CaptionModel.get_pipeline()
    
    assert model1 is model2
    assert mock_pipeline.call_count == 1

def test_generate_caption_success():
    """Test generating a caption successfully."""
    mock_pipe = MagicMock()
    mock_pipe.return_value = [{'generated_text': 'a cute cat'}]
    
    # Inject mock into singleton
    CaptionModel._instance = mock_pipe
    
    # Dummy image
    img = Image.new('RGB', (100, 100))
    result = generate_caption(img)
    
    assert result == 'a cute cat'

def test_generate_caption_error():
    """Test handling of prediction errors."""
    mock_pipe = MagicMock()
    mock_pipe.side_effect = Exception("Model failed")
    
    CaptionModel._instance = mock_pipe
    
    img = Image.new('RGB', (100, 100))
    result = generate_caption(img)
    
    assert "Error" in result
    assert "Model failed" in result
