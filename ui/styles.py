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
    
    color: #444 !important; 
    
    background: transparent !important; 
    border: none !important;
    
    border-left: 4px solid #d0d0d0 !important; 
    
    padding-top: 0px !important;
    padding-bottom: 0px !important;
    
    padding-left: 10px !important;
    
    margin-top: 2px !important;
    margin-bottom: 4px !important;
    
    line-height: 1.2 !important;
    
    white-space: pre-wrap !important; 
    max-height: 150px;
    overflow-y: auto;
}
"""