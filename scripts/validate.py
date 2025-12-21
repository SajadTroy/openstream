import requests

INPUT_FILE = "streams/community.m3u"
OUTPUT_FILE = "index.m3u"


def is_stream_working(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        with requests.get(url, headers=headers, stream=True, timeout=5) as response:
            if response.status_code != 200:
                return False

            first_chunk = next(response.iter_content(chunk_size=7)).decode(
                "utf-8", errors="ignore"
            )

            if first_chunk.startswith("#EXTM3U"):
                return True
            else:
                return False

    except Exception:
        return False


def main():
    print("Starting Deep Stream Validation...")

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    valid_streams = ["#EXTM3U\n"]
    seen_urls = set()

    for i in range(1, len(lines)):
        line = lines[i].strip()

        if line.startswith("http"):
            prev_line = lines[i - 1].strip()

            if not prev_line.startswith("#EXTINF"):
                continue

            if line in seen_urls:
                print(f"⏩ Skipping Duplicate: {prev_line.split(',')[-1].strip()}")
                continue

            if is_stream_working(line):
                print(f"✅ Working: {prev_line.split(',')[-1].strip()}")

                valid_streams.append(f"{prev_line}\n{line}\n")

                seen_urls.add(line)
            else:
                print(f"❌ Dead (Fake 200 or Offline): {line}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.writelines(valid_streams)

    print(f"Validation Complete. Total Channels: {len(seen_urls)}")


if __name__ == "__main__":
    main()
