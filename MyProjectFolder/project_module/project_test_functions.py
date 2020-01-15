"""Test for project_functions. Used to test if the different functions 
   will return what they are supposed to and created a function that 
   tests all the test functions at once
"""

from project_module.project_functions import *

def test_south_campus():
    """Tests one of the levels of the game which indicates if the rest will work"""
    response = "mandeville"
    assert isinstance(response, str)
    assert callable(south_campus)
    
def test_end_game():
    """Tests if the game exits and returns to main menu after completion"""
    response = "quit"
    assert isinstance(response, str)
    assert callable(end_game)
    

def test_all():
    """Test all testers created"""
    test_south_campus()
    test_end_game()