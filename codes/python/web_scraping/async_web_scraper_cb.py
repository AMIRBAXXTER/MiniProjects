import asyncio
import traceback
import aiohttp
import os
import datetime
import logging

URLS = [
    'https://python.org',
    'https://docker.com',
    'https://google.com',
    'https://facebook.com',
    'https://stackoverflow.com',
    'https://github.com',
    'https://reddit.com',
]


class WebScraper:
    def __init__(self, urls, directory_name=None, max_concurrent_requests=3, timeout=20, logfile='app.log'):
        self.urls = urls
        self.directory_name = directory_name
        self.max_concurrent_requests = max_concurrent_requests
        self.timeout = timeout
        self.logfile = logfile
        self._setup_directory()
        self._setup_logging()

    def mk_ch_dir(self):
        os.mkdir(self.directory_name)
        os.chdir(self.directory_name)
        self._setup_logging()

    def _setup_directory(self):

        if self.directory_name:
            if not os.path.exists(self.directory_name):
                self.mk_ch_dir()
                logging.info(f'Created directory {self.directory_name}')
            else:
                raise FileExistsError(f'directory {self.directory_name} already exists')
        else:
            self.directory_name = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.mk_ch_dir()
            logging.info(f'Created directory {self.directory_name}')

        return self.directory_name

    def _setup_logging(self):

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(os.path.join(self.logfile)),
                logging.StreamHandler()
            ]
        )

    async def _send_request(self, session, url, semaphore):
        try:
            async with semaphore:
                logging.info(f'Sending request to {url}')
                async with session.get(url, timeout=self.timeout) as response:
                    html = await response.text()
                    file_name = os.path.join(os.getcwd(), url.split('/')[-1].replace('.', '_') + '.html')
                    with open(file_name, 'w') as f:
                        f.write(html)
                    logging.info(f'Request to {url} completed and saved to {file_name}')
        except Exception as e:
            error_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_details = traceback.format_exception_only(type(e), e)
            logging.error(f'An error occurred at {error_time} while sending request to {url}: {error_details}')
            logging.debug(traceback.format_exc())

    async def fetch_all_urls(self):
        semaphore = asyncio.Semaphore(self.max_concurrent_requests)
        async with aiohttp.ClientSession() as session:
            tasks = [self._send_request(session, url, semaphore) for url in self.urls]
            await asyncio.gather(*tasks)

    def run(self):
        asyncio.run(self.fetch_all_urls())


if __name__ == "__main__":
    fetcher = WebScraper(
        urls=URLS,
        directory_name='my_directory',
        max_concurrent_requests=4,
        timeout=15,
        logfile='my_logfile.log'
    )
    fetcher.run()
