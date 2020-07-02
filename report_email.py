#!/usr/bin/env python3

from datetime import datetime
import run
import emails
import reports

heading = "Processed Update on {}".format(datetime.date(datetime.now()))
body = ""
fruits = run.get_all_details()
print(fruits)
for fruit in fruits:
  detail = "<br/>"
  detail += "name: " + fruit["name"] + "<br/>"
  detail += "weight: " + fruit["weight"] + " lbs<br/>"
  body += detail
print(heading)
print(body)

if __name__ == "__main__":
  reports.generate_report("/tmp/processed.pdf", heading, body)
  message = emails.generate_email("automation@example.com", "student-01-65941aaf72b7@example.com", "Upload Completed - Online Fruit Store",
                        "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
                        "/tmp/processed.pdf")
  emails.send_email(message)
