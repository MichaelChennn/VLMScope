import gradio as gr
import utils
from tabs import evaluation
import config
from app_decaptured import refresh_video_list

def render_tab2(username):
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
                def validate_and_run(u, t, m, v, res, think, *prompts):
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
                        
                        yield error_msg
                        return
                    

                    yield from evaluation.run_gemini_inference(
                        u, t, m, v, list(prompts), res, think
                    )
                    
                ev_btn.click(
                    fn=validate_and_run,
                    inputs=[
                        username,
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