#!/usr/bin/env python3
"""Build a portable ownership quiz. Assessment rubrics stay in the input file."""
import argparse
import hashlib
import json
from pathlib import Path


def build(data):
    for key in ('title', 'snapshot', 'scope', 'trigger'):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f'{key} must be a nonempty string')
    questions = data.get('questions')
    if not isinstance(questions, list) or not 1 <= len(questions) <= 8:
        raise ValueError('Provide between 1 and 8 questions')
    public = {key: data[key] for key in ('title', 'snapshot', 'scope', 'trigger')}
    public['questions'] = []
    ids = set()
    for q in questions:
        for key in ('id', 'topic', 'prompt'):
            if not isinstance(q.get(key), str) or not q[key].strip():
                raise ValueError(f'Each question needs {key}')
        if q['id'] in ids:
            raise ValueError('Question IDs must be unique')
        ids.add(q['id'])
        if not isinstance(q.get('rubric'), dict) or not q['rubric'].get('required'):
            raise ValueError(f"Question {q['id']} needs an agent assessment rubric")
        evidence = q.get('evidence')
        if not isinstance(evidence, list) or not evidence:
            raise ValueError(f"Question {q['id']} needs inspected evidence")
        for item in evidence:
            if not all(isinstance(item.get(k), str) and item[k].strip() for k in ('label', 'text')):
                raise ValueError('Evidence needs a label and text')
        public['questions'].append({
            **{key: q[key] for key in ('id', 'topic', 'prompt')},
            'evidence': [{key: item[key] for key in ('label', 'text')} for item in evidence]
        })
    canonical = json.dumps(public, sort_keys=True, ensure_ascii=False)
    public['quiz_id'] = hashlib.sha256(canonical.encode()).hexdigest()[:20]
    # Prevent user-supplied strings from breaking out of the JSON script element.
    payload = json.dumps(public, ensure_ascii=False).replace('&', '\\u0026').replace('<', '\\u003c').replace('>', '\\u003e')
    template = (Path(__file__).resolve().parent.parent / 'assets' / 'ownership-quiz.html').read_text()
    return template.replace('__QUIZ_DATA__', payload), public['quiz_id']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        parser.error('Input and output must be different files')
    try:
        html, quiz_id = build(json.loads(args.input.read_text()))
    except (ValueError, TypeError, KeyError, AttributeError) as exc:
        parser.error(str(exc))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html)
    print(f'Created {args.output.resolve()}\nQuiz ID: {quiz_id}')


if __name__ == '__main__':
    main()
