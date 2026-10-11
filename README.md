## Amar Dhillon

CS + Statistics @ University of Maryland ('28). I build systems and then measure whether they're right: market microstructure, cloud infrastructure, applied ML.

Looking for **Summer 2027** internships in **software engineering** and **quant development**.

[Website](https://site.adh05.com) · [LinkedIn](https://www.linkedin.com/in/amar-dhillon-917537261) · [Resume](RESUME_LINK) · EMAIL

### Now

- **SWE Intern** @ Capital One
- **Contract engineer** on an Amazon research project
- **ML research** @ UMIACS: physics-based digital twins
- **Co-founder** @ TerpLabs, a UMD student product studio

### Selected work

**[order-book-playground](https://github.com/AmarDhillon05/order-book-playground)**: a limit order book and matching engine in C++17, built on raw IEX DEEP+ exchange data
- With no resync, the engine agreed with IEX on **99,122 of 99,123 fills over 51M messages**
- First-pass `std::map` book: **100 ns p50 / 2.2 µs p99.9** per message, timed with `rdtscp` histograms against a null-book floor
- Compile-time book interface (no virtual dispatch), share-conservation checks, and handling for gaps in the feed

**[jobs](https://github.com/AmarDhillon05/jobs)**: a serverless internship monitor on AWS (Lambda, SQS, SNS, DynamoDB, CDK)
- Polls 92 companies every 10 minutes and sends push alerts plus an hourly digest
- CI runs lint, type checks, ~1k tests, `cdk synth` and `cfn-lint`, and deploys through OIDC with no stored keys

**[timber](https://github.com/AmarDhillon05/timber)**: a self-hosted multi-track audio/video editor
- Expo app for web, desktop and iOS, with hand-written DSP and a phone remote that talks to it over an SSE relay
- A Python service runs audio models (AST, BEATs, CLAP) to suggest per-track mix settings

**[Re.Sell](https://github.com/AmarDhillon05/Re.Sell)**: a C++ CLI that models sneaker resale prices
- Hamiltonian Monte Carlo sampler written from scratch, with tests that check gradients against finite differences and posteriors against analytic results

### Toolbox

C++ · Python · TypeScript · OCaml · AWS (CDK, Lambda, DynamoDB) · PyTorch · FastAPI · React / Expo

Off the clock: drums (funk, jazz fusion, metal), lifting, golf.
