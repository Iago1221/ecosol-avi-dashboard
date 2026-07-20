import math

from clean import coerce_nullable_int


def test_none_stays_none():
    assert coerce_nullable_int(None) is None


def test_nan_becomes_none():
    assert coerce_nullable_int(float("nan")) is None


def test_blank_string_becomes_none():
    assert coerce_nullable_int("") is None
    assert coerce_nullable_int("   ") is None


def test_explicit_zero_stays_zero():
    assert coerce_nullable_int(0) == 0
    assert coerce_nullable_int(0.0) == 0


def test_positive_values():
    assert coerce_nullable_int(5.0) == 5
    assert coerce_nullable_int(62) == 62
