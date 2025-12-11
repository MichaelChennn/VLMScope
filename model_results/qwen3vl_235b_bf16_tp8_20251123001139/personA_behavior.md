# Qwen3-VL-235B-bf16 Inference Results (Person A - behavior)
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

All four participants are visible in the video, positioned from left to right: PersonA(leftmost, female, long curlyhair, black sleeveless skirt), PersonC(middleleft, female, long straight hair, black short-sleeve T-shirt and skirt with shoulder), PersonB(middleright, female, long straight hair, white long-sleeve blouse with a denim vest), PersonD(rightmost, black short-sleeve T-shirt, dark pants).

⸻

TASK
1.	Tracking
Continuously track PersonA across the entire video using the time code as the frame reference.
2.	Behavior Annotation
Identify and annotate PersonA's observable physical, social or communicative behaviors over time.
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

For each detected behavior, also generate a short natural-language description of what PersonA is doing during this time.
•	Keep it 1–2 sentences maximum.
•	Describe the physical movement clearly and concretely.
•	Do not speculate about mental states or intentions.
•	This description should help clarify how the behavior label was determined.
Example descriptions:
•	"PersonA turns their head slightly to the left and nods twice while facing PersonB."
•	"PersonA is speaking continuously and moving their right hand to emphasize points."
•	"PersonA leans forward and looks down at the table."
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
"description": "PersonA nods twice quickly."
}

For continuous actions:

{
"start_time": "00:08:45",
"end_time": "00:09:02",
"behavior": "speaking_gesturing",
"interaction": "true",
"target": "group",
"confidence": 0.84,
"description": "PersonA speaks continuously to the group and moves his right hand to emphasize key points."
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
  "description": "PersonA looks down at the table surface, her head tilted forward, with her right hand near her chest."
}
{
  "start_time": "00:00:08",
  "end_time": "00:00:15",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.89,
  "description": "PersonA speaks while looking down at the table, her mouth moving and her right hand still near her chest."
}
{
  "start_time": "00:00:15",
  "end_time": "00:00:22",
  "behavior": "pointing_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonA extends her right index finger and points downward at the table surface while speaking."
}
{
  "start_time": "00:00:22",
  "end_time": "00:00:28",
  "behavior": "looking_up",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonA lifts her head and looks toward PersonB, who is standing to her right, while continuing to speak."
}
{
  "start_time": "00:00:28",
  "end_time": "00:00:35",
  "behavior": "listening",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.86,
  "description": "PersonA turns her head slightly to the right and listens to PersonB, her hands clasped in front of her."
}
{
  "start_time": "00:00:35",
  "end_time": "00:00:42",
  "behavior": "pointing_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.93,
  "description": "PersonA points downward at the table with her right index finger while speaking to the group."
}
{
  "start_time": "00:00:42",
  "end_time": "00:00:49",
  "behavior": "looking_up",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonA looks up and to her right, directing her gaze toward PersonB while listening."
}
{
  "start_time": "00:00:49",
  "end_time": "00:00:56",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.85,
  "description": "PersonA speaks to the group, her mouth moving and her gaze shifting slightly between the table and the others."
}
{
  "start_time": "00:00:56",
  "end_time": "00:01:03",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonA looks down at the table, her head tilted forward, while continuing to speak."
}
{
  "start_time": "00:01:03",
  "end_time": "00:01:10",
  "behavior": "touching_hair",
  "interaction": "false",
  "target": "none",
  "confidence": 0.84,
  "description": "PersonA raises her right hand to her hair and briefly touches or adjusts it while speaking."
}
{
  "start_time": "00:01:10",
  "end_time": "00:01:17",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.86,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:01:17",
  "end_time": "00:01:24",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.89,
  "description": "PersonA looks directly at PersonB, who is speaking, with a neutral expression."
}
{
  "start_time": "00:01:24",
  "end_time": "00:01:31",
  "behavior": "listening",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonA listens to PersonB, her head slightly tilted and her gaze fixed on PersonB."
}
{
  "start_time": "00:01:31",
  "end_time": "00:01:38",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonA looks down at the table, her head bowed slightly, while listening to PersonB."
}
{
  "start_time": "00:01:38",
  "end_time": "00:01:45",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.87,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:01:45",
  "end_time": "00:01:52",
  "behavior": "listening",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.86,
  "description": "PersonA listens to PersonB, her head slightly tilted and her gaze fixed on PersonB."
}
{
  "start_time": "00:01:52",
  "end_time": "00:01:59",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonA looks down at the table, her head bowed slightly, while listening to PersonB."
}
{
  "start_time": "00:01:59",
  "end_time": "00:02:06",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.85,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:02:06",
  "end_time": "00:02:13",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonA looks directly at PersonB, who is speaking, with a neutral expression."
}
{
  "start_time": "00:02:13",
  "end_time": "00:02:20",
  "behavior": "listening",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonA listens to PersonB, her head slightly tilted and her gaze fixed on PersonB."
}
{
  "start_time": "00:02:20",
  "end_time": "00:02:27",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonA looks down at the table, her head bowed slightly, while listening to PersonB."
}
{
  "start_time": "00:02:27",
  "end_time": "00:02:34",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.86,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:02:34",
  "end_time": "00:02:41",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.89,
  "description": "PersonA looks directly at PersonB, who is speaking, with a neutral expression."
}
{
  "start_time": "00:02:41",
  "end_time": "00:02:48",
  "behavior": "listening",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonA listens to PersonB, her head slightly tilted and her gaze fixed on PersonB."
}
{
  "start_time": "00:02:48",
  "end_time": "00:02:55",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonA looks down at the table, her head bowed slightly, while listening to PersonB."
}
{
  "start_time": "00:02:55",
  "end_time": "00:03:02",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.87,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:03:02",
  "end_time": "00:03:09",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonA looks down at the table, her head tilted forward, while speaking."
}
{
  "start_time": "00:03:09",
  "end_time": "00:03:16",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.86,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:03:16",
  "end_time": "00:03:23",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonA looks directly at PersonB, who is speaking, with a neutral expression."
}
{
  "start_time": "00:03:23",
  "end_time": "00:03:30",
  "behavior": "listening",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonA listens to PersonB, her head slightly tilted and her gaze fixed on PersonB."
}
{
  "start_time": "00:03:30",
  "end_time": "00:03:37",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonA looks down at the table, her head bowed slightly, while listening to PersonB."
}
{
  "start_time": "00:03:37",
  "end_time": "00:03:44",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.85,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:03:44",
  "end_time": "00:03:51",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonA looks down at the table, her head tilted forward, while speaking."
}
{
  "start_time": "00:03:51",
  "end_time": "00:03:58",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.86,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:03:58",
  "end_time": "00:04:05",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonA looks directly at PersonB, who is speaking, with a neutral expression."
}
{
  "start_time": "00:04:05",
  "end_time": "00:04:12",
  "behavior": "listening",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonA listens to PersonB, her head slightly tilted and her gaze fixed on PersonB."
}
{
  "start_time": "00:04:12",
  "end_time": "00:04:19",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonA looks down at the table, her head bowed slightly, while listening to PersonB."
}
{
  "start_time": "00:04:19",
  "end_time": "00:04:26",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.85,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:04:26",
  "end_time": "00:04:33",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonA looks down at the table, her head tilted forward, while speaking."
}
{
  "start_time": "00:04:33",
  "end_time": "00:04:40",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.86,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:04:40",
  "end_time": "00:04:47",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonA looks directly at PersonB, who is speaking, with a neutral expression."
}
{
  "start_time": "00:04:47",
  "end_time": "00:04:54",
  "behavior": "listening",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonA listens to PersonB, her head slightly tilted and her gaze fixed on PersonB."
}
{
  "start_time": "00:04:54",
  "end_time": "00:05:01",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonA looks down at the table, her head bowed slightly, while listening to PersonB."
}
{
  "start_time": "00:05:01",
  "end_time": "00:05:08",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.85,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:05:08",
  "end_time": "00:05:15",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonA looks down at the table, her head tilted forward, while speaking."
}
{
  "start_time": "00:05:15",
  "end_time": "00:05:22",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.86,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:05:22",
  "end_time": "00:05:29",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonA looks directly at PersonB, who is speaking, with a neutral expression."
}
{
  "start_time": "00:05:29",
  "end_time": "00:05:36",
  "behavior": "listening",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonA listens to PersonB, her head slightly tilted and her gaze fixed on PersonB."
}
{
  "start_time": "00:05:36",
  "end_time": "00:05:43",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonA looks down at the table, her head bowed slightly, while listening to PersonB."
}
{
  "start_time": "00:05:43",
  "end_time": "00:05:50",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.85,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:05:50",
  "end_time": "00:05:57",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonA looks down at the table, her head tilted forward, while speaking."
}
{
  "start_time": "00:05:57",
  "end_time": "00:06:04",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.86,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:06:04",
  "end_time": "00:06:11",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonA looks directly at PersonB, who is speaking, with a neutral expression."
}
{
  "start_time": "00:06:11",
  "end_time": "00:06:18",
  "behavior": "listening",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonA listens to PersonB, her head slightly tilted and her gaze fixed on PersonB."
}
{
  "start_time": "00:06:18",
  "end_time": "00:06:25",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonA looks down at the table, her head bowed slightly, while listening to PersonB."
}
{
  "start_time": "00:06:25",
  "end_time": "00:06:32",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.85,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:06:32",
  "end_time": "00:06:39",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonA looks down at the table, her head tilted forward, while speaking."
}
{
  "start_time": "00:06:39",
  "end_time": "00:06:46",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.86,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:06:46",
  "end_time": "00:06:53",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonA looks directly at PersonB, who is speaking, with a neutral expression."
}
{
  "start_time": "00:06:53",
  "end_time": "00:07:00",
  "behavior": "listening",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonA listens to PersonB, her head slightly tilted and her gaze fixed on PersonB."
}
{
  "start_time": "00:07:00",
  "end_time": "00:07:07",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonA looks down at the table, her head bowed slightly, while listening to PersonB."
}
{
  "start_time": "00:07:07",
  "end_time": "00:07:14",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.85,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:07:14",
  "end_time": "00:07:21",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonA looks down at the table, her head tilted forward, while speaking."
}
{
  "start_time": "00:07:21",
  "end_time": "00:07:28",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.86,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:07:28",
  "end_time": "00:07:35",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonA looks directly at PersonB, who is speaking, with a neutral expression."
}
{
  "start_time": "00:07:35",
  "end_time": "00:07:42",
  "behavior": "listening",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonA listens to PersonB, her head slightly tilted and her gaze fixed on PersonB."
}
{
  "start_time": "00:07:42",
  "end_time": "00:07:49",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonA looks down at the table, her head bowed slightly, while listening to PersonB."
}
{
  "start_time": "00:07:49",
  "end_time": "00:07:56",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.85,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:07:56",
  "end_time": "00:08:03",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonA looks down at the table, her head tilted forward, while speaking."
}
{
  "start_time": "00:08:03",
  "end_time": "00:08:10",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.86,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:08:10",
  "end_time": "00:08:17",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonA looks directly at PersonB, who is speaking, with a neutral expression."
}
{
  "start_time": "00:08:17",
  "end_time": "00:08:24",
  "behavior": "listening",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonA listens to PersonB, her head slightly tilted and her gaze fixed on PersonB."
}
{
  "start_time": "00:08:24",
  "end_time": "00:08:31",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonA looks down at the table, her head bowed slightly, while listening to PersonB."
}
{
  "start_time": "00:08:31",
  "end_time": "00:08:38",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.85,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:08:38",
  "end_time": "00:08:45",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonA looks down at the table, her head tilted forward, while speaking."
}
{
  "start_time": "00:08:45",
  "end_time": "00:08:52",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.86,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:08:52",
  "end_time": "00:08:59",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonA looks directly at PersonB, who is speaking, with a neutral expression."
}
{
  "start_time": "00:08:59",
  "end_time": "00:09:06",
  "behavior": "listening",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonA listens to PersonB, her head slightly tilted and her gaze fixed on PersonB."
}
{
  "start_time": "00:09:06",
  "end_time": "00:09:13",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonA looks down at the table, her head bowed slightly, while listening to PersonB."
}
{
  "start_time": "00:09:13",
  "end_time": "00:09:20",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.85,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:09:20",
  "end_time": "00:09:27",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.91,
  "description": "PersonA looks down at the table, her head tilted forward, while speaking."
}
{
  "start_time": "00:09:27",
  "end_time": "00:09:34",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.86,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
{
  "start_time": "00:09:34",
  "end_time": "00:09:41",
  "behavior": "looking_at_personB",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.88,
  "description": "PersonA looks directly at PersonB, who is speaking, with a neutral expression."
}
{
  "start_time": "00:09:41",
  "end_time": "00:09:48",
  "behavior": "listening",
  "interaction": "true",
  "target": "PersonB",
  "confidence": 0.87,
  "description": "PersonA listens to PersonB, her head slightly tilted and her gaze fixed on PersonB."
}
{
  "start_time": "00:09:48",
  "end_time": "00:09:55",
  "behavior": "looking_down",
  "interaction": "true",
  "target": "table",
  "confidence": 0.90,
  "description": "PersonA looks down at the table, her head bowed slightly, while listening to PersonB."
}
{
  "start_time": "00:09:55",
  "end_time": "00:10:00",
  "behavior": "speaking",
  "interaction": "true",
  "target": "group",
  "confidence": 0.85,
  "description": "PersonA speaks to the group, her mouth moving and her gaze directed toward PersonB."
}
```
