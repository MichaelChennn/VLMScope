import gradio as gr
import utils
import config

# Import logic modules from the 'tabs' package
from tabs import visualizer, evaluation, verification

# ==============================================================================
#  UI HELPER FUNCTIONS
# ==============================================================================


def refresh_video_list():
    """Refreshes the video list from the dataset folder."""
    files = utils.get_video_files()
    if not files:
        return gr.update(choices=[], value=None, label="⚠️ No videos in 'dataset'")
    return gr.update(
        choices=files, value=files[0] if files else None, label="Select Video"
    )


def refresh_json_list():
    """Refreshes the JSON result list from the model_results folder."""
    files = utils.get_model_result_files()
    if not files:
        return gr.update(choices=[], value=None)
    return gr.update(choices=files, value=files[0] if files else None)


def refresh_usage_data():
    data = utils.get_usage_summary()
    if not data:
        return gr.update(value=[])
    return gr.update(value=data)


# === Login Logic ===
def login(username):
    """
    Validates username and switches views.
    Returns: update_login_view, update_main_view, welcome_message
    """
    if not username or not username.strip():
        # Keep login visible, show error
        return (
            gr.update(visible=True),
            gr.update(visible=False),
            "⚠️ Please enter a username.",
        )

    # Hide login, show main app, update header
    welcome_msg = f"## 🎬 Video Model Workbench (Logged in as: {username})"
    return gr.update(visible=False), gr.update(visible=True), welcome_msg


# ==============================================================================
#  CSS & LAYOUT
# ==============================================================================

custom_css = """
.mono-font textarea {
    font-family: 'Consolas', 'Monaco', 'Ui-Monospace', 'Courier New', monospace !important;
    font-size: 13px !important;       
    line-height: 1.3 !important;      
    padding: 10px !important;         
    resize: none !important;          
}

footer {visibility: hidden}

.gradio-container {
    max_width: 100% !important;
}

.prompt-example-box {
    font-family: 'Consolas', 'Monaco', monospace !important;
    font-size: 13px !important;
    
    /* 1. 保持较深的颜色，清晰易读 */
    color: #444 !important; 
    
    background: transparent !important; 
    border: none !important;
    
    /* 左侧线条 */
    border-left: 4px solid #d0d0d0 !important; 
    
    /* 2. 核心修改：内边距归零，让文字紧贴上下边缘 */
    padding-top: 0px !important;
    padding-bottom: 0px !important;
    
    /* 左侧留一点距离，不然字贴着线太难看 */
    padding-left: 10px !important;
    
    /* 3. 外边距也调小，让它离上面的标题和下面的输入框更近 */
    margin-top: 2px !important;
    margin-bottom: 4px !important;
    
    /* 4. 行高调紧凑一点 */
    line-height: 1.2 !important;
    
    white-space: pre-wrap !important; 
    max-height: 150px;
    overflow-y: auto;
}
"""

with gr.Blocks(title="Video Model Workbench", css=custom_css) as demo:

    # === State for Username ===
    username_state = gr.State("")

    # ==========================
    # 1. LOGIN VIEW
    # ==========================
    # Use gr.Column instead of gr.Group to avoid ugly gray backgrounds
    with gr.Column(visible=True) as login_view:
        gr.Markdown("# 👋 Welcome to Video Workbench")
        with gr.Row():
            with gr.Column(scale=1):
                login_input = gr.Textbox(
                    label="Username",
                    placeholder="Enter your name to login...",
                    autofocus=True,
                )
                login_btn = gr.Button("Login", variant="primary")
                login_error = gr.Markdown("")

    # ==========================
    # 2. MAIN APP VIEW
    # ==========================
    # Hidden by default until logged in
    with gr.Column(visible=False) as main_view:

        header_md = gr.Markdown("# 🎬 Video Model Workbench")

        with gr.Tabs():

            # ------------------------------------------------------------------
            # TAB 1: INPUT VISUALIZER
            # ------------------------------------------------------------------
            with gr.TabItem("👁️ Input Visualizer"):
                with gr.Row():
                    # Left Column: Controls
                    with gr.Column(scale=1):
                        viz_video = gr.Dropdown(
                            label="Select Video from Dataset",
                            choices=utils.get_video_files(),
                            value=None,
                        )
                        viz_refresh = gr.Button("🔄 Refresh Video List", size="sm")

                        gr.Markdown("### Parameter Settings")
                        with gr.Tabs():

                            # Sub-tab: Gemini
                            with gr.TabItem("Gemini"):
                                gem_fps = gr.Markdown(
                                    "**Note:** Google Gemini enforces a fixed FPS of 1.0 for video processing."
                                )
                                gem_ver = gr.Dropdown(
                                    label="Model Family",
                                    choices=["Gemini 3 Pro", "Gemini 2.5 Pro"],
                                    value="Gemini 3 Pro",
                                )
                                gem_res = gr.Dropdown(
                                    ["Low", "Medium", "High"],
                                    value="Medium",
                                    label="Resolution Tier",
                                )
                                gem_btn = gr.Button(
                                    "Run Gemini Visualization", variant="primary"
                                )

                            # Sub-tab: Qwen
                            with gr.TabItem("Qwen-VL"):
                                qwen_fps = gr.Slider(
                                    0.1, 10.0, 0.5, step=0.5, label="FPS"
                                )
                                with gr.Row():
                                    qwen_min_w = gr.Number(160, label="Min Width")
                                    qwen_min_h = gr.Number(90, label="Min Height")
                                with gr.Row():
                                    qwen_max_w = gr.Number(360, label="Max Width")
                                    qwen_max_h = gr.Number(240, label="Max Height")
                                qwen_btn = gr.Button(
                                    "Run Qwen Visualization", variant="primary"
                                )

                    # Right Column: Outputs
                    with gr.Column(scale=2):
                        # 3 Horizontal Log Boxes
                        with gr.Row():
                            log_src = gr.Textbox(
                                label="🎬 Source Info",
                                lines=5,
                                elem_classes="mono-font",
                            )
                            log_cfg = gr.Textbox(
                                label="⚙️ Config", lines=5, elem_classes="mono-font"
                            )
                            log_res = gr.Textbox(
                                label="📉 Result", lines=5, elem_classes="mono-font"
                            )
                        viz_gallery = gr.Gallery(
                            label="Model Input View (Frames)", columns=4
                        )

                # Wiring Events (Tab 1)
                viz_refresh.click(refresh_video_list, outputs=[viz_video])

                qwen_btn.click(
                    visualizer.run_qwen_viz,
                    [
                        viz_video,
                        qwen_fps,
                        qwen_min_w,
                        qwen_min_h,
                        qwen_max_w,
                        qwen_max_h,
                    ],
                    [viz_gallery, log_src, log_cfg, log_res],
                )
                gem_btn.click(
                    visualizer.run_gemini_viz,
                    [viz_video, gem_res, gem_ver],
                    [viz_gallery, log_src, log_cfg, log_res],
                )

            # ------------------------------------------------------------------
            # TAB 2: MODEL EVALUATION
            # ------------------------------------------------------------------
            with gr.TabItem("🚀 Model Evaluation"):
                with gr.Tabs():
                    with gr.TabItem("Gemini"):
                        with gr.Row():
                            with gr.Column(scale=1):
                                ev_task = gr.Textbox(
                                    label="Task Name", placeholder="e.g. emotion_test"
                                )

                                # Model Selection
                                ev_model = gr.Dropdown(
                                    label="Model",
                                    choices=utils.get_gemini_models(),
                                    value="gemini-3-pro-preview",
                                    allow_custom_value=True,
                                )
                                ev_video = gr.Dropdown(
                                    label="Select Video",
                                    choices=utils.get_video_files(),
                                )
                                ev_refresh = gr.Button("🔄 Refresh Videos", size="sm")

                                # 🟢 GROUP: Advanced Settings (Res & Thinking)
                                # We wrap them in a Group or Row so we can toggle them easier,
                                # though toggling individual components is safer for layout.
                                with gr.Row() as adv_settings_row:
                                    ev_res = gr.Dropdown(
                                        ["Low", "Medium", "High"],
                                        value="Medium",
                                        label="Resolution",
                                    )
                                    ev_think = gr.Radio(
                                        ["Low", "High"],
                                        value="High",
                                        label="Thinking Level",
                                    )
                                
                                # ev_prompt = gr.Textbox(label="Prompt", lines=5)
                                ev_btn = gr.Button(
                                    "🚀 Run Inference", variant="primary"
                                )

                                ev_out = gr.Textbox(label="Output / Logs", lines=20, elem_classes="mono-font", autoscroll=True)

                            with gr.Column(scale=2):
                                gr.Markdown("### 🛠️ Structured Prompt Engineering")

                                with gr.Group():
                                    # 1. Background
                                    gr.HTML(
                                        f"<div class='prompt-example-box'>{config.EXAMPLES['bg']}</div>"
                                    )
                                    p_bg = gr.Textbox(
                                        label="1. Background Introduction",
                                        lines=3,
                                        placeholder="Enter background...",
                                    )

                                    # 2. Task Description
                                    gr.HTML(
                                        f"<div class='prompt-example-box'>{config.EXAMPLES['task']}</div>"
                                    )
                                    p_task = gr.Textbox(
                                        label="2. Task Description",
                                        lines=3,
                                        placeholder="Enter task...",
                                    )

                                    # 3. Label Identify
                                    gr.HTML(
                                        f"<div class='prompt-example-box'>{config.EXAMPLES['label']}</div>"
                                    )
                                    p_label = gr.Textbox(
                                        label="3. Label Identify",
                                        lines=3,
                                        placeholder="Enter labels...",
                                    )

                                    # 4. Condition Evaluation
                                    gr.HTML(
                                        f"<div class='prompt-example-box'>{config.EXAMPLES['cond']}</div>"
                                    )
                                    p_cond = gr.Textbox(
                                        label="4. Condition Evaluation",
                                        lines=3,
                                        placeholder="Enter conditions...",
                                    )

                                    # 5. Evidence
                                    gr.HTML(
                                        f"<div class='prompt-example-box'>{config.EXAMPLES['evi']}</div>"
                                    )
                                    p_evi = gr.Textbox(
                                        label="5. Evidence",
                                        lines=3,
                                        placeholder="Enter evidence requirements...",
                                    )

                                    # 6. Output Example
                                    gr.HTML(
                                        f"<div class='prompt-example-box'>{config.EXAMPLES['out']}</div>"
                                    )
                                    p_out = gr.Textbox(
                                        label="6. Output Example",
                                        lines=3,
                                        value="{\n'start_time': 'HH:MM:SS',\n'end_time': 'HH:MM:SS',\n'behavior': 'str',\n'confidence': float,\n'description': 'str'\n}",
                                    )

                    with gr.TabItem("Qwen-VL"):
                        gr.Markdown("🚧 Under Construction")

                # Wiring Events (Tab 2)
                ev_refresh.click(refresh_video_list, outputs=[ev_video])

                # 🟢 NEW: Dynamic Visibility Logic
                def toggle_gemini_settings(model_name):
                    # Logic: Only show Res/Think if model is Gemini 3
                    # (Adjust string matching as needed based on your model names)
                    if "gemini-3" in model_name.lower():
                        return gr.update(visible=True), gr.update(visible=True)
                    else:
                        # For Gemini 2.5 hide these settings
                        return gr.update(visible=False, value=None), gr.update(
                            visible=False, value=None
                        )

                # Bind change event
                ev_model.change(
                    fn=toggle_gemini_settings,
                    inputs=[ev_model],
                    outputs=[ev_res, ev_think],
                )

                # Run Inference
                def validate_and_run(u, k, t, m, v, res, think, *prompts):
                    """
                    Checks if any prompt textbox is empty before calling the backend.
                    """
                    field_names = [
                        "1. Background Introduction", 
                        "2. Task Description", 
                        "3. Label Identify", 
                        "4. Condition Evaluation", 
                        "5. Evidence", 
                        "6. Output Example"
                    ]
                    
                    missing_fields = []
                    for name, content in zip(field_names, prompts):
                        if not content or not str(content).strip():
                            missing_fields.append(name)
                    
                    if missing_fields:
                        error_msg = "⚠️ Validation Error: The following prompt sections are empty:\n"
                        for f in missing_fields:
                            error_msg += f"- {f}\n"
                        
                        error_msg += "\n⛔ Inference aborted. Please fill all sections."
                        
                        gr.Warning(f"Missing {len(missing_fields)} prompt sections!")
                        
                        return error_msg
                    

                    return evaluation.run_gemini_inference(
                        u, k, t, m, v, list(prompts), res, think
                    )
                    
                ev_btn.click(
                    fn=validate_and_run,
                    inputs=[
                        username_state,
                        ev_task,
                        ev_model,
                        ev_video,
                        ev_res,
                        ev_think,
                        p_bg,
                        p_task,
                        p_label,
                        p_cond,
                        p_evi,
                        p_out,
                    ],
                    outputs=[ev_out],
                )

            # ------------------------------------------------------------------
            # TAB 3: RESULT VERIFICATION
            # ------------------------------------------------------------------
            with gr.TabItem("✅ Result Verification"):
                ver_state = gr.State([])

                with gr.Row():
                    # Left Column: Setup
                    with gr.Column(scale=1):
                        gr.Markdown("### 1. Source Setup")
                        ver_video = gr.Dropdown(
                            label="Video (Dataset)", choices=utils.get_video_files()
                        )
                        ver_refresh_vid = gr.Button("🔄 Refresh Videos", size="sm")

                        gr.Markdown("---")
                        ver_mode = gr.Radio(
                            ["Load from File", "Paste Raw JSON"],
                            label="JSON Source",
                            value="Load from File",
                        )

                        with gr.Group(visible=True) as grp_file:
                            ver_file = gr.Dropdown(
                                label="Select Result File",
                                choices=utils.get_model_result_files(),
                            )
                            ver_refresh_file = gr.Button(
                                "🔄 Refresh Results", size="sm"
                            )

                        with gr.Group(visible=False) as grp_raw:
                            ver_raw = gr.Textbox(
                                label="Raw JSON", lines=3, placeholder="{...}"
                            )

                        # Visibility Toggle Logic
                        def toggle(m):
                            return {
                                grp_file: gr.update(visible=(m == "Load from File")),
                                grp_raw: gr.update(visible=(m == "Paste Raw JSON")),
                            }

                        ver_mode.change(toggle, [ver_mode], [grp_file, grp_raw])

                        ver_load_btn = gr.Button("📥 Load Analysis", variant="primary")
                        ver_status = gr.Textbox(label="Status", interactive=False)

                        ver_prompt_display = gr.Textbox(
                            label="📜 Original Prompt (from Metadata)",
                            lines=10,
                            interactive=False,
                            elem_classes="mono-font",
                        )

                        gr.Markdown("### 4. Export")
                        ver_save_btn = gr.Button("💾 Save Verified Results")
                        ver_save_log = gr.Textbox(show_label=False)

                    # Right Column: Player & Labeling
                    with gr.Column(scale=2):
                        ver_sel = gr.Dropdown(
                            label="2. Select Segment", choices=[], interactive=True
                        )
                        ver_player = gr.Video(
                            label="Clip Playback", autoplay=True, height=500
                        )
                        ver_details = gr.Markdown(label="Details", height=200)

                        gr.Markdown("### 3. Annotation")
                        with gr.Row():
                            ver_lbl_status = gr.Textbox(
                                value="⚪ Unlabeled", label="Current", interactive=False
                            )
                            btn_t = gr.Button("✅ True", variant="primary")
                            btn_ns = gr.Button("⚠️ Not Sure", variant="secondary")
                            btn_f = gr.Button("❌ False", variant="stop")

                        ver_cmt = gr.Textbox(
                            label="Comment", placeholder="Type reason...", lines=1
                        )

                # Wiring Events (Tab 3)
                ver_refresh_vid.click(refresh_video_list, outputs=[ver_video])
                ver_refresh_file.click(refresh_json_list, outputs=[ver_file])

                ver_load_btn.click(
                    verification.load_data,
                    [ver_video, ver_mode, ver_raw, ver_file],
                    [ver_sel, ver_state, ver_status, ver_prompt_display],
                )

                ver_sel.change(
                    verification.update_ui,
                    [ver_sel, ver_state, ver_video],
                    [ver_player, ver_details, ver_cmt, ver_lbl_status],
                )

                # Label Buttons
                btn_t.click(
                    lambda c, d, cm: verification.handle_label(c, d, cm, True),
                    [ver_sel, ver_state, ver_cmt],
                    [ver_state, ver_lbl_status, ver_sel],
                )
                btn_ns.click(
                    lambda c, d, cm: verification.handle_label(c, d, cm, "not_sure"),
                    [ver_sel, ver_state, ver_cmt],
                    [ver_state, ver_lbl_status, ver_sel],
                )
                btn_f.click(
                    lambda c, d, cm: verification.handle_label(c, d, cm, False),
                    [ver_sel, ver_state, ver_cmt],
                    [ver_state, ver_lbl_status, ver_sel],
                )

                ver_cmt.change(
                    verification.save_comment,
                    [ver_sel, ver_state, ver_cmt],
                    [ver_state],
                )

                # Note: Passing username_state to save results with username
                ver_save_btn.click(
                    verification.save_file,
                    [ver_state, username_state, ver_video, ver_file],
                    [ver_save_log],
                )

            # ------------------------------------------------------------------
            # TAB 4: USAGE DASHBOARD (NEW)
            # ------------------------------------------------------------------
            with gr.TabItem("💰 Usage & Cost"):
                gr.Markdown("### API Token Usage & Cost Estimator")
                gr.Markdown(
                    "_Pricing based on standard Google Cloud rates (per 1M tokens)._"
                )

                usage_refresh_btn = gr.Button("🔄 Refresh Data", size="sm")

                # Table Structure
                usage_table = gr.Dataframe(
                    headers=[
                        "User",
                        "Model",
                        "Input Tokens",
                        "Output Tokens",
                        "Thinking Tokens",
                        "Total Tokens",
                        "Est. Cost ($)",
                        "Last Active",
                    ],
                    datatype=[
                        "str",
                        "str",
                        "number",
                        "number",
                        "number",
                        "number",
                        "str",
                        "str",
                    ],
                    row_count=5,
                    col_count=(8, "fixed"),
                    interactive=False,
                )

                # Auto-load data when app starts (optional, or just rely on click)
                demo.load(refresh_usage_data, outputs=usage_table)

            usage_refresh_btn.click(refresh_usage_data, outputs=[usage_table])

    # ==========================
    # LOGIN BUTTON EVENT LOGIC
    # ==========================
    login_btn.click(
        fn=login, inputs=[login_input], outputs=[login_view, main_view, header_md]
    ).then(
        # Save username to State
        fn=lambda x: x,
        inputs=[login_input],
        outputs=[username_state],
    )

if __name__ == "__main__":
    utils.cleanup_temp_folder()
    demo.queue().launch(share=False)
