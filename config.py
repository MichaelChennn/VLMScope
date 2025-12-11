import os

# ==============================================================================
# GLOBAL CONFIGURATION
# ==============================================================================

# Directory for source videos
DATASET_DIR = "dataset"

# Directory where Model Evaluation (Tab 2) saves raw JSONs
MODEL_RESULTS_DIR = "model_results"

# Directory where Result Verification (Tab 3) saves annotated JSONs
HUMAN_RESULTS_DIR = "human_results"

# Directory for temporary video clips (cleaned up automatically)
TEMP_DIR = "temp_clips"

# File to log API usage and costs
API_USAGE_FILE = "api_usage.json"

# Ensure all necessary directories exist
for d in [DATASET_DIR, MODEL_RESULTS_DIR, HUMAN_RESULTS_DIR, TEMP_DIR]:
    os.makedirs(d, exist_ok=True)
    
# Models for Gemini
GEMINI_MODELS = [
    "gemini-2.5-pro",
    "gemini-3-pro-preview",
]

# Pricing Table (USD per 1M tokens)
PRICING_TABLE = {
    "gemini-3": {
        "input_low": 2.00,   # <= 200k context
        "input_high": 4.00,  # > 200k context
        "output_low": 12.00, # <= 200k context
        "output_high": 18.00 # > 200k context
    },
    "gemini-2": { # Applies to 2.5 and 2.0
        "input_low": 1.25,
        "input_high": 2.50,
        "output_low": 10.00,
        "output_high": 15.00
    }
}

# ==============================================================================
# PROMPT TEMPLATES
# ==============================================================================
BACKGROUND_PROMPTS_EXAMPLES = """
Example:

There are four participants engaged in a group decision-making task (NASA Moon Survival Task). The input is a video recording with:
- Visual cues of participants' facial expressions and body language.
- Transcripts of their spoken dialogue.
- A time code is displayed at the bottom left corner of each frame.
All four participants are visible in the video, positioned from left to right: PersonA(leftmost, female, long curlyhair, black sleeveless skirt), PersonC(middleleft, female, long straight hair, black short-sleeve T-shirt and skirt with shoulder), PersonB(middleright, female, long straight hair, white long-sleeve blouse with a denim vest), PersonD(rightmost, black short-sleeve T-shirt, dark pants).
"""

TASK_PROMPTS_EXAMPLES = """
Examlpe:

1. Continuously track PersonA across the entire video using the time code as the frame reference.
2. Detect and annotate changes in PersonA's emotional state over time based on visual and speech cues.
- Example emotion labels: happy, neutral, confused, frustrated, surprised, focused, enthusiastic, curious, confident, relaxed, thoughtful, skeptical, uncertain, hesitant, annoyed, anxious, tense, agreeing, disagreeing, bored, uncomfortable
3. For each detected emotional state, provide the start time and end time to indicate how long the emotion lasts.
- Use the format hh:mm:ss.
- If the emotion is momentary (e.g., a short smile or brief surprise), start_time and end_time can be the same or nearly identical.
...
"""

LABEL_PROMPTS_EXAMPLES = """
Example:

Communicative:
speaking, listening, nodding, shaking_head, pointing_left, pointing_right,
turning_head_left, turning_head_right, raising_hand, shrugging, smiling, laughing.
Attentive / Gaze-related:
- looking_down, looking_up, looking_at_screen, looking_at_personB, looking_at_personD,
following_gaze, head_tilt.
Self-directed / Micro-movements:
- adjusting_posture, touching_face, touching_chin, scratching_head, rubbing_hands,
fidgeting, crossing_arms, uncrossing_arms, playing_with_pen.
Task-oriented / Object interaction:
- writing, typing, holding_paper, using_mouse, reaching_for_object, moving_chair,
tapping_table, opening_bottle, adjusting_glasses.
Other short labels:
- breathing_deeply, yawning, clapping, stretching, adjusting_clothes.
- You may output any other relevant physical action if observed, even if not listed.
"""

CONDITIONS_PROMPTS_EXAMPLES = """
Example:

2a.	Target Presence (Has Target?)
Determine whether the observed behavior is directed toward a specific target (e.g., a person, screen, or object). Output a boolean in the "interaction" field: use "true" if the behavior is directed at a target; use "false" if it is not target-directed or the target is indeterminate.
2b.	Target Identification
If the previous step outputs "true", specify the behavior's target in the "target" field. The target can be PersonA, PersonB, PersonC, group, monitor, or another object (provide a concise object name). If the previous step outputs "false", set "target" to "none".
"""

EVIDENCE_PROMPTS_EXAMPLES = """
Example:

For each detected behavior, also generate a short natural-language description of what PersonA is doing during this time.
- Keep it 1-2 sentences maximum.
- Describe the physical movement clearly and concretely.
- Do not speculate about mental states or intentions.
- This description should help clarify how the behavior label was determined.
Example descriptions:
- "PersonA turns their head slightly to the left and nods twice while facing PersonB."
- "PersonA is speaking continuously and moving their right hand to emphasize points."
- "PersonA leans forward and looks down at the table."
"""

OUTPUT_PROMPTS_EXAMPLES = """
Examlpe:

{
"start_time": "hh:mm:ss",
"end_time": "hh:mm:ss",
"emotion": "happy/neutral/confused/.../uncertain/or-new-label",
"description": "PersonA feels satisfied with the answer and nods his head",
"confidence": 0.0-1.0
}
"""

# ==============================================================================
#  PROMPT EXAMPLES DATA
# ==============================================================================

EXAMPLES = {
    "bg": BACKGROUND_PROMPTS_EXAMPLES,

    "task": TASK_PROMPTS_EXAMPLES,

    "label": LABEL_PROMPTS_EXAMPLES,

    "cond": CONDITIONS_PROMPTS_EXAMPLES,

    "evi": EVIDENCE_PROMPTS_EXAMPLES,

    "out": OUTPUT_PROMPTS_EXAMPLES,
}