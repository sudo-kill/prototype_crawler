import os
import asyncio
import random
import aiohttp
import re
import colorama

'''
старый код, любые ошибки / баги / нечитаемый код прощаются 
words.txt словарь с поддоменами
'''


class Crawler:
    def __init__(self, url: str, response_code_visible: bool = True):
        self.domain_url = url
        self.response_code_visible = response_code_visible

    async def crawl(self):
        async with aiohttp.ClientSession() as session:
            with open('words.txt', 'r') as f:
                for word in f:
                    word = word.strip().replace('\n', '')
                    url = f'https://{word}.{self.domain_url}'
                    try:
                        async with session.get(url) as response:
                            response_code = response.status
                            if self.response_code_visible is True:
                                if 100 <= response_code < 300:
                                    print(colorama.Fore.GREEN, f'[{response_code}] {url}')
                                elif 400 <= response_code < 500:
                                    print(colorama.Fore.RED, f'[{response_code}] {url}')
                            elif self.response_code_visible is False:
                                if 200 <= response_code < 300:
                                    print(colorama.Fore.GREEN, f'{url}')
                                # elif 400 <= response_code < 500:
                                #     print(colorama.Fore.RED, f'{url}')
                    except:
                        pass


async def main():
    target = input('Введите адрес сайта: ')
    http_status = input('Показывать статус коды?  [Y/n]: ')
    code = False if http_status.lower() == 'n' else True
    crawler = Crawler(url=target, response_code_visible=code)
    await crawler.crawl()


if __name__ == "__main__":
    asyncio.run(main())
