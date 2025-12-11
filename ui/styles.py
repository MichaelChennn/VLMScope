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