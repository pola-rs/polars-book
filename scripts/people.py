import itertools
from github import Github

g = Github(None)

ICON_TEMPLATE="[![{login}]({avatar_url}){{.contributor_icon}}]({html_url})"

if __name__ == "__main__":
    repo = g.get_repo("pola-rs/polars")
    contributors = repo.get_contributors()

    with open("./docs/people.md","w") as f:
        for c in itertools.islice(contributors, 50):
            f.write(ICON_TEMPLATE.format(login=c.login,avatar_url=c.avatar_url,html_url=c.html_url) + "\n")
