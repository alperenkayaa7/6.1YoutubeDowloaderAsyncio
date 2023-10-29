import asyncio

import pytube
from pytube import YouTube

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

async def dowload1():
    url = input("enter video url :")
    path ="/Users/kaya/Desktop/İndirilen\ Müzikler"

    pytube.YouTube(url).streams.get_highest_resolution().download(path)


async def dowload2():
    url = input("enter video url :")
    path = "/Users/kaya/Desktop/İndirilen\ Müzikler"

    pytube.YouTube(url).streams.get_highest_resolution().download(path)

asyncio.run(dowload1())
asyncio.run(dowload2())