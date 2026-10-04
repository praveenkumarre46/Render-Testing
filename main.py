from html import escape

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def home(name: str = "Preethi Priya") -> str:
	safe_name = escape(name)
	if safe_name:
		content = f"""
			<section id="welcome">
				<p class="eyebrow">Just for you</p>
				<h1>Welcome {safe_name}</h1>
				<p class="note">I have a little question for you...</p>
				<button class="yes" id="start" type="button">Start</button>
			</section>
			<section id="questions" hidden>
				<p class="eyebrow" id="recipient">A tiny question for {safe_name}</p>
				<h1 id="question" aria-live="polite" tabindex="-1">Do you love me? 🥰</h1>
				<div class="answers" id="answers">
					<button class="yes" id="yes" type="button">Yes 💖</button>
					<button class="no" id="no" type="button">No 🙈</button>
				</div>
				<p class="note" id="note">Choose honestly. I can take it. Probably.</p>
				<div class="celebration" id="celebration" aria-hidden="true"></div>
			</section>
			<script>
				const questions = [
					"Are you sure you don't love me? 🥺",
					"Not even a teeny, tiny bit? 🥹",
					"What if I ask with my best puppy eyes? 🐶",
					"Could your answer maybe be a little bit yes? 💕",
					"One last time: do you love me? 💌"
				];
				let questionIndex = -1;
				document.getElementById("start").addEventListener("click", () => {{
					document.getElementById("welcome").hidden = true;
					document.getElementById("questions").hidden = false;
					document.getElementById("question").focus();
				}});
				document.getElementById("no").addEventListener("click", () => {{
					questionIndex = (questionIndex + 1) % questions.length;
					document.getElementById("question").textContent = questions[questionIndex];
					document.getElementById("note").textContent = "Hmm. Let me ask that a different way...";
				}});
				document.getElementById("yes").addEventListener("click", () => {{
					const recipientName = document.getElementById("recipient").textContent.slice("A tiny question for ".length);
					document.getElementById("question").textContent = `I love you too, ${{recipientName}}! 💖`;
					document.getElementById("answers").remove();
					document.getElementById("note").textContent = "You just made my whole day.";
					const celebration = document.getElementById("celebration");
					celebration.setAttribute("aria-hidden", "false");
					for (let index = 0; index < 18; index += 1) {{
						const heart = document.createElement("span");
						heart.innerHTML = "&hearts;";
						heart.style.setProperty("--x", `${{Math.random() * 100}}%`);
						heart.style.setProperty("--delay", `${{Math.random() * .8}}s`);
						celebration.append(heart);
					}}
				}});
			</script>"""
	else:
		content = """
			<p class="eyebrow">A little something for you</p>
			<h1>Before I ask you something...</h1>
			<form action="/" method="get">
				<label for="name">What's your name?</label>
				<input id="name" name="name" placeholder="Your name" required>
				<button class="yes" type="submit">Open your surprise</button>
			</form>"""
	return f"""<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>A little question</title>
		<style>
			:root {{
				color-scheme: light;
				font-family: "Palatino Linotype", "Book Antiqua", Georgia, serif;
				color: #293d35;
				background: #f4e8df;
			}}
			* {{ box-sizing: border-box; }}
			section[hidden] {{ display: none; }}
			body {{
				min-height: 100vh;
				margin: 0;
				display: grid;
				place-items: center;
				padding: 24px;
				background-color: #f4e8df;
				background-image:
					radial-gradient(ellipse at 8% 90%, rgba(225,120,99,.14), transparent 36%),
					linear-gradient(145deg, rgba(255,255,255,.75), transparent 60%),
					repeating-linear-gradient(0deg, transparent 0 35px, rgba(41,61,53,.035) 35px 36px);
			}}
			main {{
				position: relative;
				width: min(100%, 520px);
				overflow: hidden;
				padding: clamp(30px, 8vw, 58px);
				border: 1px solid #e3d2c5;
				border-radius: 8px;
				background: #fffdf8;
				box-shadow: 0 24px 60px rgba(88,54,43,.12);
			}}
			main::before {{
				position: absolute;
				top: 0;
				left: 0;
				width: 100%;
				height: 6px;
				background: linear-gradient(90deg, #e17963 0 34%, #e8b958 34% 66%, #548575 66% 100%);
				content: "";
			}}
			.eyebrow {{
				margin: 0 0 18px;
				color: #a65c49;
				font: 700 .76rem "Segoe UI", sans-serif;
				letter-spacing: .12em;
				text-transform: uppercase;
			}}
			h1 {{
				min-height: 2.2em;
				margin: 0 0 28px;
				font-size: clamp(2rem, 7vw, 2.8rem);
				font-weight: 500;
				line-height: 1.12;
			}}
			form {{ display: grid; gap: 12px; }}
			label {{ font: 650 .9rem "Segoe UI", sans-serif; }}
			input {{
				width: 100%;
				min-height: 50px;
				padding: 0 15px;
				border: 1px solid #cbb9aa;
				border-radius: 5px;
				background: #fffefa;
				color: #293d35;
				font: 1rem "Segoe UI", sans-serif;
			}}
			input:focus {{ outline: 3px solid rgba(84,133,117,.25); border-color: #548575; }}
			button {{
				min-height: 50px;
				padding: 0 22px;
				border: 1px solid transparent;
				border-radius: 5px;
				font: 650 .98rem "Segoe UI", sans-serif;
				cursor: pointer;
				transition: background-color .18s ease, transform .18s ease, border-color .18s ease;
			}}
			button:hover {{ transform: translateY(-2px); }}
			button:focus-visible {{ outline: 3px solid #e17963; outline-offset: 3px; }}
			.yes {{ background: #397568; color: #fffdf8; }}
			.yes:hover {{ background: #2c6257; }}
			.no {{ border-color: #d8c9bd; background: transparent; color: #725f54; }}
			.no:hover {{ border-color: #bba394; background: #faf3ec; }}
			.answers {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
			.note {{ min-height: 1.5em; margin: 21px 0 0; color: #817369; font: .92rem "Segoe UI", sans-serif; }}
			.celebration {{ position: absolute; inset: 0; overflow: hidden; pointer-events: none; }}
			.celebration span {{
				position: absolute;
				bottom: -24px;
				left: var(--x);
				color: #df7964;
				font-size: 22px;
				animation: float-up 2.6s var(--delay) ease-out forwards;
			}}
			@keyframes float-up {{ to {{ transform: translateY(-440px) rotate(25deg); opacity: 0; }} }}
			@media (min-width: 520px) {{ form {{ grid-template-columns: 1fr auto; align-items: end; }} form label {{ grid-column: 1 / -1; }} }}
			@media (prefers-reduced-motion: reduce) {{ *, *::before, *::after {{ animation-duration: .01ms !important; transition-duration: .01ms !important; }} }}
			}}
		</style>
	</head>
	<body>
		<main>
			{content}
		</main>
	</body>
</html>"""


