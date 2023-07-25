import csv
import urllib.request
GITHUB_CSV = "https://raw.githubusercontent.com/TransperfectTPT/versions/main/versions.csv"


def get_version(toolname):
    # Instead of pandas, we will use the csv module
    response = urllib.request.urlopen(GITHUB_CSV)
    lines = [l.decode('utf-8') for l in response.readlines()]
    # print(lines)
    cr = csv.reader(lines)
    for row in cr:
        # list indices must be integer or slices, not str
        if row[0] == toolname:
            gh_version = row[1]
            print(f'Tool: {toolname}, GitHub version: {gh_version}')
            return gh_version


def compare_versions(toolname, current_version):
    try:
        gh_version = get_version(toolname)

        if gh_version is None:
            print(f"Tool name not found: {toolname}")
            raise KeyError(f"Tool name not found: {toolname}")

        if gh_version > current_version:
            print(f"New version available: {gh_version}")
            raise ValueError(f"New version available: {gh_version}. Please update your tool from Confluence or contact the BCN Automation Team.")
        else:
            print("You have the latest version")

    except KeyError as key_error:
        print(f"Tool name not found: {key_error}")


if __name__ == '__main__':
    compare_versions("Storyline Exports Wizard", "1.0")
