import requests

INPUT_FILE = "streams/community.m3u"
OUTPUT_FILE = "index.m3u"


def is_stream_working(url):
    try:
        with requests.get(url, stream=True, timeout=5) as response:

            if response.status_code != 200:
                return False

            first_chunk = next(response.iter_content(chunk_size=7)).decode(
                "utf-8", errors="ignore"
            )

            if first_chunk.startswith("#EXTM3U"):
                return True
            else:
                return False

    except Exception as e:
        return False


def main():
    print("Starting Deep Stream Validation...")

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    valid_streams = ["#EXTM3U\n"]

    for i in range(1, len(lines)):
        line = lines[i].strip()

        if line.startswith("http"):
            prev_line = lines[i - 1].strip()

            if not prev_line.startswith("#EXTINF"):
                continue

            if is_stream_working(line):
                print(f"✅ Working: {prev_line.split(',')[-1].strip()}")
                valid_streams.append(f"{prev_line}\n{line}\n")
            else:
                print(f"❌ Dead (Fake 200 or Offline): {line}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.writelines(valid_streams)

    print("Validation Complete. index.m3u updated.")


if __name__ == "__main__":
    main()
