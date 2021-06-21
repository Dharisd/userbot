import youtube_dl


class TikTok:

    async def download_tiktok(url):
        ydl_opts = {
            'outtmpl': 'downloads/tiktok.%(ext)s',
            'ignoreerrors': True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])


        #should return downloaded file path
        return "downloads/tiktok.mp4"

