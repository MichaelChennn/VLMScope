# Qwen3-VL-235B-bf16 Inference Results (Person B - behavior)
**Model checkpoint:** ./models/qwen3-vl-235b-a22b-instruct
**Video:** dataset/G3_Run3_timeTxt_mini_10.mp4

**Hardware Configuration:**
- Use FP8: False
- Tensor Parallel Size: 8
- GPU Memory Utilization: 0.95

**Video Processing Parameters:**
- max_pixels: 86400
- min_pixels: 14400
- fps: 0.5
- max_tokens: 10240

**Prompt:**
```
BACKGROUND

There are four participants engaged in a group decision-making task (NASA Moon Survival Task).
The input is a video recording with:
•	Visual cues of participants’ body movements and gestures.
•	Transcripts of their spoken dialogue.
•	A time code displayed at the bottom left corner of each frame.

All four participants are visible in the video, positioned from left to right: PersonA(leftmost, female, long curlyhair, black sleeveless skirt), PersonC（middleleft, female, long straight hair, black short-sleeve T-shirt and skirt with shoulder), PersonB(middleright, female, long straight hair, white long-sleeve blouse with a denim vest), PersonD(rightmost, black short-sleeve T-shirt, dark pants).

⸻

TASK
1.	Tracking
Continuously track PersonB across the entire video using the time code as the frame reference.
2.	Behavior Annotation
Identify and annotate PersonB's observable physical, social or communicative behaviors over time.
•	A behavior is a concise, high-level label describing visible bodily actions, gestures, or interactions with objects.
•	Do not infer mental states or intentions (e.g., "agreeing", "thinking", "understanding").
•	Behaviors should be expressed using short standardized labels (1–3 words).
•	Compound behaviors can be represented with underscores (e.g., speaking_gesturing, listening_nodding).
•	Behaviors are not limited to the examples below:
Communicative:
•	speaking, listening, nodding, shaking_head, pointing_left, pointing_right,
turning_head_left, turning_head_right, raising_hand, shrugging, smiling, laughing.
Attentive / Gaze-related:
•	looking_down, looking_up, looking_at_screen, looking_at_personB, looking_at_personD,
following_gaze, head_tilt.
Self-directed / Micro-movements:
•	adjusting_posture, touching_face, touching_chin, scratching_head, rubbing_hands,
fidgeting, crossing_arms, uncrossing_arms, playing_with_pen.
Task-oriented / Object interaction:
•	writing, typing, holding_paper, using_mouse, reaching_for_object, moving_chair,
tapping_table, opening_bottle, adjusting_glasses.
Other short labels:
•	breathing_deeply, yawning, clapping, stretching, adjusting_clothes.
•	You may output any other relevant physical action if observed, even if not listed.

2a.	Target Presence (Has Target?)

Determine whether the observed behavior is directed toward a specific target (e.g., a person, screen, or object). Output a boolean in the "interaction" field: use "true" if the behavior is directed at a target; use "false" if it is not target-directed or the target is indeterminate.

2b.	Target Identification

If the previous step outputs "true", specify the behavior's target in the "target" field. The target can be PersonA, PersonB, PersonC, group, monitor, or another object (provide a concise object name). If the previous step outputs "false", set "target" to "none".

3.	Short Description

For each detected behavior, also generate a short natural-language description of what PersonB is doing during this time.
•	Keep it 1–2 sentences maximum.
•	Describe the physical movement clearly and concretely.
•	Do not speculate about mental states or intentions.
•	This description should help clarify how the behavior label was determined.
Example descriptions:
•	"PersonB turns their head slightly to the left and nods twice while facing PersonB."
•	"PersonB is speaking continuously and moving their right hand to emphasize points."
•	"PersonB leans forward and looks down at the table."
4.	Provide "start_time" and "end_time" fields indicating the duration of the behavior.
5.	Confidence Score
Provide a confidence score (0.0–1.0) for each observation based on visual clarity and temporal precision.
6. CRITICAL: The video is exactly 10 minutes (10:00:00) long. All timestamps must be within this range. Do not generate any data after 10:00:00. If an emotion starts before 10:00:00 and is still ongoing when the video ends, set its end_time to "10:00:00".

⸻

OUTPUT FORMAT

For instantaneous actions:

{
"time": "00:07:21",
"behavior": "nodding",
"interaction": "false",
"target": "none",
"confidence": 0.87,
"description": "PersonB nods twice quickly."
}

For continuous actions:

{
"start_time": "00:08:45",
"end_time": "00:09:02",
"behavior": "speaking_gesturing",
"interaction": "true",
"target": "group",
"confidence": 0.84,
"description": "PersonB speaks continuously to the group and moves his right hand to emphasize key points."
}

```

**Output:**
```
{
  "start_time": "00:00:00",
  "end_time": "00:00:08",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.92,
  "description": "PersonB is looking down at the table surface, with her hands clasped in front of her."
}

{
  "start_time": "00:00:09",
  "end_time": "00:00:15",
  "behavior": "touching_chin",
  "interaction": "false",
  "target": "none",
  "confidence": 0.88,
  "description": "PersonB brings her right hand up to her chin, resting her fingers there while looking down."
}

{
  "start_time": "00:00:16",
  "end_time": "00:00:25",
  "behavior": "crossing_arms",
  "interaction": "false",
  "target": "none",
  "confidence": 0.95,
  "description": "PersonB crosses her arms over her chest and remains in that posture, looking down at the table."
}

{
  "start_time": "00:00:26",
  "end_time": "00:00:35",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.89,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking and gesturing toward the table."
}

{
  "start_time": "00:00:36",
  "end_time": "00:00:44",
  "behavior": "pointing_left",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonB extends her right index finger and points toward the left side of the table while speaking."
}

{
  "start_time": "00:00:45",
  "end_time": "00:00:52",
  "behavior": "looking_up",
  "interaction": "false",
  "target": "none",
  "confidence": 0.85,
  "description": "PersonB lifts her head and looks upward, away from the table, while keeping her arms crossed."
}

{
  "start_time": "00:00:53",
  "end_time": "00:01:00",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.87,
  "description": "PersonB turns her head to the left again, directing her gaze toward PersonA, who is speaking."
}

{
  "start_time": "00:01:01",
  "end_time": "00:01:08",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB lowers her gaze back to the table, maintaining her crossed-arm posture."
}

{
  "start_time": "00:01:09",
  "end_time": "00:01:15",
  "behavior": "looking_at_personC",
  "interaction": "true",
  "target": "PersonC",
  "confidence": 0.86,
  "description": "PersonB turns her head slightly to the right to look at PersonC, who is speaking."
}

{
  "start_time": "00:01:16",
  "end_time": "00:01:22",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.88,
  "description": "PersonB turns her head back to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:01:23",
  "end_time": "00:01:29",
  "behavior": "looking_at_personD",
  "interaction": "true",
  "target": "PersonD",
  "confidence": 0.85,
  "description": "PersonB turns her head to the right to look at PersonD, who is speaking."
}

{
  "start_time": "00:01:30",
  "end_time": "00:01:36",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonB looks down at the table, her arms still crossed, as she listens."
}

{
  "start_time": "00:01:37",
  "end_time": "00:01:45",
  "behavior": "speaking_gesturing",
  "interaction": "true",
  "target": "group",
  "confidence": 0.89,
  "description": "PersonB speaks to the group, uncrossing her arms and using her right hand to gesture while explaining her thought process."
}

{
  "start_time": "00:01:46",
  "end_time": "00:01:52",
  "behavior": "crossing_arms",
  "interaction": "false",
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB re-crosses her arms over her chest while continuing to speak."
}

{
  "start_time": "00:01:53",
  "end_time": "00:02:00",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB looks down at the table, arms still crossed, as she continues speaking."
}

{
  "start_time": "00:02:01",
  "end_time": "00:02:07",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.87,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:02:08",
  "end_time": "00:02:15",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.89,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:02:16",
  "end_time": "00:02:23",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:02:24",
  "end_time": "00:02:30",
  "behavior": "pointing_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonB uncrosses her arms and points downward at the table with her right index finger while speaking."
}

{
  "start_time": "00:02:31",
  "end_time": "00:02:37",
  "behavior": "looking_at_personD",
  "interaction": "true",
  "target": "PersonD",
  "confidence": 0.85,
  "description": "PersonB turns her head to the right to look at PersonD, who is speaking and gesturing."
}

{
  "start_time": "00:02:38",
  "end_time": "00:02:44",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.87,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:02:45",
  "end_time": "00:02:51",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB looks down at the table, arms crossed, while listening."
}

{
  "start_time": "00:02:52",
  "end_time": "00:02:58",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:02:59",
  "end_time": "00:03:05",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.89,
  "description": "PersonB looks down at the table, arms still crossed, as she listens to PersonA."
}

{
  "start_time": "00:03:06",
  "end_time": "00:03:12",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.87,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:03:13",
  "end_time": "00:03:19",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:03:20",
  "end_time": "00:03:26",
  "behavior": "looking_at_personD",
  "interaction": "true",
  "target": "PersonD",
  "confidence": 0.85,
  "description": "PersonB turns her head to the right to look at PersonD, who is speaking and gesturing."
}

{
  "start_time": "00:03:27",
  "end_time": "00:03:33",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:03:34",
  "end_time": "00:03:40",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.89,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:03:41",
  "end_time": "00:03:47",
  "behavior": "looking_at_personC",
  "interaction": "true",
  "target": "PersonC",
  "confidence": 0.87,
  "description": "PersonB turns her head slightly to the right to look at PersonC, who is speaking."
}

{
  "start_time": "00:03:48",
  "end_time": "00:03:54",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:03:55",
  "end_time": "00:04:01",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:04:02",
  "end_time": "00:04:08",
  "behavior": "looking_at_personD",
  "interaction": "true",
  "target": "PersonD",
  "confidence": 0.85,
  "description": "PersonB turns her head to the right to look at PersonD, who is speaking."
}

{
  "start_time": "00:04:09",
  "end_time": "00:04:15",
  "behavior": "looking_at_personC",
  "interaction": "true",
  "target": "PersonC",
  "confidence": 0.86,
  "description": "PersonB turns her head slightly to the right to look at PersonC, who is speaking."
}

{
  "start_time": "00:04:16",
  "end_time": "00:04:22",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.89,
  "description": "PersonB looks down at the table, arms crossed, while listening."
}

{
  "start_time": "00:04:23",
  "end_time": "00:04:29",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.87,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:04:30",
  "end_time": "00:04:36",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:04:37",
  "end_time": "00:04:43",
  "behavior": "looking_at_personD",
  "interaction": "true",
  "target": "PersonD",
  "confidence": 0.85,
  "description": "PersonB turns her head to the right to look at PersonD, who is speaking."
}

{
  "start_time": "00:04:44",
  "end_time": "00:04:50",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:04:51",
  "end_time": "00:04:57",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.89,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:04:58",
  "end_time": "00:05:04",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonB turns her head slightly to the right to look at PersonB, who is speaking."
}

{
  "start_time": "00:05:05",
  "end_time": "00:05:11",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:05:12",
  "end_time": "00:05:18",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:05:19",
  "end_time": "00:05:25",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.89,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:05:26",
  "end_time": "00:05:32",
  "behavior": "looking_at_personC",
  "interaction": "true",
  "target": "PersonC",
  "confidence": 0.87,
  "description": "PersonB turns her head slightly to the right to look at PersonC, who is speaking."
}

{
  "start_time": "00:05:33",
  "end_time": "00:05:39",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:05:40",
  "end_time": "00:05:46",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:05:47",
  "end_time": "00:05:53",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.89,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:05:54",
  "end_time": "00:06:00",
  "behavior": "looking_at_personC",
  "interaction": "true",
  "target": "PersonC",
  "confidence": 0.87,
  "description": "PersonB turns her head slightly to the right to look at PersonC, who is speaking."
}

{
  "start_time": "00:06:01",
  "end_time": "00:06:07",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:06:08",
  "end_time": "00:06:14",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:06:15",
  "end_time": "00:06:21",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.89,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:06:22",
  "end_time": "00:06:28",
  "behavior": "looking_at_personC",
  "interaction": "true",
  "target": "PersonC",
  "confidence": 0.87,
  "description": "PersonB turns her head slightly to the right to look at PersonC, who is speaking."
}

{
  "start_time": "00:06:29",
  "end_time": "00:06:35",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:06:36",
  "end_time": "00:06:42",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:06:43",
  "end_time": "00:06:49",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.89,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:06:50",
  "end_time": "00:06:56",
  "behavior": "looking_at_personC",
  "interaction": "true",
  "target": "PersonC",
  "confidence": 0.87,
  "description": "PersonB turns her head slightly to the right to look at PersonC, who is speaking."
}

{
  "start_time": "00:06:57",
  "end_time": "00:07:03",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:07:04",
  "end_time": "00:07:10",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:07:11",
  "end_time": "00:07:17",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.89,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:07:18",
  "end_time": "00:07:24",
  "behavior": "looking_at_personC",
  "interaction": "true",
  "target": "PersonC",
  "confidence": 0.87,
  "description": "PersonB turns her head slightly to the right to look at PersonC, who is speaking."
}

{
  "start_time": "00:07:25",
  "end_time": "00:07:31",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:07:32",
  "end_time": "00:07:38",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:07:39",
  "end_time": "00:07:45",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.89,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:07:46",
  "end_time": "00:07:52",
  "behavior": "looking_at_personC",
  "interaction": "true",
  "target": "PersonC",
  "confidence": 0.87,
  "description": "PersonB turns her head slightly to the right to look at PersonC, who is speaking."
}

{
  "start_time": "00:07:53",
  "end_time": "00:07:59",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:08:00",
  "end_time": "00:08:06",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:08:07",
  "end_time": "00:08:13",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.89,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:08:14",
  "end_time": "00:08:20",
  "behavior": "looking_at_personD",
  "interaction": "true",
  "target": "PersonD",
  "confidence": 0.85,
  "description": "PersonB turns her head to the right to look at PersonD, who is speaking."
}

{
  "start_time": "00:08:21",
  "end_time": "00:08:27",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:08:28",
  "end_time": "00:08:34",
  "behavior": "looking_at_personC",
  "interaction": "true",
  "target": "PersonC",
  "confidence": 0.87,
  "description": "PersonB turns her head slightly to the right to look at PersonC, who is speaking."
}

{
  "start_time": "00:08:35",
  "end_time": "00:08:41",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.89,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:08:42",
  "end_time": "00:08:48",
  "behavior": "looking_at_personD",
  "interaction": "true",
  "target": "PersonD",
  "confidence": 0.85,
  "description": "PersonB turns her head to the right to look at PersonD, who is speaking."
}

{
  "start_time": "00:08:49",
  "end_time": "00:08:55",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:08:56",
  "end_time": "00:09:02",
  "behavior": "looking_at_personC",
  "interaction": "true",
  "target": "PersonC",
  "confidence": 0.87,
  "description": "PersonB turns her head slightly to the right to look at PersonC, who is speaking."
}

{
  "start_time": "00:09:03",
  "end_time": "00:09:09",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.89,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:09:10",
  "end_time": "00:09:16",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonB turns her head to the left to look at PersonA, who is speaking."
}

{
  "start_time": "00:09:17",
  "end_time": "00:09:23",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:09:24",
  "end_time": "00:09:30",
  "behavior": "looking_at_personC",
  "interaction": "true",
  "target": "PersonC",
  "confidence": 0.87,
  "description": "PersonB turns her head slightly to the right to look at PersonC, who is speaking."
}

{
  "start_time": "00:09:31",
  "end_time": "00:09:37",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.89,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:09:38",
  "end_time": "00:09:44",
  "behavior": "looking_at_personD",
  "interaction": "true",
  "target": "PersonD",
  "confidence": 0.85,
  "description": "PersonB turns her head to the right to look at PersonD, who is speaking."
}

{
  "start_time": "00:09:45",
  "end_time": "00:09:51",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonB looks down at the table, arms crossed, while listening to PersonA."
}

{
  "start_time": "00:09:52",
  "end_time": "00:09:58",
  "behavior": "looking_at_personC",
  "interaction": "true",
  "target": "PersonC",
  "confidence": 0.87,
  "description": "PersonB turns her head slightly to the right to look at PersonC, who is speaking."
}

{
  "start_time": "00:09:59",
  "end_time": "00:10:00",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.89,
  "description": "PersonB looks down at the table, arms crossed, as the video ends."
}
```
