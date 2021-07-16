"""
This module contains utilities for the Questions GameSection.
"""
import os
from dataclasses import dataclass
from json import load


@dataclass
class Question:
    id: str
    prompt: str
    choices: list[str]
    correct: int

    def is_index_correct(self, index: int) -> bool:
        return index == self.correct


def gather_questions(questions: list[dict]) -> list[Question]:
    return [
        Question(
            q['id'],
            q['prompt'],
            q['choices'],
            q['correct']
        )
        for q in questions
    ]


def get_all_questions(fp: os.PathLike) -> list[Question]:
    with open(fp, 'r') as f:
        contents = load(f)

    return gather_questions(contents)
