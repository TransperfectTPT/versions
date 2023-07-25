# import pandas as pd
import csv
GITHUB_CSV = r"https://raw.githubusercontent.com/TransperfectTPT/versions/main/versions.csv"


def get_version(toolname):
    df = pd.read_csv(GITHUB_CSV, header=0, index_col=0)
    gh_version = df.loc[toolname, "version"]
    print(f'Tool: {toolname}, GitHub version: {gh_version}')
    return gh_version


def compare_versions(toolname, current_version):
    try:
        gh_version = get_version(toolname)

        if gh_version > current_version:
            print(f"New version available: {gh_version}")
            raise ValueError(f"New version available: {gh_version}. Please update your tool from Confluence or contact the BCN Automation Team.")
        else:
            print("You have the latest version")

    except KeyError as key_error:
        print(f"Tool name not found: {key_error}")


if __name__ == '__main__':
    get_version("Tool example 1")
