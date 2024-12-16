import pytest
from project import calc_child,calc_teen
from tools import get_labour_type, get_labour_financing_type
from unittest.mock import patch

def test_get_labour_type():
    with patch('builtins.input', return_value = 'cc'):
        assert get_labour_type() == 'cc'
    with patch('builtins.input', return_value = 'natural'):
        assert get_labour_type() == 'natural'
    with patch('builtins.input', side_effect=['incorrect_input', 'natural']):
        assert get_labour_type() == 'natural'

def test_calc_child():
    assert calc_child() ==  280056.49732331914

def test_calc_teen():
    assert calc_teen() == 318589.36746430886

def test_get_labour_financing_type():
    with patch('builtins.input', return_value = 'priv'):
        assert get_labour_financing_type() == 'priv'
    with patch('builtins.input', return_value = 'nfz'):
        assert get_labour_financing_type() == 'nfz'
    with patch('builtins.input', side_effect=['incorrect_input', 'priv']):
        assert get_labour_financing_type() == 'priv'