import gradio as gr
import utils
from ui import styles
from ui import tab1_viz
from ui import tab2_eval
from ui import tab3_verify
from ui import tab4_usage

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

with gr.Blocks(title="Video Model Workbench", css=styles.custom_css) as demo:

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
            tab1_viz.render_tab1()
            
            # ------------------------------------------------------------------
            # TAB 2: MODEL EVALUATION
            # ------------------------------------------------------------------
            tab2_eval.render_tab2(username_state)
                                    
            # ------------------------------------------------------------------
            # TAB 3: RESULT VERIFICATION
            # ------------------------------------------------------------------
            tab3_verify.render_tab3(username_state)
            
            # ------------------------------------------------------------------
            # TAB 4: USAGE DASHBOARD (NEW)
            # ------------------------------------------------------------------
            tab4_usage.render_tab4(demo)

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
