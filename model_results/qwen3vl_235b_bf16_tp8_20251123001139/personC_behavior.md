# Qwen3-VL-235B-bf16 Inference Results (Person C - behavior)
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
Continuously track PersonC across the entire video using the time code as the frame reference.
2.	Behavior Annotation
Identify and annotate PersonC's observable physical, social or communicative behaviors over time.
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

For each detected behavior, also generate a short natural-language description of what PersonC is doing during this time.
•	Keep it 1–2 sentences maximum.
•	Describe the physical movement clearly and concretely.
•	Do not speculate about mental states or intentions.
•	This description should help clarify how the behavior label was determined.
Example descriptions:
•	"PersonC turns their head slightly to the left and nods twice while facing PersonB."
•	"PersonC is speaking continuously and moving their right hand to emphasize points."
•	"PersonC leans forward and looks down at the table."
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
"description": "PersonC nods twice quickly."
}

For continuous actions:

{
"start_time": "00:08:45",
"end_time": "00:09:02",
"behavior": "speaking_gesturing",
"interaction": "true",
"target": "group",
"confidence": 0.84,
"description": "PersonC speaks continuously to the group and moves his right hand to emphasize key points."
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
  "description": "PersonC looks down at the table surface, maintaining a fixed gaze without moving their head significantly."
}

{
  "start_time": "00:00:09",
  "end_time": "00:00:15",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.89,
  "description": "PersonC turns their head slightly to the left and looks toward PersonA while PersonA is speaking."
}

{
  "start_time": "00:00:16",
  "end_time": "00:00:25",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonC lowers their gaze back to the table, appearing to observe something on its surface."
}

{
  "start_time": "00:00:26",
  "end_time": "00:00:32",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing."
}

{
  "start_time": "00:00:33",
  "end_time": "00:00:40",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.93,
  "description": "PersonC looks down at the table again, possibly following the movement of PersonA’s hand."
}

{
  "start_time": "00:00:41",
  "end_time": "00:00:47",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonC looks toward PersonB, who is speaking and holding a small object."
}

{
  "start_time": "00:00:48",
  "end_time": "00:00:55",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:00:56",
  "end_time": "00:01:02",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonC looks down at the table, maintaining a steady gaze without significant head movement."
}

{
  "start_time": "00:01:03",
  "end_time": "00:01:09",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.85,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:01:10",
  "end_time": "00:01:16",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.87,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:01:17",
  "end_time": "00:01:23",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.89,
  "description": "PersonC looks toward PersonB, who is speaking and holding a small object."
}

{
  "start_time": "00:01:24",
  "end_time": "00:01:30",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonC looks down at the table, possibly following the movement of PersonA’s hand."
}

{
  "start_time": "00:01:31",
  "end_time": "00:01:37",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:01:38",
  "end_time": "00:01:44",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.92,
  "description": "PersonC looks down at the table, maintaining a steady gaze without significant head movement."
}

{
  "start_time": "00:01:45",
  "end_time": "00:01:51",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.86,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:01:52",
  "end_time": "00:01:58",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonC looks down at the table, possibly following the movement of PersonA’s hand."
}

{
  "start_time": "00:01:59",
  "end_time": "00:02:05",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:02:06",
  "end_time": "00:02:12",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.85,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:02:13",
  "end_time": "00:02:19",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:02:20",
  "end_time": "00:02:26",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonC looks down at the table, maintaining a steady gaze without significant head movement."
}

{
  "start_time": "00:02:27",
  "end_time": "00:02:33",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.86,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:02:34",
  "end_time": "00:02:40",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.87,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:02:41",
  "end_time": "00:02:47",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.89,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:02:48",
  "end_time": "00:02:54",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonC looks down at the table, possibly following the movement of PersonA’s hand."
}

{
  "start_time": "00:02:55",
  "end_time": "00:03:01",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:03:02",
  "end_time": "00:03:08",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:03:09",
  "end_time": "00:03:15",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:03:16",
  "end_time": "00:03:22",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonC looks down at the table, maintaining a steady gaze without significant head movement."
}

{
  "start_time": "00:03:23",
  "end_time": "00:03:29",
  "behavior": "looking_at_personD",
  "interaction": "true",
  "target": "PersonD",
  "confidence": 0.85,
  "description": "PersonC turns their head to the right and looks at PersonD, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:03:30",
  "end_time": "00:03:36",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:03:37",
  "end_time": "00:03:43",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:03:44",
  "end_time": "00:03:50",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonC looks down at the table, possibly following the movement of PersonA’s hand."
}

{
  "start_time": "00:03:51",
  "end_time": "00:03:57",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:03:58",
  "end_time": "00:04:04",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:04:05",
  "end_time": "00:04:11",
  "behavior": "looking_at_personD",
  "interaction": "true",
  "target": "PersonD",
  "confidence": 0.85,
  "description": "PersonC turns their head to the right and looks at PersonD, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:04:12",
  "end_time": "00:04:18",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.87,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:04:19",
  "end_time": "00:04:25",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonC looks down at the table, maintaining a steady gaze without significant head movement."
}

{
  "start_time": "00:04:26",
  "end_time": "00:04:32",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:04:33",
  "end_time": "00:04:39",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:04:40",
  "end_time": "00:04:46",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonC looks down at the table, possibly following the movement of PersonA’s hand."
}

{
  "start_time": "00:04:47",
  "end_time": "00:04:53",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:04:54",
  "end_time": "00:05:00",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:05:01",
  "end_time": "00:05:07",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonC looks down at the table, maintaining a steady gaze without significant head movement."
}

{
  "start_time": "00:05:08",
  "end_time": "00:05:14",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.85,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:05:15",
  "end_time": "00:05:21",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:05:22",
  "end_time": "00:05:28",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonC looks down at the table, possibly following the movement of PersonA’s hand."
}

{
  "start_time": "00:05:29",
  "end_time": "00:05:35",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:05:36",
  "end_time": "00:05:42",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:05:43",
  "end_time": "00:05:49",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonC looks down at the table, maintaining a steady gaze without significant head movement."
}

{
  "start_time": "00:05:50",
  "end_time": "00:05:56",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:05:57",
  "end_time": "00:06:03",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.85,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:06:04",
  "end_time": "00:06:10",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonC looks down at the table, possibly following the movement of PersonA’s hand."
}

{
  "start_time": "00:06:11",
  "end_time": "00:06:17",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:06:18",
  "end_time": "00:06:24",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:06:25",
  "end_time": "00:06:31",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonC looks down at the table, maintaining a steady gaze without significant head movement."
}

{
  "start_time": "00:06:32",
  "end_time": "00:06:38",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.87,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:06:39",
  "end_time": "00:06:45",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.86,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:06:46",
  "end_time": "00:06:52",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonC looks down at the table, possibly following the movement of PersonA’s hand."
}

{
  "start_time": "00:06:53",
  "end_time": "00:06:59",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.85,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:07:00",
  "end_time": "00:07:06",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:07:07",
  "end_time": "00:07:13",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonC looks down at the table, maintaining a steady gaze without significant head movement."
}

{
  "start_time": "00:07:14",
  "end_time": "00:07:20",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:07:21",
  "end_time": "00:07:27",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:07:28",
  "end_time": "00:07:34",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonC looks down at the table, possibly following the movement of PersonA’s hand."
}

{
  "start_time": "00:07:35",
  "end_time": "00:07:41",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.85,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:07:42",
  "end_time": "00:07:48",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:07:49",
  "end_time": "00:07:55",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonC looks down at the table, maintaining a steady gaze without significant head movement."
}

{
  "start_time": "00:07:56",
  "end_time": "00:08:02",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:08:03",
  "end_time": "00:08:09",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:08:10",
  "end_time": "00:08:16",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonC looks down at the table, possibly following the movement of PersonA’s hand."
}

{
  "start_time": "00:08:17",
  "end_time": "00:08:23",
  "behavior": "looking_at_personD",
  "interaction": "true",
  "target": "PersonD",
  "confidence": 0.85,
  "description": "PersonC turns their head to the right and looks at PersonD, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:08:24",
  "end_time": "00:08:30",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:08:31",
  "end_time": "00:08:37",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonC looks down at the table, maintaining a steady gaze without significant head movement."
}

{
  "start_time": "00:08:38",
  "end_time": "00:08:44",
  "behavior": "looking_at_personD",
  "interaction": "true",
  "target": "PersonD",
  "confidence": 0.86,
  "description": "PersonC turns their head to the right and looks at PersonD, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:08:45",
  "end_time": "00:08:51",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:08:52",
  "end_time": "00:08:58",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonC looks down at the table, possibly following the movement of PersonA’s hand."
}

{
  "start_time": "00:08:59",
  "end_time": "00:09:05",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.85,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:09:06",
  "end_time": "00:09:12",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:09:13",
  "end_time": "00:09:19",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonC looks down at the table, maintaining a steady gaze without significant head movement."
}

{
  "start_time": "00:09:20",
  "end_time": "00:09:26",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:09:27",
  "end_time": "00:09:33",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:09:34",
  "end_time": "00:09:40",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonC looks down at the table, possibly following the movement of PersonA’s hand."
}

{
  "start_time": "00:09:41",
  "end_time": "00:09:47",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonC turns their head to the right and looks at PersonB, who is speaking and gesturing with their hands."
}

{
  "start_time": "00:09:48",
  "end_time": "00:09:54",
  "behavior": "looking_at_personA",
  "interaction": "true",
  "target": "PersonA",
  "confidence": 0.86,
  "description": "PersonC turns their head to the left to look at PersonA, who is speaking and gesturing."
}

{
  "start_time": "00:09:55",
  "end_time": "00:10:00",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonC looks down at the table, maintaining a steady gaze without significant head movement."
}
```
