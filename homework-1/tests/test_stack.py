"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest
from src.stack import Stack, Node


def test_push():
    stack = Stack()
    stack.push('test_data')
    node = stack.top
    assert isinstance(stack.top, Node)
    assert stack.top.data == 'test_data'
    assert stack.top.next_node is None
    stack.push('test_data1')
    assert isinstance(stack.top.next_node, Node)
    assert stack.top.data == 'test_data1'
    assert stack.top.next_node is node
