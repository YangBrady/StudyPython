import sys

sys.path.append("..")

import env.config as conf


def main():
    print(conf.output_dir)


if __name__ == "__main__":
    main()
