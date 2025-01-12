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


def setup_logging(directory_name):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(os.path.join(directory_name, 'app.log')),
            logging.StreamHandler()
        ]
    )


def create_directory(directory_name: str = None) -> str:
    if directory_name:
        if not os.path.exists(directory_name):
            os.mkdir(directory_name)
            setup_logging(directory_name)
            logging.info(f'created directory {directory_name}')
        else:
            raise FileExistsError(f'directory {directory_name} already exists')
        return directory_name
    else:
        directory_name = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        os.mkdir(directory_name)
        setup_logging(directory_name)
        logging.info(f'created directory {directory_name}')
    os.chdir(directory_name)
    return directory_name


async def send_request(session, url):
    try:

        logging.info(f"sending request to {url}")

        async with session.get(url, timeout=20) as response:
            html = await response.text()
            file_name = os.path.join(os.getcwd(), url.split('/')[-1].replace('.', '_') + '.html')
            with open(file_name, 'w') as f:
                f.write(html)
            logging.info(f"request to {url} completed and saved to {file_name}")

    except Exception as e:
        error_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_details = traceback.format_exception_only(type(e), e)
        logging.error(f'An error occurred at {error_time} while sending request to {url}: {error_details}')
        logging.debug(traceback.format_exc())


async def main():
    create_directory()
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, url) for url in URLS]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
