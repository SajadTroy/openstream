# OpenStream 📺

**The Open Source, Community-Curated IPTV Aggregator.**

OpenStream is a collaborative project to build a reliable, clean, and tested list of public streaming channels.
We rely on the community to add links, and we use **GitHub Actions** to automatically test them daily, ensuring the final playlist is always "Green" (100% working).

## 🚀 How to Use

### For Viewers (Watch TV)
Copy the link below and paste it into your favorite IPTV Player (TiviMate, VLC, IPTV Smarters, OttPlayer, etc.):


```
https://raw.githubusercontent.com/SajadTroy/OpenStream/main/index.m3u

```

### For Contributors (Add Channels)
We welcome contributions! Please follow these rules to keep the list clean:

1.  **Go to** the `streams/` folder and edit `community.m3u`.
2.  **Add your channel** following the M3U format (see below).
3.  **Submit a Pull Request (PR)**.
4.  Once merged, our bot will test the link. If it works, it will appear in the main list within 24 hours.

#### Submission Format
Please include the `group-title` (Category) and a clean logo URL if possible.

```text
#EXTINF:-1 group-title="Category" tvg-logo="[https://example.com/logo.png](https://example.com/logo.png)", Channel Name
https://link-to-stream.m3u8

```

## ⚠️ Legal Disclaimer

* **OpenStream does not host any content.** We are a directory of links found publicly on the internet.
* **No Piracy.** We strictly ban any pay-TV, premium sports, or copyrighted content. Do not submit links to HBO, Sky, BeIN, etc.
* **DMCA:** If you are a content owner and want a link removed, please open an Issue, and we will remove it immediately.

## 🤖 How it Works

* **Daily Scan:** Every day at 08:00 UTC, a GitHub Action runs a Python script.
* **Validation:** The script checks every link in the database.
* **Filtering:** Dead links (404/Timeout) are removed from the final output.
* **Result:** The `index.m3u` file is updated with only working streams.

## 📄 License

This project is licensed under the [MIT License](https://www.google.com/search?q=LICENSE).