#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(filename, heading, body):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_heading = Paragraph(heading, styles["h1"])
  report_body = Paragraph(body, styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_heading, report_body])
