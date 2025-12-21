import requests

INPUT_FILE = "streams/community.m3u"
OUTPUT_FILE = "index.m3u"


def is_stream_working(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except:
        return False


def main():
    print("Starting Stream Validation...")

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    valid_streams = ["#EXTM3U\n"]

    for i in range(1, len(lines)):
        line = lines[i].strip()

        if line.startswith("http"):
            prev_line = lines[i - 1].strip()

            if is_stream_working(line):
                print(f"✅ Working: {line}")
                valid_streams.append(f"{prev_line}\n{line}\n")
            else:
                print(f"❌ Dead: {line}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.writelines(valid_streams)

    print("Validation Complete. index.m3u updated.")


if __name__ == "__main__":
    main()
