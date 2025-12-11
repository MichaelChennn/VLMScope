import gradio as gr
import utils
from tabs import verification
from app_decaptured import refresh_video_list

def refresh_json_list():
    """Refreshes the JSON result list from the model_results folder."""
    files = utils.get_model_result_files()
    if not files:
        return gr.update(choices=[], value=None)
    return gr.update(choices=files, value=files[0] if files else None)

def render_tab3(username):
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
                    [ver_state, username, ver_video, ver_file],
                    [ver_save_log],
                )