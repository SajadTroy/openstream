# Contributing to OpenStream

First off, thank you for considering contributing to OpenStream! This project relies on community submissions to keep the playlist fresh, reliable, and diverse.

We welcome all types of contributions, including adding new channels, fixing broken links, and improving the validation scripts.

## Quick Guide: Adding a Channel

The most common way to contribute is by adding new public streaming links.

1.  **Fork** this repository.
2.  **Edit** the file `streams/community.m3u`.
3.  **Add** your channel link at the bottom of the file using the format below.
4.  **Submit** a Pull Request (PR).

### Channel Format
All entries must follow the standard M3U format. Please include a `group-title` (Category) and a `tvg-logo` (Image URL) whenever possible.

```text
#EXTINF:-1 group-title="Category" tvg-logo="[https://example.com/logo.png](https://example.com/logo.png)", Channel Name
https://link-to-stream.m3u8

```

**Requirements:**

* **Public Access:** Links must be publicly available.
* **Direct Stream:** The URL should point to a stream (e.g., `.m3u8`), not a web page.
* **Status:** Ensure the link is active before submitting.

## Validation Process

We use an automated system to ensure quality:

* **Daily Scan:** A GitHub Action runs daily to validate all links.
* **Duplicate Check:** Our script automatically checks for and skips duplicate URLs.
* **Content Check:** The validator ensures the link returns a `200 OK` status and contains valid stream data (starts with `#EXTM3U`).

If your PR fails the automated check, please review your link to ensure it is accessible and working.

## Legal & Content Guidelines

By contributing to this repository, you agree to the following terms outlined in our Disclaimer:

1. **Liability:** You warrant that you have the legal right to share the link. The risk of copyright infringement lies solely with the contributor.
2. **Ownership:** Do not submit content you do not own or have the right to share. This repository is a search index, not a host.
3. **DMCA:** We strictly comply with DMCA takedowns. If you submit copyrighted or illegal content, it will be removed.

## Reporting Issues

* **Broken Links:** If you find a dead link in the main playlist, you can open an Issue or submit a PR to remove it. (Note: Our daily bot automatically removes most dead links).
* **Copyright:** For DMCA/Copyright issues, please open a GitHub Issue immediately, and we will remove the infringing link.

Thank you for helping keep OpenStream green.