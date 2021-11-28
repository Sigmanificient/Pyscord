import argparse


def display_docs():
    import webbrowser
    webbrowser.open("https://docs.pincer.dev")


def display_version():
    import pincer
    print("Pincer", pincer.__version__)


def init(project_name, project_path):
    pass


def main():
    parser = argparse.ArgumentParser(
        description="A cli tool to help you enhance your pincer experience."
    )

    parser.add_argument(
        "-d", "--docs",
        help="Open the documentation in the web browser",
        action="store_true"
    )

    parser.add_argument(
        "-v", "--version",
        help="Show the version of the pincer",
        action="store_true"
    )

    parser.add_argument(
        "-i", "--init",
        help="Initialize a new pincer project",
        nargs=1, default=None
    )

    parser.add_argument(
        "-p", "--path",
        help="The path to the project",
        nargs=1, default=None
    )

    args = parser.parse_args()

    if args.docs:
        return display_docs()

    if args.version:
        return display_version()

    if args.init:
        return init(args.init[0], args.path[0])

    parser.print_help()


if __name__ == '__main__':
    main()
