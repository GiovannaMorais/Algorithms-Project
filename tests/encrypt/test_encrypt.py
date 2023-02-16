from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message = 'ABCDEFA'

    assert encrypt_message(message, 3) == 'CBA_AFED'
    assert encrypt_message(message, 4) == 'AFE_DCBA'
    assert encrypt_message(message, 9) == 'AFEDCBA'

    with pytest.raises(TypeError):
        encrypt_message(message, 'key')
    with pytest.raises(TypeError):
        encrypt_message(3, 3)
