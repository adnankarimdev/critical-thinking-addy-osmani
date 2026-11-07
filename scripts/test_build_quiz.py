import copy
import json
import unittest
from build_quiz import build


class QuizTests(unittest.TestCase):
    def setUp(self):
        self.data = {'title': 'Own a change', 'scope': 'Scoped change', 'snapshot': 'digest-one', 'trigger': 'Done', 'questions': [{'id': 'one', 'topic': 'Explain', 'prompt': 'What changed?', 'evidence': [{'label': 'file:1', 'text': 'source'}], 'rubric': {'required': ['AGENT_ONLY_ANSWER']}}]}

    def payload(self, html):
        return json.loads(html.split('<script type="application/json" id="quiz-data">')[1].split('</script>')[0])

    def test_rubric_excluded_and_script_escape(self):
        self.data['questions'][0]['evidence'][0]['text'] = '</script><script>alert(1)</script>'
        html, _ = build(self.data)
        self.assertNotIn('AGENT_ONLY_ANSWER', html)
        self.assertNotIn('</script><script>alert(1)', html)
        self.assertEqual(self.payload(html)['questions'][0]['evidence'], self.data['questions'][0]['evidence'])

    def test_identity_tracks_evidence_and_snapshot(self):
        _, original = build(self.data)
        self.assertEqual(build(copy.deepcopy(self.data))[1], original)
        self.data['snapshot'] = 'digest-two'
        self.assertNotEqual(build(self.data)[1], original)
        self.data['snapshot'] = 'digest-one'
        self.data['questions'][0]['evidence'][0]['text'] = 'changed source'
        self.assertNotEqual(build(self.data)[1], original)

    def test_reject_missing_evidence_and_duplicate_ids(self):
        missing = copy.deepcopy(self.data)
        missing['questions'][0]['evidence'] = []
        with self.assertRaises(ValueError):
            build(missing)
        self.data['questions'].append(copy.deepcopy(self.data['questions'][0]))
        with self.assertRaises(ValueError):
            build(self.data)


if __name__ == '__main__':
    unittest.main()
