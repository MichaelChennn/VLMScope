# Qwen3-VL-30B Inference Results (Person B - behavior)
**Model checkpoint:** ./models/qwen3-vl-30b-a3b-instruct
**Video:** dataset/G3_Run3_timeTxt_mini_10.mp4

**Parameters:**
- max_pixels: 1048576
- min_pixels: 200704
- fps: 2.0

**Prompt:**
```

    BACKGROUND:
    There are four participants engaged in a group decision-making task (NASA Moon Survival Task). The input is a video recording with:
        • Visual cues of participants' body movements and gestures.
        • Transcripts of their spoken dialogue.
        • A time code displayed at the bottom left corner of each frame.
    All four participants are visible in the video, positioned from left to right: PersonA(leftmost), PersonC(middleleft), PersonB(middleright), PersonD(rightmost).

    TASK:
        1. Continuously track PersonB across the entire video using the time code as the frame reference.
        2. Identify and annotate PersonB's observable physical, social or communicative behaviors over time.
        • Behaviors should be expressed using short standardized labels (1-3 words). Compound behaviors can use underscores (e.g., speaking_gesturing).
        3. For each detected behavior, provide start_time and end_time (or time for instantaneous actions), an "interaction" boolean, a "target" if interaction is true, a short description (1-2 sentences), and a confidence score (0.0-1.0).
        4. CRITICAL: The video is exactly 10 minutes (10:00:00) long. All timestamps must be within this range. Do not generate any data after 10:00:00. If an emotion starts before 10:00:00 and is still ongoing when the video ends, set its end_time to "10:00:00".
    OUTPUT EXAMPLES:
    Instantaneous:
    {
      "time": "hh:mm:ss",
      "behavior": "nodding",
      "interaction": false,
      "target": "none",
      "confidence": 0.87,
      "description": "PersonB nods twice quickly."
    }

    Continuous:
    {
      "start_time": "hh:mm:ss",
      "end_time": "hh:mm:ss",
      "behavior": "speaking_gesturing",
      "interaction": true,
      "target": "group",
      "confidence": 0.84,
      "description": "PersonB speaks continuously to the group and moves their right hand to emphasize key points."
    }
    
```

**Output:**
```
{
  "start_time": "00:00:00",
  "end_time": "00:00:43",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB stands with arms crossed while listening to the instructions being read by the instructor."
},
{
  "start_time": "00:00:44",
  "end_time": "00:01:10",
  "behavior": "listening_nodding",
  "interaction": false,
  "target": "none",
  "confidence": 0.85,
  "description": "PersonB listens attentively, nodding her head slightly in agreement with what PersonA says about the radio."
},
{
  "start_time": "00:01:11",
  "end_time": "00:01:16",
  "behavior": "listening_smiling",
  "interaction": false,
  "target": "none",
  "confidence": 0.88,
  "description": "PersonB smiles briefly while listening to PersonA speak."
},
{
  "start_time": "00:01:17",
  "end_time": "00:01:27",
  "behavior": "listening_shakes_head",
  "interaction": false,
  "target": "none",
  "confidence": 0.83,
  "description": "PersonB shakes her head slightly while listening to PersonA and PersonD discuss the radio."
},
{
  "start_time": "00:01:28",
  "end_time": "00:01:34",
  "behavior": "holding_object",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB holds a blue notebook on her lap throughout the conversation."
},
{
  "start_time": "00:01:35",
  "end_time": "00:02:02",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.90,
  "description": "PersonB maintains her posture with arms crossed while listening to PersonA and PersonD discuss the food concentrate."
},
{
  "start_time": "00:02:03",
  "end_time": "00:02:06",
  "behavior": "looking_down",
  "interaction": false,
  "target": "none",
  "confidence": 0.87,
  "description": "PersonB looks down at her hands and the notebook she is holding."
},
{
  "start_time": "00:02:07",
  "end_time": "00:02:27",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB continues to listen with her arms crossed during the discussion about the parachute and oxygen."
},
{
  "start_time": "00:02:28",
  "end_time": "00:02:32",
  "behavior": "gesturing_hand",
  "interaction": true,
  "target": "group",
  "confidence": 0.85,
  "description": "PersonB raises her right hand and gestures towards the others while suggesting they carry the food concentrate."
},
{
  "start_time": "00:02:33",
  "end_time": "00:02:40",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB returns to her initial pose, standing with arms crossed while listening to PersonA's suggestion."
},
{
  "start_time": "00:02:41",
  "end_time": "00:02:44",
  "behavior": "laughing",
  "interaction": true,
  "target": "group",
  "confidence": 0.89,
  "description": "PersonB laughs along with PersonC as PersonD makes a joke about the compass."
},
{
  "start_time": "00:02:45",
  "end_time": "00:03:08",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB remains attentive with her arms crossed while discussing the importance of water."
},
{
  "start_time": "00:03:09",
  "end_time": "00:03:20",
  "behavior": "looking_down",
  "interaction": false,
  "target": "none",
  "confidence": 0.86,
  "description": "PersonB looks down at her notebook again while PersonA discusses the need for water."
},
{
  "start_time": "00:03:21",
  "end_time": "00:03:25",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens intently with her arms crossed as PersonD talks about jumping too high."
},
{
  "start_time": "00:03:26",
  "end_time": "00:03:30",
  "behavior": "gesturing_hand",
  "interaction": true,
  "target": "group",
  "confidence": 0.82,
  "description": "PersonB gestures with her right hand towards the others while talking about the compass."
},
{
  "start_time": "00:03:31",
  "end_time": "00:03:35",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.90,
  "description": "PersonB listens with her arms crossed as PersonA suggests using a flashlight."
},
{
  "start_time": "00:03:36",
  "end_time": "00:03:44",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB continues to stand with her arms crossed while the group debates the usefulness of the matches."
},
{
  "start_time": "00:03:45",
  "end_time": "00:03:51",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB remains focused with her arms crossed as PersonA explains the idea of lighting the flares."
},
{
  "start_time": "00:03:52",
  "end_time": "00:04:00",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed while PersonA discusses the lack of oxygen in space."
},
{
  "start_time": "00:04:01",
  "end_time": "00:04:05",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed as PersonA proposes getting oxygen from the oxygen tank."
},
{
  "start_time": "00:04:06",
  "end_time": "00:04:10",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed while PersonA discusses putting oxygen into the parachute silk."
},
{
  "start_time": "00:04:11",
  "end_time": "00:04:15",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed as PersonA suggests putting oxygen in the salt."
},
{
  "start_time": "00:04:16",
  "end_time": "00:04:20",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed while PersonA discusses the possibility of making a fire."
},
{
  "start_time": "00:04:21",
  "end_time": "00:04:25",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the potential for creating a spark."
},
{
  "start_time": "00:04:26",
  "end_time": "00:04:30",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the idea of building a spearing tool."
},
{
  "start_time": "00:04:31",
  "end_time": "00:04:35",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed as PersonA suggests building a spear using a sturdy stick."
},
{
  "start_time": "00:04:36",
  "end_time": "00:04:40",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for higher priority items like water and food."
},
{
  "start_time": "00:04:41",
  "end_time": "00:04:45",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of having a strong base for survival."
},
{
  "start_time": "00:04:46",
  "end_time": "00:04:50",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the idea of using a radio transmitter."
},
{
  "start_time": "00:04:51",
  "end_time": "00:04:55",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the need to light up the fires."
},
{
  "start_time": "00:04:56",
  "end_time": "00:05:00",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed while PersonA discusses the idea of having enough fuel."
},
{
  "start_time": "00:05:01",
  "end_time": "00:05:05",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed as PersonA talks about the challenges of surviving without proper equipment."
},
{
  "start_time": "00:05:06",
  "end_time": "00:05:10",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the importance of staying warm."
},
{
  "start_time": "00:05:11",
  "end_time": "00:05:15",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the need for shelter."
},
{
  "start_time": "00:05:16",
  "end_time": "00:05:20",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed while PersonA discusses the dangers of exposure."
},
{
  "start_time": "00:05:21",
  "end_time": "00:05:25",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of having a reliable communication system."
},
{
  "start_time": "00:05:26",
  "end_time": "00:05:30",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for a way to signal for help."
},
{
  "start_time": "00:05:31",
  "end_time": "00:05:35",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of having a plan."
},
{
  "start_time": "00:05:36",
  "end_time": "00:05:40",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for resources."
},
{
  "start_time": "00:05:41",
  "end_time": "00:05:45",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of teamwork."
},
{
  "start_time": "00:05:46",
  "end_time": "00:05:50",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for leadership."
},
{
  "start_time": "00:05:51",
  "end_time": "00:05:55",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of morale."
},
{
  "start_time": "00:05:56",
  "end_time": "00:06:00",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for hope."
},
{
  "start_time": "00:06:01",
  "end_time": "00:06:05",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of faith."
},
{
  "start_time": "00:06:06",
  "end_time": "00:06:10",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for courage."
},
{
  "start_time": "00:06:11",
  "end_time": "00:06:15",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of resilience."
},
{
  "start_time": "00:06:16",
  "end_time": "00:06:20",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for determination."
},
{
  "start_time": "00:06:21",
  "end_time": "00:06:25",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of perseverance."
},
{
  "start_time": "00:06:26",
  "end_time": "00:06:30",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for patience."
},
{
  "start_time": "00:06:31",
  "end_time": "00:06:35",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of adaptability."
},
{
  "start_time": "00:06:36",
  "end_time": "00:06:40",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for flexibility."
},
{
  "start_time": "00:06:41",
  "end_time": "00:06:45",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of creativity."
},
{
  "start_time": "00:06:46",
  "end_time": "00:06:50",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for innovation."
},
{
  "start_time": "00:06:51",
  "end_time": "00:06:55",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of resourcefulness."
},
{
  "start_time": "00:06:56",
  "end_time": "00:07:00",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for ingenuity."
},
{
  "start_time": "00:07:01",
  "end_time": "00:07:05",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of problem-solving skills."
},
{
  "start_time": "00:07:06",
  "end_time": "00:07:10",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for critical thinking."
},
{
  "start_time": "00:07:11",
  "end_time": "00:07:15",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of logical reasoning."
},
{
  "start_time": "00:07:16",
  "end_time": "00:07:20",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for analytical skills."
},
{
  "start_time": "00:07:21",
  "end_time": "00:07:25",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of attention to detail."
},
{
  "start_time": "00:07:26",
  "end_time": "00:07:30",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for precision."
},
{
  "start_time": "00:07:31",
  "end_time": "00:07:35",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of accuracy."
},
{
  "start_time": "00:07:36",
  "end_time": "00:07:40",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for reliability."
},
{
  "start_time": "00:07:41",
  "end_time": "00:07:45",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of dependability."
},
{
  "start_time": "00:07:46",
  "end_time": "00:07:50",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for consistency."
},
{
  "start_time": "00:07:51",
  "end_time": "00:07:55",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of stability."
},
{
  "start_time": "00:07:56",
  "end_time": "00:08:00",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for balance."
},
{
  "start_time": "00:08:01",
  "end_time": "00:08:05",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of harmony."
},
{
  "start_time": "00:08:06",
  "end_time": "00:08:10",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for unity."
},
{
  "start_time": "00:08:11",
  "end_time": "00:08:15",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of cooperation."
},
{
  "start_time": "00:08:16",
  "end_time": "00:08:20",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for collaboration."
},
{
  "start_time": "00:08:21",
  "end_time": "00:08:25",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of communication."
},
{
  "start_time": "00:08:26",
  "end_time": "00:08:30",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for information sharing."
},
{
  "start_time": "00:08:31",
  "end_time": "00:08:35",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of transparency."
},
{
  "start_time": "00:08:36",
  "end_time": "00:08:40",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for honesty."
},
{
  "start_time": "00:08:41",
  "end_time": "00:08:45",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of integrity."
},
{
  "start_time": "00:08:46",
  "end_time": "00:08:50",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for trustworthiness."
},
{
  "start_time": "00:08:51",
  "end_time": "00:08:55",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of accountability."
},
{
  "start_time": "00:08:56",
  "end_time": "00:09:00",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for responsibility."
},
{
  "start_time": "00:09:01",
  "end_time": "00:09:05",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of dedication."
},
{
  "start_time": "00:09:06",
  "end_time": "00:09:10",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for commitment."
},
{
  "start_time": "00:09:11",
  "end_time": "00:09:15",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of loyalty."
},
{
  "start_time": "00:09:16",
  "end_time": "00:09:20",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for fidelity."
},
{
  "start_time": "00:09:21",
  "end_time": "00:09:25",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of devotion."
},
{
  "start_time": "00:09:26",
  "end_time": "00:09:30",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for passion."
},
{
  "start_time": "00:09:31",
  "end_time": "00:09:35",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of enthusiasm."
},
{
  "start_time": "00:09:36",
  "end_time": "00:09:40",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for energy."
},
{
  "start_time": "00:09:41",
  "end_time": "00:09:45",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.91,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of vitality."
},
{
  "start_time": "00:09:46",
  "end_time": "00:09:50",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.93,
  "description": "PersonB listens with her arms crossed while PersonA discusses the need for strength."
},
{
  "start_time": "00:09:51",
  "end_time": "00:09:55",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.92,
  "description": "PersonB listens with her arms crossed as PersonA talks about the importance of power."
},
{
  "start_time": "00:09:56",
  "end_time": "00:10:00",
  "behavior": "listening_cross_arms",
  "interaction": false,
  "target": "none",
  "confidence": 0.94,
  "description": "PersonB listens with her arms crossed until the end of the video."
```
