import os
import re
import json
from datetime import datetime
from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound
)

# YOUR EXPERTS + VIDEOS
VIDEOS = {
    "Nathan Gotch": "https://youtube.com/watch?v=6o0mabKRmIo",
    "Marvomatic_AI_Automations": "https://youtu.be/FIYwJPPdtug",
    "Tim_the_SEO_Guru": "https://youtu.be/S3XcqumU2wQ?si=RQXvFERU_AgLqy3p",
    "Ahrefs_Sam_Oh": "https://youtu.be/tiW6xRYSXmM",
    "Authority_Hacker": "https://youtu.be/JMbRFcQobHU"
}

# CONFIG
OUTPUT_FOLDER = "research/youtube-transcripts"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# HELPERS
def extract_video_id(url):
    patterns = [
        r"v=([A-Za-z0-9_-]{11})",
        r"youtu\.be/([A-Za-z0-9_-]{11})"
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    raise ValueError(f"Could not extract video id from {url}")


def save_markdown(expert, video_id, transcript_text):
    filename = f"{expert}_{video_id}.md"
    filepath = os.path.join(OUTPUT_FOLDER, filename)

    content = f"""# Transcript

**Expert:** {expert}

**Video ID:** {video_id}

**Collected:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

{transcript_text}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath


def fetch_transcript(video_id):
    api = YouTubeTranscriptApi()
    
    # Fetch the transcript wrapper object
    transcript_obj = api.fetch(video_id)
    
    # FIX: Explicitly serialize custom class objects into a raw dictionary list
    transcript_list = transcript_obj.to_raw_data()
    
    lines = []
    for snippet in transcript_list:
        # Standard dictionary lookups are now guaranteed safe
        timestamp = round(snippet['start'], 2)
        lines.append(f"[{timestamp}] {snippet['text']}")
        
    return "\n".join(lines)


def main():
    report = []

    for expert, url in VIDEOS.items():
        print(f"\nProcessing: {expert}")
        try:
            video_id = extract_video_id(url)
            transcript_text = fetch_transcript(video_id)

            filepath = save_markdown(
                expert,
                video_id,
                transcript_text
            )

            report.append({
                "expert": expert,
                "video_id": video_id,
                "status": "success",
                "file": filepath
            })
            print("✓ Transcript saved")

        except TranscriptsDisabled:
            report.append({
                "expert": expert,
                "status": "transcripts_disabled"
            })
            print("✗ Transcript disabled")

        except NoTranscriptFound:
            report.append({
                "expert": expert,
                "status": "no_transcript_found"
            })
            print("✗ No transcript found")

        except Exception as e:
            report.append({
                "expert": expert,
                "status": "error",
                "message": str(e)
            })
            print(f"✗ Error: {e}")

    with open(
        os.path.join(OUTPUT_FOLDER, "report.json"),
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    print("\nDone.")
    print("Report saved.")


if __name__ == "__main__":
    main()
