from github import Github
import requests
import os
import json

# Organization name 
organization = 'fuchicorp'

## Getting GitHub user and 
g = Github('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', base_url='https://api.github.com')
org = g.get_organization(organization)


repo = g.get_repo("AsiaO1/create-github-issue-with-python")
print(repo)

# create miletone and create issue with milestone and assigned user ? try putting in into for loop and pass all milestones
milestone1 = repo.create_milestone("1 Cluster Deployment")
milestone2 = repo.create_milestone("2 Common Tools Deployment")


title1="1 Cluster Deployment"

# users = [ user for user in org.get_members('')]
repo.create_issue(title=title1, assignee="AsiaO1", milestone=milestone1)


# close all issues
# def close_all_issues(repo):
#   open_issues = repo.get_issues(state='open')
#   for issue in open_issues:
#     issue.edit(state="closed")
        