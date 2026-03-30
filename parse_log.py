import csv
import re

input_file = "sensorlog.txt"
output_file = "heat_data.csv"

with open(input_file, "r") as fin, open(output_file, "w", newline="") as fout:
    writer = csv.writer(fout)
    writer.writerow(["time_sec", "node_id", "temperature", "alert"])

    for line in fin:
        # Match full pattern
        match = re.search(r"(\d+):(\d+\.\d+)\s+ID:(\d+)\s+DATA,(-?\d+),(\d+)", line)

        if match:
            minutes = int(match.group(1))
            seconds = float(match.group(2))
            time_sec = minutes * 60 + seconds   # convert to seconds

            node_id = int(match.group(3))
            temp = int(match.group(4))
            alert = int(match.group(5))

            writer.writerow([time_sec, node_id, temp, alert])

print("✅ Done! heat_data.csv ready")