import gradio as gr
import random

# ---------------------------- Helper Functions ----------------------------

def parseIntegers(inputText):
    tokens = inputText.replace(",", " ").split()
    nums = []
    for token in tokens:
        if token.strip().lstrip("-").isdigit():
            nums.append(int(token))
        else:
            raise ValueError(f"Invalid number: {token}")
    return nums


def generateRandomCase():
    length = random.randint(6, 14)
    arr = sorted(random.sample(range(5, 60), length))
    target = random.choice(arr) if random.random() < 0.7 else random.randint(5, 60)
    return ", ".join(map(str, arr)), str(target)


# ---------------------------- Visualization ----------------------------

def renderCards(array, L, R, M, message):
    tiles = ""

    for i, value in enumerate(array):

        bg = "#ffffff"
        shadow = "0 1px 3px rgba(0,0,0,0.08)"
        border = "1px solid #d0e3ff"
        text = "#0a1a44"

        if L <= i <= R:
            bg = "#e9f2ff"

        if i == M:
            bg = "#fff5d6"
            border = "1px solid #f7c948"
            shadow = "0 0 6px rgba(247,201,72,0.6)"

        pointer = ""
        if i == L: pointer += "L "
        if i == M: pointer += "M "
        if i == R: pointer += "R"

        tiles += f"""
        <div style="display:flex;flex-direction:column;align-items:center;gap:4px;">
            
            <div style="
                width:60px;height:60px;
                display:flex;align-items:center;justify-content:center;
                background:{bg};
                border-radius:14px;
                font-weight:700;
                border:{border};
                box-shadow:{shadow};
                color:{text};
                font-size:18px;
            ">
                {value}
            </div>

            <div style="font-size:12px;color:#1e3a8a;width:60px;text-align:center;">
                {pointer}
            </div>

        </div>
        """

    return f"""
    <div style="margin-top:18px;">
        <div style="display:flex;gap:12px;flex-wrap:wrap;">
            {tiles}
        </div>

        <div style="margin-top:12px;font-weight:600;color:#1e40af;">
            {message}
        </div>
    </div>
    """


# ---------------------------- Binary Search Logic ----------------------------

def binarySearchUI(arrayText, targetText):
    try:
        arr = parseIntegers(arrayText)
        target = int(targetText)
    except Exception as error:
        return f"<div class='status-error'>{error}</div>", "Input error"

    if not arr:
        return "<div class='status-error'>Array is empty.</div>", "Input error"

    if arr != sorted(arr):
        return "<div class='status-error'>Array must be sorted.</div>", "Input error"

    L, R = 0, len(arr) - 1
    visuals = [f"<h2 style='color:#1e3a8a;margin-top:0;'>Binary Search (Target = {target})</h2>"]
    step = 1

    while L <= R:
        M = (L + R) // 2
        visuals.append(
            renderCards(arr, L, R, M, f"Step {step}: Checking index {M}")
        )

        if arr[M] == target:

            visuals.append(
                f"""
                <div style="
                    background:#d1fadf;
                    border:2px solid #36c676;
                    color:black;
                    padding:12px;
                    border-radius:30px;
                    font-weight:700;
                    text-align:center;
                    margin-top:10px;
                ">
                    Target found at index {M}
                </div>
                """
            )

            return "\n".join(visuals), f"Target found at index {M}"

        if arr[M] < target:
            L = M + 1
        else:
            R = M - 1

        step += 1

    visuals.append("<div class='status-error'>✗ Target not found</div>")
    return "\n".join(visuals), "Not found"



# ---------------------------- Redesigned CSS ----------------------------

custom_css = """
<style>

body {
    background: #eef5ff !important;
}

/* Gradient header banner */
.header-banner {
    width:100%;
    padding:30px 10px;
    text-align:center;
    background: linear-gradient(135deg, #d9e9ff, #f7fbff);
    border-radius:16px;
    margin-bottom:25px;
    box-shadow:0 3px 10px rgba(0,0,0,0.05);
}

/* Glass input panel */
.glass-panel {
    background: rgba(255,255,255,0.55);
    backdrop-filter: blur(10px);
    border-radius:20px;
    padding:20px;
    border:1px solid rgba(200,220,255,0.6);
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

/* Output stage */
.output-stage {
    background:white;
    border-radius:20px;
    padding:22px;
    border:1px solid #d0e3ff;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

/* Success message (UPDATED TO BLACK TEXT) */
.status-success {
    background:#d1fadf;
    border:2px solid #36c676;
    color:black;
    padding:12px;
    border-radius:30px;
    font-weight:700;
    text-align:center;
    margin-top:10px;
}

/* Error message */
.status-error {
    background:#ffe0e0;
    border:2px solid #ff6b6b;
    color:#7c1c1c;
    padding:12px;
    border-radius:30px;
    font-weight:700;
    text-align:center;
    margin-top:10px;
}

/* Info message */
.status-info {
    background:#e3f0ff;
    border:2px solid #63a1ff;
    color:#0f2e6d;
    padding:12px;
    border-radius:30px;
    font-weight:700;
    text-align:center;
    margin-top:10px;
}

/* Fix textbox shrinking */
input, textarea, .gr-textbox input, .gr-textbox textarea {
    min-height: 48px !important;
    font-size: 16px !important;
    padding: 10px 14px !important;
}

</style>
"""


# ---------------------------- UI LAYOUT ----------------------------

with gr.Blocks(title="Binary Search Visualizer") as demo:

    gr.HTML(custom_css)

    gr.HTML("""
    <div class="header-banner">
        <h1 style="color:#1e3a8a; margin:0;">Binary Search Visualizer</h1>
        <p style="color:#385bab; font-size:18px; margin-top:6px;">A clean step-by-step visual explanation</p>
    </div>
    """)

    with gr.Row():

        # Input Panel
        with gr.Column(scale=4):
            gr.HTML("<div class='glass-panel'>")
            arrayInput = gr.Textbox(label="Sorted Integer List", value="1, 2, 3, 4, 5, 6")
            targetInput = gr.Textbox(label="Target Value", value="2")
            runButton = gr.Button("Run Search")
            randomButton = gr.Button("Random Example")
            gr.HTML("</div>")

        # Output Panel
        with gr.Column(scale=6):
            gr.HTML("<div class='output-stage'>")
            statusOutput = gr.HTML("<div class='status-info'>Awaiting input…</div>")
            htmlOutput = gr.HTML()
            gr.HTML("</div>")

    runButton.click(binarySearchUI, [arrayInput, targetInput], [htmlOutput, statusOutput])
    randomButton.click(generateRandomCase, outputs=[arrayInput, targetInput])

demo.launch()
