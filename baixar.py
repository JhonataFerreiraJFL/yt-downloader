import argparse
import yt_dlp
import os

def baixar_video(url, quality, folder):
    os.makedirs(folder, exist_ok=True)

    # pega APENAS um stream já pronto (sem merge)
    format_str = f"best[height<={quality}][ext=mp4]/best[ext=mp4]/best"

    ydl_opts = {
        "format": format_str,
        "outtmpl": os.path.join(folder, "%(title)s.%(ext)s"),
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--quality", type=int, default=1080)
    parser.add_argument("--folder", default="downloads")

    args = parser.parse_args()

    baixar_video(args.url, args.quality, args.folder)
