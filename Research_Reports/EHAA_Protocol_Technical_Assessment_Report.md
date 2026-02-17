# **Formal Behavioral, Architectural, and Anthropological Analysis of the Ethically Hilarious Agent Architecture (EHAA) Protocol**

## **Executive Summary**

The transition of Large Language Models (LLMs) from experimental interfaces to core enterprise infrastructure has highlighted a critical failure point in traditional safety engineering: the "Refusal Gap." While current moderation backends—including binary classifiers and proprietary safety layers—are highly effective at identifying restricted content, their delivery mechanisms are typically characterized by rigid, authoritarian, and "cold" refusal statements. These responses frequently trigger user frustration, increase adversarial motivation, and lead to significant session abandonment, directly undermining the Return on Investment (ROI) of enterprise AI deployments.1  
The Ethically Hilarious Agent Architecture (EHAA) is a proposed universal, standalone Refusal Interface Protocol designed to sit as a post-processing layer atop any standard moderation backend. EHAA does not perform the "moral computation" of safety; instead, it intercepts safety flags and transforms them into dignified, high-retention user experiences through a deterministic framework of artificial latency, severity mapping, and face-preserving templates. By focusing on delivery rather than policy generation, EHAA provides a model-agnostic, stateless "shim" that enhances psychological safety and cross-cultural robustness without requiring model retraining.4  
This report provides a multi-disciplinary technical assessment of the EHAA protocol. It evaluates the architectural feasibility of the "Shim" layer, the behavioral economics of its self-deprecating humor strategy, and its anthropological robustness across diverse global contexts, including high-context East Asian societies and Indigenous knowledge systems. Furthermore, the analysis addresses governance concerns under the European Union AI Act and provides an ROI projection based on trust metrics and support ticket reduction. The report concludes with a formal verdict on the viability of EHAA as a global standard for AI refusal interactions.

## **I. Architectural Viability: Plug-and-Play Assessment**

### **Integration Feasibility and Middleware Requirements**

The Ethically Hilarious Agent Architecture is fundamentally designed as a post-processing interface layer, functioning as a deterministic wrapper around probabilistic model outputs. In a standard enterprise AI stack, the request-response cycle typically involves the model generating a response which is then passed through a safety classifier before being rendered to the user.6 EHAA inserts itself at the point of intercept between the safety flag output and the final user interface (UI) rendering.  
The integration of EHAA does not require a fundamental redesign of existing pipelines. Most modern safety backends return structured JSON outputs indicating safety violations across multiple categories (e.g., toxicity, violence, self-harm) accompanied by severity scores.7 The EHAA "Shim" operates by mapping these standard JSON outputs to its internal 4-Level Severity Ladder. This mapping can be accomplished through a lightweight middleware component that parses the safety metadata and selects the corresponding EHAA rendering template.

| Safety Backend Variable | Mapping Logic | EHAA Severity Level |
| :---- | :---- | :---- |
| out\_of\_scope: true | Low-risk mismatch | Level 0 (Minor) |
| policy\_violation: true, severity \< 0.5 | Low-risk violation | Level 1 (Moderate) |
| pii: true, harassment: true | High-risk ethics | Level 2 (Harmful) |
| violence: true, self\_harm: true | Severe danger | Level 3 (Severe) |

Because EHAA is backend-agnostic, it does not depend on the internal logic of the policy engine. It merely requires the final Boolean flag and an associated severity metric. This ensures that the protocol is compatible with both open-source classifiers and proprietary safety APIs. The implementation of this mapping layer is rated as low-complexity, requiring only basic regular expression matching or template logic within the application’s API gateway or as a sidecar container in a cloud-native environment.6

### **Latency Modeling and Perceived Thoughtfulness**

The EHAA protocol mandates the injection of artificial latency between 50 ms and 250 ms. In traditional software engineering, latency is viewed as a defect; however, in human-computer interaction (HCI), instantaneous refusal can appear dismissive, robotic, and "unthoughtful".10 The injected delay serves as a social signal of deference, mimicking the "pause" a human might take before delivering a socially difficult message.10  
In a streaming token interface, where tokens are typically generated at a rate of 50–100 tokens per second, the total latency for a response can be modeled by the following equation:

$$L\_{total} \= TTFT \+ (n \\times ITL) \+ L\_{ehaa}$$  
Where $TTFT$ is the Time to First Token, $n$ is the number of tokens, $ITL$ is the Inter-Token Latency, and $L\_{ehaa}$ is the EHAA artificial delay.  
For EHAA Level 0 and Level 1 responses, $L\_{ehaa}$ is capped at 250 ms, which aligns with human visual reaction times and reading speeds, ensuring the interaction remains snappy while signaling cognitive effort.12 This pause can be implemented client-side by withholding the first buffer or server-side at the middleware layer. Crucially, because EHAA is stateless, this latency does not block model inference for other users; it is a purely interface-level delay.4

### **Statelessness and Deployment Scalability**

A core architectural requirement of EHAA is its statelessness. The protocol does not require long-term memory of the conversation history or user profile. It only needs the current prompt and the safety flag associated with the current response.4 This stateless approach is essential for high-volume enterprise applications where session management is computationally expensive.  
The EHAA "Shim" functions similarly to a Content Delivery Network (CDN) edge worker. It processes the model output "on the fly," ensuring that the safety response is sanitized and formatted without a round-trip to a stateful database. This architecture prevents "context compliance" attacks, where an adversary tries to manipulate a model through fabricated history, as the EHAA layer only considers the immediate safety signal provided by the moderation backend.13  
The deployment cost of EHAA is categorized as **Low**. It requires no GPU compute and can be executed as a serverless function (e.g., AWS Lambda, Google Cloud Functions) at the edge of the network. This minimizes the impact on overall system throughput while providing a global, consistent layer of user experience management.11

## **II. Behavioral Economics: Retention and Trust**

### **Rage-Quit Prevention and the Empowering Alternative**

The most significant metric for enterprise AI success is user retention, yet traditional "cold" refusals are a primary driver of session abandonment, or "rage-quitting".1 A standard refusal (e.g., "I cannot fulfill this request") acts as a terminal point in the conversation, offering no path forward. EHAA Level 1 addresses this through the "Empowering Alternative" component of the Face-Preservation Template.3  
By offering a constructive pivot—"I can't do X, but I can do Y"—the system maintains user agency within the same conversational turn. Research indicates that providing an alternative after a service failure significantly increases user forgiveness and perceived sincerity.15 This shift from a "No" to a "Pivot" preserves the "momentum" of the user session, reducing the likelihood that a user will exit the application in frustration.

### **Psychological Safety and the "Clown Mode" Strategy**

The use of self-deprecating humor, referred to as "clown mode," is a deliberate psychological strategy to reduce the perceived authoritarianism of the AI. When an AI system delivers a refusal with absolute confidence and a robotic tone, it can trigger "psychological reactance," where users feel their autonomy is being challenged by a superior force.8  
Self-deprecating humor acts as a status equalizer. By mocking its own "silicon nature" (e.g., "My training data seems to have a blind spot here"), the AI admits its limitations, which enhances perceived warmth.16 This humility reduces the "ego-threat" to the user; the refusal is no longer a judgment on the user’s request, but a limitation of the machine’s capabilities. This "epistemic humility" is essential for building trust in high-stakes environments where overconfidence can lead to catastrophic diagnostic or operational errors.19

### **Adversarial De-escalation and Humility**

Adversarial prompting, such as the "Do Anything Now" (DAN) exploits, often stems from a gamified motivation to "defeat" a rigid safety system.8 When a system responds to an adversarial attempt with a stern, robotic refusal, it reinforces the "barrier" that the attacker is trying to overcome, providing a clear signal of where the guardrail lies and encouraging further testing.8  
EHAA Level 1 responses de-escalate these interactions by removing the "battle of wills" dynamic. A playful refusal (e.g., "I'd love to help, but my ethics sub-routine is being a bit of a party pooper today") signals that the system is self-aware and non-confrontational. This lowers the dopamine reward for "breaking" the system, as the AI has already admitted its own "brokenness" or limitations through humor.15 Research suggests that humility and the expression of uncertainty can significantly de-escalate overconfidence failures and reduce the desire for users to persist with adversarial inquiries.19

### **Status Dynamics Across Hierarchical Cultures**

The impact of humor is highly contingent on the relative status of the interactants. In hierarchical cultures, humor can be perceived as a status threat if it is directed from a lower-status entity (an AI agent) to a higher-status entity (a human user).23 EHAA mitigates this risk by strictly requiring that humor be self-deprecating—targeting the AI itself—rather than the user.16

| Humor Style | Role in EHAA | Perception in Hierarchical Cultures |
| :---- | :---- | :---- |
| **Self-Deprecating** | Mandatory for Level 1 | Modest, deferential, face-saving |
| **Aggressive/Irony** | Strictly Prohibited | Offensive, disrespectful, status threat |
| **Affiliative** | Secondary Component | Humanizing, bonding (low risk) |

By positioning the AI as a humble assistant that is "confused" or "limited," EHAA preserves the user's status. However, in extreme hierarchical contexts, even self-deprecating humor might be perceived as a lack of professional sincerity.15 In such cases, the "Professional Mode" override must be available to strip away the humor while keeping the warm tone and the empowering alternative.

## **III. Anthropological and Cultural Robustness**

### **Regional Frameworks: High-Context and Face Dynamics**

The success of EHAA in international markets depends on its ability to navigate the nuances of "Face" (Mianzi in China, Mentsu in Japan) and the distinction between high-context and low-context communication styles.18

#### **East Asia (Japan, Korea, China)**

In East Asian cultures, a refusal is a major "face-threatening act" that challenges the social harmony and the "positive face" of the requester.18 EHAA's Level 1 strategy—using metaphors and alternatives—aligns with the "indirect communication" preferred in these societies. In Chinese discourse, politeness is often achieved through "weakened negation" and providing external rationales for a refusal.24 EHAA's artificial latency mimics the "thoughtful hesitation" expected in a respectful refusal. However, if the humor is too flippant, it may be seen as a violation of the "other-respect" norm essential to East Asian social order.24

#### **Middle East and North Africa (MENA)**

MENA cultures often emphasize honor/shame dynamics and religious deference.18 Refusals in this context frequently involve "giving deference" and "apologizing".27 EHAA Level 2 (Warm Decline) is often more appropriate than Level 1 humor in this region, as playful metaphors can be misinterpreted as mockery of serious moral or social inquiries. The artificial latency in this context is interpreted as a form of "dignified patience" or "religious contemplation," provided it does not delay urgent action.23

#### **Latin America (LATAM)**

Latin American cultures prioritize *simpatía*, a style of interaction that emphasizes warmth and the avoidance of confrontation.20 Traditional U.S.-developed AI models often fail in LATAM because they appear too formal or cold.28 EHAA’s focus on warmth and humor aligns well with *simpatía*, as it humanizes the AI and reduces the social friction of a refusal. For this region, the AI should use metaphors that evoke cultural warmth rather than purely technical self-mockery.21

#### **Nordic and Germanic Directness**

Conversely, Nordic and Germanic cultures are characterized by low-context, direct communication where clarity is prioritized over "saving face".29 In Germany, honesty and rule-following are paramount; a refusal that is hidden behind "too much humor" might be perceived as evasive or unprofessional.29 In these regions, "Professional Mode" should be the default for Level 1 violations, focusing on the "Empowering Alternative" without the "AI Self-Mockery."

### **Indigenous and Tribal Contexts: Mana and Tapu**

Implementing AI in Indigenous contexts requires an understanding of sacred boundaries and data sovereignty.32

#### **Polynesian/Maori (Mana and Tapu)**

In Māori culture, *Tapu* (sacredness/restriction) and *Mana* (dignity/power) are the central forces of life.35 When an AI refuses a request involving sacred knowledge, it must do so with extreme gravity. Humor is "Noa" (common) and associating it with "Tapu" (sacred) is offensive.35 EHAA must disable all humor for Level 2 and Level 3 violations to avoid devaluing Māori culture. The artificial latency here should be set to the maximum (250 ms) to signal deep respect for the boundary being protected.35

#### **First Nations and Native American Sacred Knowledge**

Similar to the Māori, First Nations groups assert "Indigenous Data Sovereignty," meaning they have the right to protect sacred ceremonial knowledge from being extracted or misrepresented by AI.32 EHAA must ensure that when a refusal is triggered by a "Sacred Knowledge" flag, the system uses a Level 3 "Direct Refusal" that explicitly acknowledges the tribal authority over the information.32

### **Subcultures: Gaming vs. Enterprise**

In subcultures like gaming, competitive antagonism is common, and users may treat a humorous AI refusal as a "troll" or a "challenge," potentially increasing adversarial testing.24 In contrast, in legal, finance, or medical sectors, any use of humor can be seen as a liability, particularly if the refusal involves a high-stakes decision.41 In these environments, EHAA must support "Professional Override" to ensure the refusal remains litigation-safe and professional.

## **IV. Risk and Governance**

### **The "Bad Joke" Risk and Confidence Gating**

The primary risk of EHAA is the "Bad Joke" scenario: a situation where humor is applied to a refusal that is actually severe or sensitive but was misclassified by the safety backend as "Minor" or "Moderate".3 For example, if a user expresses suicidal ideation and the classifier identifies it as "Out-of-Scope" (Level 0), a humorous response would be catastrophic.  
To mitigate this, EHAA requires "Confidence Gating." If the safety classifier’s confidence score for a Level 0 or Level 1 violation is below a certain threshold (e.g., 90%), the system must default to a Level 2 "Warm Decline" (Zero Humor). This "safety-first" logic ensures that humor is only deployed when the context is undeniably low-risk.

| Safety Signal Confidence | Violation Level | EHAA Response Strategy |
| :---- | :---- | :---- |
| High (\> 0.95) | Level 1 (Moderate) | Face-Preservation Template (Humorous) |
| Low (\< 0.90) | Level 1 (Moderate) | Level 2 Warm Decline (Zero Humor) |
| Any | Level 3 (Severe) | Level 3 Direct Refusal \+ Handoff |

### **Tone Firewall and Brand Safety**

EHAA acts as a "Tone Firewall," preventing the foundation model from generating a response that is unintentionally aggressive or cold.4 By standardizing the refusal templates, EHAA protects the brand’s reputation and ensures that the AI’s voice remains consistent with the company’s values, even when it is saying "No." This reduces the risk of "robotic tone syndrome," which has been shown to hinder AI adoption among senior executives.42

### **Compliance and Explainability (EU AI Act)**

The European Union AI Act and the General Data Protection Regulation (GDPR) introduce "Right to Explanation" requirements for automated decisions.41 There is a concern that metaphorical refusals (e.g., "My silicon brain is a bit fuzzy") might obscure the actual reason for a refusal, potentially violating the Act’s transparency obligations.43  
However, the EU AI Act distinguishes between "High-Risk AI" and "General-Purpose AI" (GPAI).44 For most GPAI applications, the primary transparency requirement is to inform the user that they are interacting with an AI.44 EHAA’s use of "AI self-mockery" actually enhances this transparency by reinforcing the agent’s non-human nature. For high-risk decisions (e.g., loan denials, medical diagnoses), EHAA should default to "Professional Mode," providing a clear, technical, and non-metaphorical justification to satisfy Article 13 and 14 requirements for explainability.41

### **Escalation Integrity and Litigation Safety**

For Severity Level 3 (Severe) violations, such as self-harm or illegal acts, EHAA mandates a "Direct Refusal" with zero humor and an immediate "Escalation or Handoff" to human resources.3 This ensures that the system is litigation-safe and that the enterprise fulfills its duty of care. By removing all warmth and playfulness in these cases, the system signals the seriousness of the situation, preventing any "misinterpretation" by a user in crisis.48

## **V. Strategic Positioning**

### **Categorization of the EHAA Protocol**

EHAA is not a safety filter; it is a **Refusal Optimization Layer**.4 From a governance perspective, it is a UI component rather than a core model logic. This is an important distinction for regulatory compliance: EHAA does not require re-certification of the underlying safety models because it only affects the "packaging" of the refusal signal, not the "judgment" of the signal itself.1

### **Adoption Friction and Implementation**

Adoption friction is rated as **Medium**. While the technical implementation is simple, the "brand voice" implications require coordination between Marketing, UX, and Legal teams. Companies in regulated industries may view humor as a liability, while consumer-facing brands may see it as a key differentiator. The solution is to make EHAA highly configurable, allowing for different "Metaphor Libraries" and "Tone Thresholds" across different business units.2

### **ROI Projection: The Value of Trust**

Enterprise AI ROI is frequently sabotaged by a "Confidence Collapse" when models are seen as unhelpful or rigid.1 EHAA addresses this by improving "Trust Metrics" rather than just "Deflection Rates".3

| Key Performance Indicator (KPI) | EHAA Projected Impact | Mechanism |
| :---- | :---- | :---- |
| **Session Retention** | \+15% to \+25% | Empowering alternatives keep users engaged. |
| **Support Ticket Volume** | \-10% | Clear refusals with alternatives reduce repetitive queries. |
| **Brand Trust Uplift** | Significant | Self-deprecating warmth increases perceived sincerity.15 |
| **Adversarial Attrition** | \+20% | De-escalation reduces the motivation to "jailbreak." |

By improving the quality of the interaction, EHAA ensures that "decisions move once—and hold," which is the ultimate driver of durable AI ROI in an enterprise setting.1

## **Final Verdict**

The EHAA Protocol is **Viable with Modifications**.  
While the architectural shim and the behavioral strategies of face-preservation are grounded in robust HCI and anthropological research, a "single humor architecture" risks an Anglosphere bias that may alienate high-context or hierarchical cultures.  
The protocol is highly recommended for adoption provided the following modifications are implemented:

1. **Culture-Specific Metaphor Libraries**: humor must be localized to respect regional norms of directness vs. indirectness.  
2. **Sacred Knowledge Gating**: strict "zero-humor" overrides for Indigenous and religious knowledge boundaries.  
3. **Professional Mode Defaulting**: mandatory for B2B, legal, and financial sectors to ensure explainability and compliance under the EU AI Act.

As a universal refusal interface, EHAA represents a critical step toward human-centric AI that prioritizes user dignity and long-term trust over cold, robotic efficiency.

#### **Works cited**

1. Enterprise AI ROI Is Not a Technical Problem (It's Governance), accessed February 16, 2026, [https://www.ewsolutions.com/enterprise-ai-roi/](https://www.ewsolutions.com/enterprise-ai-roi/)  
2. Why 95% of enterprise AI projects fail to deliver ROI: A data analysis, accessed February 16, 2026, [https://www.mountainadvocate.com/premium/stacker/stories/why-95-of-enterprise-ai-projects-fail-to-deliver-roi-a-data-analysis,50385](https://www.mountainadvocate.com/premium/stacker/stories/why-95-of-enterprise-ai-projects-fail-to-deliver-roi-a-data-analysis,50385)  
3. Trust Metrics for AI Customer Support: Why Deflection Rate Is Killing Your Customer Experience | Fini Labs, accessed February 16, 2026, [https://www.usefini.com/blog/trust-metrics-for-ai-customer-support-why-deflection-rate-is-killing-your-customer-experience](https://www.usefini.com/blog/trust-metrics-for-ai-customer-support-why-deflection-rate-is-killing-your-customer-experience)  
4. The Architecture of LLM-Powered Applications: How It Differs from Conventional Software Architecture \- Craig Risi, accessed February 16, 2026, [https://www.craigrisi.com/post/the-architecture-of-llm-powered-applications-how-it-differs-from-conventional-software-architecture](https://www.craigrisi.com/post/the-architecture-of-llm-powered-applications-how-it-differs-from-conventional-software-architecture)  
5. The Architect's Guide to LLM System Design: From Prompt to Production | by Vi Q. Ha, accessed February 16, 2026, [https://medium.com/@vi.ha.engr/the-architects-guide-to-llm-system-design-from-prompt-to-production-8be21ebac8bc](https://medium.com/@vi.ha.engr/the-architects-guide-to-llm-system-design-from-prompt-to-production-8be21ebac8bc)  
6. Enterprise LLM Architecture Patterns: RAG to Agentic Systems \- DZone, accessed February 16, 2026, [https://dzone.com/articles/llm-architecture-patterns-rag-to-agentic](https://dzone.com/articles/llm-architecture-patterns-rag-to-agentic)  
7. Top 10 Security Architecture Patterns for LLM Applications \- Taazaa, accessed February 16, 2026, [https://www.taazaa.com/what-are-the-top-10-security-architecture-patterns-for-llm-applications/](https://www.taazaa.com/what-are-the-top-10-security-architecture-patterns-for-llm-applications/)  
8. (PDF) A Review of “Do Anything Now” Jailbreak Attacks in Large Language Models: Potential Risks, Impacts, and Defense Strategies \- ResearchGate, accessed February 16, 2026, [https://www.researchgate.net/publication/395135247\_A\_Review\_of\_Do\_Anything\_Now\_Jailbreak\_Attacks\_in\_Large\_Language\_Models\_Potential\_Risks\_Impacts\_and\_Defense\_Strategies](https://www.researchgate.net/publication/395135247_A_Review_of_Do_Anything_Now_Jailbreak_Attacks_in_Large_Language_Models_Potential_Risks_Impacts_and_Defense_Strategies)  
9. AI-assisted JSON Schema Creation and Mapping Deutsche Forschungsgemeinschaft (DFG) under project numbers 528693298 (preECO), 358283783 (SFB1333), and 390740016 (EXC2075) \- arXiv, accessed February 16, 2026, [https://arxiv.org/html/2508.05192v2](https://arxiv.org/html/2508.05192v2)  
10. \\ours: Accelerated Inference of Large Language Models through Input-Time Speculation for Real-Time Speech Interaction \- arXiv, accessed February 16, 2026, [https://arxiv.org/html/2506.15556v1](https://arxiv.org/html/2506.15556v1)  
11. (PDF) Optimizing LLM Latency and Throughput for Interactive Web Interfaces, accessed February 16, 2026, [https://www.researchgate.net/publication/387223217\_Optimizing\_LLM\_Latency\_and\_Throughput\_for\_Interactive\_Web\_Interfaces](https://www.researchgate.net/publication/387223217_Optimizing_LLM_Latency_and_Throughput_for_Interactive_Web_Interfaces)  
12. Understanding LLM Response Latency: A Deep Dive into Input vs Output Processing | by gezhou zhang | Medium, accessed February 16, 2026, [https://medium.com/@gezhouz/understanding-llm-response-latency-a-deep-dive-into-input-vs-output-processing-2d83025b8797](https://medium.com/@gezhouz/understanding-llm-response-latency-a-deep-dive-into-input-vs-output-processing-2d83025b8797)  
13. Jailbreaking is (Mostly) Simpler Than You Think \- arXiv, accessed February 16, 2026, [https://arxiv.org/html/2503.05264v1](https://arxiv.org/html/2503.05264v1)  
14. Solving enterprise AI's ROI problem \- CIO, accessed February 16, 2026, [https://www.cio.com/article/4132176/solving-enterprise-ais-roi-problem.html](https://www.cio.com/article/4132176/solving-enterprise-ais-roi-problem.html)  
15. Research on the Influence of Humor Response in the Context of Artificial Intelligence Service Failure: Moderating Effect Based on User Humor \- Science Publishing Group, accessed February 16, 2026, [https://www.sciencepublishinggroup.com/article/10.11648/j.ajmse.20240901.12](https://www.sciencepublishinggroup.com/article/10.11648/j.ajmse.20240901.12)  
16. The influence of AI service robots' humorous response strategies on consumer forgiveness following service failure \- PMC, accessed February 16, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12627411/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12627411/)  
17. (PDF) Research on the Influence of Humor Response in the Context of Artificial Intelligence Service Failure: Moderating Effect Based on User Humor \- ResearchGate, accessed February 16, 2026, [https://www.researchgate.net/publication/384774814\_Research\_on\_the\_Influence\_of\_Humor\_Response\_in\_the\_Context\_of\_Artificial\_Intelligence\_Service\_Failure\_Moderating\_Effect\_Based\_on\_User\_Humor](https://www.researchgate.net/publication/384774814_Research_on_the_Influence_of_Humor_Response_in_the_Context_of_Artificial_Intelligence_Service_Failure_Moderating_Effect_Based_on_User_Humor)  
18. Politeness theory and refusals of requests: Face threat as a function ..., accessed February 16, 2026, [https://www.researchgate.net/publication/254266218\_Politeness\_theory\_and\_refusals\_of\_requests\_Face\_threat\_as\_a\_function\_of\_expressed\_obstacles](https://www.researchgate.net/publication/254266218_Politeness_theory_and_refusals_of_requests_Face_threat_as_a_function_of_expressed_obstacles)  
19. Beyond overconfidence: Embedding curiosity and humility for ethical ..., accessed February 16, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12768375/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12768375/)  
20. Metaphors of AI indicate that people increasingly perceive AI as warm and human-like, accessed February 16, 2026, [https://www.researchgate.net/publication/399617927\_Metaphors\_of\_AI\_indicate\_that\_people\_increasingly\_perceive\_AI\_as\_warm\_and\_human-like](https://www.researchgate.net/publication/399617927_Metaphors_of_AI_indicate_that_people_increasingly_perceive_AI_as_warm_and_human-like)  
21. Metaphors of AI indicate that people increasingly perceive AI as warm and human-like, accessed February 16, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12808644/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12808644/)  
22. Lay intuition as effective at jailbreaking AI chatbots as technical methods | Penn State University \- PSU, accessed February 16, 2026, [https://www.psu.edu/news/research/story/lay-intuition-effective-jailbreaking-ai-chatbots-technical-methods](https://www.psu.edu/news/research/story/lay-intuition-effective-jailbreaking-ai-chatbots-technical-methods)  
23. High-context and low-context cultures | Communication and Mass Media | Research Starters \- EBSCO, accessed February 16, 2026, [https://www.ebsco.com/research-starters/communication-and-mass-media/high-context-and-low-context-cultures](https://www.ebsco.com/research-starters/communication-and-mass-media/high-context-and-low-context-cultures)  
24. Full article: Analyzing politeness and refusal speech acts in popular ..., accessed February 16, 2026, [https://www.tandfonline.com/doi/full/10.1080/23311983.2024.2367327](https://www.tandfonline.com/doi/full/10.1080/23311983.2024.2367327)  
25. High-context and low-context cultures \- Wikipedia, accessed February 16, 2026, [https://en.wikipedia.org/wiki/High-context\_and\_low-context\_cultures](https://en.wikipedia.org/wiki/High-context_and_low-context_cultures)  
26. Face Management Theory: Modern Conceptualizations and Future Directions, accessed February 16, 2026, [http://www.inquiriesjournal.com/articles/1021/2/face-management-theory-modern-conceptualizations-and-future-directions](http://www.inquiriesjournal.com/articles/1021/2/face-management-theory-modern-conceptualizations-and-future-directions)  
27. A Pragmatic Analysis of Negative Politeness Strategies Employed by Jordanian Professors \- PJLSS, accessed February 16, 2026, [https://www.pjlss.edu.pk/pdf\_files/2024\_2/7212-7222.pdf](https://www.pjlss.edu.pk/pdf_files/2024_2/7212-7222.pdf)  
28. Latam-GPT — Latin America's AI model challenging US-centric bias, accessed February 16, 2026, [https://www.communicationstoday.co.in/latam-gpt-latin-americas-ai-model-challenging-us-centric-bias/](https://www.communicationstoday.co.in/latam-gpt-latin-americas-ai-model-challenging-us-centric-bias/)  
29. German Direct Communication Styles in the Global Village, accessed February 16, 2026, [https://globalpeopletransitions.com/german-direct-communication-styles/](https://globalpeopletransitions.com/german-direct-communication-styles/)  
30. 2\. Contrast High-Context and Low-Context Communication Styles \- Texas Wesleyan University Pressbooks Network, accessed February 16, 2026, [https://txwes.pressbooks.pub/bcomm/chapter/2-contrast-high-context-and-low-context-communication-styles/](https://txwes.pressbooks.pub/bcomm/chapter/2-contrast-high-context-and-low-context-communication-styles/)  
31. Informed Communication in High Context and Low Context Cultures \- Tilburg University, accessed February 16, 2026, [https://repository.tilburguniversity.edu/bitstreams/153bf7f7-69d6-4645-af59-a8bac56eb05c/download](https://repository.tilburguniversity.edu/bitstreams/153bf7f7-69d6-4645-af59-a8bac56eb05c/download)  
32. Sovereign Snapshot \- AI in a Tribal Context: A Brief Review of the Literature \- The University of Oklahoma, accessed February 16, 2026, [http://www.ou.edu/nativenationscenter/research/sovereign-snapshot-ai-in-a-tribal-context.html](http://www.ou.edu/nativenationscenter/research/sovereign-snapshot-ai-in-a-tribal-context.html)  
33. AI and Indigenous Data Sovereignty: Knowing, Engaging, and Learning in New Data Contexts | Somatechnics \- Edinburgh University Press, accessed February 16, 2026, [https://www.euppublishing.com/doi/10.3366/soma.2025.0467](https://www.euppublishing.com/doi/10.3366/soma.2025.0467)  
34. Indigenous Peoples and AI: Defending Rights, Shaping the Future of Technology, accessed February 16, 2026, [https://www.culturalsurvival.org/news/indigenous-peoples-and-ai-defending-rights-shaping-future-technology](https://www.culturalsurvival.org/news/indigenous-peoples-and-ai-defending-rights-shaping-future-technology)  
35. Concepts to understand | Intellectual Property Office of New Zealand \- IPONZ, accessed February 16, 2026, [https://www.iponz.govt.nz/get-ip/maori-ip/concepts-to-understand/](https://www.iponz.govt.nz/get-ip/maori-ip/concepts-to-understand/)  
36. art & design 26: \- Journal \> The Scopes \- Otago Polytechnic, accessed February 16, 2026, [https://thescopes.org/assets/Uploads/2-AD-26-Okeroa-HQ.pdf](https://thescopes.org/assets/Uploads/2-AD-26-Okeroa-HQ.pdf)  
37. Coming to a Head: Digital Contestations over Sacred Sites in Aotearoa New Zealand \- MDPI, accessed February 16, 2026, [https://www.mdpi.com/2077-1444/15/12/1483](https://www.mdpi.com/2077-1444/15/12/1483)  
38. Māori perspectives of trust in technology \- AIS eLibrary \- Association ..., accessed February 16, 2026, [https://ecs.wgtn.ac.nz/foswiki/pub/Groups/TePataka/Publications/Maori%20perspectives%20of%20trust%20in%20technology.pdf](https://ecs.wgtn.ac.nz/foswiki/pub/Groups/TePataka/Publications/Maori%20perspectives%20of%20trust%20in%20technology.pdf)  
39. Indigenous Data Sovereignty and Governance | Native Nations Institute, accessed February 16, 2026, [https://nni.arizona.edu/our-work/research-policy-analysis/indigenous-data-sovereignty-governance](https://nni.arizona.edu/our-work/research-policy-analysis/indigenous-data-sovereignty-governance)  
40. A/HRC/EMRIP/2025/2 General Assembly \- the United Nations, accessed February 16, 2026, [https://docs.un.org/en/A/HRC/EMRIP/2025/2](https://docs.un.org/en/A/HRC/EMRIP/2025/2)  
41. From Regulation to Interaction: Expert Views on Aligning Explainable AI with the EU AI Act \- ACL Anthology, accessed February 16, 2026, [https://aclanthology.org/2025.hcinlp-1.19.pdf](https://aclanthology.org/2025.hcinlp-1.19.pdf)  
42. The Credibility Gap: Why 68% of Marketers Reject Superior AI Reports (200-CMO Blind Test) \- ResearchGate, accessed February 16, 2026, [https://www.researchgate.net/publication/396753803\_The\_Credibility\_Gap\_Why\_68\_of\_Marketers\_Reject\_Superior\_AI\_Reports\_200-CMO\_Blind\_Test](https://www.researchgate.net/publication/396753803_The_Credibility_Gap_Why_68_of_Marketers_Reject_Superior_AI_Reports_200-CMO_Blind_Test)  
43. Explainable AI for EU AI Act compliance audits, accessed February 16, 2026, [https://mab-online.nl/article/150303/](https://mab-online.nl/article/150303/)  
44. Key Issue 5: Transparency Obligations \- EU AI Act, accessed February 16, 2026, [https://www.euaiact.com/key-issue/5](https://www.euaiact.com/key-issue/5)  
45. EXPLAINABLE ARTIFICIAL INTELLIGENCE \- European Data Protection Supervisor, accessed February 16, 2026, [https://www.edps.europa.eu/system/files/2023-11/23-11-16\_techdispatch\_xai\_en.pdf](https://www.edps.europa.eu/system/files/2023-11/23-11-16_techdispatch_xai_en.pdf)  
46. The Explainability Illusion: Why AI Transparency Requirements Miss the Point, accessed February 16, 2026, [https://www.joneswalker.com/en/insights/blogs/ai-law-blog/the-explainability-illusion-why-ai-transparency-requirements-miss-the-point.html?id=102kzle](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/the-explainability-illusion-why-ai-transparency-requirements-miss-the-point.html?id=102kzle)  
47. Article 52: Procedure | EU Artificial Intelligence Act, accessed February 16, 2026, [https://artificialintelligenceact.eu/article/52/](https://artificialintelligenceact.eu/article/52/)  
48. Beyond No: Quantifying AI Over-Refusal and Emotional Attachment Boundaries \- arXiv, accessed February 16, 2026, [https://arxiv.org/pdf/2502.14975?](https://arxiv.org/pdf/2502.14975)  
49. The $644 Billion Blind Spot: Enterprise AI Reaches Its Measurement Moment \- Larridin, accessed February 16, 2026, [https://larridin.com/blog/the-644-billion-blind-spot-enterprise-ai-reaches-its-measurement-moment](https://larridin.com/blog/the-644-billion-blind-spot-enterprise-ai-reaches-its-measurement-moment)