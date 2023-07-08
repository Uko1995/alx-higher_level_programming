#!/usr/bin/python3
"""
module for lazy_matrix_mul()
"""
from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrix using numpy

    Args:
        m_a (list): First matrix
        m_b (list): second matrix

    Returns:
        The result of multiply m_a by m_b

    """
    return matmul(m_a, m_b)
