import pytest
import sys
import os

# FIX: ensure the project root is in sys.path so tests can import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)

# --- check_guess -------------------------------------------------------------

def test_winning_guess():
    # when guess equals secret you should get outcome "Win" and a celebration message
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_guess_with_non_numeric():
    # even if a string is passed it should still compare by str
    outcome, message = check_guess("77",  "77")
    assert outcome == "Win"

# --- get_range_for_difficulty ------------------------------------------------

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)


def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_range_default():
    assert get_range_for_difficulty("SomethingElse") == (1, 100)

# --- parse_guess -------------------------------------------------------------

def test_parse_valid_integer():
    ok, guess, err = parse_guess("42")
    assert ok is True
    assert guess == 42
    assert err is None


def test_parse_float_string():
    ok, guess, err = parse_guess("3.0")
    assert ok is True
    assert guess == 3


def test_parse_empty():
    ok, guess, err = parse_guess("")
    assert ok is False
    assert guess is None
    assert "Enter a guess" in err


def test_parse_none():
    ok, guess, err = parse_guess(None)
    assert not ok
    assert guess is None


def test_parse_bad_input():
    ok, guess, err = parse_guess("not a number")
    assert ok is False
    assert guess is None
    assert "not a number" in err.lower()

# --- update_score ------------------------------------------------------------

def test_update_score_win_minimum_points():
    # attempt_number 0 should still grant 100 - 10*1 = 90
    assert update_score(0, "Win", 0) == 90


def test_update_score_win_floor():
    # if computed points go below 10, floor at 10
    assert update_score(0, "Win", 20) == 10


def test_update_score_too_high_even():
    assert update_score(0, "Too High", 2) == 5


def test_update_score_too_high_odd():
    assert update_score(10, "Too High", 3) == 5


def test_update_score_too_low():
    assert update_score(10, "Too Low", 1) == 5


def test_update_score_unknown_outcome():
    assert update_score(10, "Something", 5) == 10
