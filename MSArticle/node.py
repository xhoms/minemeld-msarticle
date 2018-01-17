import logging
import requests
import re
import itertools
import csv

from minemeld.ft.csv import CSVFT

LOG = logging.getLogger(__name__)
RE_PATTERN = 'https:\\/\\/download\\.microsoft\\.com\\/download\\/[a-zA-Z0-9\\/\\-\\.]+'


class Miner(CSVFT):
    _re_obj = re.compile(RE_PATTERN)

    def configure(self):
        super(Miner, self).configure()

    def _build_iterator(self, now):
        if self.url is None:
            raise RuntimeError(
                '{} - URL not provided'.format(self.name)
            )
        # Step 1: Get the article and locate the direct download link
        r = requests.get(self.url)
        try:
            r.raise_for_status()
        except:
            LOG.error('%s - exception in request: %s %s',
                      self.name, r.status_code, r.content)
            raise
        article_text = r.text
        m = self._re_obj.findall(article_text)
        if len(m) == 0:
            LOG.error('%s - unable to find a direct download link in: %s', self.name, self.url)
            raise RuntimeError('{} - No direct download link found'.format(self.name))
        # Step 2: Grab the CSV File
        r = requests.get(m[0], stream=True)
        try:
            r.raise_for_status()
        except:
            LOG.error('%s - exception in request: %s %s',
                      self.name, r.status_code, r.content)
            raise
        response = r.raw

        if self.ignore_regex is not None:
            response = itertools.ifilter(
                lambda x: self.ignore_regex.match(x) is None,
                response
            )

        csvreader = csv.DictReader(
            response,
            fieldnames=self.fieldnames,
            **self.dialect
        )

        return csvreader
