import gradio as gr
import utils
import config

def render_tab4(demo):
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
                demo.load(utils.refresh_usage_data, outputs=usage_table)

                usage_refresh_btn.click(utils.refresh_usage_data, outputs=[usage_table])