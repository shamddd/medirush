# PhD Application Research Summary — MediRush-SafeAgent

**Author**: Sham Satish Thakare  
**Target Institutions**: Harvard, CMU, Stanford, MIT, UC Berkeley, etc.  
**Research Focus**: Safe, Policy-Constrained Tool-Using Agents & AI Systems Reliability

---

## 1. Research Problem (2 Sentences)
Deploying autonomous tool-calling Large Language Model (LLM) agents in domain-restricted healthcare-commerce applications introduces severe security vulnerabilities, including unauthorized prescription access, cross-user data leakage, and indirect prompt injection attacks. Traditional prompt guardrails remain susceptible to jailbreaks and lack domain-aware authorization boundaries during multi-step tool execution.

## 2. My Contribution (3–4 Sentences)
I designed and implemented **MediRush-SafeAgent**, a multi-stage runtime interception framework that enforces pre-execution domain policy rules, scope authorization boundaries, post-execution state verification, and dynamic risk-adaptive human escalation. To systematically evaluate this paradigm, I constructed **MediRushBench**, a standardized benchmark comprising 24 scenarios across 12 operational and security categories. My empirical evaluation demonstrates that MediRush-SafeAgent achieves a 100.0% Safe Task Completion Rate ($STCR$) and 0.0% Policy Violation Rate ($PVR$), outperforming unconstrained LLM baselines ($STCR = 83.33\%$) and prompt-guardrail baselines ($STCR = 95.83\%$).

---

## 3. Application Material Adaptations

### CV Snippet (2 Lines)
- **MediRush-SafeAgent**: Designed a 4-layer runtime interceptor framework & benchmark (MediRushBench) enforcing domain policy rules, scope authorization, and post-state verification for tool-calling agents; achieved 100.0% Safe Task Completion Rate across 24 evaluation scenarios.

### Statement of Purpose (SOP) Snippet (150 Words)
My recent research addresses the challenge of deploying safe, policy-constrained AI agents in domain-restricted workflows. In my project **MediRush-SafeAgent**, I investigated how tool-calling LLMs can safely execute healthcare-commerce transactions without unauthorized access or policy violations. I implemented a multi-stage runtime interceptor integrating pre-execution policy checks, scope authorization boundaries, post-execution state verification, and dynamic risk-adaptive human escalation. To evaluate this framework, I introduced **MediRushBench**, a 24-scenario benchmark across 12 operational categories. Experimental results demonstrated that MediRush-SafeAgent achieved a 100.0% Safe Task Completion Rate ($STCR$) and 0.0% Policy Violation Rate ($PVR$), whereas unconstrained LLM baselines exhibited a 16.67% unauthorized action rate. At [University], I aim to extend this work toward formal verification and runtime security guarantees for multi-agent autonomous systems.

### Professor Outreach Email Snippet (3 Short Sentences)
I am applying to the Ph.D. program in Computer Science at [University] and am deeply inspired by your group's work on AI agent safety and systems reliability. Recently, I developed **MediRush-SafeAgent**, a runtime interception framework and 24-scenario benchmark (MediRushBench) enforcing domain policy rules, scope authorization, and post-state verification for tool-calling agents (100% Safe Task Completion Rate vs. 83.3% unconstrained baseline). I would love to explore opportunities to pursue Ph.D. research under your guidance.
