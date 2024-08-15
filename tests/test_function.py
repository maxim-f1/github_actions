from random import randint

import pytest

from src.main import function


@pytest.mark.asyncio
@pytest.mark.parametrize('a', [randint(-255, 255) for _ in range(20)])
async def test_success(a):
    assert await function(a) == a * 2
