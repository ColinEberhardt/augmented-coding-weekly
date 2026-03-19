#!/usr/bin/env python3
"""
Creates a new draft newsletter issue based on the latest existing issue.
Increments the issue number by 1 and the date by one week.
"""

import os
import re
from datetime import datetime, timedelta


def find_latest_issue(posts_dir="_posts"):
    """Find the latest issue file in the posts directory."""
    pattern = re.compile(r"(\d{4}-\d{2}-\d{2})-issue-(\d+)\.md")

    latest_date = None
    latest_number = 0
    latest_file = None

    for filename in os.listdir(posts_dir):
        match = pattern.match(filename)
        if match:
            date_str, issue_num = match.groups()
            issue_num = int(issue_num)
            date = datetime.strptime(date_str, "%Y-%m-%d")

            if latest_date is None or date > latest_date or (date == latest_date and issue_num > latest_number):
                latest_date = date
                latest_number = issue_num
                latest_file = filename

    return latest_date, latest_number, latest_file


def create_new_issue(posts_dir="_posts"):
    """Create a new draft issue file."""
    latest_date, latest_number, latest_file = find_latest_issue(posts_dir)

    if latest_date is None:
        print("No existing issues found!")
        return

    print(f"Latest issue: {latest_file}")
    print(f"  Date: {latest_date.strftime('%Y-%m-%d')}")
    print(f"  Issue number: {latest_number}")

    # Calculate new issue details
    new_date = latest_date + timedelta(days=7)
    new_number = latest_number + 1
    new_filename = f"{new_date.strftime('%Y-%m-%d')}-issue-{new_number}.md"
    new_filepath = os.path.join(posts_dir, new_filename)

    # Check if file already exists
    if os.path.exists(new_filepath):
        print(f"\nError: File {new_filename} already exists!")
        return

    # Create the draft content
    content = f"""---
layout: post
title: ! 'Issue #{new_number}'
author: ceberhardt
published: false
thumbnail:
summary:
---

"""

    # Write the new file
    with open(new_filepath, 'w') as f:
        f.write(content)

    print(f"\nCreated new issue: {new_filename}")
    print(f"  Date: {new_date.strftime('%Y-%m-%d')}")
    print(f"  Issue number: {new_number}")
    print(f"  Path: {new_filepath}")


if __name__ == "__main__":
    create_new_issue()
