"""pandoc-code-glob is a panflute pandoc filter to recursively search for
file patterns to be included for the \pycode latex macro."""

import glob

import panflute as pf


def prepare(doc):
    pass


def action(elem, doc):
    if isinstance(elem, pf.elements.RawInline) and elem.format == 'tex':
        if '\\pycode{' in elem.text:
            start = elem.text.index('\\pycode{') + len('\\pycode{')
            end = start + elem.text[start:].index('}')

            filename = elem.text[start:end]

            hits = glob.glob('**/{}'.format(filename), recursive=True)
            if len(hits) < 1:
                pf.debug('Found no matches for filename `{}`'.format(filename))
                return
            if len(hits) > 1:
                pf.debug('Found multiple matches for filename `{}`'
                         .format(filename))

            elem.text = elem.text[:start] + hits[0] + elem.text[end:]


def finalize(doc):
    pass


def main(doc=None):
    return pf.run_filter(action,
                         prepare=prepare,
                         finalize=finalize,
                         doc=doc)


if __name__ == '__main__':
    main()
