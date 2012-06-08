#!/usr/bin/python
from enrolments_db import EnrolmentWriter, DuplicateChecker
from mock import MagicMock
import unittest

class EnrolmentTests(unittest.TestCase):
    
    def testEnrolmentCreatedForNonExistingEnrolment(self):
        enrolment = Enrolment(100, 200)
        dc_mock = MagicMock(spec=DuplicateChecker)
        dc_mock.has_existing_enrolment.return_value = False
        ew_mock = MagicMock(spec=EnrolmentWriter)
        
        enrolment.process_enrolment(dc_mock, ew_mock)
        
        self.assertEqual(True, ew_mock.create_enrolment.called)
    
    def testEnrolmentNotCreatedForExistingEnrolment(self):
        enrolment = Enrolment(100, 200)
        dc_mock = MagicMock(spec=DuplicateChecker)
        dc_mock.has_existing_enrolment.return_value = True
        ew_mock = MagicMock(spec=EnrolmentWriter)
        
        enrolment.process_enrolment(dc_mock, ew_mock)
        
        self.assertEqual(False, ew_mock.create_enrolment.called)

class Enrolment:
    
    def __init__(self, course_id, learner_id):
        self.course_id = course_id
        self.learner_id = learner_id
    
    def process_enrolment(self, duplicate_checker, enrolment_writer):
        if not duplicate_checker.has_existing_enrolment(self.course_id, self.learner_id):
            enrolment_writer.create_enrolment(self.course_id, self.learner_id)

if __name__ == '__main__':
    unittest.main()
