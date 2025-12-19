import gradio as gr
import utils
from tabs import visualizer  

def render_tab1():
    with gr.TabItem("👁️ Input Visualizer"):
        with gr.Row():
            # ==========================
            # Left Column: Controls
            # ==========================
            with gr.Column(scale=1):
                viz_video = gr.Dropdown(
                    label="Select Video from Dataset",
                    choices=utils.get_video_files(),
                    value=None,
                )
                viz_refresh = gr.Button("🔄 Refresh Video List", size="sm")

                gr.Markdown("### Parameter Settings")
                with gr.Tabs():
                    
                    # --- Sub-tab: Gemini ---
                    with gr.TabItem("Gemini"):
                        gr.Markdown("**Note:** Google Gemini enforces a fixed FPS of 1.0 for video processing.")
                        
                        gem_ver = gr.Dropdown(
                            label="Model Family",
                            choices=["Gemini 3 Models", "Gemini 2.5 Models"], # 保持和你 visualizer.py 里的逻辑一致
                            value="Gemini 3 Models",
                        )
                        gem_res = gr.Dropdown(
                            ["Low", "Medium", "High"],
                            value="Medium",
                            label="Resolution Tier",
                        )
                        gem_btn = gr.Button("Run Gemini Visualization", variant="primary")

                    # --- Sub-tab: Qwen ---
                    with gr.TabItem("Qwen-VL"):
                        qwen_fps = gr.Slider(0.1, 10.0, 0.5, step=0.5, label="FPS")
                        
                        with gr.Row():
                            qwen_min_w = gr.Number(160, label="Min Width")
                            qwen_min_h = gr.Number(90, label="Min Height")
                        with gr.Row():
                            qwen_max_w = gr.Number(360, label="Max Width")
                            qwen_max_h = gr.Number(240, label="Max Height")
                        
                        qwen_btn = gr.Button("Run Qwen Visualization", variant="primary")

            # ==========================
            # Right Column: Outputs
            # ==========================
            with gr.Column(scale=2):
                # 3 Horizontal Log Boxes
                with gr.Row():
                    log_src = gr.Textbox(label="🎬 Source Info", lines=5, elem_classes="mono-font")
                    log_cfg = gr.Textbox(label="⚙️ Config", lines=5, elem_classes="mono-font")
                    log_res = gr.Textbox(label="📉 Result", lines=5, elem_classes="mono-font")
                
                viz_gallery = gr.Gallery(label="Model Input View (Frames)", columns=4)

        # ==========================
        # Event Wiring
        # ==========================
        
        # 1. Refresh Logic
        viz_refresh.click(utils.refresh_video_list, outputs=[viz_video])

        # 2. Qwen Logic
        qwen_btn.click(
            visualizer.run_qwen_viz,
            inputs=[
                viz_video,
                qwen_fps,
                qwen_min_w,
                qwen_min_h,
                qwen_max_w,
                qwen_max_h,
            ],
            outputs=[viz_gallery, log_src, log_cfg, log_res],
        )

        # 3. Gemini Logic
        gem_btn.click(
            visualizer.run_gemini_viz,
            inputs=[viz_video, gem_res, gem_ver],
            outputs=[viz_gallery, log_src, log_cfg, log_res],
        )