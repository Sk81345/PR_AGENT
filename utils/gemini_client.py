import os

from github import Github


def get_github_client():

    token = os.getenv("PR_AGENT_GITHUB_TOKEN") or os.getenv("GITHUB_TOKEN")

    if not token:

        raise ValueError(

            "Missing GitHub token. Set PR_AGENT_GITHUB_TOKEN or GITHUB_TOKEN."

        )

    return Github(token)
