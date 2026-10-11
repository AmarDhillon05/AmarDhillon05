# Amar Dhillon

**CS + Statistics @ University of Maryland ('28)**

[![Website](https://img.shields.io/badge/site.adh05.com-111111?style=flat-square)](https://site.adh05.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square)](https://www.linkedin.com/in/amar-dhillon-917537261)

### Now

<table>
<tr>
<td width="50%" valign="top"><b>SWE Intern</b> · Capital One</td>
<td width="50%" valign="top"><b>ML Research</b> · UMIACS, physics-based digital twins</td>
</tr>
<tr>
<td width="50%" valign="top"><b>Contract Engineer</b> · Amazon research project</td>
<td width="50%" valign="top"><b>Co-founder</b> · TerpLabs, a UMD student product studio</td>
</tr>
</table>

### Selected work

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/AmarDhillon05/order-book-playground"><b>order-book-playground</b></a><br>
<sub>C++17 · IEX DEEP+ market data · matching engine</sub>
<p>A limit order book and matching engine built on raw exchange data.</p>
<ul>
<li>With no resync, it agreed with IEX on <b>99,122 of 99,123 fills</b> over 51M messages</li>
<li><b>100 ns p50 / 2.2 µs p99.9</b> per message, timed with <code>rdtscp</code></li>
<li>Compile-time book interface; tested in CI under ASan/UBSan</li>
</ul>
</td>
<td width="50%" valign="top">
<a href="https://github.com/AmarDhillon05/jobs"><b>jobs</b></a><br>
<sub>Python · AWS Lambda, SQS, SNS, DynamoDB · CDK</sub>
<p>A serverless monitor that alerts me when tech internships are posted.</p>
<ul>
<li>Polls <b>92 companies every 10 minutes</b>; push alerts plus an hourly digest</li>
<li><b>~1k tests</b>, <code>cdk synth</code> and <code>cfn-lint</code> in CI</li>
<li>Deploys through GitHub OIDC with no stored AWS keys</li>
</ul>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/AmarDhillon05/timber"><b>timber</b></a><br>
<sub>TypeScript · Expo / Electron · FastAPI · audio ML</sub>
<p>A self-hosted multi-track audio/video editor.</p>
<ul>
<li>One codebase for web, desktop and iOS, with <b>hand-written DSP</b></li>
<li>A phone remote talks to the editor over an SSE relay</li>
<li>Audio models (AST, BEATs, CLAP) suggest per-track mix settings</li>
</ul>
</td>
<td width="50%" valign="top">
<a href="https://github.com/AmarDhillon05/Re.Sell"><b>Re.Sell</b></a><br>
<sub>C++17 · Bayesian inference · on-disk B-tree</sub>
<p>A CLI that tracks and models sneaker resale prices.</p>
<ul>
<li><b>Hamiltonian Monte Carlo written from scratch</b></li>
<li>Tests check gradients against finite differences and posteriors against closed-form results</li>
<li>Local store is a paged B-tree on disk</li>
</ul>
</td>
</tr>
</table>

### Toolbox

<table>
<tr><td><b>Languages</b></td><td>C++ · Python · TypeScript · OCaml</td></tr>
<tr><td><b>Infrastructure</b></td><td>AWS (Lambda, SQS, SNS, DynamoDB, CDK) · GitHub Actions</td></tr>
<tr><td><b>ML &amp; data</b></td><td>PyTorch · Hugging Face · FastAPI · pandas</td></tr>
<tr><td><b>Frontend</b></td><td>React · Next.js · Expo · Electron</td></tr>
</table>

<sub>Off the clock: drums · lifting · golf</sub>
