import requests
import os
import concurrent.futures

STREAMS_DIR = "streams"
OUTPUT_FILE = "index.m3u"
MAX_WORKERS = 500


def check_stream(url):
    """
    Checks if a stream URL is working and returns True/False.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        with requests.get(url, headers=headers, stream=True, timeout=10) as response:
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
    print("Starting Deep Stream Validation (Concurrent)...")

    if not os.path.exists(STREAMS_DIR):
        print(f"Error: Directory '{STREAMS_DIR}' not found.")
        return

    m3u_files = sorted([f for f in os.listdir(STREAMS_DIR) if f.endswith(".m3u")])

    if not m3u_files:
        print("No .m3u files found in streams directory.")
        return

    all_candidates = []
    seen_urls = set()

    print("Gathering streams from files...")
    for file_name in m3u_files:
        file_path = os.path.join(STREAMS_DIR, file_name)

        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for i in range(1, len(lines)):
            line = lines[i].strip()

            if line.startswith("http"):
                prev_line = lines[i - 1].strip()

                if not prev_line.startswith("#EXTINF"):
                    continue

                if line in seen_urls:
                    print(f"⏩ Skipping Duplicate: {prev_line.split(',')[-1].strip()}")
                    continue

                seen_urls.add(line)
                all_candidates.append((len(all_candidates), prev_line, line))

    print(f"Total unique streams to check: {len(all_candidates)}")
    print(f"Checking with {MAX_WORKERS} concurrent workers...")

    valid_results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_candidate = {
            executor.submit(check_stream, item[2]): item for item in all_candidates
        }

        for future in concurrent.futures.as_completed(future_to_candidate):
            idx, info, url = future_to_candidate[future]
            channel_name = info.split(",")[-1].strip()

            try:
                is_working = future.result()
                if is_working:
                    print(f"✅ Working: {channel_name}")
                    valid_results.append((idx, f"{info}\n{url}\n"))
                else:
                    print(f"❌ Dead (Fake 200 or Offline): {url}")
            except Exception as exc:
                print(f"❌ Error checking {channel_name}: {exc}")

    valid_results.sort(key=lambda x: x[0])

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for _, content in valid_results:
            f.write(content)

    print(f"Validation Complete. Total Working Channels: {len(valid_results)}")


if __name__ == "__main__":
    main()
