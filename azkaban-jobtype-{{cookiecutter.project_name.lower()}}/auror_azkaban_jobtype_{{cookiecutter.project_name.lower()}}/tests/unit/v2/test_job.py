#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from auror_azkaban_jobtype_{{cookiecutter.project_name.lower()}}.v2.job import {{cookiecutter.project_name}}


class {{cookiecutter.project_name}}JobTest(TestCase):

    def test_example(self):
        self.assertEqual("true", "true")