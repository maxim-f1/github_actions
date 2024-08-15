import pytest

from src.main import function


@pytest.mark.asyncio
async def test_success():
    assert await function(2) == 4
