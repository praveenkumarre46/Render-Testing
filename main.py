from html import escape

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def home(name: str = "") -> str:
		safe_name = escape(name)
		greeting = f"<h1>Hi {safe_name}</h1>" if safe_name else ""
		return f"""<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Say hello</title>
		<style>
			:root {{
				color-scheme: light;
				font-family: "Palatino Linotype", "Book Antiqua", Georgia, serif;
				color: #183b36;
				background: #e5f0e9;
			}}
			* {{ box-sizing: border-box; }}
			body {{
				min-height: 100vh;
				margin: 0;
				display: grid;
				place-items: center;
				padding: 24px;
				background-color: #e5f0e9;
				background-image:
					linear-gradient(135deg, rgba(255,255,255,.58), transparent 55%),
					repeating-linear-gradient(0deg, transparent 0 31px, rgba(24,59,54,.035) 31px 32px),
					repeating-linear-gradient(90deg, transparent 0 31px, rgba(24,59,54,.035) 31px 32px);
			}}
			main {{
				position: relative;
				width: min(100%, 560px);
				overflow: hidden;
				padding: clamp(28px, 7vw, 56px);
				border: 1px solid #d5e2da;
				border-radius: 8px;
				background: #fffefa;
				box-shadow: 0 24px 60px rgba(24,59,54,.12);
			}}
			main::before {{
				position: absolute;
				top: 0;
				left: 0;
				width: 100%;
				height: 7px;
				background: linear-gradient(90deg, #e77b5b 0 24%, #e8b957 24% 48%, #3b8174 48% 100%);
				content: "";
			}}
			h1 {{
				margin: 0 0 30px;
				font-size: clamp(2rem, 7vw, 3rem);
				font-weight: 500;
				line-height: 1.1;
			}}
			form {{ display: grid; gap: 12px; }}
			label {{ font-family: "Segoe UI", sans-serif; font-size: .9rem; font-weight: 650; }}
			input {{
				width: 100%;
				min-height: 50px;
				padding: 0 15px;
				border: 1px solid #b8cbc0;
				border-radius: 5px;
				background: #fbfcf8;
				color: #183b36;
				font: 1rem "Segoe UI", sans-serif;
			}}
			input:focus {{ outline: 3px solid rgba(59,129,116,.22); border-color: #3b8174; }}
			button {{
				min-height: 50px;
				margin-top: 5px;
				padding: 0 20px;
				border: 0;
				border-radius: 5px;
				background: #205e54;
				color: #fffefa;
				font: 650 .98rem "Segoe UI", sans-serif;
				cursor: pointer;
				transition: background-color .18s ease, transform .18s ease;
			}}
			button:hover {{ background: #17483f; transform: translateY(-1px); }}
			button:focus-visible {{ outline: 3px solid #e77b5b; outline-offset: 3px; }}
			main > h1:last-child {{
				margin: 28px 0 0;
				padding-top: 22px;
				border-top: 1px solid #dce7df;
				color: #b45238;
			}}
			@media (min-width: 520px) {{
				form {{ grid-template-columns: 1fr auto; align-items: end; }}
				label {{ grid-column: 1 / -1; }}
				button {{ margin: 0; }}
			}}
			@media (prefers-reduced-motion: reduce) {{ button {{ transition: none; }} }}
		</style>
	</head>
	<body>
		<main>
			<h1>What's your name?</h1>
			<form action="/" method="get">
				<label for="name">Name</label>
				<input id="name" name="name" value="{safe_name}" required>
				<button type="submit">Say hello</button>
			</form>
			{greeting}
		</main>
	</body>
</html>"""


