#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader


def render_pages():
    loader = FileSystemLoader('source')
    env = Environment(loader=loader)

    for name in loader.list_templates():
        if name.startswith('_'):
            continue

        template = env.get_template(name)
        print "writing {}".format(name)
        with open(name, 'w') as handle:
            output = template.render()
            handle.write(output)


def main():
    render_pages()


if __name__ == '__main__':
    main()


# def static_links():
    # return (
        # ("documentation", "https://nameko.readthedocs.org"),
        # ("source code", "https://github.com/onefinestay/nameko"),
    # )
# TEMPLATE = object()
# links = [
    # ("index", TEMPLATE),
    # ("documentation", "https://nameko.readthedocs.org"),
    # ("community", TEMPLATE),
    # ("source code", "https://github.com/onefinestay/nameko"),
# ]
