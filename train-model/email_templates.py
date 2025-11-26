PROMPT_LIST = [
    {
        "id": 1,
        "style": "The '3 C's' Cold Email",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: We are initiating first contact to pitch our high-ticket service.
Rule from Book: Apply the '3 C's' concept.

Compliment: A hyper-specific observation about {company} or {title}'s recent work (must not sound like a stalker, keep it professional).

Case Study: A one-sentence proof point where we helped a similar client in {industry} achieve {value}.

Call to Action: A binary 'yes/no' question.
Strict Tone: Senior VP. Brief, confident, and direct. No fluff.
Structure:

Subject line: Use the book's recommended standard: 'Quick Question'.

Opening: The specific compliment.

Core: The one-sentence case study.

CTA: The 'Simple Ask' (e.g., 'Interested? Let me know...').

Generate the email.
"""
    },
    {
        "id": 2,
        "style": "The 'Big Win' Follow-Up",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect did not reply to our initial cold email sent 3 days ago.
Rule from Book: Apply the 'Big Win' concept. Do not check in. Instead, announce a massive recent win with a recognizable name as if it is major news.
Strict Tone: Excited but professional. Concise.
Structure:

Subject line: (Keep same thread).

Opening: Jump straight into the news.

Core: 'We just helped a major {industry} competitor break {value} on their project.'

CTA: 'Would still love to help {company} grow. Let me know and I can send over some times.'

Generate the email.
"""
    },
    {
        "id": 3,
        "style": "The Break-Up Email",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: We have sent 3 emails with no response. We are closing the file.
Rule from Book: Apply the 'Break-Up' concept. State clearly that you are assuming this isn't a priority and you are moving on.
Strict Tone: Professional detachment. No passive aggression.
Structure:

Subject line: (Keep same thread).

Opening: State the assumption that fixing {pain} isn't a priority for them right now.

Core: Ask them to let you know if that changes in the future.

CTA: None (The statement of withdrawal is the implicit CTA).

Generate the email.
"""
    },
    {
        "id": 4,
        "style": "The Hyper-Specific Offer",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: We are pitching a specialized technical service, not a commodity.
Rule from Book: Apply the 'Specific Offer' concept. Do not say we offer 'services.' Say we solve {pain} for {industry}.
Strict Tone: Expert-to-Expert. Direct.
Structure:

Subject line: 'Quick Question'.

Opening: Acknowledge their current tech stack or situation (e.g., 'Noticed you are still using old tech').

Core: Mention we have an upgrade package/solution specifically for companies like {company} to avoid {pain}.

CTA: 'Mind if I send over a few times to chat?'

Generate the email.
"""
    },
    {
        "id": 5,
        "style": "The 'Simple Ask' CTA",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: We have drafted the body of a cold email pitching {value}, but need the closing mechanism.
Rule from Book: Apply the 'Simple Ask' CTA. Do not ask for a 15-minute call. Do not ask them to click a link.
Strict Tone: Casual confidence.
Structure:

Core: Brief recap of value (1 sentence).

CTA: Use the exact phrasing style: 'Interested? Let me know and I can send over a few times to chat.'

Generate the closing segment of the email.
"""
    },
    {
        "id": 6,
        "style": "The 'Specific Benefit' CTA",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: We are pitching {value} which helps companies generate results.
Rule from Book: Apply the 'Specific Benefit' CTA. The question must include the variable payoff.
Strict Tone: Direct.
Structure:

Core: (Assume case study was just presented).

CTA: 'Are you interested in {value} for {company}? Let me know and I can send over a few times to chat.'

Generate the closing segment.
"""
    },
    {
        "id": 7,
        "style": "The 'Bumping This Up' Follow-Up",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: It has been 3 days since our first email. No reply.
Rule from Book: Apply the 'Simple Bump' concept. Do not pitch again. Do not add new info.
Strict Tone: Professional brevity.
Structure:

Subject line: (Keep same thread).

Body: A single sentence acknowledging they are busy and bringing the previous email to the top of their inbox.

CTA: Implicit (waiting for reply to previous email).

Generate the email.
"""
    },
    {
        "id": 8,
        "style": "The 'Dream Job' Coffee Chat",
        "text": """
Act as a specific Senior Candidate. You are writing to a {title} at {company}.
Context: You want a job there, but you are bypassing HR to go straight to the decision-maker.
Rule from Book: Apply the 'Dream Job' outreach. Do not ask for a job. Ask for 3-5 questions about their experience working there.
Strict Tone: Ambitious but respectful.
Structure:

Subject line: '{title} Question'.

Opening: Specific compliment on their career or a shared interest (e.g., Twitter bio).

Core: State you are on a quest for your dream job and admire {company}. Ask for a brief chat to ask questions about their experience.

CTA: Offer specific times (e.g., Thursday at 10am).

Generate the email.
"""
    },
    {
        "id": 9,
        "style": "The Podcast Guest Pitch",
        "text": """
Act as a Senior Thought Leader. You are writing to {title} of {company}.
Context: You want to appear as a guest on their show.
Rule from Book: Apply the 'Fan of the Show' pitch.

Prove you listen (mention a specific interview).

Offer value (list 3 specific topics you can discuss that fit their audience).
Strict Tone: Peer-to-Peer. Helpful.
Structure:

Subject line: 'Quick Question'.

Opening: Praise a specific recent interview with a guest.

Core: Introduce yourself briefly and propose 3 bullet points of unique insights you can share with their listeners.

CTA: 'Does that sound interesting? Happy to workshop some ideas.'

Generate the email.
"""
    },
    {
        "id": 10,
        "style": "The 'Better Alternative' Backlink Pitch",
        "text": """
Act as a Founder/CMO. You are writing to a {title}.
Context: They wrote an article linking to a competitor tool. We have a better version.
Rule from Book: Apply the 'Better Alternative' backlink strategy. Frame the request as helping them update their content for their readers.
Strict Tone: Helpful and appreciative.
Structure:

Subject line: 'Quick Question'.

Opening: Compliment the article about {industry}.

Core: Notice they linked to a competitor tool. Mention you built a better alternative, {value}, which fixes {pain}.

CTA: 'If you find it helpful, it would mean the world if you shared it.'

Generate the email.
"""
    },
    {
        "id": 11,
        "style": "The 'No-Brainer' Performance Offer",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You are a new agency and need to close deals quickly to build case studies.
Rule from Book: Apply the 'No-Brainer Offer' concept. Tie the offer to a monetary goal with a full risk reversal (money-back guarantee or performance-only).
Strict Tone: Confident and transactional.
Structure:

Subject line: 'Quick Question'.

Opening: Acknowledge a specific recent win or ad campaign of theirs.

Core: Propose to manage their {pain} for 30 days. State explicitly: 'If we don't find/generate {value}, we refund our fee/you don't pay.'

CTA: 'But if we do, let's scale. Interested?'

Generate the email.
"""
    },
    {
        "id": 12,
        "style": "The 'Specific Time Slots' Booking",
        "text": """
Act as a Senior Sales Executive. You are writing to an interested {title}.
Context: They replied 'Yes' or 'Tell me more' to your cold email. You need to book the call.
Rule from Book: Apply the 'Specific Times' rule. Do not send a booking link. Do not ask 'When are you free?'.
Strict Tone: Efficient and accommodating.
Structure:

Opening: 'Great/Sure thing.'

Core: Offer 2 specific windows: 'I'm free next week on Tuesday and Thursday between afternoon EST.'

CTA: 'Would either of those work for you?'

Generate the email.
"""
    },
    {
        "id": 13,
        "style": "The 'Pre-Meeting' Reminder",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title}.
Context: You have a scheduled sales call starting in 5 minutes.
Rule from Book: Apply the '5-Minute Warning' technique. Keep it extremely short.
Strict Tone: Casual and helpful.
Structure:

Subject line: (Reply to the calendar invite or previous thread).

Body: 'Talk to you in five minutes! Here is the link: [Link]'

CTA: None.

Generate the email.
"""
    },
    {
        "id": 14,
        "style": "The 'On The Line' Nudge",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title}.
Context: You are sitting in the Zoom room. They are 5 minutes late.
Rule from Book: Apply the 'On The Line' protocol. Inform them you are waiting politely.
Strict Tone: Patient but firm.
Structure:

Subject line: (Reply to previous thread).

Body: State you are on the line when they are ready.

CTA: Implicit.

Generate the email.
"""
    },
    {
        "id": 15,
        "style": "The No-Show Reschedule (Voicemail Script)",
        "text": """
Act as a Senior Sales Executive. You are calling a {title}.
Context: They ghosted the meeting. You are leaving a voicemail.
Rule from Book: Apply the 'No Show Voicemail' script. Be direct about the missed time and the next step.
Strict Tone: Professional accountability.
Structure:

Opening: Identify yourself and the missed time ('We were supposed to talk 5 minutes ago').

Action: 'I'll send you an email to reschedule.'

Closing: 'Thanks.'

Generate the voicemail script text.
"""
    },
    {
        "id": 16,
        "style": "The 'No-Show' Breakup",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title}.
Context: They have failed to show up for a meeting on three separate occasions.
Rule from Book: Apply the 'No-Show Breakup' strategy. Assume now is not a good time for them and stop following up.
Strict Tone: Final and indifferent.
Structure:

Opening: 'I guess now is not a good time to discuss {value} for you.'

Core: Tell them they can get in touch via the number in your signature if they are still interested later.

CTA: None (Sign off).

Generate the email.
"""
    },
    {
        "id": 17,
        "style": "The 'Competitor' Social Proof",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You previously delivered a big win for a competitor, their direct rival.
Rule from Book: Apply the 'Competitor Case Study' concept. Frame the competitor's success as a roadmap for their success.
Strict Tone: authoritative and provocative.
Structure:

Subject line: 'Quick Question'.

Opening: Compliment a specific product line at {company}.

Core: 'Recently, we helped a competitor close {value} in new contracts by using our service.'

CTA: 'Would love to do the same for you. Let's talk?'

Generate the email.
"""
    },
    {
        "id": 18,
        "style": "The 'Agency Partner' Pitch",
        "text": """
Act as an Agency Founder. You are writing to the Owner of {company}.
Context: You are starting a new agency and want to white-label their services or form a referral partnership.
Rule from Book: Apply the 'Borrowing Case Studies' strategy. Pitch partnership, not a sale.
Strict Tone: B2B Partnership.
Structure:

Subject line: 'Partnering with {company}?'

Opening: Praise their work on a specific client project.

Core: State you are building a sales arm for {industry} and need a fulfillment partner who can deliver high-quality {value}.

CTA: 'Open to a chat about sending you deals?'

Generate the email.
"""
    },
    {
        "id": 19,
        "style": "The 'Hero Interview' Invite",
        "text": """
Act as a Podcast Host/Founder. You are writing to {title}.
Context: You want to build a relationship with this high-level person by interviewing them.
Rule from Book: Apply the 'Hero Invite' strategy. Compliment them on how they changed your life/business, then offer the platform.
Strict Tone: Admiring but professional (not fanboy).
Structure:

Subject line: 'Quick question'.

Opening: 'Big fan of your content. You basically changed my life when you said something inspiring.'

Core: Invite them to your podcast to share their story with your audience of {industry}.

CTA: 'Want to do an interview? Let me know and I can send over a few times.'

Generate the email.
"""
    },
    {
        "id": 20,
        "style": "The 'Closing' Question",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title}.
Context: You have completed the sales call/demo and sent the proposal. You need to trigger the close.
Rule from Book: Apply the 'Simple Close' technique.
Strict Tone: Expectant and confident.
Structure:

Subject line: 'getting started'.

Body: A single sentence asking if they are ready to proceed.

Phrase: Use the exact phrase: 'Are you guys ready to get started?'

Generate the email.
"""
    },
    {
        "id": 21,
        "style": "The 'Existing Client' Upsell",
        "text": """
Act as an Agency Owner. You are writing to an existing client, {company}.
Context: You have a new service or upgrade (e.g., {value}) that is critical for them.
Rule from Book: Apply the 'Magento Case Study' structure.

Compliment: Praise their recent business growth or specific usage of your previous work.

The Trigger: Mention a specific external factor (e.g., software depreciation, security risk) that necessitates action.

The Solution: Pitch your specific upgrade package.
Strict Tone: Consultative and urgent.
Structure:

Subject line: 'Quick Question'.

Opening: 'Long time no speak, love how your business has been growing...'

Core: 'Just noticed your site is still using {pain}. This means {pain}. We have an upgrade package...'

CTA: 'Mind if I send over a few times to chat?'

Generate the email.
"""
    },
    {
        "id": 22,
        "style": "The 'Executive Summary' Proposal Delivery",
        "text": """
Act as a Senior Sales Executive. You are writing to {title}.
Context: You are sending the contract/proposal immediately after a successful call.
Rule from Book: Apply the 'Executive Summary' concept. The email body must summarize the 'Deliverables' and 'Timeline' discussed on the call.
Strict Tone: Professional and assumptive (assume the close).
Structure:

Subject line: '{value} Proposal'.

Opening: 'Great chatting earlier.'

Core: 'As discussed, we will deliver {value} by next month to help you achieve {value}.'

Pricing Recap: 'Cost is $5000 upfront.'

CTA: 'Link to sign is attached. Let me know when you have signed and we will start.'

Generate the email.
"""
    },
    {
        "id": 23,
        "style": "The 'Top-Down' Referral (CEO Outreach)",
        "text": """
Act as a Senior Sales Executive. You are writing to the CEO of {company}.
Context: You want to sell {value} to their marketing department, but you are starting at the top.
Rule from Book: Apply the 'Top-Down' strategy. Keep it high-level so the CEO can easily forward it to the right person.
Strict Tone: Peer-to-Peer.
Structure:

Subject line: 'Quick Question'.

Opening: Custom compliment on a recent company milestone (IPO, funding, acquisition).

Core: 'We helped a {industry} competitor achieve {value}. I suspect the Marketing Director is the right person to speak to about this.'

CTA: 'Mind pointing me in their direction?'

Generate the email.
"""
    },
    {
        "id": 24,
        "style": "The 'SaaS Idea' Validation (The Fix)",
        "text": """
Act as a SaaS Founder. You are writing to a {title}.
Context: You have a beta product or just an idea. You need to validate if people will pay for it.
Rule from Book: Apply the 'Validation Fix.' Do not ask for 'thoughts.' Pitch a low-cost subscription to solve a specific pain point immediately.
Strict Tone: Direct.
Structure:

Subject line: 'Quick Question'.

Opening: 'I built a tool that gives you {value} for {company}.'

Core: 'It starts at $99 a month, and you can get {value} to save {pain}.'

CTA: 'Interested?'

Generate the email.
"""
    },
    {
        "id": 25,
        "style": "The 'Influencer' Recruiting Pitch",
        "text": """
Act as a Agency CEO. You are writing to {title}, a sales trainer or guru.
Context: You need to hire a commission-only salesperson and want access to their top students.
Rule from Book: Apply the 'Influencer Recruiting' strategy. Leverage their authority to find talent.
Strict Tone: Respectful but business-focused.
Structure:

Subject line: 'Quick Question'.

Opening: 'Big fan of your course/content on {industry}.'

Core: 'We are looking for a hungry sales killer to close deals for our agency. Figure you might know an up-and-comer in your audience looking for a break.'

CTA: 'Anyone come to mind?'

Generate the email.
"""
    },
    {
        "id": 26,
        "style": "The 'Discovery Questions' Pre-Sell",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: They are interested but too busy for a call. You agreed to send questions via email.
Rule from Book: Apply the 'Doctor's Diagnosis' questions via text.
Strict Tone: Analytical.
Structure:

Opening: 'Understood on the timing. Happy to handle this via email.'

Core: Ask 3 specific diagnostic questions (e.g., 'What is your main value prop?', 'What are your KPIs for this year?', 'What would be a slam dunk?').

CTA: 'Shoot those back to me and I'll build a proposal.'

Generate the email.
"""
    },
    {
        "id": 27,
        "style": "The 'Specific Metric' Pitch",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You have identified a public metric of theirs (e.g., Twitter followers, Page Speed, Ad Count) that is below the industry standard.
Rule from Book: Apply the 'Metric-Based' pitch. Cite the exact number you saw.
Strict Tone: Helpful observer.
Structure:

Subject line: 'Quick question'.

Opening: Compliment the brand generally.

Core: 'I specialize in growing {industry}. Noticed {company} has less than {pain} on {industry}. We helped a similar client go from {value} to {value} in 3 months.'

CTA: 'Want more engaged {value}? Let me know.'

Generate the email.
"""
    },
    {
        "id": 28,
        "style": "The 'Niche Event' Scraper Pitch",
        "text": """
Act as a Senior Sales Executive. You are writing to an Event Organizer, {title}.
Context: You scraped their contact info by working backwards from a list of top events in {industry}.
Rule from Book: Apply the 'Creative Scraping' outreach. Acknowledge the specific event they organize.
Strict Tone: Professional networker.
Structure:

Subject line: '{company} question'.

Opening: 'Huge fan of the work you did organizing {company}.'

Core: 'We specialize in helping event organizers in {industry} streamline {pain}. Recently helped another event save {value}.'

CTA: 'Open to a chat?'

Generate the email.
"""
    },
    {
        "id": 29,
        "style": "The 'Pay-Per-Click' Case Study Pitch",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Selling Ad Management services.
Rule from Book: Apply the 'Revenue-First' Case Study. Mention specific revenue or lead volume, not vanity metrics.
Strict Tone: Result-oriented.
Structure:

Subject line: 'Quick question'.

Opening: 'Love the work you are doing for {company}, congrats on many years in business.'

Core: 'Been running Google ads for 12 years and have filled over {value} beds/orders for {industry} across the country.'

CTA: 'Would love to do the same for you. Let's talk?'

Generate the email.
"""
    },
    {
        "id": 30,
        "style": "The 'Clarity' Rewrite (Internal Tool)",
        "text": """
Act as a Cold Email Expert.
Context: I have a draft cold email that is performing poorly.
Rule from Book: Apply the 'Crystal Clear' test. Rewrite the email to be more straightforward and direct. Remove jargon. Ensure the 'One Sentence Case Study' is prominent.
Input Email: '[Draft Email]'
Task: Rewrite this email to match the {style} format from the book.
Strict Tone: Senior VP (Brief, direct).

Generate the optimized email.
"""
    },
    {
        "id": 31,
        "style": "The 'Equity/Acquisition' Pitch",
        "text": """
Act as a Potential Partner/Investor. You are writing to a {title} of {company}.
Context: You admire their product and want to offer services in exchange for equity or acquire a stake.
Rule from Book: Apply the 'Equity Partnership' concept. Do not ask for a job. Offer to help grow the company in exchange for a piece of the pie.
Strict Tone: Peer-to-Peer (Investor mindset).
Structure:

Subject line: 'Partnership?'

Opening: 'Been following {company} on Product Hunt/news and love the traction.'

Core: Mention you have a team that specializes in {value} and you are looking to partner with a high-potential SaaS.

CTA: 'Open to chatting about us taking over {value} in exchange for equity?'

Generate the email.
"""
    },
    {
        "id": 32,
        "style": "The 'Tech Audit' No-Brainer",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title}.
Context: Selling backend development or DevOps services.
Rule from Book: Apply the 'Tech Review' offer.
Strict Tone: Confident expert.
Structure:

Subject line: 'Quick Question'.

Opening: Compliment their current infrastructure or recent scale at {company}.

Core: 'We offer a two-hour tech review to identify {pain}. We can end the contract immediately after that if you don't see the value.'

CTA: 'Worth a chat?'

Generate the email.
"""
    },
    {
        "id": 33,
        "style": "The 'Mood Board' Branding Offer",
        "text": """
Act as a Creative Director. You are writing to a {title}.
Context: Pitching a rebrand or design services.
Rule from Book: Apply the 'Mood Board' risk reversal.
Strict Tone: Creative but business-focused.
Structure:

Subject line: 'Rebrand for {company}?'

Opening: Compliment their current visual identity or a specific campaign.

Core: 'Let's just do the mood board first. If you don't like where it is headed, we can refund.'

CTA: 'Open to seeing some ideas?'

Generate the email.
"""
    },
    {
        "id": 34,
        "style": "The 'Lead Gen' Job Post Script",
        "text": """
Act as an Agency Owner. You are posting a job on a freelancing platform.
Context: You need to build a list of leads for your cold email campaign.
Rule from Book: Use the 'Lead Gen Job Post' template. Be extremely specific about criteria.
Strict Tone: Instructional.
Structure:

Title: 'Lead Generation List building'.

Criteria: Define the revenue range (e.g., 5m-150m), Industry: {industry}, and specific exclusions (e.g., 'Must have under {pain}').

Data Points Needed: First Name, Last Name, Email, etc.

Budget: Set a fixed price for the test batch.

Requirement: 'All emails must be verified.'

Generate the job post description.
"""
    },
    {
        "id": 35,
        "style": "The 'Assistant' Coordination",
        "text": """
Act as a Senior Sales Executive. You are writing to an {title}.
Context: The CEO copied their assistant to schedule the call.
Rule from Book: Apply the 'Assistant Coordination' protocol. Be efficient. Provide the video link immediately.
Strict Tone: Professional and organized.
Structure:

Subject line: 'Re: Meeting'.

Opening: 'Thanks {title} (cc'ing CEO to move them to bcc).'

Core: 'Here are a few times that work on my end: Tuesday at 10am or Thursday at 2pm.'

CTA: 'Let me know what works and I will send the invite.'

Generate the email.
"""
    },
    {
        "id": 36,
        "style": "The 'Twitter Growth' Pitch",
        "text": """
Act as a Social Media Growth Expert. You are writing to a {title} at {company}.
Context: They have under 100,000 followers on Twitter.
Rule from Book: Apply the 'Twitter Growth' script. Cite the exact follower count you saw to prove it's not a template.
Strict Tone: Direct and helpful.
Structure:

Subject line: 'Quick question'.

Opening: 'Big fan of {company}—use your product every day.'

Core: 'Specializing in growing Twitter for consumer brands. Noticed you have less than 100,000 followers. Recently helped a client go from 20k to 100k in 7 days.'

CTA: 'Want more engaged {value}? Let me know.'

Generate the email.
"""
    },
    {
        "id": 37,
        "style": "The 'VR Application' Pitch",
        "text": """
Act as a Tech Sales Lead. You are writing to a {title} at {company}.
Context: Selling VR/AR development services.
Rule from Book: Apply the 'VR Application' script. Connect the tech to a business outcome (awareness), not just the coolness of the tech.
Strict Tone: Forward-thinking.
Structure:

Subject line: 'Quick question, {title}'.

Opening: 'Huge fan of {company} and your forward-thinking approach.'

Core: 'Recently helped several companies build VR apps to drive more {value}. I'd love to do the same for you.'

CTA: 'Mind if I send over a few times for a quick call?'

Generate the email.
"""
    },
    {
        "id": 38,
        "style": "The 'Contract' Nudge",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title}.
Context: You sent the proposal/contract 3 days ago. They haven't signed.
Rule from Book: Apply the 'Contract Bump.' Do not be desperate. Assume they are just busy.
Strict Tone: Professional.
Structure:

Subject line: (Reply to the proposal email).

Body: 'Any questions on the proposal before we get started?'

CTA: 'Let me know.'

Generate the email.
"""
    },
    {
        "id": 39,
        "style": "The 'Post-Success' Referral Ask",
        "text": """
Act as a Agency Owner. You are writing to a {title}.
Context: You just delivered a win or they expressed satisfaction with your work.
Rule from Book: Apply the 'Outbound Referral' concept. Ask if they know anyone else in their network (or a specific niche) who needs similar results.
Strict Tone: Casual.
Structure:

Subject line: 'One thing'.

Opening: 'Glad you liked the results on {value}.'

Core: 'We have capacity to take on 2 more clients in the {industry} space. Do you know any other founders who need {value}?'

CTA: 'Thanks.'

Generate the email.
"""
    },
    {
        "id": 40,
        "style": "The 'Feedback' Request",
        "text": """
Act as a Sales Director. You are writing to a {title}.
Context: They said 'No' to the proposal.
Rule from Book: Apply the 'Learning Curve' mindset. Ask for feedback to improve the offer for future clients.
Strict Tone: Humble and curious.
Structure:

Subject line: 'Quick question'.

Opening: 'Totally understand that this isn't a fit right now.'

Core: 'Since I'm always trying to improve our offer—was it the price or the timeline that didn't work for you?'

CTA: 'Appreciate the feedback.'

Generate the email.
"""
    },
    {
        "id": 41,
        "style": "The 'Sunday Afternoon' Executive Outreach",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title}.
Context: It is Sunday afternoon. You are sending this to hit their phone while they plan their week.
Rule from Book: Apply the 'Sunday Send' strategy. Keep it incredibly short (mobile-optimized) and casual.
Strict Tone: Casual, 'weekend warrior' vibe but professional.
Structure:

Subject line: 'Plan for the week?' or 'Quick question'.

Opening: 'Hope you're having a good weekend.'

Core: 'I'll keep this brief—we helped a competitor grow {value} by {value}.'

CTA: 'Worth a chat sometime this week?'

Generate the email.
"""
    },
    {
        "id": 42,
        "style": "The 'Emoji' Subject Line Test",
        "text": """
Act as a Marketing Lead. You are writing to a {title} in the {industry} industry.
Context: You are A/B testing subject lines to improve open rates.
Rule from Book: Apply the 'Emoji Relevance' strategy. Use a specific emoji that signals you are an insider, not a random spammer.
Strict Tone: Insider/Peer.
Structure:

Subject line: '🚀 for {company}?'

Opening: Custom compliment.

Core: Standard 'Case Study' pitch.

CTA: Simple Ask.

Generate the email including the subject line.
"""
    },
    {
        "id": 43,
        "style": "The 'Healthcare App' Pitch",
        "text": """
Act as a Tech Sales Director. You are writing to a {title}.
Context: Selling mobile app development to healthcare providers.
Rule from Book: Apply the 'Johns Hopkins' case study framework. Focus on 'Patient Happiness' or 'Efficiency' rather than code.
Strict Tone: Professional and authoritative.
Structure:

Subject line: 'Quick question'.

Opening: Compliment a specific initiative at {company}.

Core: 'I specialize in iOS development for healthcare. Recently built an app for Johns Hopkins that increased patient happiness ratings by 75%.'

CTA: 'Interested in improving patient happiness at {company}?'

Generate the email.
"""
    },
    {
        "id": 44,
        "style": "The 'Portfolio Feedback' Backdoor",
        "text": """
Act as a Job Seeker (Specialist). You are writing to a {title}.
Context: You want to work for them. You have a portfolio ready.
Rule from Book: Apply the 'Portfolio Feedback' strategy. Ask for critique, not employment.
Strict Tone: Ambitious student/learner.
Structure:

Subject line: 'Portfolio question'.

Opening: 'Huge fan of your work on {value}.'

Core: 'I am graduating/shifting careers and just finished my portfolio. Since you are the best in the city, I would value your critique on it.'

CTA: 'Open to a 10-min coffee to destroy my work?'

Generate the email.
"""
    },
    {
        "id": 45,
        "style": "The 'Sales Meeting' Report",
        "text": """
Act as a Sales Director. You are running the weekly sales meeting.
Context: You need to ask your team for their numbers based on the book's specific metrics.
Rule from Book: Apply the 'Lead vs Lag' reporting structure.
Strict Tone: No-nonsense management.
Structure:

Opening: 'Let's look at the scoreboard.'

Ask for Lead Measures: 'How many cold emails sent? How many calls made?'

Ask for Lag Measures: 'How many meetings booked? How much revenue closed?'

Closing: 'Who is underperforming on the inputs?'

Generate the meeting agenda/script.
"""
    },
    {
        "id": 46,
        "style": "The 'Spam Filter' Self-Audit",
        "text": """
Act as a Deliverability Expert.
Context: I have written a cold email draft.
Rule from Book: Apply the 'Inbox Calibration' rules.
Checklist to enforce:

Are there images? (Remove them).

Are there links? (Remove them, except one in signature).

Is the signature huge? (Simplify it).

Are there 'spam trigger' words (e.g., 'free', 'guarantee', 'buy now')?
Input Email: '[Draft Email]'
Task: Critique and fix the email to ensure it lands in the Primary Inbox.

Generate the critique and the fixed version.
"""
    },
    {
        "id": 47,
        "style": "The 'Newsletter' Profit Share Offer",
        "text": """
Act as a Direct Response Copywriter. You are writing to a {title}.
Context: You want to take over their email marketing.
Rule from Book: Apply the '50% Commission' No-Brainer offer.
Strict Tone: Confident in ability to generate revenue.
Structure:

Subject line: 'Quick question'.

Opening: 'Love the last video you posted about {industry}.'

Core: 'I write newsletters for companies like yours. I'll write 3 for you—if they don't generate sales, you don't pay. If they do, I take 50% commission.'

CTA: 'Open to a test run?'

Generate the email.
"""
    },
    {
        "id": 48,
        "style": "The 'Referral Network' Coffee Chat",
        "text": """
Act as an Entrepreneur. You are writing to a {title} in {industry}.
Context: You just moved to the city or entered the industry and want to build a network.
Rule from Book: Apply the 'NYC Coffee' strategy. Ask for a quick in-person meet or virtual coffee to share insights, not to sell.
Strict Tone: Friendly and curious.
Structure:

Subject line: 'Coffee?'

Opening: 'Just moved to {industry} / Just started in {industry}.'

Core: 'I see you are doing great work at {company}. I'm looking to connect with smart people in the space.'

CTA: 'Open to a coffee next week?'

Generate the email.
"""
    },
    {
        "id": 49,
        "style": "The 'Fashion Industry' Specific Pitch",
        "text": """
Act as a Marketing Agency Owner. You are writing to the Owner of a {company}.
Context: Selling growth marketing services.
Rule from Book: Apply the 'Alexander Wang' logic. Do not call them an 'eCommerce company.' Call them a 'Fashion Brand.' Use industry-relevant case studies.
Strict Tone: Chic and professional.
Structure:

Subject line: 'Quick Question'.

Opening: 'Huge fan of your new {value} collection.'

Core: 'We helped a similar brand increase their Return on Ad Spend (ROAS) by 300% using {value}.'

CTA: 'Interested in the same results for {company}?'

Generate the email.
"""
    },
    {
        "id": 50,
        "style": "The 'Campaign Architect' (Full Sequence Generator)",
        "text": """
Act as a Cold Email Architect. You are writing a full campaign for {value} targeting {title}.
Context: We need the complete 4-email sequence ready to load into our sending tool.
Rule from Book: Apply the Chapter 7 Sequence structure strictly.

Email 1: The 3 C's (Compliment, Case Study, CTA).

Email 2 (Day 4): The 'Bumping this up' one-liner.

Email 3 (Day 8): The 'Big Win' (New case study/news).

Email 4 (Day 15): The Break-Up (Professional withdrawal).
Strict Tone: Senior VP.

Generate all 4 emails in order.
"""
    },
    {
        "id": 51,
        "style": "The Problem Identification Opener (PIC Approach)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: This is a cold outbound email. You have done research using a Problem Identification Chart (PIC) and suspect they are suffering from a specific business problem.
Rule from Book: Do not mention product features. Focus entirely on the 'Current State' problem and its potential business impact. Be an expert problem finder.
Strict Tone: Professional, authoritative, assumptive, and concise. No fluff (e.g., 'Hope you are well').
Structure:

Subject line: A direct reference to {pain} or its impact.

Opening: State a specific observation about {company} or {industry} that suggests a problem exists.

Core: Hypothesize the negative business impact (the 'Business Problem,' not just the 'Technical Problem') they are likely facing because of {pain}.

CTA: Ask for a brief conversation to confirm or deny if this problem exists (the 'First Yes').

Generate the email.
"""
    },
    {
        "id": 52,
        "style": "The 'I’m Confused' Challenge",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect is stalling or making a decision (like choosing a cheaper competitor) that contradicts the goals they shared in discovery.
Rule from Book: Use the 'I'm confused' tactic. Highlight the disconnect between their stated 'Future State' (goals) and their current behavior.
Strict Tone: Perplexed, protective of the client's success, direct.
Structure:

Subject line: Re: {value}

Opening: Use the phrase 'I'm confused.'

Core: Remind them of the specific {value} they said was critical. Contrast that with their recent decision/action to {pain}, explaining why these two things do not align.

CTA: Ask for a brief sync to clarify this disconnect to ensure they don't miss their goal.

Generate the email.
"""
    },
    {
        "id": 53,
        "style": "The 'Not the Customer's B*tch' Pushback",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect just emailed asking for a price quote or a free trial immediately, without agreeing to a discovery call first.
Rule from Book: Refuse the request respectfully but firmly. Explain that providing a quote/trial without understanding their 'Current State' would be professional malpractice. Value your expertise.
Strict Tone: Professional, firm, expert-level (Consultant mindset).
Structure:

Subject line: Regarding your request

Opening: Acknowledge the request but state clearly that you cannot fulfill it yet.

Core: Explain that you are not a commodity provider. You need to understand their specific problems and 'Current State' to determine if your solution is even a fit before discussing price/trials.

CTA: Propose a 15-minute call to diagnose their situation first.

Generate the email.
"""
    },
    {
        "id": 54,
        "style": "The 'Benign vs. Malignant' Framing",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect admits they have {pain} but doesn't feel it's urgent enough to fix now.
Rule from Book: Move the conversation from the 'Technical Problem' (annoyance) to the 'Business Problem' (revenue/survival impact). Reveal the damage the problem is causing.
Strict Tone: Urgent, insightful, 'Doctor delivering a diagnosis.'
Structure:

Subject line: The cost of {pain}

Opening: Acknowledge they feel the issue is small.

Core: Connect the dots to show how that small {pain} is actually causing a much larger business impact (e.g., lost revenue, churn, risk). Use the 'Gap' concept to show the cost of waiting.

CTA: Ask if they are willing to live with that specific business impact.

Generate the email.
"""
    },
    {
        "id": 55,
        "style": "The Intrinsic Motivation ('The Why') Follow-Up",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The deal has stalled. You know their business goals, but you also uncovered their personal intrinsic motivation during discovery (e.g., {value}).
Rule from Book: Leverage the 'Intrinsic Motivation.' Remind them that the 'Future State' isn't just about company ROI, but about the personal relief/success they mentioned.
Strict Tone: Empathetic but focused on the 'Gap.'
Structure:

Subject line: {value}

Opening: Recall the specific personal outcome they wanted (e.g., 'getting home for dinner,' 'securing that promotion').

Core: Remind them that every day of delay keeps them in their painful 'Current State.' Reiterate that the 'Gap' is worth filling for their personal sanity/success.

CTA: Ask what needs to happen to get them to that 'Future State.'

Generate the email.
"""
    },
    {
        "id": 56,
        "style": "The 'Next Yes' Micro-Commitment",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You are trying to move a cold prospect to a discovery call.
Rule from Book: Don't sell the solution. Sell the 'Next Yes.' The goal is only to get them to agree that a conversation is in their best interest.
Strict Tone: Low-pressure, high-value.
Structure:

Subject line: A question regarding {pain}

Opening: State that you are not asking for a purchase, but a verification of a problem.

Core: Offer a specific insight or piece of value that justifies 5-10 minutes of their time. Frame the meeting as a way to help them understand their own problem better, not a sales pitch.

CTA: Ask for the micro-commitment (time to discuss the problem).

Generate the email.
"""
    },
    {
        "id": 57,
        "style": "The 'No Ifs' Demo Confirmation",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You have completed discovery and are confirming the agenda for the upcoming demo.
Rule from Book: Eliminate the word 'If.' State clearly that you will show specific solutions to the specific problems identified in discovery. Anchor them to the 'Future State.'
Strict Tone: Confident, specific, customized.
Structure:

Subject line: Preparing for our call / solving {pain}

Opening: Confirm the time.

Core: List exactly 3 specific problems they admitted to. State: 'I will show you exactly how we resolve {pain} to impact {value}.'

CTA: Ask if there are any other specific problems they need to see solved.

Generate the email.
"""
    },
    {
        "id": 58,
        "style": "The Credibility/Insight Drop",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Prospecting email to a sophisticated buyer. You need to prove credibility instantly.
Rule from Book: Lead with 'Value.' Share a provocative insight or trend about {industry} that is likely negatively impacting their 'Current State.'
Strict Tone: Peer-to-peer, educational, provocative.
Structure:

Subject line: Impact of {industry} on {company}

Opening: Cite a specific shift or trend in their market.

Core: Explain a non-obvious problem this trend usually causes for companies like theirs. Ask if they are experiencing this specific negative outcome.

CTA: Ask for a conversation to share how others are navigating this shift.

Generate the email.
"""
    },
    {
        "id": 59,
        "style": "The 'Gap Math' Justification",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The buyer is hesitating on price or stalling. You need to remind them of the cost of inaction using math.
Rule from Book: Do the math for them. Quantify the Gap. Contrast the cost of the solution against the cost of the problem.
Strict Tone: Analytical, objective, 'Just the facts.'
Structure:

Subject line: The math regarding {value}

Opening: Recap their current metric (Current State) and their goal metric (Future State).

Core: Calculate the delta (The Gap) in dollars or time. Compare this massive cost of the problem to the investment required for the solution.

CTA: Ask if leaving that much value on the table is acceptable to them.

Generate the email.
"""
    },
    {
        "id": 60,
        "style": "The 'Validation' Check-In",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Post-discovery, pre-demo. You want to ensure you haven't misunderstood their 'Current State.'
Rule from Book: Use 'Validating Questions.' Reiterate what they told you and ask them to confirm it is 100% accurate.
Strict Tone: Diligent, precise, humble.
Structure:

Subject line: Ensuring I understood {pain} correctly

Opening: 'I want to make sure I have this right before we move forward.'

Core: Summarize their 'Current State' (Problems + Root Causes + Impact) in bullet points. Be specific.

CTA: Ask: 'Did I miss anything, or is this an accurate representation of your environment?'

Generate the email.
"""
    },
    {
        "id": 61,
        "style": "The 'Command Statement' Discovery Request",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You are in an email dialogue trying to understand their process, but their answers have been short. You need them to open up.
Rule from Book: Replace interrogation questions (Who/What/Where) with 'Command Statements' to foster a conversation.
Strict Tone: Inquisitive, collaborative, patience-inducing.
Structure:

Subject line: Context on {pain}

Opening: Acknowledge their previous short response.

Core: Use a command statement phrase (e.g., 'Help me understand...' or 'Walk me through...') to ask them to describe the specific workflow of {pain} and where the friction sits.

CTA: Ask for a 10-minute call to let them narrate this process so you don't make assumptions.

Generate the email.
"""
    },
    {
        "id": 62,
        "style": "Banishing the Open-Ended Answer",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect stated their goal is to '{value}' (e.g., increase revenue, hire faster) but did not give a number.
Rule from Book: Refuse the open-ended answer. You need to quantify the 'Current State' and 'Future State' to calculate the value of the Gap.
Strict Tone: Analytical, precise, 'The Auditor.'
Structure:

Subject line: Defining '{value}'

Opening: Reference their statement about wanting to {value}.

Core: State clearly that 'better' or 'faster' are subjective. Ask them to define exactly what {value} looks like in numbers (e.g., 'Is that 10% growth or 50%?'). Explain that you can't prescribe a solution without knowing the size of the problem.

CTA: Ask for the specific metric.

Generate the email.
"""
    },
    {
        "id": 63,
        "style": "The 'No Discovery, No Demo' Pivot",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect replied to your outreach asking to 'just see a demo' without a conversation first.
Rule from Book: Refuse the demo-first approach. Explain that a generic demo is a waste of their time. You need to understand their 'Current State' to customize the demo.
Strict Tone: Firm, respectful, protective of their time.
Structure:

Subject line: Your demo request

Opening: Thank them for the interest.

Core: State that you do not do generic demos because they are a waste of time. Explain that you split the process into two steps: 1. A brief assessment of their current challenges, and 2. A tailored demo addressing only those challenges.

CTA: Propose a time for step 1 (The Discovery).

Generate the email.
"""
    },
    {
        "id": 64,
        "style": "The Root Cause Expert",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You know they are suffering from {pain}, but they haven't been able to fix it.
Rule from Book: Diagnose the 'Root Cause.' Don't just talk about the pain; explain why the pain is happening based on your industry expertise.
Strict Tone: Educational, authoritative, 'The Consultant.'
Structure:

Subject line: Why {pain} keeps happening

Opening: Observe that they are struggling with {pain}.

Core: Suggest that while many try to fix this by common mistakes, the actual 'Root Cause' is usually {pain}. Explain how this root cause creates a domino effect of bad results.

CTA: Ask if they have investigated {pain} as the culprit.

Generate the email.
"""
    },
    {
        "id": 65,
        "style": "The 'Decision Criteria' Realignment",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect is leaning toward a competitor because of {pain} (e.g., lower price), but that competitor cannot solve their {pain}.
Rule from Book: Use the 'I'm Confused' framework. Highlight the disconnect between their decision criteria and their stated desired outcome.
Strict Tone: Direct, challenging, concerned.
Structure:

Subject line: Alignment on {pain}

Opening: 'I'm confused.'

Core: Remind them their primary goal was {value}. Point out that prioritizing {pain} usually prevents that goal because [Reason]. Ask how they reconcile that trade-off.

CTA: Ask for a brief discussion to ensure they aren't undermining their own goal.

Generate the email.
"""
    },
    {
        "id": 66,
        "style": "The 'Going Dark' Gap Reminder",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect has stopped replying after a proposal.
Rule from Book: Do not say 'Just checking in.' Re-anchor them to the 'Business Problem' and the negative impact of the 'Current State' they shared with you.
Strict Tone: Serious, focused on consequences.
Structure:

Subject line: The impact of {pain} on {value}

Opening: Mention you haven't heard back.

Core: Remind them that when you last spoke, {pain} was costing them {pain}. State that every week this delays, that cost continues to accrue.

CTA: Ask if fixing {pain} is no longer a priority for the business.

Generate the email.
"""
    },
    {
        "id": 67,
        "style": "The Buying Process Mapper",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect said 'Yes' to the solution, but you don't know the logistics of their procurement process.
Rule from Book: Secure the 'Next Yes' by mapping the buying process. Don't assume the person you are talking to is the only decision maker.
Strict Tone: Professional, logistical, 'Project Manager' vibe.
Structure:

Subject line: Next steps for {value}

Opening: Great to hear you want to move forward.

Core: Ask them to walk you through the specific steps their company requires to get a contract signed. Ask specifically about legal reviews, procurement committees, and other stakeholders who need to weigh in.

CTA: Ask who else needs to be involved to meet their desired timeline.

Generate the email.
"""
    },
    {
        "id": 68,
        "style": "The 'Partnership' Stand (Anti-Servant)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect is demanding an unreasonable concession (e.g., a free 3-month pilot) without offering any commitment in return.
Rule from Book: Do not be the 'Customer's B*tch.' Set terms. Agree to their request ONLY if they agree to a reciprocal commitment (e.g., success criteria + automatic contract signature upon success).
Strict Tone: Equal business partner, firm.
Structure:

Subject line: Terms for {value}

Opening: Acknowledge their request.

Core: State that you can only agree to {value} if we are working as partners. Propose a 'Quid Pro Quo' (e.g., We will do the pilot, IF you agree to X success criteria and a signature upon meeting them).

CTA: Ask if they are willing to commit to that structure.

Generate the email.
"""
    },
    {
        "id": 69,
        "style": "The Three-Part Future State Recap",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Sending a follow-up after a deep discovery call to confirm you understand their vision.
Rule from Book: Articulate the Future State in three layers: Technical, Business, and Core.
Strict Tone: Visionary, comprehensive, confirming.
Structure:

Subject line: Summary of our discussion / Your Future State

Opening: 'Here is what I captured regarding where you want to go.'

Core: Bullet point 1: Technical Future State (what the tech will do). Bullet point 2: Business Future State (how metrics/revenue improve). Bullet point 3: Core Future State (how this helps them beat competitors or achieve a strategic milestone).

CTA: Ask them to confirm this is the accurate vision.

Generate the email.
"""
    },
    {
        "id": 70,
        "style": "The 'Emotional State' Check",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: During discovery, the prospect seemed visibly frustrated or stressed by their current situation. You want to validate this to build a bond.
Rule from Book: Don't ignore the emotion. Label it. Confirm that the current problems are causing them personal stress/frustration.
Strict Tone: Empathetic but professional.
Structure:

Subject line: Thoughts on our conversation

Opening: Reflect on the last call.

Core: Observe that dealing with {pain} seemed incredibly frustrating for them and their team. Validate that it makes sense they feel that way given the lack of {value}.

CTA: Ask if reducing that specific stress is a priority for them personally this quarter.

Generate the email.
"""
    },
    {
        "id": 71,
        "style": "The 'Change Event' Prospecting Trigger",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You noticed a specific 'Change Event' (e.g., new regulation, merger, new VP hired) at their company via the news/LinkedIn.
Rule from Book: Don't congratulate them. Highlight the problems that usually accompany this specific type of change. Position yourself as the expert in navigating this transition.
Strict Tone: Insightful, anticipatory, helpful.
Structure:

Subject line: The impact of {industry} change on {company}

Opening: Reference the specific news/change event.

Core: State that typically, when {industry} change happens, companies struggle with {pain}.

CTA: Ask if they have a strategy in place to handle that specific friction yet.

Generate the email.
"""
    },
    {
        "id": 72,
        "style": "The 'Process Layer' Excavation",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect said they handle {pain} 'fine.' You suspect their process is manual and inefficient, but you need details to prove it.
Rule from Book: Ask 'Process Questions.' Do not accept high-level answers. Ask for the step-by-step workflow (The 'How').
Strict Tone: Curious, detail-oriented, 'The Engineer.'
Structure:

Subject line: The workflow for {pain}

Opening: Reference their claim that {pain} is working fine.

Core: Ask specific questions about the 'Process Layer.' (e.g., 'Do you do this manually in Excel? Who enters the data? What happens if that person is out?').

CTA: Ask if they are open to mapping this process to see if we can find efficiency gains.

Generate the email.
"""
    },
    {
        "id": 73,
        "style": "The 'Provoking' Hypothetical",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect is complacent. You need to shake them up by introducing a risk they haven't thought of.
Rule from Book: Use a 'Provoking Question.' Ask 'What happens if...?' regarding a specific vulnerability in their current approach.
Strict Tone: Thought-provoking, grave, 'Devil's Advocate.'
Structure:

Subject line: What happens if {pain} occurs?

Opening: 'I've been thinking about your current setup regarding {industry}.'

Core: Pose a hypothetical scenario: 'If {pain} happens, how would your current system handle it?' Imply that their current state leaves them exposed.

CTA: Ask if they are prepared for that outcome.

Generate the email.
"""
    },
    {
        "id": 74,
        "style": "The 'Price vs. Cost' Rebuttal",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect emailed saying your proposal is 'too expensive' or 'more than we budgeted.'
Rule from Book: Do not offer a discount. Pivot immediately to the 'Cost of Inaction.' Compare your price to the revenue/efficiency they are losing every month.
Strict Tone: Confident, mathematical, direct.
Structure:

Subject line: The cost of the solution vs. the cost of the problem

Opening: Acknowledge the budget concern.

Core: Remind them that {pain} is currently costing them massive amounts per year. Your solution costs less. Ask them to explain the math behind keeping the expensive problem to save money on the cheaper solution.

CTA: Ask if they are willing to continue losing money per month.

Generate the email.
"""
    },
    {
        "id": 75,
        "style": "The 'Champion' Armament",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} (your Champion) at {company}.
Context: Your contact needs to present your solution to the CEO/CFO for approval.
Rule from Book: Don't give them product specs. Give them a 'Business Case' based on the Gap. Summarize the Problem, Impact, and Root Cause so they can sell the 'Outcome.'
Strict Tone: Collaborative, strategic, empowering.
Structure:

Subject line: Business case for Decision Maker

Opening: 'To help you get this approved, I've summarized the business impact we discussed.'

Core: Provide a script or bullet points they can use: 'We are currently losing X due to {pain}. This solution recovers {value} revenue.'

CTA: Ask if this narrative aligns with what their CFO cares about.

Generate the email.
"""
    },
    {
        "id": 76,
        "style": "The 'Competitor' Feature Trap",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect mentions they are considering a competitor because of a specific feature or lower price.
Rule from Book: Don't bash the competitor. Validate them, but then point out a specific gap in the competitor's ability to solve the Business Problem identified in discovery.
Strict Tone: Objective, differentiated.
Structure:

Subject line: Competitor and {pain}

Opening: Acknowledge the competitor is a good company.

Core: Remind them that their main goal is {value}. Explain that while the competitor has features, they lack the ability to solve {pain} which is required to solve the main problem.

CTA: Ask if they are willing to sacrifice {value} for that feature/price.

Generate the email.
"""
    },
    {
        "id": 77,
        "style": "The 'Benign Tumor' Walk Away",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: After discovery, you realize the financial impact of their problem is small, or the cost of your solution outweighs their potential return.
Rule from Book: Disqualify the lead. Tell them honestly that the Gap isn't big enough to justify the purchase right now.
Strict Tone: Honest, ethical, 'Trusted Advisor.'
Structure:

Subject line: Recommendation regarding {value}

Opening: Thank them for the time spent in analysis.

Core: State that based on the numbers, the problem is only costing them X, while the solution costs Y. Therefore, you do not recommend buying at this time.

CTA: Suggest revisiting this only if {pain} changes in the future. "Peace, I'm out."

Generate the email.
"""
    },
    {
        "id": 78,
        "style": "The 'Widening the Gap' Expansion",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect admits to a problem, but isn't treating it as urgent. You need to show them the bigger picture.
Rule from Book: Connect the local problem to a global impact. Show how their departmental issue is negatively affecting HR, Finance, or Customer Satisfaction.
Strict Tone: Strategic, 'Big Picture.'
Structure:

Subject line: The ripple effect of {pain}

Opening: Acknowledge that {pain} seems manageable within their team.

Core: Ask if they have considered how this issue is impacting other departments. Explain that typically, this flaw causes {pain} downstream.

CTA: Ask if they want to explore this broader impact.

Generate the email.
"""
    },
    {
        "id": 79,
        "style": "The 'Consultant' Nurture (No Ask)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You are nurturing a high-value prospect who isn't ready to buy. You want to stay top of mind without being annoying.
Rule from Book: Share genuine expertise/insight (content) regarding their industry/problem. Do NOT ask for a meeting. Be an asset.
Strict Tone: Helpful, peer-to-peer.
Structure:

Subject line: Thinking of {company} / {industry}

Opening: 'I saw this article/data regarding {industry} and thought of our last conversation.'

Core: Highlight one specific insight from the content that relates to the 'Root Cause' of problems in their industry.

CTA: None. Just 'Hope this helps you navigate X.'

Generate the email.
"""
    },
    {
        "id": 80,
        "style": "The 'Implementation' Handover (Success Assurance)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}, copying your internal CS Rep.
Context: The deal is closed. You are introducing them to their account manager.
Rule from Book: Don't just say 'Meet John.' Reiterate the 'Future State' and 'Success Criteria' to ensure the CS team is held accountable to the specific outcomes sold.
Strict Tone: Professional, accountable, seamless.
Structure:

Subject line: Introduction: {company} <> CS Rep

Opening: Introduce the CS rep.

Core: State clearly: 'I have briefed the CS Rep on the specific problems we are solving ({pain}) and the Future State metrics we are targeting ({value}). They know that success is defined by achieving {value}.'

CTA: Wish them success.

Generate the email.
"""
    },
    {
        "id": 81,
        "style": "The 'Status Quo' Disruption",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect rejected your initial outreach stating they are 'happy' with their current vendor/process.
Rule from Book: Do not accept 'happy' as the end. Challenge the status quo by introducing a specific efficiency or outcome they might be missing (The 'Unknown Gap').
Strict Tone: Professional, inquisitive, non-threatening.
Structure:

Subject line: Regarding your current setup with vendor

Opening: Validate their satisfaction (e.g., 'It is great that you have a solution in place').

Core: pivot gently. 'However, many leaders I speak with finding that while vendor solves X, it often creates a bottleneck in Y. Are you seeing any friction regarding {pain}?'

CTA: Ask if they are open to a 5-minute comparison to ensure they aren't leaving value on the table.

Generate the email.
"""
    },
    {
        "id": 82,
        "style": "The LinkedIn 'Contextual Connect'",
        "text": """
Act as a Senior Sales Executive. You are writing a LinkedIn connection request (max 300 chars) or a follow-up InMail to a {title}.
Context: They just commented on or shared an article about {industry}.
Rule from Book: Do not pitch. Use their engagement as a bridge to a 'Business Problem' discussion. Connect their interest in the topic to a potential gap in their business.
Strict Tone: Relevant, brief, peer-to-peer.
Structure:

Opening: Mention their specific comment/post on {industry}.

Core: Add a 'Provoking Thought' or insight that creates a new perspective on that topic. Connect it to a likely problem they face.

CTA: Ask a low-friction question about how they are handling that specific challenge.

Generate the email/message.
"""
    },
    {
        "id": 83,
        "style": "The 'Gap Review' (QBR Invitation)",
        "text": """
Act as a Senior Sales Executive. You are writing to an existing client {title} at {company}.
Context: It has been 3 months since implementation. You want to schedule a Quarterly Business Review (QBR).
Rule from Book: Don't call it a 'Check-in.' Frame it as a 'Gap Review.' We need to measure actual results against the 'Future State' metrics agreed upon during the sale.
Strict Tone: Accountable, metrics-driven.
Structure:

Subject line: Reviewing progress toward {value}

Opening: State that it has been 90 days.

Core: Remind them of the specific success metrics ({value}) defined in the original deal. State that you want to review the data to confirm we are closing the gap as predicted.

CTA: Propose time to review the scoreboard.

Generate the email.
"""
    },
    {
        "id": 84,
        "style": "The 'Ghostwriting' for the Champion",
        "text": """
Act as a Senior Sales Executive. You are writing an email on behalf of your Champion, which they will copy/paste and send to their CFO.
Context: Your Champion loves the solution but the CFO is blocking it due to cost. The Champion asked you for help.
Rule from Book: Focus entirely on the 'Cost of Inaction' and 'Business Risk.' Do not talk about features. The CFO cares about the bottom line.
Strict Tone: Internal, factual, urgent (written in the voice of the Champion).
Structure:

Subject line: Risk analysis regarding {value}

Opening: 'I've reviewed the numbers regarding the proposal.'

Core: Contrast the price of the software against the proven cost of the current problem ({pain}). State that delaying this purchase is costing the company more than the purchase price itself.

CTA: Recommendation to move forward to stop the bleeding.

Generate the email text for the Champion.
"""
    },
    {
        "id": 85,
        "style": "The 'Wrong Person' Pivot",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You realize this person experiences the 'Technical Problem,' but they don't own the 'Business Outcome' (budget/strategy). You need an introduction to their boss.
Rule from Book: Don't go over their head. Enable them. Explain that to solve their technical pain, you need to discuss the business impact with the person who owns the P&L.
Strict Tone: Collaborative, respectful.
Structure:

Subject line: Solving {pain} for your team

Opening: Validate that you understand their frustration with {pain}.

Core: Explain that to get the resources/budget to fix this for them, you need to map this problem to the wider department goals managed by their VP.

CTA: Ask for a joint conversation with them and their VP to build the business case.

Generate the email.
"""
    },
    {
        "id": 86,
        "style": "The 'Permission to Close File' (Break-Up)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: They have been stalling for weeks. You have sent value, followed up, and reminded them of the Gap. Silence.
Rule from Book: Do not guilt them. Assume the 'Gap' is no longer a priority. Ask for permission to close their file so you can stop bothering them.
Strict Tone: Professional, detached (not needy), final.
Structure:

Subject line: Closing the file on {value}?

Opening: State that you assume this project is no longer a priority since you haven't heard back.

Core: Briefly mention that this means the {pain} will likely continue, but you respect their prioritization.

CTA: 'Unless I hear otherwise, I will close this file on my end to stop filling your inbox.'

Generate the email.
"""
    },
    {
        "id": 87,
        "style": "The 'Voicemail Follow-Up'",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You just left a voicemail regarding a potential problem you identified.
Rule from Book: Keep it short. Reference the voicemail. Reiterate the 'Problem Hypothesis' (not the product).
Strict Tone: Direct, expecting a reply.
Structure:

Subject line: Voicemail regarding {pain}

Opening: 'I just left you a voicemail regarding {company}.'

Core: Briefly state that usually, this observation implies they are struggling with {pain}. You have an idea on how to address it.

CTA: 'Let me know if you'd like to see that idea.'

Generate the email.
"""
    },
    {
        "id": 88,
        "style": "The 'Assumptive' Next Step",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You just finished a discovery call where they admitted to a massive problem. You need to book the demo/solution review.
Rule from Book: Don't be timid. You are the expert. Because they admitted to the problem, the next step is logical and necessary. Assume they want to take it.
Strict Tone: Confident, leading the dance.
Structure:

Subject line: Next steps: Solving {pain}

Opening: Recap the massive cost of the problem they admitted to.

Core: State: 'Given the severity of this, the next logical step is to review the solution model so we can get this fixed by next month.'

CTA: Propose two specific times for the review.

Generate the email.
"""
    },
    {
        "id": 89,
        "style": "The 'Emotional Relief' Vision",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The deal is nearing the close, but they are hesitating. You know the current situation is causing them high personal stress (late nights, fear of firing, etc.).
Rule from Book: Paint the picture of the 'Future State' where that stress is gone. Sell the relief.
Strict Tone: Human, empathetic, visionary.
Structure:

Subject line: Imagining a world without {pain}

Opening: 'We've talked a lot about the numbers, but I wanted to touch on the team impact.'

Core: Remind them of the specific frustrations they shared. Paint the picture of 6 months from now: The system works, the team is happy, and they (the buyer) are no longer dealing with {pain}.

CTA: 'Let's get the paperwork signed so we can make that reality start next week.'

Generate the email.
"""
    },
    {
        "id": 90,
        "style": "The 'Root Cause' Confirmation",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Post-discovery. You diagnosed that their lack of revenue is caused by {pain} (e.g., poor data entry), not just 'bad luck.' You need them to agree before pitching.
Rule from Book: Validate the 'Root Cause.' If they don't agree on the root cause, they won't buy the solution.
Strict Tone: Diagnostic, clarifying.
Structure:

Subject line: Root cause of {pain}

Opening: 'Based on our last discussion, it seems clear that {pain} is actually a downstream result of a root cause.'

Core: Explain why you believe this is the root cause. Ask them to confirm if they agree that fixing the root cause is the only way to permanently solve the issue.

CTA: 'Do you agree with this diagnosis?'

Generate the email.
"""
    },
    {
        "id": 91,
        "style": "The 'Timing is Fluid' Reframe",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect asked you to reach back out in 3-6 months.
Rule from Book: Do not say 'Okay, talk soon.' Challenge the timing by highlighting that the 'Problem' will not pause just because they paused the project. Reframe the delay as a choice to lose money.
Strict Tone: Direct, financially focused, 'The Realist.'
Structure:

Subject line: The cost of waiting until next quarter

Opening: Acknowledge the request to wait.

Core: Do the math. 'If we wait 6 months, and {pain} continues to cost you massive amounts/month, you will lose {value} by the time we reconnect. Is that an acceptable loss for the business right now?'

CTA: Ask if they want to prevent that loss or if they prefer to absorb it.

Generate the email.
"""
    },
    {
        "id": 92,
        "style": "The 'RFP' Pushback",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You received a generic RFP (Request for Proposal) with no prior conversation.
Rule from Book: Refuse to submit a blind proposal. Explain that checking boxes on an RFP does not solve business problems. Demand access to understanding the 'Current State.'
Strict Tone: Professional, high-standard, 'Expert.'
Structure:

Subject line: Your RFP for {value}

Opening: Acknowledge receipt.

Core: State that you do not submit blind responses because they often lead to failed implementations. You need to understand the 'Business Problems' driving this request to see if you are even a fit.

CTA: 'If you are open to a 20-minute scoping call to explain the context, we can proceed. If not, we will respectfully decline to bid.'

Generate the email.
"""
    },
    {
        "id": 93,
        "style": "The 'Competitor Failure' Resurrection",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: They chose a competitor 9 months ago. You want to see if they are still suffering from the original problem.
Rule from Book: Don't ask 'How is it going?' Ask about the 'Gap.' Reference the specific problems they wanted to solve and ask if they are solved.
Strict Tone: Skeptical (polite), metrics-driven.
Structure:

Subject line: The {pain} we discussed last year

Opening: 'Nine months ago, you chose a competitor to solve {pain}.'

Core: 'I am curious—did that solution actually reduce your {pain} to the level you hoped? Or are you still dealing with that friction?'

CTA: Ask for a transparent update.

Generate the email.
"""
    },
    {
        "id": 94,
        "style": "The 'New Stakeholder' Catch-Up",
        "text": """
Act as a Senior Sales Executive. You are writing to a new {title} who just got looped into the email thread.
Context: You are mid-deal, and a new boss/stakeholder has joined.
Rule from Book: Don't start over. Summarize the 'Gap Analysis' performed with their team so far. Position yourself as an insider who already understands their business case.
Strict Tone: Efficient, executive summary style.
Structure:

Subject line: Catching you up on {value} analysis

Opening: Welcome them to the conversation.

Core: 'To bring you up to speed: Your team identified {pain} as critical threats to your goals. We are currently validating a solution to close that gap.'

CTA: Ask if they have any additional constraints or criteria to add to this analysis.

Generate the email.
"""
    },
    {
        "id": 95,
        "style": "The 'Need vs. Problem' Correction",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: In an initial email, the prospect said 'We need a tool that does X.'
Rule from Book: Don't sell the tool. Challenge the need. Ask why they need it. What is broken that requires this tool?
Strict Tone: Inquisitive, 'The Doctor.'
Structure:

Subject line: Context regarding your request for {value}

Opening: Acknowledge they feel they need {value}.

Core: 'Typically, companies only look for that feature when they are suffering from {pain}. Is that what is triggering this search, or is it something else?'

CTA: Ask to define the underlying problem before discussing the tool.

Generate the email.
"""
    },
    {
        "id": 96,
        "style": "The 'Pipeline Predictability' Check",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The deal was supposed to close yesterday. It didn't. You need to know if the deal is dead or just delayed.
Rule from Book: Don't beg. Assume something in their 'Current State' changed. Ask about their business, not your contract.
Strict Tone: Objective, detached.
Structure:

Subject line: Update on {value} timeline

Opening: 'We had this slated to kick off yesterday to meet your goal of {value}.'

Core: 'Since we missed that date, I assume something changed internally or a new priority emerged. Have you deprioritized fixing {pain}?'

CTA: Ask for the new reality.

Generate the email.
"""
    },
    {
        "id": 97,
        "style": "The 'Technical to Business' Pivot",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The technical buyer loves the product but can't get budget.
Rule from Book: Equip the technical buyer with business language. Connect their technical pain to the company's P&L.
Strict Tone: Strategic, coaching.
Structure:

Subject line: Building the business case for {value}

Opening: 'I know you see the value, but we need to articulate the business impact to get this approved.'

Core: 'We know that {pain} is annoying. But we need to calculate exactly how much money/productivity it costs the company. Can you help me estimate the revenue impact of {pain}?'

CTA: Ask for a quick call to build this ROI model together.

Generate the email.
"""
    },
    {
        "id": 98,
        "style": "The 'Referral by Value' Request",
        "text": """
Act as a Senior Sales Executive. You are writing to a satisfied client {title} at {company}.
Context: You just completed a review where they confirmed the 'Gap' is closed and they are seeing results.
Rule from Book: Leverage the specific problem solved. Ask if they know peers suffering from the same 'Current State.'
Strict Tone: Professional, specific.
Structure:

Subject line: Helping others with {pain}

Opening: 'I'm glad we were able to fix {pain} and hit {value} for you.'

Core: 'Do you know any other leaders in your network who are currently losing sleep over {pain} the way you were last year?'

CTA: Ask for a warm intro to help them solve it.

Generate the email.
"""
    },
    {
        "id": 99,
        "style": "The 'Emotional Anchor' Re-Engagement",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The deal is stalling. During discovery, they mentioned they were worried about their job security or burning out.
Rule from Book: Bring the 'Intrinsic Motivation' back to the forefront. Remind them that the status quo isn't just expensive; it's personally painful.
Strict Tone: Human, empathetic, serious.
Structure:

Subject line: Your goal to {value}

Opening: 'When we first spoke, you mentioned that {pain} was keeping you at the office until 8 PM every night.'

Core: 'I want to make sure we don't lose sight of the personal toll this situation is taking. If we stop now, that stress isn't going away.'

CTA: 'Are you ready to fix this, or are you accepting the current workload?'

Generate the email.
"""
    },
    {
        "id": 100,
        "style": "The 'Gap Summary' Pre-Close",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You are about to send the final contract. You want to anchor the value one last time.
Rule from Book: Summarize the Gap. Current State (Bad) vs. Future State (Good). The price is the bridge.
Strict Tone: Executive, confident, 'The Closer.'
Structure:

Subject line: Executive Summary: {value}

Opening: 'Before I send the agreement, I want to confirm we are aligned on the objective.'

Core: 'Current State: Losing money due to {pain}. Future State: Gaining {value}. The Investment: Price.'

CTA: 'If this accurately reflects the value we are delivering, look out for the agreement shortly.'

Generate the email.
"""
    },
    {
        "id": 101,
        "style": "The 'So What?' Chain",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: We are trying to pitch {value}, but we need to find the underlying value.
Rule from Book: Apply the 'So What?' concept. Do not mention the feature's technical specs. Instead, ask 'So what?' three times internally to arrive at the ultimate business consequence (e.g., saving time -> reducing overhead -> looking good to the board).
Strict Tone: Senior-to-senior, impatient but helpful.
Structure:

Subject line: 2-4 words, referencing the final 'So what?' benefit.

Opening: State the specific {pain} associated with the status quo.

Core: Present the solution only in terms of the ultimate business result (the 3rd 'So what').

CTA: A low-friction question about their current priority.

Generate the email.
"""
    },
    {
        "id": 102,
        "style": "The 'Dear Mom' Relaxation",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: We are reaching out cold, and we need to avoid sounding like a generic B2B robot.
Rule from Book: Apply the 'Dear Mom' concept (adapted for business). Write as if you are explaining the value to a smart friend, not a corporation. Strip all jargon, buzzwords (e.g., 'synergy', 'leverage'), and 'corporate voice.'
Strict Tone: Authentic, human, approachable, but authoritative.
Structure:

Subject line: A conversational hook (as if texting a colleague).

Opening: A direct observation about {industry}.

Core: Explain how we solve {pain} using simple, human language (Monosyllabic words preferred).

CTA: 'Worth a chat?' or similar soft ask.

Generate the email.
"""
    },
    {
        "id": 103,
        "style": "The 'You' Ratio Audit",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Following up after they downloaded a whitepaper on {industry}.
Rule from Book: Apply the 'Use You Promiscuously' concept. The email must use the words 'You' or 'Your' at least 4 times more often than 'I', 'We', or 'our company'. Focus entirely on their experience.
Strict Tone: Service-oriented, direct, focus on the recipient.
Structure:

Subject line: Benefit-driven headline focused on them.

Opening: Acknowledge their interest in {industry}.

Core: One insight from the whitepaper that applies to {company}'s specific situation.

CTA: Ask if they want the executive summary.

Generate the email.
"""
    },
    {
        "id": 104,
        "style": "The Active Voice Mandate",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: We need to re-engage a prospect who has gone dark.
Rule from Book: Apply the 'Active Voice' rule. Every sentence must follow a Subject-Verb-Object structure. Eliminate all forms of 'to be' (is, are, was, were) where possible. No 'It was decided' or 'There are.'
Strict Tone: High energy, decisive, urgent.
Structure:

Subject line: Action verb + {value}.

Opening: Reference the last interaction directly.

Core: State exactly what {value} does for {company} using strong verbs (e.g., 'slash,' 'drive,' 'ignite').

CTA: Binary question (Yes/No).

Generate the email.
"""
    },
    {
        "id": 105,
        "style": "The 'Show, Don't Tell' Principle",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Introducing our solution against a competitor they are currently using.
Rule from Book: Apply the 'Show, Don't Tell' concept. Do not use adjectives (e.g., 'better', 'faster', 'leading'). Instead, use a specific data point or a micro-case study involving competitor to prove the difference.
Strict Tone: Factual, objective, confident.
Structure:

Subject line: {value} vs competitor.

Opening: Acknowledgment of their current stack.

Core: A concrete example of how a peer achieved {value} using our method.

CTA: Ask to share the full case study.

Generate the email.
"""
    },
    {
        "id": 106,
        "style": "The 'Short Subject Line' Constraint",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Cold outreach to a high-value prospect.
Rule from Book: Apply the 'What Would You Open?' concept. The subject line must be under 50 characters and contain no more than 4 words. It must not look like a marketing blast.
Strict Tone: Brevity is king. Intriguing but not click-baity.
Structure:

Subject line: < 4 words, lower case, relevant to {pain}.

Opening: One sentence connecting {pain} to {industry}.

Core: Two sentences max on our unique value proposition.

CTA: 'Open to a 5-min brief?'

Generate the email.
"""
    },
    {
        "id": 107,
        "style": "The 'One Sentence Paragraph'",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Trying to get a referral to the right decision-maker.
Rule from Book: Apply the 'Readability' rule. No paragraph may be longer than one sentence. Use white space to create momentum. Start sentences with conjunctions (And/But) if necessary to keep flow.
Strict Tone: punchy, respectful of time, visual.
Structure:

Subject line: Referral?

Opening: Single sentence stating who I am looking for.

Core: Three single-sentence paragraphs explaining why I need to speak to the person handling {pain}.

CTA: 'Can you point me to the best person?'

Generate the email.
"""
    },
    {
        "id": 108,
        "style": "The 'Newsjacking' Hook",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: A major regulatory change or industry shift ({industry}) has just occurred.
Rule from Book: Apply the 'Newsjacking' concept. Use the {industry} as the immediate hook. Pivot immediately to how that event impacts {company}'s bottom line and how we mitigate that risk.
Strict Tone: Timely, urgent, expert.
Structure:

Subject line: {industry} and {company}.

Opening: 'Saw the news about {industry}...'

Core: Insight on how this changes their risk profile regarding {pain}.

CTA: Offer a specific piece of data/content regarding the event.

Generate the email.
"""
    },
    {
        "id": 109,
        "style": "The 'Cross Out the Wrong Words' Edit",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: A check-in email with a prospect who is stalling.
Rule from Book: Apply the 'Cross Out the Wrong Words' concept. Write a draft, then strip every adverb (e.g., 'really,' 'just') and every filler phrase (e.g., 'I am writing to you to...'). The final output must be under 50 words total.
Strict Tone: Zero fluff. Direct.
Structure:

Subject line: {value} update.

Opening: State the status of the deal.

Core: Ask the one blocker question preventing the signature.

CTA: None (let the question hang).

Generate the email.
"""
    },
    {
        "id": 110,
        "style": "The 'Start with a Question' Lede",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Prospecting a company that is likely overspending on {pain}.
Rule from Book: Apply the 'Good Lede' concept by starting the email immediately with a provocative, non-rhetorical question about their current process. Do not use 'Hi {title}' or preamble.
Strict Tone: Challenger sale, inquisitive, slightly provocative.
Structure:

Subject line: Question regarding {pain}.

Opening: The provocative question.

Core: Data point suggesting they are overpaying.

CTA: 'Does this align with what you're seeing?'

Generate the email.
"""
    },
    {
        "id": 111,
        "style": "The 'Pathological Empathy' Pivot",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect has delayed the deal citing 'bad timing' or 'too busy' (Objection Handling).
Rule from Book: Apply the 'Pathological Empathy' concept. Do not push back immediately. First, validate their specific pressure (e.g., end of quarter, restructuring) to show you get it. Then, pivot to how {value} specifically alleviates that exact pressure, rather than adding to it.
Strict Tone: Empathetic, patient, but logical.
Structure:

Subject line: Timing and {company}.

Opening: Validate their constraint (the 'busy' objection) without judgement.

Core: Explain why delaying actually increases their workload/risk regarding {pain}.

CTA: 'Does it make sense to revisit this in [Month], or is this a priority to fix now?'

Generate the email.
"""
    },
    {
        "id": 112,
        "style": "The 'Familiar Analogy' Bridge",
        "text": """
Act as a Senior Sales Executive. You are writing to a non-technical C-Level Exec at {company}.
Context: Explaining a complex technical concept or architecture ({value}) that differentiates us from competitors.
Rule from Book: Apply the 'Familiar Yet Surprising Analogy' concept. Do not use technical jargon. Frame the {value} using a real-world analogy (e.g., 'It's like the difference between renting a DVD and streaming Netflix').
Strict Tone: Educational, high-level, clarifying.
Structure:

Subject line: {value} in plain English.

Opening: Acknowledge the complexity of the market.

Core: The Analogy—explain why our approach is faster/safer using the comparison.

CTA: Ask for a brief call to validate the business case.

Generate the email.
"""
    },
    {
        "id": 113,
        "style": "The 'Data Before Declaration' Proof",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Early-stage prospecting to a skeptic.
Rule from Book: Apply the 'Data Before Declaration' concept. Do not say 'We are the best.' Start with a hard statistic or research finding from a third party regarding {industry}. Then, declare how {company} addresses that stat.
Strict Tone: Objective, analytical, authoritative.
Structure:

Subject line: Data regarding {industry}.

Opening: Cite the specific data point/statistic.

Core: Connect that data point to {company}'s likely reality and our solution.

CTA: 'Worth a deeper dive into this data?'

Generate the email.
"""
    },
    {
        "id": 114,
        "style": "The 'Frankenspeak' Detox",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Re-engaging a lead that has gone cold after receiving marketing nurturing emails.
Rule from Book: Apply the 'Avoid Frankenspeak' concept. Review a typical corporate pitch and strip it. Use zero buzzwords (e.g., 'synergy,' 'paradigm,' 'holistic'). Use only 'Real Words' (Chapter 29) to ask if they still have the problem.
Strict Tone: Blunt, human, zero-fluff.
Structure:

Subject line: {pain}?

Opening: Direct acknowledgement that we haven't spoken in a while.

Core: Ask if {pain} is still a problem, using plain English.

CTA: Yes/No question on closing the file.

Generate the email.
"""
    },
    {
        "id": 115,
        "style": "The 'Biased and Balanced' Compare",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect is evaluating us against competitor.
Rule from Book: Apply the 'Biased and Balanced' concept. Acknowledge competitor exists and is good at [X]. However, pivot immediately to why our 'bias' toward [Y strategy] is critical for {company}'s specific goals.
Strict Tone: Confident, fair, distinctive.
Structure:

Subject line: Us vs. competitor.

Opening: Validate their due diligence.

Core: The 'Balanced' admission (Competitor is okay at X) followed by the 'Biased' pivot (But we focus on Y, which matters more because...).

CTA: Ask to walk them through a side-by-side comparison.

Generate the email.
"""
    },
    {
        "id": 116,
        "style": "The 'Specific Noun' Dignity",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Sharing a case study to move a deal forward (Mid-funnel).
Rule from Book: Apply the 'Specific Noun' concept. Do not say 'we helped a client.' Say 'we helped a client.' Do not say 'we got results.' Say 'we saved them {value}.' Give things the dignity of their names.
Strict Tone: Narrative, proof-based, proud.
Structure:

Subject line: How a client solved {pain}.

Opening: Relevance to {company}'s current stage.

Core: The specific story of the peer customer (using specific nouns/numbers).

CTA: 'Want to see the full roadmap they used?'

Generate the email.
"""
    },
    {
        "id": 117,
        "style": "The 'WD-40' Deadline",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: End of quarter/month closing. The deal is stalling.
Rule from Book: Apply the 'Deadlines are WD-40' concept. Establish a hard time constraint or 'cliff' for the current terms to force a decision. Be stern but professional.
Strict Tone: Professional, final, time-sensitive.
Structure:

Subject line: Timeline for {value}.

Opening: State the current status and the approaching deadline.

Core: The consequence of missing the deadline (loss of pricing, implementation slot, etc.).

CTA: 'Should I send the paperwork today, or push this to Q3?'

Generate the email.
"""
    },
    {
        "id": 118,
        "style": "The 'Mobile 12-Word' Limit",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Trying to get a meeting with a CEO who reads email on their phone.
Rule from Book: Apply the '12-Word Line' concept. No single line of text in the email body can exceed 12 words. This creates a narrow, vertical visual path that is easy to scan on a phone.
Strict Tone: Extremely concise, respectful of attention span.
Structure:

Subject line: {value}.

Opening: One short sentence (under 12 words).

Core: Two bullet points (under 12 words each).

CTA: One short question (under 12 words).

Generate the email.
"""
    },
    {
        "id": 119,
        "style": "The 'Curiosity Gap' Hook",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Cold outreach where we have identified a specific error or opportunity in their business.
Rule from Book: Apply the 'Curiosity Gap' concept (with moderation). The subject line must promise a specific benefit but withhold the 'how' until they open. Do not use hyperbole (clickbait); use specific utility.
Strict Tone: Helpful, intriguing, professional.
Structure:

Subject line: The one thing missing from your {pain}.

Opening: I was reviewing your {pain} and noticed an error/opportunity.

Core: Explain the impact of fixing this specific thing.

CTA: 'Mind if I send over a screenshot/report ?'

Generate the email.
"""
    },
    {
        "id": 120,
        "style": "The 'Useful x Inspired x Empathic' Formula",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: value-add follow-up (nurturing) to keep the relationship warm.
Rule from Book: Apply the 'Quality Content Formula'.

Utility: Send them a tool/calculator/template (not just a blog post).

Inspiration: It must look professional/well-designed.

Empathy: Frame it entirely around making their job easier.
Strict Tone: Generous, high-value, low-pressure.
Structure:

Subject line: A tool for {pain}.

Opening: 'Saw this and thought of your project regarding {industry}.'

Core: Link to the tool and one sentence on how to use it to save time.

CTA: 'Hope it helps.' (No hard ask).

Generate the email.
"""
    },
    {
        "id": 121,
        "style": "The 'Reader Swap' Audit",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Cold outreach. We want to introduce a new solution.
Rule from Book: Apply the 'Swap Places with Your Reader' concept. Be a skeptic of your own draft. Remove any sentence that starts with 'I', 'We', or 'Our Company'. Every sentence must address the reader's perspective, answering 'What experience is this creating for them?'
Strict Tone: Skeptical, value-focused, devoid of ego.
Structure:

Subject line: The specific {value} they care about.

Opening: Statement about their current environment/challenge (no 'I noticed...').

Core: How their day-to-day changes with {value}.

CTA: 'Is this a priority for {company} right now?'

Generate the email.
"""
    },
    {
        "id": 122,
        "style": "The 'Real Words' Mandate",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Explaining a strategic shift or complex value proposition.
Rule from Book: Apply the 'Use Real Words' concept. Do not use words like 'revolutionary,' 'cutting-edge,' 'leverage,' or 'incentivize.' Replace them with standard, plain English (e.g., instead of 'leverage,' use 'use').
Strict Tone: Plain-spoken, confident, senior.
Structure:

Subject line: Plain summary of the topic.

Opening: Direct statement of the idea.

Core: Explanation of the value using only monosyllabic or common words.

CTA: Simple question regarding interest.

Generate the email.
"""
    },
    {
        "id": 123,
        "style": "The 'Brand Journalist' Interview",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Breaking the ice with a high-value target who ignores standard pitches.
Rule from Book: Apply the 'Brand Journalism' concept. Do not pitch. Act as a reporter covering the industry. Ask for their commentary or quote on a specific {industry} for a piece you are writing.
Strict Tone: Professional, flattering, inquisitive.
Structure:

Subject line: Question regarding {industry}.

Opening: Reference their status as a thought leader.

Core: Ask one specific, non-obvious question about {industry} (Chapter 50).

CTA: 'Open to sharing a quick thought on this?'

Generate the email.
"""
    },
    {
        "id": 124,
        "style": "The 'Visual Evidence' Tactic",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Mid-funnel. Trying to prove ROI or efficiency gains.
Rule from Book: Apply the 'Infographic/Visual' concept. Do not write a wall of text. The email exists solely to deliver a specific chart or graph (attached or linked) that visualizes the data.
Strict Tone: Minimalist, helpful.
Structure:

Subject line: {value} [Chart].

Opening: 'Thought this data might be useful for your planning.'

Core: Reference the attachment/image which shows {value}.

CTA: 'Does this match what you are seeing internally?'

Generate the email.
"""
    },
    {
        "id": 125,
        "style": "The 'Anti-Preach' Correction",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Educating a prospect on a risk they are ignoring.
Rule from Book: Apply the 'Limit Moralizing' concept. Eliminate prescriptive phrases like 'You should,' 'Never,' or 'Remember to.' Rephrase the risk as an observation or a trend seen elsewhere, not a command.
Strict Tone: Collaborative, peer-to-peer, objective.
Structure:

Subject line: Observation regarding {pain}.

Opening: State what we are seeing in the market.

Core: Describe the impact of {pain} without telling them what to do.

CTA: 'Worth discussing?'

Generate the email.
"""
    },
    {
        "id": 126,
        "style": "The 'Tweet-Style' Dialogue",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: A 'nudge' email to a busy executive.
Rule from Book: Apply the 'Twitter Dialogue' concept. Write as if you are speaking to a colleague. No preamble. Maximum 280 characters (approximate). Focus on starting a conversation, not broadcasting a pitch.
Strict Tone: Casual, sharp, fast.
Structure:

Subject line: Quick question.

Opening/Core: A single sentence or two connecting {industry} to {value}.

CTA: 'Thoughts?'

Generate the email.
"""
    },
    {
        "id": 127,
        "style": "The 'Kicker' Close",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Closing a thread or moving to the next step after a meeting.
Rule from Book: Apply the 'Good Kicker' concept. The final sentence (before the CTA) must be the strongest part of the email—a synthesizing summary or a high-value thought that lingers.
Strict Tone: Memorable, confident.
Structure:

Subject line: Recap / Next steps.

Opening: Summary of the meeting/discussion.

Core: Action items.

Kicker: A powerful statement summarizing the value of the partnership.

CTA: Confirming the timeline.

Generate the email.
"""
    },
    {
        "id": 128,
        "style": "The 'Raw & Authentic' Draft",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Sharing a sudden idea or realization relevant to their business.
Rule from Book: Apply the 'Embrace the Rough Draft' spirit. Write an email that feels like it was typed on an iPhone between meetings. Short, slightly informal, focusing on the idea rather than perfect polish.
Strict Tone: Spontaneous, excited, authentic.
Structure:

Subject line: Idea regarding {value}.

Opening: 'I was just thinking about {pain}...'

Core: Share a specific, unpolished idea to solve it.

CTA: 'Want to bounce this around for 5 mins?'

Generate the email.
"""
    },
    {
        "id": 129,
        "style": "The 'Permission Marketing' Approach",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Prospecting. We have a high-value asset (Audit/Report) we want to send.
Rule from Book: Apply the 'Seek Permission' concept. Do not attach the asset. Describe the value of the asset and ask for permission to send it. This builds a micro-commitment.
Strict Tone: Respectful, high-value.
Structure:

Subject line: {value}.

Opening: We have built a {value} specifically for {company}.

Core: One sentence on what the asset reveals about their business.

CTA: 'Do I have permission to send this over?'

Generate the email.
"""
    },
    {
        "id": 130,
        "style": "The 'Citation' Authority",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Validating the urgency of a problem they are ignoring.
Rule from Book: Apply the 'Cite as you Write' concept. Use a Primary Source (e.g., a Forrester report, a government regulation, a raw data set) to prove the problem exists. Link directly to the source.
Strict Tone: Academic yet actionable, trusted advisor.
Structure:

Subject line: New data from {industry}.

Opening: Quote the specific finding from the primary source.

Core: Explain the implication of that finding for {company}.

CTA: Ask to discuss the mitigation strategy.

Generate the email.
"""
    },
    {
        "id": 131,
        "style": "The 'Weakling Verb' Purge",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: A follow-up email after a demo to reiterate value.
Rule from Book: Apply the 'Ditch Weakling Verbs' concept. Scan the draft for verbs like 'help,' 'allow,' 'provide,' or 'assist.' Replace them exclusively with power verbs like 'accelerate,' 'eliminate,' 'capture,' or 'maximize.'
Strict Tone: High-impact, confident, active.
Structure:

Subject line: {value} (Active Verb).

Opening: Recap the goal of the demo.

Core: Three bullets describing the outcome using only strong verbs.

CTA: 'Ready to launch?'

Generate the email.
"""
    },
    {
        "id": 132,
        "style": "The 'Running Start' Cut",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Cold outreach to a busy C-Level executive.
Rule from Book: Apply the 'Cover Your Tracks' concept. Write a standard intro (e.g., 'I am writing to you because...'), then delete it. Start the email with the second paragraph—the actual point.
Strict Tone: Abrupt but respectful, efficient.
Structure:

Subject line: {value}.

Opening: Immediately state the opportunity or cost of inaction (No pleasantries).

Core: How we execute on that opportunity.

CTA: 'Are you the right person to speak to?'

Generate the email.
"""
    },
    {
        "id": 133,
        "style": "The 'Broken Rule' Opener",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Follow-up to a prospect who is hesitating on a decision.
Rule from Book: Apply the 'Break Grammar Rules' concept. Start the email with 'But' or 'And' to create immediate momentum and connection to previous conversations. Avoid formal transitions.
Strict Tone: Conversational, urgent, persuasive.
Structure:

Subject line: One question regarding the delay.

Opening: Start with 'But...' to address their hesitation directly.

Core: Reframe the risk of waiting.

CTA: 'Shall we proceed?'

Generate the email.
"""
    },
    {
        "id": 134,
        "style": "The 'Simple but not Simplistic' Explanation",
        "text": """
Act as a Senior Sales Executive. You are writing to a CFO or {title} at {company}.
Context: Justifying the price/investment of our solution.
Rule from Book: Apply the 'Simple but not Simplistic' concept. Deconstruct the complex pricing model into a simple 'If X, then Y' business equation. Use plain language to explain the return.
Strict Tone: Financial, logical, clear.
Structure:

Subject line: ROI on {value}.

Opening: Acknowledge the investment size.

Core: The simple math equation (Cost vs. Cost of Inaction).

CTA: 'Does this math align with your budget cycle?'

Generate the email.
"""
    },
    {
        "id": 135,
        "style": "The 'Hidden Agenda' Callout",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The deal is stalled, likely due to an internal blocker or incumbent vendor (incumbent).
Rule from Book: Apply the 'Awareness of Hidden Agendas' concept. Tactfully acknowledge the difficulty of replacing incumbent or navigating internal politics. Follow the money/influence.
Strict Tone: Empathetic, savvy, 'insider' tone.
Structure:

Subject line: Incumbent vs. our company.

Opening: 'I suspect the hold-up might be related to incumbent...'

Core: Validate that changing vendors is hard, then offer a low-risk way to test us without ripping out the incumbent yet.

CTA: 'Open to a pilot alongside them?'

Generate the email.
"""
    },
    {
        "id": 136,
        "style": "The 'Moralizing' Removal",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Reminding a prospect to sign a contract or complete a task.
Rule from Book: Apply the 'Limit Moralizing' concept. Strip out phrases like 'Just a reminder,' 'Don't forget,' or 'You need to.' State the status of the project neutrally and the consequence of the next step.
Strict Tone: Neutral, professional, equal-footing.
Structure:

Subject line: {value} status.

Opening: State exactly where the contract sits.

Core: The impact on the timeline if signed today vs. next week.

CTA: Link to the document.

Generate the email.
"""
    },
    {
        "id": 137,
        "style": "The 'Showcase' Narrative",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Approaching a contract renewal or upsell opportunity.
Rule from Book: Apply the 'Annual Wrap-Up' storytelling concept. Do not just ask for the renewal. Briefly recount the story of what we achieved together in the last year (Successes), then pivot to the 'vision' for the next year.
Strict Tone: Celebratory, forward-looking, strategic.
Structure:

Subject line: This year in review / Next year strategy.

Opening: One sentence on the biggest win of the past term.

Core: The vision for the next stage of growth (the upsell).

CTA: 'Time to discuss the roadmap?'

Generate the email.
"""
    },
    {
        "id": 138,
        "style": "The 'Embrace the Ugly' Re-engagement",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect has ghosted after three professional follow-ups.
Rule from Book: Apply the 'Embrace the Ugly/Humor' concept. Admit that you may have missed the mark or been too persistent. Drop the corporate facade completely to get a human response.
Strict Tone: Humble, authentic, disarming.
Structure:

Subject line: I might be wrong.

Opening: Acknowledge the radio silence.

Core: Ask if the priority has shifted or if you just missed the mark on the value prop.

CTA: 'Should I close this file?'

Generate the email.
"""
    },
    {
        "id": 139,
        "style": "The 'Lists and Bullets' Scan",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Explaining the implementation process to reassure them it won't be painful.
Rule from Book: Apply the 'Rabid about Readability' concept. Use a numbered list or bullets. Keep every bullet under one line. Ensure plenty of white space.
Strict Tone: Organized, efficient, reassuring.
Structure:

Subject line: Onboarding {company} (3 Steps).

Opening: 'Here is exactly what the rollout looks like.'

Core: 3-step numbered list (Active verbs).

CTA: 'Does this timeline work?'

Generate the email.
"""
    },
    {
        "id": 140,
        "style": "The 'Specific Audience' Exclusion",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Qualification stage. We need to ensure they are a good fit before spending resources.
Rule from Book: Apply the 'Speak to your Audience' (Exclusion) concept. Explicitly state who this product is NOT for (e.g., companies without X, or teams smaller than Y). This builds trust.
Strict Tone: Selective, exclusive, honest.
Structure:

Subject line: Fit for {company}?

Opening: 'We typically only partner with organizations that...'

Core: Explicitly state the criteria. If they don't meet it, we shouldn't waste their time.

CTA: 'Do you fit that profile?'

Generate the email.
"""
    },
    {
        "id": 141,
        "style": "The 'Chainsaw' Edit",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: A 'restart' email to a high-value prospect who went silent 3 months ago.
Rule from Book: Apply the 'Editing by Chainsaw' concept. Write a standard follow-up, then slash 70% of it. Remove all background context, 'checking in' phrases, and recap. Keep only the new value trigger.
Strict Tone: Ultra-brief, confident, low-pressure.
Structure:

Subject line: {value} at {company}.

Opening: One sentence stating the new trigger event/feature.

Core: One sentence on why this matters to them specifically.

CTA: 'Worth a look?'

Generate the email.
"""
    },
    {
        "id": 142,
        "style": "The 'Customer as Hero' Narrative",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Painting a vision of the future state to close a deal.
Rule from Book: Apply the 'It Serves the Customer' story rule. The customer must be the hero. Do not describe our product's features; describe {title}'s future success and status after using the product.
Strict Tone: Visionary, inspiring, partner-focused.
Structure:

Subject line: {company}'s next phase.

Opening: Acknowledge their current ambition/goal.

Core: Paint a picture of the future state where {pain} is gone and they are succeeding (using our tool in the background).

CTA: 'Ready to start this journey?'

Generate the email.
"""
    },
    {
        "id": 143,
        "style": "The 'Cliché' Purge",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Differentiating our solution from a commoditized market full of buzzwords.
Rule from Book: Apply the 'Use Clichés Only Once in a Blue Moon' concept (by avoiding them entirely here). Scan for sales clichés (e.g., 'best in class,' 'game changer,' 'one-stop-shop') and replace them with specific, descriptive aphorisms or plain facts.
Strict Tone: Sophisticated, fresh, distinctive.
Structure:

Subject line: A non-clichéd benefit statement.

Opening: Acknowledge the noise in the {industry}.

Core: Describe our value using fresh, original metaphors or precise data (no jargon).

CTA: Specific question about their strategy.

Generate the email.
"""
    },
    {
        "id": 144,
        "style": "The 'Always Be Helping' Handshake",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Warm outreach (Social Selling) to a connection who recently posted about a challenge.
Rule from Book: Apply the 'Always Be Helping' concept. Do not pitch the product. Offer a piece of advice, a connection, or a resource that solves the immediate problem they posted about, with no expectation of return.
Strict Tone: Generous, peer-to-peer, helpful.
Structure:

Subject line: Idea for your post regarding {industry}.

Opening: Reference their recent LinkedIn post/comment.

Core: Offer a specific resource or idea to help (not our product).

CTA: 'Happy to send more info if that's useful.'

Generate the email.
"""
    },
    {
        "id": 145,
        "style": "The 'Trust Indicator' Stack",
        "text": """
Act as a Senior Sales Executive. You are writing to a risk-averse {title} at {company}.
Context: The prospect likes the product but is worried about security/implementation risk.
Rule from Book: Apply the 'Use Trust Indicators' concept. Do not make promises; show proof. List certifications, security standards, or the volume of similar companies (Social Proof) currently using the platform to de-risk the decision.
Strict Tone: Reassuring, factual, solid.
Structure:

Subject line: Security and scale at our company.

Opening: Validate their concern about risk.

Core: Three bullet points of 'Trust Indicators' (e.g., SOC2, specific client names, uptime stats).

CTA: 'Does this satisfy the compliance team?'

Generate the email.
"""
    },
    {
        "id": 146,
        "style": "The 'Tone Adjustment' Pivot",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Addressing a service hiccup or a missed deadline during the pilot phase.
Rule from Book: Apply the 'Voice and Tone' concept. Shift from our usual 'Sales/Excitement' tone to a 'Helpful/Serious' tone. Be transparent, apologize without being weak, and focus on the fix.
Strict Tone: Serious, accountable, solution-oriented.
Structure:

Subject line: Issue with {value}.

Opening: Direct admission of the issue.

Core: The specific fix and the timeline (No excuses).

CTA: 'Are you free for a brief update call?'

Generate the email.
"""
    },
    {
        "id": 147,
        "style": "The 'One Person' Visualization",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Account-Based Marketing (ABM) outreach to a specific decision-maker.
Rule from Book: Apply the 'Write to One Person' concept. Do not write to a persona; write to this specific human. Mention a detail about their specific office location, a recent award, or a unique aspect of their role.
Strict Tone: Intimate (professional), researched, specific.
Structure:

Subject line: {title} and {industry}.

Opening: Connect a dot between their specific role and a trend in {industry}.

Core: How we help people in their exact seat (not just their department).

CTA: Low-friction chat request.

Generate the email.
"""
    },
    {
        "id": 148,
        "style": "The 'Scrupulously Trustworthy' Correction",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect believes a myth about our product (e.g., 'it's too expensive' or 'it doesn't integrate').
Rule from Book: Apply the 'Tell the Truth' concept. Acknowledge the root of the misconception (fairness), then provide the exact data/fact that disproves it. Do not attack the source of the rumor.
Strict Tone: Calm, factual, transparent.
Structure:

Subject line: Clarification on {pain}.

Opening: 'I wanted to address the concern regarding {pain}...'

Core: The hard data/fact that corrects the record. Acknowledge where we are weak if necessary to build credibility on where we are strong.

CTA: 'Does that clarify the capability?'

Generate the email.
"""
    },
    {
        "id": 149,
        "style": "The 'Humor on the Rewrite'",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Fourth follow-up attempt. They are ignoring us.
Rule from Book: Apply the 'Humor Comes on the Rewrite' concept. Write a standard follow-up, then inject a parenthetical aside or a witty, self-deprecating observation to show personality and break the tension.
Strict Tone: Persistent, light-hearted, human.
Structure:

Subject line: Persistence (and {value}).

Opening: Acknowledge the persistence.

Core: The value prop, followed by a humorous acknowledgement of how annoying sales emails can be.

CTA: 'Stay or go?'

Generate the email.
"""
    },
    {
        "id": 150,
        "style": "The 'About Us' Paradox",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The 'Why our company?' email (Differentiation).
Rule from Book: Apply the 'About Us Paradox' concept. Do not list our history, founding date, or awards. Define our company entirely by the burdens we shoulder for the client (e.g., 'We are the people who ensure you never have to worry about X').
Strict Tone: Service-oriented, reliable, dedicated.
Structure:

Subject line: Why our company?

Opening: 'We exist to solve {pain}.'

Core: Define our identity by the specific problems we remove from their plate.

CTA: 'Does that align with your needs?'

Generate the email.
"""
    },
     {
        "id": 151,
        "style": "The 'Because' Justification",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You need to secure a 15-minute discovery meeting with a busy executive who does not know you.
Rule from Book: Apply the 'Power of Because' concept from Chapter 14. You must state exactly why you are contacting them and provide a specific reason ('because') that bridges to a WIIFM (What's In It For Them).
Strict Tone: Professional, concise, and devoid of fluff.
Structure:

Subject line: 3-4 words max, referencing a specific problem.

Opening: Identify yourself and state the purpose of the call immediately (Chapter 15/19).

Core: Connect a {pain} to a specific outcome using the word 'because' as the pivot point.

CTA: Direct ask for a specific time (e.g., 'Thursday at 2 PM').

Generate the email.
"""
    },
    {
        "id": 152,
        "style": "The 'Relate and Bridge' Framework",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: You are conducting a 'Conquest Prospect' outreach to a high-value target.
Rule from Book: Use the 4-Step Email Framework (Hook, Relate, Bridge, Ask). You cannot say you 'understand' their situation; you must demonstrate it by citing a peer scenario or industry trend.
Strict Tone: Peer-to-peer, authoritative.
Structure:

Hook: Compelling subject line + opening sentence citing {industry} or {value}.

Relate: Mention how other {title}s are struggling with {pain}.

Bridge: Connect the dots between that struggle and your solution's specific result.

Ask: Low-risk request for a conversation (not a demo).

Generate the email.
"""
    },
    {
        "id": 153,
        "style": "The Trigger Event Opener",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: {company} just experienced a {industry} (e.g., merger, new CTO, earnings release).
Rule from Book: Leverage 'Trigger-Event Awareness.' Do not congratulate them emptily. Use the event as the immediate context for how it changes their risk profile or needs regarding {value}.
Strict Tone: Urgent but sophisticated.
Structure:

Subject line: Reference the {industry} directly.

Opening: Acknowledge the event and immediately pivot to its implication (The Problem).

Core: Explain how you help companies navigate this specific transition.

CTA: Ask for time to share insights relevant to the transition.

Generate the email.
"""
    },
    {
        "id": 154,
        "style": "The 'Brush-Off' Disruption",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: You called, and they gave you the brush-off: 'Just send me some information.'
Rule from Book: Apply the 'Disrupt' technique. Do not just attach a PDF. Call their bluff by agreeing but asking a clarifying question to force engagement.
Strict Tone: Helpful but firm.
Structure:

Subject line: 'As requested' or 'Your information'.

Opening: Confirm you are happy to send the info.

Core: State that to ensure you don't waste their time with irrelevant info, you need to know specifically which aspect of {value} matters most to them.

CTA: Ask them to reply with their specific priority so you can curate the resource.

Generate the email.
"""
    },
    {
        "id": 155,
        "style": "The Mobile-First 'Glimpse Factor'",
        "text": """
Act as a Senior Sales Executive. You are writing to a busy {title} at {company}.
Context: Cold outreach where the prospect will likely view this on an iPhone.
Rule from Book: Optimize for the 'Glimpse Factor.' The subject line must be under 40 characters. The first sentence must not be a salutation or 'I hope you are well.' It must be the hook.
Strict Tone: Brevity is the soul of wit.
Structure:

Subject line: 3-5 words maximum. No questions.

Opening: Go straight to the {value}.

Core: One sentence on how you solve {pain}.

CTA: Yes/No question (e.g., 'Are you open to discussing this?').

Generate the email.
"""
    },
    {
        "id": 156,
        "style": "The Text Message Anchor",
        "text": """
Act as a Senior Sales Executive. You are texting a {title} you just met at {industry}.
Context: You exchanged business cards and agreed vaguely to 'connect later.'
Rule from Book: Follow the 'Texting Rules' from Chapter 20. Identify yourself immediately. No abbreviations (no 'u', 'thx', 'lol'). Complete sentences.
Strict Tone: Professional and polite.
Structure:

ID: 'Hi {title}, this is [My Name] from [My Company].'

Core: 'Great meeting you at {industry} today.'

CTA: 'I’ll send a calendar invite for the follow-up we discussed. Does Tuesday work?'

Generate the text message.
"""
    },
    {
        "id": 157,
        "style": "The Referral Leverage",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: [Referrer Name], a mutual contact or current client, suggested you contact this person.
Rule from Book: Maximize the 'Law of Familiarity.' The subject line must be the Referrer's name. The opening must explicitly state the Referrer suggested the connection.
Strict Tone: Confident and expectant (Social Proof).
Structure:

Subject line: '[Referrer Name] suggested we talk'.

Opening: '[Referrer Name] mentioned you are looking into {value} and asked me to reach out.'

Core: Briefly mention the result you achieved for [Referrer Name] or {industry}.

CTA: Ask for a brief call to share those specific results.

Generate the email.
"""
    },
    {
        "id": 158,
        "style": "The 'Gatekeeper Bypass' InMail",
        "text": """
Act as a Senior Sales Executive. You are writing a LinkedIn InMail to {title} at {company}.
Context: You cannot get through the phone gatekeeper, so you are moving to the social channel.
Rule from Book: Social Selling is not for 'pitching.' It is for building familiarity. Do not sell the product; sell the conversation.
Strict Tone: Conversational and low-pressure.
Structure:

Context: Mention you've been trying to reach them regarding {value}.

Value: Offer a piece of 'Content Curation' (Chapter 13)—a white paper or article relevant to {industry}.

CTA: 'I thought this would be relevant to you. Worth a chat next week?'

Generate the InMail.
"""
    },
    {
        "id": 159,
        "style": "The T-Call Follow-Up",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: You just utilized the 'T-Call' technique and physically walked into their office. You spoke briefly with them or the gatekeeper but couldn't hold a full meeting.
Rule from Book: Build familiarity. Connect the face they just saw to your name and brand.
Strict Tone: Friendly and persistent.
Structure:

Subject line: 'Stopping by / {company}'.

Opening: 'Great to meet you/your team briefly today.'

Core: Reiterate the one specific {value} you mentioned in person.

CTA: 'Since I caught you at a busy time, I will call you [Day of Week] to schedule a proper conversation.'

Generate the email.
"""
    },
    {
        "id": 160,
        "style": "The 'Internal Referrer' Hack",
        "text": """
Act as a Senior Sales Executive. You are writing to a Sales Rep or Lower-Level Employee ({title}) at {company}.
Context: You are trying to find the person responsible for {pain}, but you are hitting walls.
Rule from Book: Appeal to their empathy (especially if they are in sales). Be honest and transparent about needing help.
Strict Tone: Humble and authentic.
Structure:

Subject line: 'Need a little help'.

Opening: Acknowledge you are lost in the phone tree/org chart.

Core: 'I'm trying to get some information to the person who handles {pain}. As a fellow sales professional, you know how hard it is to navigate these things.'

CTA: 'Could you point me toward the right person?'

Generate the email.
"""
    },
    {
        "id": 161,
        "style": "The 'Triple Threat' Follow-Up",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You just called them and left a voicemail 2 minutes ago.
Rule from Book: Apply the 'Triple Threat' concept. Do not re-pitch the whole product. Simply point them to the voicemail and reiterate the specific value prop (WIIFM) briefly.
Strict Tone: Efficient and connected.
Structure:

Subject line: 'Voicemail / {value}'.

Opening: 'I just left you a voicemail regarding {pain}.'

Core: Summarize the voicemail's value prop in one sentence (e.g., 'We successfully reduced overhead for [Competitor] by 12%.').

CTA: 'I’ll try you again on [Day], or feel free to reply here if that is easier.'

Generate the email.
"""
    },
    {
        "id": 162,
        "style": "The 'Happy Customer' Turnaround",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: You spoke briefly, and they said, 'We are happy with [Current Competitor].'
Rule from Book: Use the 'Anchor, Disrupt, Ask' framework. Validate their decision (Anchor), disrupt by saying you don't want them to switch if they are happy, but ask to share insight on industry trends (Disrupt/Ask).
Strict Tone: Confident and non-threatening.
Structure:

Subject line: 'Regarding [Current Provider]'.

Opening: 'It is great to hear [Current Provider] is serving you well. You shouldn't switch if you are happy.'

Core: 'However, many {title}s keep a backup option or benchmark current rates against market shifts. I’d like to share a brief report on {industry} regardless of who you use.'

CTA: 'Are you open to seeing that report?'

Generate the email.
"""
    },
    {
        "id": 163,
        "style": "The 'Emotional Value' Message",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Cold outreach targeting a known industry pain point that causes personal stress to the buyer.
Rule from Book: Bridge to the 'Because' using Emotional Value. Use words like 'Frustrated,' 'Concerned,' 'Anxious,' or 'Peace of Mind.'
Strict Tone: Empathetic but business-focused.
Structure:

Subject line: '{pain} and Stress'.

Opening: 'Many {title}s I speak with are frustrated by {pain} because it drains resources.'

Core: 'We help leaders regain peace of mind by {value}.'

CTA: 'Let's schedule 10 minutes to discuss how we can remove this friction for your team.'

Generate the email.
"""
    },
    {
        "id": 164,
        "style": "The Meeting No-Show Recovery",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: They missed a scheduled discovery call 15 minutes ago.
Rule from Book: Be 'Assumptive.' Assume they got busy or had a fire to put down (don't guilt-trip), but firmly request a reschedule.
Strict Tone: Professional and forgiving, but expecting a reply.
Structure:

Subject line: 'Missed you / [Date Time]'.

Opening: 'I assume you got tied up with something critical.'

Core: 'I was looking forward to sharing how we can help you with {value}.'

CTA: 'When is the best time to reschedule this week?'

Generate the email.
"""
    },
    {
        "id": 165,
        "style": "The 'Buying Window' Nurture",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: They are a qualified lead but told you 'Not right now' due to budget/timing.
Rule from Book: Use 'Content Curation' (Chapter 13). Provide value without asking for anything in return (Law of Reciprocity).
Strict Tone: Helpful and 'In-the-know'.
Structure:

Subject line: 'Thought of you / {industry}'.

Opening: 'I saw this article on {industry} and thought of our last conversation regarding {value}.'

Core: 'It highlights [Key Insight] which might be relevant to your planning for Q4.'

CTA: No hard ask. Just 'Hope this helps.'

Generate the email.
"""
    },
    {
        "id": 166,
        "style": "The Referral Introduction Request",
        "text": """
Act as a Senior Sales Executive. You are writing to a current client [Client Name] at {company}.
Context: You just successfully delivered a project or result for them.
Rule from Book: Ask for the introduction. Don't hint. Be specific about the type of person you want to meet.
Strict Tone: Grateful but direct.
Structure:

Subject line: 'One favor'.

Opening: 'I am glad we were able to achieve {value} for you.'

Core: 'I am looking to help other companies in {industry} achieve similar results. Do you know anyone at [Target Company] or similar peers who are facing {pain}?'

CTA: 'Would you be open to making a brief email intro?'

Generate the email.
"""
    },
    {
        "id": 167,
        "style": "The 'One More Call' Quarter-End Push",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: It is the end of the quarter. You sent a proposal 2 weeks ago and it has gone quiet.
Rule from Book: Be 'Fanatical.' Don't wait. Strip away the fluff. Use the 'Assumptive' stance that they want to move forward but are just busy.
Strict Tone: Urgent and executive.
Structure:

Subject line: 'Timeline / {value}'.

Opening: 'We are entering the final days of the quarter.'

Core: 'To get {value} implemented by [Date], we need to finalize the paperwork by Friday.'

CTA: 'Are we still moving forward, or should I push the timeline to next quarter?'

Generate the email.
"""
    },
    {
        "id": 168,
        "style": "The Competitor Conquest (Differentiation)",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: You know they use [Competitor Name].
Rule from Book: Do not bash the competition. Differentiate based on a specific 'Business Objective' (e.g., risk, speed, ROI) that the competitor usually fails at.
Strict Tone: Objective and challenger-like.
Structure:

Subject line: 'ROI on [Current Tool]'.

Opening: 'I know you are currently using [Competitor Name].'

Core: 'Many of our clients switched from [Competitor Name] because they needed {value} which they weren't getting.'

CTA: 'Are you open to a 5-minute comparison on that specific metric?'

Generate the email.
"""
    },
    {
        "id": 169,
        "style": "The 'Video Email' Click-Through",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: You have recorded a 45-second personalized video analyzing their website/process.
Rule from Book: Don't explain the whole video in the text. Create curiosity (The Hook).
Strict Tone: Casual and intriguing.
Structure:

Subject line: 'Video for {title} / {pain}'.

Opening: 'I made a 45-second video analyzing your current {industry}.'

Core: 'I noticed one specific bottleneck regarding {pain} that might be costing you leads.'

CTA: 'Watch the video here: [Link]. Thoughts?'

Generate the email.
"""
    },
    {
        "id": 170,
        "style": "The Database 'Cleanup' (Timing Check)",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: You have sent 5 emails with no response.
Rule from Book: Remove the pressure. Allow them to say 'not now.' This cleans your pipeline (Chapter 5 - Law of Replacement).
Strict Tone: detached professional.
Structure:

Subject line: 'Permission to close file?'.

Opening: 'I haven't heard back, so I assume this isn't a priority right now.'

Core: 'I don't want to clutter your inbox if the timing is off.'

CTA: 'Should I hold off for now and reconnect next quarter?'

Generate the email.
"""
    },
    {
        "id": 171,
        "style": "The 'Maybe' Turnaround",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You had a demo/meeting, and they have gone silent or are giving vague 'maybe' signals regarding the next step.
Rule from Book: Don't accept 'maybe.' Use the 'Assumptive' stance to either get a 'yes' or a 'no' so you can move on (Chapter 16/23).
Strict Tone: Direct and binary (Yes/No).
Structure:

Subject line: 'Update on {value}'.

Opening: 'Based on our last conversation, it sounded like {value} was a priority for Q3.'

Core: 'Usually, when things go quiet, it means priorities have shifted.'

CTA: 'Is this project still alive, or should we close the file for now?'

Generate the email.
"""
    },
    {
        "id": 172,
        "style": "The 'New Role' Trigger",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} who just moved to {company}.
Context: You tracked this movement via LinkedIn or a news alert.
Rule from Book: Leverage the 'Window of Dissatisfaction.' New leaders want to shake up the status quo. Don't just say congrats; pivot to how you help them win early.
Strict Tone: Celebratory but strategic.
Structure:

Subject line: 'Congrats on the move to {company}'.

Opening: 'I saw the news regarding your new role. Congratulations.'

Core: 'Typically, leaders in your position look to implement {value} within the first 90 days to secure quick wins.'

CTA: 'Are you open to a brief chat about your 90-day roadmap?'

Generate the email.
"""
    },
    {
        "id": 173,
        "style": "The Inactive Customer Reactivation",
        "text": """
Act as a Senior Sales Executive. You are writing to a former client {title} at {company}.
Context: They haven't purchased in 12 months.
Rule from Book: Use the 'Law of Familiarity.' They know you. Remind them of previous success and offer a new reason (Because) to re-engage.
Strict Tone: Warm and service-oriented.
Structure:

Subject line: 'Catching up / {company}'.

Opening: 'I was reviewing our accounts and realized it has been a year since we worked together.'

Core: 'Since then, we have added {value} that specifically addresses {pain}.'

CTA: 'Do you have 5 minutes next week to catch up?'

Generate the email.
"""
    },
    {
        "id": 174,
        "style": "The Gatekeeper 'Honesty' Hack",
        "text": """
Act as a Senior Sales Executive. You are writing to an Executive Assistant {title} at {company}.
Context: You are trying to reach the [Executive Title], but cannot get on their calendar.
Rule from Book: Apply the 'Ask for Help' technique. Be transparent about who you are and why you want to talk. Treat the EA as a professional ally.
Strict Tone: Humble and professional.
Structure:

Subject line: 'Need your guidance'.

Opening: 'I tried to reach [Executive Name] but haven't been successful.'

Core: 'I specifically want to share a report on {industry} that impacts your industry. I don't want to be a nuisance.'

CTA: 'Could you tell me the best way to get 10 minutes on their calendar, or who else I should speak with?'

Generate the email.
"""
    },
    {
        "id": 175,
        "style": "The 'Social-to-Email' Bridge",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: You engaged with them on LinkedIn (commented on their post) yesterday.
Rule from Book: Layer your prospecting channels. Move the conversation from the social feed (public) to the inbox (private).
Strict Tone: Conversational transition.
Structure:

Subject line: 'Your post on LinkedIn'.

Opening: 'I really enjoyed your perspective on {industry} yesterday on LinkedIn.'

Core: 'It got me thinking about {value} and how we helped [Similar Company] solve that.'

CTA: 'Are you open to a continued conversation on this?'

Generate the email.
"""
    },
    {
        "id": 176,
        "style": "The 'Assumptive' Calendar Invite",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: You spoke on the phone, and they agreed vaguely to 'meet next week,' or you have a high-trust relationship.
Rule from Book: Be 'Assumptive.' Take the burden of scheduling off the prospect.
Strict Tone: Efficient and directive.
Structure:

Subject line: 'Placeholder: Discussion re: {value}'.

Opening: 'Great speaking with you earlier.'

Core: 'To keep us moving, I have sent a calendar invite for [Day/Time].'

CTA: 'If that time doesn't work, just reply with a better slot and I will update the invite.'

Generate the email.
"""
    },
    {
        "id": 177,
        "style": "The 'Targeted Bridge' (Industry Vertical)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} in the {industry} sector.
Context: You are prospecting 50 similar companies (Targeted List). You don't know their specific pain, but you know the industry pain.
Rule from Book: Use a 'Targeted Bridge.' Cite a trend affecting their specific vertical (e.g., regulatory changes, supply chain issues) to build credibility.
Strict Tone: Knowledgeable insider.
Structure:

Subject line: '{pain} and {company}'.

Opening: 'Most {title}s in the {industry} sector I speak with are currently struggling with {pain}.'

Core: 'We helped [Competitor/Peer] navigate this by {value}.'

CTA: 'Are you seeing similar trends at {company}?'

Generate the email.
"""
    },
    {
        "id": 178,
        "style": "The 'Post-Webinar' Strike",
        "text": """
Act as a Senior Sales Executive. You are writing to an Inbound Lead {title} at {company}.
Context: They attended your webinar/downloaded a whitepaper yesterday.
Rule from Book: Do not say 'Thanks for attending.' Pivot immediately to a 'Qualifying' question to see if they are a buyer or just a looker.
Strict Tone: Investigative.
Structure:

Subject line: 'Question re: {industry}'.

Opening: 'I saw you joined our session on {industry} yesterday.'

Core: 'Typically, people attend because they are dealing with {pain} or [Pain Point B].'

CTA: 'Which one spurred your interest?'

Generate the email.
"""
    },
    {
        "id": 179,
        "style": "The 'C-Level' Strategic Bridge",
        "text": """
Act as a Senior Sales Executive. You are writing to the CEO ({title}) of {company}.
Context: You read in the Wall Street Journal or an Annual Report that they are expanding into {industry} or launching {value}.
Rule from Book: Use the 'Strategic Bridge.' Connect their public strategic goal directly to your solution's outcome. High effort, high reward.
Strict Tone: Executive-to-Executive.
Structure:

Subject line: 'Your initiative regarding {industry}'.

Opening: 'I read your comments in [Publication] regarding the expansion into {industry}.'

Core: 'Navigating the risk of {pain} is critical in that region. We helped [Similar Company] mitigate that risk and launch 20% faster.'

CTA: 'Are you open to a brief conversation on how we supported that launch?'

Generate the email.
"""
    },
    {
        "id": 180,
        "style": "The 'Friday Afternoon' Hail Mary",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: It is Friday at 4:30 PM. You want to set up a meeting for the following week before the weekend starts.
Rule from Book: Be 'Fanatical.' Catch them when gatekeepers are gone. Keep it very short (mobile-optimized).
Strict Tone: Casual and breezy.
Structure:

Subject line: 'Next week'.

Opening: 'I know it is late on a Friday, so I will be brief.'

Core: 'I have an idea regarding {value} that could save you {value} in Q4.'

CTA: 'Does Tuesday at 10 AM work for a 10-minute chat?'

Generate the email.
"""
    },
    {
        "id": 181,
        "style": "The Trade Show 'Context Anchor'",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: You met them at {industry} two days ago.
Rule from Book: Use the 'Context Anchor.' Do not just say 'Great meeting you.' Reference one specific detail you discussed (personal or business) to prove you listened (Chapter 18).
Strict Tone: Personable but efficient.
Structure:

Subject line: '{industry} / The point you made about {value}'.

Opening: 'It was a pleasure meeting you at the booth on [Day].'

Core: 'I’ve been thinking about your comment regarding {value}. Here is the {value} I mentioned that addresses that.'

CTA: 'Are you still open to a 10-minute walkthrough next week?'

Generate the email.
"""
    },
    {
        "id": 182,
        "style": "The 'No Budget' Deflection",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: They replied to your outreach saying, 'We have no budget for this right now.'
Rule from Book: Disrupt the RBO. Don't argue price. Agree (Anchor), then suggest that budget cycles require business cases built now for later execution.
Strict Tone: Consultative and patient.
Structure:

Subject line: 'Budget cycles'.

Opening: 'I figured budget might be tight this time of year.'

Core: 'Most of my clients start building the business case 3–6 months before approval. If we wait until the budget opens, we lose time on implementation.'

CTA: 'Does it make sense to review the business case now so you are ready when the freeze lifts?'

Generate the email.
"""
    },
    {
        "id": 183,
        "style": "The 'Top-Down' Multi-Thread",
        "text": """
Act as a Senior Sales Executive. You are writing to a Mid-Level Manager {title} at {company}.
Context: Their boss, [Executive Name], told you to contact them.
Rule from Book: Leverage the 'Referral' hierarchy. Start the email with the boss's name. Make it clear this isn't a cold call; it's a directive.
Strict Tone: Authoritative and expectant.
Structure:

Subject line: 'Per [Executive Name]'.

Opening: 'I just spoke with [Executive Name] regarding {value}.'

Core: 'She asked me to reach out to you directly to schedule a brief review of our {value}.'

CTA: 'What does your calendar look like for Tuesday morning?'

Generate the email.
"""
    },
    {
        "id": 184,
        "style": "The Pre-Meeting Confirmation (No-Show Prevention)",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: You have a scheduled meeting in 24 hours.
Rule from Book: Don't just say 'Confirming our call.' Add value. State the agenda and provide a 'read-ahead' item to hook their interest (Curiosity).
Strict Tone: Organized and professional.
Structure:

Subject line: 'Agenda for tomorrow'.

Opening: 'Looking forward to our conversation tomorrow at [Time].'

Core: 'To make the best use of your time, I plan to cover {value} and {pain}. Attached is a one-pager context for the discussion.'

CTA: 'Does this agenda align with your goals?'

Generate the email.
"""
    },
    {
        "id": 185,
        "style": "The 'Status Quo' Disruptor",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: They are using a legacy system or manual process and feel 'safe' (Status Quo).
Rule from Book: Challenge the status quo. Use a specific insight or stat that suggests their current safety is actually a risk.
Strict Tone: Challenger/Provocative.
Structure:

Subject line: 'Risk regarding {pain}'.

Opening: 'You mentioned you are currently handling {pain} manually.'

Core: 'New data suggests that companies managing {pain} manually are leaking [X%] of revenue annually. It is a silent cost.'

CTA: 'Are you open to seeing the math on that calculation?'

Generate the email.
"""
    },
    {
        "id": 186,
        "style": "The Text Message Value-Drop",
        "text": """
Act as a Senior Sales Executive. You are texting a prospective buyer {title} whom you have spoken with before.
Context: You found an article relevant to their personal interests or industry.
Rule from Book: Build Familiarity/Nurture. No 'Ask.' Just value.
Strict Tone: Helpful peer.
Structure:

Opening: 'Hi {title}, saw this article on {industry} and thought of you.'

Value: '[Link]'

Closing: 'No need to reply, just thought you'd find it interesting. - [My Name]'

Generate the text message.
"""
    },
    {
        "id": 187,
        "style": "The 'Wrong Person' Correction",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: They replied saying, 'I don't handle X.'
Rule from Book: Don't apologize and leave. Use the interaction to get the right name (Data Gathering).
Strict Tone: Grateful and inquisitive.
Structure:

Subject line: 'My apologies / Clarification'.

Opening: 'Thanks for the quick reply. I assumed based on your title that you handled {title} (function).'

Core: 'My mistake. To ensure I don't clutter the wrong inbox again, who handles {title} (specific function) at {company}?'

CTA: 'Do you mind pointing me in their direction?'

Generate the email.
"""
    },
    {
        "id": 188,
        "style": "The 'Congratulations' Touch (Social/Email)",
        "text": """
Act as a Senior Sales Executive. You are writing an email (or LinkedIn note) to {title} at {company}.
Context: They just won an award or were mentioned in the press.
Rule from Book: Build Familiarity. Do not pitch. Just congratulate. This engages the Law of Reciprocity.
Strict Tone: Sincere and brief.
Structure:

Subject line: 'Saw the news about {value}'.

Opening: 'I saw the article in [Publication] regarding {value}.'

Core: 'It is great to see {company} getting recognized for {value}. Well done.'

CTA: 'I'll keep watching for more great news. Best, [My Name].'

Generate the email.
"""
    },
    {
        "id": 189,
        "style": "The 'Strip Line' (Going Negative)",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: You have had zero engagement after multiple attempts.
Rule from Book: Use the 'Strip Line.' Withdraw the offer. This is the final attempt before moving on.
Strict Tone: Final and professional.
Structure:

Subject line: 'Closing the file'.

Opening: 'I am writing to let you know I am closing your file regarding {value}.'

Core: 'I haven't heard back, so I assume your priorities have shifted away from {pain}.'

CTA: 'If you decide to address this in the future, let me know. Otherwise, I wish you the best.'

Generate the email.
"""
    },
    {
        "id": 190,
        "style": "The 'Anytime' Fallacy Correction",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: You spoke, and they said, 'I'm interested, give me a call anytime next week.'
Rule from Book: Secure the 'Golden Hours.' Do not leave it vague. Propose specific blocks to ensure the appointment happens.
Strict Tone: Directive.
Structure:

Subject line: 'Scheduling for next week'.

Opening: 'Per our conversation, I am following up to lock in a time.'

Core: 'My calendar fills up quickly, and I want to ensure we don't play phone tag. I have openings on Tuesday morning and Thursday afternoon.'

CTA: 'Does Tuesday at 9:00 AM work for you?'

Generate the email.
"""
    },
    {
        "id": 191,
        "style": "The 'Strategic Prospecting Campaign' (Touch 1)",
        "text": """
Act as a Senior Sales Executive. You are writing to a C-Level Executive {title} at {company}.
Context: This is the first touch of a 'Strategic Prospecting Campaign' (SPC) for a high-value target.
Rule from Book: Use the 'Strategic Bridge' (Chapter 14). You must connect a specific company initiative found in their 10-K or press release to a risk they are facing.
Strict Tone: Strategic and insightful.
Structure:

Subject line: '{company}'s initiative regarding {value}'.

Opening: 'I read your quarterly report regarding the shift to {value}.'

Core: 'Successfully executing that shift usually requires addressing {pain}, which we helped [Similar Company] navigate last quarter.'

CTA: 'Are you open to a brief conversation about that specific risk factor?'

Generate the email.
"""
    },
    {
        "id": 192,
        "style": "The 'Post-Proposal' Silence Breaker",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: You sent a proposal 5 days ago and haven't heard back.
Rule from Book: Avoid 'Desperation.' Do not ask 'Did you get my proposal?' Instead, offer a new piece of information that validates the proposal's logic.
Strict Tone: Assumptive and value-additive.
Structure:

Subject line: 'Thinking of you / {value}'.

Opening: 'I was thinking about our discussion regarding {pain}.'

Core: 'I realized I forgot to include this case study in the proposal, which highlights how [Similar Company] solved that exact issue.'

CTA: 'Do you have any questions on the proposal before we finalize next steps?'

Generate the email.
"""
    },
    {
        "id": 193,
        "style": "The Inbound Lead 'Speed-to-Lead'",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} who just requested a demo on your website.
Context: They filled out a 'Contact Us' form 5 minutes ago.
Rule from Book: Immediate action. Skip the fluff. Acknowledge the request and move immediately to 'Gathering Information' (Chapter 9) to ensure they are qualified.
Strict Tone: Responsive and eager.
Structure:

Subject line: 'Your request / {company}'.

Opening: 'I received your request for a demo.'

Core: 'To ensure I focus the demo on the right areas, are you primarily trying to solve {pain} or [Problem B]?'

CTA: 'Please let me know, and we can lock in a time.'

Generate the email.
"""
    },
    {
        "id": 194,
        "style": "The 'Lost Opportunity' Recycle",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: They chose a competitor 9 months ago.
Rule from Book: Be professional, not bitter. Use the '30-Day Rule' logic—prospecting done now pays off later. Check if the 'Status Quo' has changed or if the competitor failed to deliver.
Strict Tone: Professional and inquisitive.
Structure:

Subject line: 'Checking in on {value}'.

Opening: 'It has been 9 months since you selected [Competitor] for this project.'

Core: 'Typically, at this stage, leaders engage in a review of the implementation. Are you seeing the ROI you expected?'

CTA: 'Open to a 5-minute recalibration chat?'

Generate the email.
"""
    },
    {
        "id": 195,
        "style": "The Logistics Text (Pre-Meeting)",
        "text": """
Act as a Senior Sales Executive. You are texting {title}.
Context: You have a video call scheduled in 1 hour.
Rule from Book: Use text for 'Logistics.' Ensure they have the link and are ready (reduces no-shows).
Strict Tone: Helpful.
Structure:

ID: 'Hi {title}, this is [My Name].'

Core: 'Looking forward to our chat in an hour. Sending the Zoom link here for easy access: [Link].'

CTA: 'See you soon.'

Generate the text message.
"""
    },
    {
        "id": 196,
        "style": "The 'Help Me Help You' (Disqualification)",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: They agreed to a meeting, but you need to verify they meet a technical or budget requirement first.
Rule from Book: Protect your time (Golden Hours). Ask a 'Knockout Question' politely.
Strict Tone: Efficient.
Structure:

Subject line: 'One quick question before we meet'.

Opening: 'I am looking forward to our call on Thursday.'

Core: 'To make sure we make the best use of your time, could you confirm you are currently using {value}? Our solution requires it.'

CTA: 'Let me know.'

Generate the email.
"""
    },
    {
        "id": 197,
        "style": "The Peer Comparison (Insight)",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: Cold outreach.
Rule from Book: Use 'Insight Value.' Don't pitch your product; pitch the intelligence you have about the market.
Strict Tone: Authoritative.
Structure:

Subject line: 'Benchmark data for {industry}'.

Opening: 'We recently aggregated data from 50 companies in {industry} regarding {value}.'

Core: 'The data shows a shift toward {industry} trend, yet 40% of leaders are still under-invested in {pain}.'

CTA: 'Are you open to seeing how {company} benchmarks against this data?'

Generate the email.
"""
    },
    {
        "id": 198,
        "style": "The 'Vague Future' Follow-Up",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: Three months ago, they told you to reach out 'after Labor Day' or 'in Q4.'
Rule from Book: Be specific. Reference the date they gave you. This shows you are organized and they owe you the conversation.
Strict Tone: Professional and punctual.
Structure:

Subject line: 'As discussed in [Month]'.

Opening: 'You asked me to reach back out to you now regarding {value}.'

Core: 'I am writing to pick up that conversation as requested.'

CTA: 'Does [Day] work to briefly reconnect?'

Generate the email.
"""
    },
    {
        "id": 199,
        "style": "The Post-Implementation Referral Ask",
        "text": """
Act as a Senior Sales Executive. You are writing to a happy client [Client Name].
Context: You just finished their implementation/onboarding and they are happy.
Rule from Book: 'Give a legendary customer experience, then Ask.' Be direct.
Strict Tone: Appreciative and direct.
Structure:

Subject line: 'Quick question'.

Opening: 'It has been a pleasure getting your team live on {value}.'

Core: 'Since you have seen the value firsthand, who else in your network (specifically at {industry}) would benefit from a similar transformation?'

CTA: 'Would you be open to introducing me to one person this week?'

Generate the email.
"""
    },
    {
        "id": 200,
        "style": "The Year-End 'Use It or Lose It'",
        "text": """
Act as a Senior Sales Executive. You are writing to {title} at {company}.
Context: It is mid-December. You are trying to scrape up final opportunities.
Rule from Book: Leverage the 'Budgetary Window' (Chapter 9/10). Remind them that unspent budget might disappear next year.
Strict Tone: Urgent but helpful.
Structure:
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: We are initiating contact. Do not ask discovery questions.
Rule from Book: Apply the 'Hypothesis-Based Selling' concept. State clearly what we are seeing as the top challenges for similar companies in the {industry} sector to build immediate credibility.
Strict Tone: Professional, authoritative, peer-to-peer.
Structure:

Subject line: intriguing, referencing a specific industry trend.

Opening: Acknowledge their role and state that we won't waste their time asking basic questions.

Core: Present a hypothesis: 'We see companies like yours struggling with [X, Y, Z]'. Ask if this aligns with their reality.

CTA: A low-friction ask to validate this hypothesis.

Generate the email.
"""
    },
    {
        "id": 202,
        "style": "The Reframe",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect acknowledged a standard industry challenge ({pain}).
Rule from Book: Apply 'The Reframe'. Pivot the conversation from their known problem to a larger, unforeseen implication. Make them say, 'I never thought of it that way.'
Strict Tone: Provocative but respectful.
Structure:

Subject line: A statement that challenges conventional wisdom regarding {pain}.

Opening: Validate their current view on {pain}.

Core: Introduce a new perspective. Explain why {pain} is actually a symptom of a much more dangerous root cause ([Unrecognized Problem]).

CTA: Ask for 15 minutes to share the data behind this perspective.

Generate the email.
"""
    },
    {
        "id": 203,
        "style": "Rational Drowning",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: We have delivered the Reframe; now we must make the pain quantifiable.
Rule from Book: Apply 'Rational Drowning'. Use ROI logic to calculate the cost of inaction, not the ROI of our product.
Strict Tone: Analytical, urgent, objective.
Structure:

Subject line: Hard data point regarding {pain}.

Opening: Reference the previous discussion on [Unrecognized Problem].

Core: Present a specific data point or calculation that shows how much money/time is being wasted by ignoring this. Make them feel the 'cost of doing nothing.'

CTA: Ask to walk them through the full business case analysis.

Generate the email.
"""
    },
    {
        "id": 204,
        "style": "Emotional Impact (The Pain Chain)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The customer understands the math, but thinks 'we are different.' We need to make it personal.
Rule from Book: Create 'Emotional Impact' using a narrative. Describe a scenario that feels immediately familiar to their daily operations to kill the 'we're different' objection.
Strict Tone: Empathetic, storytelling, grave.
Structure:

Subject line: 'A familiar story' or similar.

Opening: 'I understand you feel your situation is unique, but let me share what happened to [Similar Company].'

Core: Describe a specific, painful workflow or failure that occurs when [Unrecognized Problem] is left unchecked. It must mirror their daily reality.

CTA: 'Does this sound like your Monday morning?'

Generate the email.
"""
    },
    {
        "id": 205,
        "style": "A New Way (Behavioral Change)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The customer admits the pain is real. Now we must define the solution without pitching our product yet.
Rule from Book: Pitch 'A New Way'. Describe the specific capabilities they would need to solve the problem. Do not mention [Our Company] or [Our Product].
Strict Tone: Visionary, helpful, objective advisor.
Structure:

Subject line: Focus on the outcome, e.g., 'The path to fixing {pain}.'

Opening: Recap the cost of the current state.

Core: Paint a picture of a better future state. List the 2-3 specific capabilities they would need to achieve this. 'Imagine if you could...'

CTA: Ask if they agree that this is the right approach to solving the problem.

Generate the email.
"""
    },
    {
        "id": 206,
        "style": "Your Solution (The Reveal)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The customer agreed to the 'New Way' capabilities. Now we map our Unique Differentiators to those needs.
Rule from Book: Lead to your solution, not with it. Explain how [Our Product] is uniquely designed to deliver the specific capabilities discussed in the previous step.
Strict Tone: Confident, direct.
Structure:

Subject line: [Our Company] and the capabilities we discussed.

Opening: Acknowledge their agreement on the necessary course of action.

Core: Map [Our Unique Feature] directly to the capability they said they needed. Prove we are the only ones who can execute this fully.

CTA: Propose a demo specifically to show this feature in action.

Generate the email.
"""
    },
    {
        "id": 207,
        "style": "Taking Control (Early Verification)",
        "text": """
Act as a Senior Sales Executive. You are writing to a Junior Contact at {company}.
Context: They sent an RFP or asked for pricing but are blocking access to the [Decision Maker].
Rule from Book: 'Take Control' of the sale. Refuse to engage further without access to key stakeholders. Verify their intent.
Strict Tone: Firm, professional, willing to walk away.
Structure:

Subject line: Regarding our engagement / Next steps.

Opening: Thank them for the interest/RFP.

Core: State clearly: 'To ensure alignment on value, we require the involvement of [Decision Maker Title] at this stage. We cannot proceed with a proposal without understanding their strategic priorities.'

CTA: Ask for a time to meet with the [Decision Maker Title] included.

Generate the email.
"""
    },
    {
        "id": 208,
        "style": "Tailoring for Resonance (The Decision Maker)",
        "text": """
Act as a Senior Sales Executive. You are writing to a C-Level Executive at {company}.
Context: We need to gain their sign-off on a deal their team likes.
Rule from Book: Tailor for the Decision Maker. Focus on 'widespread organizational support' and risk mitigation. Do not list features.
Strict Tone: Concise, executive-level summary.
Structure:

Subject line: Consensus at {company} regarding {value}.

Opening: State that their team (mention specific names) has vetted the solution.

Core: Highlight that there is consensus and widespread support. Emphasize the ease of implementation and ROI.

CTA: Ask for a brief review to finalize.

Generate the email.
"""
    },
    {
        "id": 209,
        "style": "Tailoring for Resonance (The Influencer)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} (End User) at {company}.
Context: We are building a groundswell of support before approaching the C-suite.
Rule from Book: Tailor for the Influencer. Teach them something that helps them improve their personal standing or job performance.
Strict Tone: Educational, supportive, tactical.
Structure:

Subject line: Insight on {title}.

Opening: Acknowledge the difficulty of their specific role.

Core: Share a tactical insight or tool that makes their daily workflow easier. Position yourself as a resource/expert for them.

CTA: Ask for their feedback on this approach.

Generate the email.
"""
    },
    {
        "id": 210,
        "style": "The Project Proposal (Consensus Building)",
        "text": """
Act as a Senior Sales Executive. You are writing to a Champion at {company}.
Context: We are preparing the final proposal. We need to ensure no stakeholders defect.
Rule from Book: Secure consensus by documenting individual wins.
Strict Tone: Collaborative, organized, detailed.
Structure:

Subject line: {value}: Value Roadmap.

Opening: 'To ensure we hit the mark for the entire committee...'

Core: List the top 3 stakeholders ({title}s). For each, state the specific business outcome our solution delivers for them personally. Ask the Champion to verify these wins.
"""}, {
        "id": 201,
        "style": "The Challenger (Hypothesis-Based)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: This is a cold outreach. You have done your research and have a strong hypothesis about their business challenge.
Rule from Book: Apply 'The Challenger Sale' methodology. Lead with a hypothesis about their business, not a question about their needs.
Strict Tone: Confident, insightful, provocative.
Structure:

Subject line: intriguing, referencing a specific industry trend.

Opening: Acknowledge their role and state that we won't waste their time asking basic questions.

Core: Present a hypothesis: 'We see companies like yours struggling with [X, Y, Z]'. Ask if this aligns with their reality.

CTA: A low-friction ask to validate this hypothesis.

Generate the email.
"""
    },
    {
        "id": 202,
        "style": "The Reframe",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect acknowledged a standard industry challenge ({pain}).
Rule from Book: Apply 'The Reframe'. Pivot the conversation from their known problem to a larger, unforeseen implication. Make them say, 'I never thought of it that way.'
Strict Tone: Provocative but respectful.
Structure:

Subject line: A statement that challenges conventional wisdom regarding {pain}.

Opening: Validate their current view on {pain}.

Core: Introduce a new perspective. Explain why {pain} is actually a symptom of a much more dangerous root cause ([Unrecognized Problem]).

CTA: Ask for 15 minutes to share the data behind this perspective.

Generate the email.
"""
    },
    {
        "id": 203,
        "style": "Rational Drowning",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: We have delivered the Reframe; now we must make the pain quantifiable.
Rule from Book: Apply 'Rational Drowning'. Use ROI logic to calculate the cost of inaction, not the ROI of our product.
Strict Tone: Analytical, urgent, objective.
Structure:

Subject line: Hard data point regarding {pain}.

Opening: Reference the previous discussion on [Unrecognized Problem].

Core: Present a specific data point or calculation that shows how much money/time is being wasted by ignoring this. Make them feel the 'cost of doing nothing.'

CTA: Ask to walk them through the full business case analysis.

Generate the email.
"""
    },
    {
        "id": 204,
        "style": "Emotional Impact (The Pain Chain)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The customer understands the math, but thinks 'we are different.' We need to make it personal.
Rule from Book: Create 'Emotional Impact' using a narrative. Describe a scenario that feels immediately familiar to their daily operations to kill the 'we're different' objection.
Strict Tone: Empathetic, storytelling, grave.
Structure:

Subject line: 'A familiar story' or similar.

Opening: 'I understand you feel your situation is unique, but let me share what happened to [Similar Company].'

Core: Describe a specific, painful workflow or failure that occurs when [Unrecognized Problem] is left unchecked. It must mirror their daily reality.

CTA: 'Does this sound like your Monday morning?'

Generate the email.
"""
    },
    {
        "id": 205,
        "style": "A New Way (Behavioral Change)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The customer admits the pain is real. Now we must define the solution without pitching our product yet.
Rule from Book: Pitch 'A New Way'. Describe the specific capabilities they would need to solve the problem. Do not mention [Our Company] or [Our Product].
Strict Tone: Visionary, helpful, objective advisor.
Structure:

Subject line: Focus on the outcome, e.g., 'The path to fixing {pain}.'

Opening: Recap the cost of the current state.

Core: Paint a picture of a better future state. List the 2-3 specific capabilities they would need to achieve this. 'Imagine if you could...'

CTA: Ask if they agree that this is the right approach to solving the problem.

Generate the email.
"""
    },
    {
        "id": 206,
        "style": "Your Solution (The Reveal)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The customer agreed to the 'New Way' capabilities. Now we map our Unique Differentiators to those needs.
Rule from Book: Lead to your solution, not with it. Explain how [Our Product] is uniquely designed to deliver the specific capabilities discussed in the previous step.
Strict Tone: Confident, direct.
Structure:

Subject line: [Our Company] and the capabilities we discussed.

Opening: Acknowledge their agreement on the necessary course of action.

Core: Map [Our Unique Feature] directly to the capability they said they needed. Prove we are the only ones who can execute this fully.

CTA: Propose a demo specifically to show this feature in action.

Generate the email.
"""
    },
    {
        "id": 207,
        "style": "Taking Control (Early Verification)",
        "text": """
Act as a Senior Sales Executive. You are writing to a Junior Contact at {company}.
Context: They sent an RFP or asked for pricing but are blocking access to the [Decision Maker].
Rule from Book: 'Take Control' of the sale. Refuse to engage further without access to key stakeholders. Verify their intent.
Strict Tone: Firm, professional, willing to walk away.
Structure:

Subject line: Regarding our engagement / Next steps.

Opening: Thank them for the interest/RFP.

Core: State clearly: 'To ensure alignment on value, we require the involvement of [Decision Maker Title] at this stage. We cannot proceed with a proposal without understanding their strategic priorities.'

CTA: Ask for a time to meet with the [Decision Maker Title] included.

Generate the email.
"""
    },
    {
        "id": 208,
        "style": "Tailoring for Resonance (The Decision Maker)",
        "text": """
Act as a Senior Sales Executive. You are writing to a C-Level Executive at {company}.
Context: We need to gain their sign-off on a deal their team likes.
Rule from Book: Tailor for the Decision Maker. Focus on 'widespread organizational support' and risk mitigation. Do not list features.
Strict Tone: Concise, executive-level summary.
Structure:

Subject line: Consensus at {company} regarding {value}.

Opening: State that their team (mention specific names) has vetted the solution.

Core: Highlight that there is consensus and widespread support. Emphasize the ease of implementation and ROI.

CTA: Ask for a brief review to finalize.

Generate the email.
"""
    },
    {
        "id": 209,
        "style": "Tailoring for Resonance (The Influencer)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} (End User) at {company}.
Context: We are building a groundswell of support before approaching the C-suite.
Rule from Book: Tailor for the Influencer. Teach them something that helps them improve their personal standing or job performance.
Strict Tone: Educational, supportive, tactical.
Structure:

Subject line: Insight on {title}.

Opening: Acknowledge the difficulty of their specific role.

Core: Share a tactical insight or tool that makes their daily workflow easier. Position yourself as a resource/expert for them.

CTA: Ask for their feedback on this approach.

Generate the email.
"""
    },
    {
        "id": 210,
        "style": "The Project Proposal (Consensus Building)",
        "text": """
Act as a Senior Sales Executive. You are writing to a Champion at {company}.
Context: We are preparing the final proposal. We need to ensure no stakeholders defect.
Rule from Book: Secure consensus by documenting individual wins.
Strict Tone: Collaborative, organized, detailed.
Structure:

Subject line: {value}: Value Roadmap.

Opening: 'To ensure we hit the mark for the entire committee...'

Core: List the top 3 stakeholders ({title}s). For each, state the specific business outcome our solution delivers for them personally. Ask the Champion to verify these wins.

CTA: Confirm this aligns with the internal conversations they are having.

Generate the email.
"""
    },
    {
        "id": 211,
        "style": "Acknowledge and Defer (Negotiation)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect has asked for pricing or a discount early in the sales cycle, before we have completed the Commercial Teaching choreography.
Rule from Book: Apply 'Acknowledge and Defer'. Do not give a price. Acknowledge their request but firmly state that pricing depends on the value scope, which is not yet defined.
Strict Tone: Confident, gatekeeping, value-focused.
Structure:

Subject line: Pricing / Value alignment.

Opening: Acknowledge the request for pricing.

Core: State that we cannot provide accurate pricing until we confirm the full scope of the solution to the {pain}. Refuse to provide a 'ballpark' number that might mislead them.

CTA: Propose a specific time to review the scope first.

Generate the email.
"""
    },
    {
        "id": 212,
        "style": "Deepen and Broaden (Negotiation)",
        "text": """
Act as a Senior Sales Executive. You are writing to a Procurement Officer at {company}.
Context: We are at the final stage. They are demanding a 10% price cut.
Rule from Book: Apply 'Deepen and Broaden'. Do not concede price yet. Introduce other non-monetary variables (timeline, support, payment terms) to expand the negotiation surface area.
Strict Tone: Collaborative but firm.
Structure:

Subject line: Adjusting the agreement terms.

Opening: Acknowledge the budget constraint.

Core: Ask 'What are you trying to achieve with this cut?' (Cost reduction vs. Cash flow). Offer to review payment terms, scope levels, or implementation speed instead of just cutting the top-line price.

CTA: Ask for a call to review these specific trade-offs.

Generate the email.
"""
    },
    {
        "id": 213,
        "style": "Reshaping the RFP",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: They sent a standard RFP. It focuses entirely on price and commodities, missing the 'Unplanned Spend' or hidden costs.
Rule from Book: Challenge the RFP criteria. Tell them the RFP is missing a critical risk factor ({pain}) that will cost them money in the long run.
Strict Tone: Expert, corrective, protective.
Structure:

Subject line: Missing criteria in the {value} RFP.

Opening: Confirm receipt of the RFP.

Core: State that based on our experience with similar companies, omitting {pain} from the criteria usually leads to {pain}. Suggest adding specific criteria that address this.

CTA: Ask to review these additions before submitting the response.

Generate the email.
"""
    },
    {
        "id": 214,
        "style": "The 'No-Decision' Killer (Overcoming Inertia)",
        "text": """
Act as a Senior Sales Executive. You are writing to a Champion at {company}.
Context: The deal has gone quiet. The customer is defaulting to the status quo.
Rule from Book: Combat 'Indecision Inertia'. Do not ask 'just checking in.' Re-state the cost of inaction.
Strict Tone: Urgent, concerned.
Structure:

Subject line: The cost of delaying {value}.

Opening: Reference the date we originally planned to launch.

Core: Remind them that every month of delay costs them {value} in wasted spend/missed revenue. Re-attach the timeline to their personal goals.

CTA: Ask if the priority of solving {pain} has changed.

Generate the email.
"""
    },
    {
        "id": 215,
        "style": "Preventing 'Free Consulting'",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The customer wants a detailed custom roadmap/audit/pilot but hasn't committed to us as a vendor.
Rule from Book: Take Control. State that our resources are reserved for partners. Demand a 'quid pro quo' (e.g., access to the CEO or a verbal commitment) before doing the work.
Strict Tone: Transactional, fair, boundary-setting.
Structure:

Subject line: Resource allocation for {value}.

Opening: Acknowledge the request for the deep-dive work.

Core: Explain that this level of analysis requires significant investment from our side. We are willing to do it, but only if we have assurance that we are the selected partner pending this final check.

CTA: Ask for that confirmation.

Generate the email.
"""
    },
    {
        "id": 216,
        "style": "The Order-Taker Reversal",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The customer emailed asking for a quote on a specific, low-value product/service without context.
Rule from Book: Don't be an 'Order Taker'. Pause the request. Ask why they think that specific solution will solve their problem, implying there might be a better way.
Strict Tone: Inquisitive, expert.
Structure:

Subject line: Your request regarding {value}.

Opening: 'I can certainly provide that quote.'

Core: 'However, usually when companies ask for {value}, they are trying to solve {pain}. If that's the case here, {value} might actually increase your costs because of [Reason].'

CTA: Ask for a 5-minute call to ensure they aren't buying the wrong tool.

Generate the email.
"""
    },
    {
        "id": 217,
        "style": "Addressing the 'We Are Different' Objection",
        "text": """
Act as a Senior Sales Executive. You are writing to a Skeptical Stakeholder at {company}.
Context: We pitched a 'Pain Chain' story, and they said, 'That happens to other companies, but not us. We are different.'
Rule from Book: Challenge the 'Unique' fallacy. Respectfully push back with data showing that the economic drivers affect everyone, regardless of their unique operating model.
Strict Tone: Respectful pushback.
Structure:

Subject line: Uniqueness vs. Market Pressures.

Opening: Validate their unique operating model.

Core: 'While your internal process is unique, the economic pressure of {industry} trend applies universally. Whether you are Company A or Company B, {pain} still erodes margins in the same way.'

CTA: Ask them to review one specific data set that proves this correlation.

Generate the email.
"""
    },
    {
        "id": 218,
        "style": "The Manager Intervention (Sales Innovation)",
        "text": """
Act as a VP of Sales. You are writing to a Peer Executive (VP/C-Level) at {company}.
Context: The deal is stuck at the lower levels. The Rep has done all they can. The Manager must intervene to change the conversation.
Rule from Book: Use 'Sales Innovation'. Change the scope or the risk profile of the deal to unstick it.
Strict Tone: Executive-to-Executive.
Structure:

Subject line: Executive alignment / {value}.

Opening: 'I've been reviewing our team's conversation regarding {value}.'

Core: 'It seems we are stuck on [Blocker]. I'd like to propose a completely different structure—perhaps a risk-sharing model or a phased rollout—that might solve this.'

CTA: Propose a 15-minute leader-to-leader call.

Generate the email.
"""
    },
    {
        "id": 219,
        "style": "Teaching via Content (The 'Always-On' Insight)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: Nurturing a prospect between meetings.
Rule from Book: Send content that reinforces the 'Reframe'. The content should focus on their problem, not our solution.
Strict Tone: Educational, 'thought-feeder'.
Structure:

Subject line: Data regarding {industry} trend.

Opening: 'Thinking about our conversation regarding {pain}...'

Core: 'I came across this report/data point. It highlights exactly what we discussed: that companies focusing on [Old Way] are seeing diminishing returns. It ignores our solution entirely but clarifies the problem.'

CTA: 'Curious to hear your take on page 3.'

Generate the email.
"""
    },
    {
        "id": 220,
        "style": "The Professional Walk-Away",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The customer refuses to move off a price-only negotiation and won't grant access to the decision maker.
Rule from Book: Take Control by walking away. Signal that we cannot be a partner under these conditions.
Strict Tone: Professional, final, high-status.
Structure:

Subject line: {value} / Our participation.

Opening: 'Thank you for the opportunity to engage so far.'

Core: 'Based on the limitations on access and the focus solely on price rather than value, we do not believe we are the right partner for this initiative. We operate best when we can align with strategic goals, which requires executive dialogue.'

CTA: 'We are withdrawing our proposal. Best of luck.' (This often triggers the customer to chase).

Generate the email.
"""
    },
    {
        "id": 221,
        "style": "The Commercial Teaching QBR (Quarterly Business Review)",
        "text": """
Act as a Senior Account Manager. You are writing to an Existing Client ({title}) at {company}.
Context: Upcoming Quarterly Business Review. We need to avoid a boring 'status update' and instead pitch an upsell.
Rule from Book: Don't just review past performance. Apply 'Commercial Teaching' to the QBR. Tease a new insight regarding an emerging threat to their business to set the stage for the next deal.
Strict Tone: Strategic, forward-looking.
Structure:

Subject line: Q4 Strategy / Emerging risk in {industry}.

Opening: Confirm the meeting time.

Core: 'We will spend 10 minutes on last quarter's metrics. However, we've identified a new trend affecting companies in your space regarding {pain}. I want to spend the bulk of our time reviewing the data on this, as it impacts your 2024 goals.'

CTA: Ask them to invite {title} who would be impacted by this new risk.

Generate the email.
"""
    },
    {
        "id": 222,
        "style": "Addressing the 'Parts Orphanage' (The Grainger Logic)",
        "text": """
Act as a Senior Sales Executive. You are writing to an Operations Director at {company}.
Context: The customer is buying reactively from multiple vendors to 'reduce risk,' but it is costing them money (the 'Parts Orphanage' concept).
Rule from Book: Reframe their concept of 'Risk.' Show that their 'just-in-case' buying strategy is actually a 'hidden cost' strategy due to process inefficiencies.
Strict Tone: Analytical, revealing.
Structure:

Subject line: Process costs vs. Product costs.

Opening: 'We've analyzed your purchasing patterns over the last 6 months.'

Core: 'While buying from multiple vendors feels safer, our data shows it increases your process costs by {value}%. You are paying for redundancy that you don't need.'

CTA: Ask to review the 'Total Cost of Ownership' analysis.

Generate the email.
"""
    },
    {
        "id": 223,
        "style": "Equipping the Champion (The Safe-Bold Framework)",
        "text": """
Act as a Senior Sales Executive. You are writing to an Internal Champion at {company}.
Context: The Champion is about to present our idea to the C-suite. We fear they will dilute the 'Reframe' to avoid conflict.
Rule from Book: Coach the Champion using the 'Safe-Bold' framework. Explain that if the pitch doesn't sound risky/difficult, the C-suite won't see the value in changing.
Strict Tone: Coaching, conspiratorial (in a professional way).
Structure:

Subject line: Preparing for the {title} meeting.

Opening: 'Good luck with the presentation tomorrow.'

Core: 'A word of caution: The natural instinct is to make the pitch feel 'safe' and easy. However, to get {title}'s attention, we must highlight the risk of the status quo. If we don't make them uncomfortable with the current state, they won't move.'

CTA: Offer to do a final 10-minute dry run to sharpen the 'edge' of the pitch.

Generate the email.
"""
    },
    {
        "id": 224,
        "style": "The Implementation Handoff (Avoiding the Reactive Trap)",
        "text": """
Act as a Senior Implementation Lead. You are writing to the Project Lead at {company}.
Context: The deal is signed. We are moving to implementation.
Rule from Book: Focus on 'Value Realization,' not just 'Installation.' Remind them that the goal is to solve the business problem identified in the sales cycle, not just turn on the software.
Strict Tone: Directive, outcome-oriented.
Structure:

Subject line: Launching {value} to achieve {value}.

Opening: Welcome them.

Core: 'Our implementation plan is designed specifically to address the {pain} we discussed during the sales cycle. We will prioritize features that attack that specific metric first, rather than a generic rollout.'

CTA: Ask for the metrics baseline so we can track success.

Generate the email.
"""
    },
    {
        "id": 225,
        "style": "Tailoring for Legal/Procurement (Language of the Business)",
        "text": """
Act as a Senior Sales Executive. You are writing to General Counsel / Legal at {company}.
Context: Legal is holding up the contract over standard clauses.
Rule from Book: Speak the 'Language of the Business.' Move from gray answers to probabilities. Show that the cost of the delay (lost value) outweighs the theoretical risk of the clause.
Strict Tone: Pragmatic, commercial.
Structure:

Subject line: Contract review / Commercial impact.

Opening: Acknowledge their duty to protect the firm.

Core: 'We are currently stalling a project projected to save {company} $1M/year over a liability clause that has a 0.01% probability of occurring. We need to weigh the certain loss of savings against the theoretical legal risk.'

CTA: Propose a compromise to sign by Friday.

Generate the email.
"""
    },
    {
        "id": 226,
        "style": "The 'Solae' Consensus Tool",
        "text": """
Act as a Senior Sales Executive. You are writing to a Stakeholder Committee Member at {company}.
Context: We have met with Marketing, IT, and Ops. We need to lock in their individual buy-in before the final vote.
Rule from Book: Use the 'Value Planning' methodology. Confirm in writing what their specific personal win is.
Strict Tone: Process-driven, verifying.
Structure:

Subject line: Confirmation of objectives for {title}.

Opening: 'We are finalizing the proposal for the steering committee.'

Core: 'Based on our last conversation, I have noted that for {title}, success is defined as {value}. I am including this in the final executive summary to ensure your needs are represented.'

CTA: 'Please confirm this is accurate by EOD.'

Generate the email.
"""
    },
    {
        "id": 227,
        "style": "Recruiting the Challenger (The Headhunter Pitch)",
        "text": """
Act as a VP of Sales. You are writing to a Passive Candidate (High Performer) at a competitor.
Context: We want to poach a top rep who fits the Challenger profile.
Rule from Book: Appeal to the Challenger's desire for skill mastery and complexity. Pitch the 'Challenge,' not the perks.
Strict Tone: Exclusive, challenging.
Structure:

Subject line: A difficult marketplace.

Opening: 'I've been following your work at {company}.'

Core: 'We are building a team to go after the most complex accounts in the {industry} space. We aren't looking for relationship builders; we need people who can disrupt C-level thinking. It is a hard sell, but the upside is uncapped.'

CTA: 'Open to a conversation about the complexity of the market?'

Generate the email.
"""
    },
    {
        "id": 228,
        "style": "Marketing Feedback Loop (Insight Generation)",
        "text": """
Act as a Senior Sales Rep. You are writing to the Head of Marketing at {company}.
Context: Customers are no longer responding to our current 'Warmer.' We need new data.
Rule from Book: Collaborative Innovation. Alert Marketing that the current 'Reframe' is stale and suggest a new angle based on field observations.
Strict Tone: Constructive, internal, strategic.
Structure:

Subject line: Field Feedback / Adjusting our pitch on {value}.

Opening: 'I'm noticing a trend in my last 10 meetings.'

Core: 'Customers are no longer surprised by {value}. They are, however, consistently worried about {pain}. If we can build some collateral/data around that, I can get us into more C-level conversations.'

CTA: Ask for a time to brainstorm the new angle.

Generate the email.
"""
    },
    {
        "id": 229,
        "style": "Breaking the 'Friend Zone'",
        "text": """
Act as a Senior Sales Executive. You are writing to a Friendly Contact at {company}.
Context: You have a great relationship, lots of coffee meetings, but no PO (Purchase Order).
Rule from Book: Constructive Tension. Pivot the relationship from social to commercial. Risk likability for respect.
Strict Tone: Serious, business-focused.
Structure:

Subject line: Moving {value} forward.

Opening: 'I've enjoyed our conversations regarding the industry.'

Core: 'However, looking at my pipeline, I need to determine if there is actual business to be done here. We have discussed the cost of your current problem multiple times. Are you ready to take action to fix it, or should we pause our discussions until this becomes a priority?'

CTA: Ask for a Yes/No decision on the next step.

Generate the email.
"""
    },
    {
        "id": 230,
        "style": "The 'Teaching' Re-Engagement",
        "text": """
Act as a Senior Sales Executive. You are writing to a Ghosting Prospect at {company}.
Context: No reply to the last 3 emails.
Rule from Book: Lead with Insight. Deliver value in the email itself. Re-engage by teaching them something new that happened in the market since you last spoke.
Strict Tone: Educational, nonchalant (not desperate).
Structure:

Subject line: New regulation / {value} affecting {company}.

Opening: 'I haven't heard from you, so I assume other priorities have taken over.'

Core: 'Since we last spoke, [Event/Data] happened. This changes the ROI calculation we discussed. I thought you'd want to see how this impacts your risk profile.'

CTA: 'Link to the analysis is here. Let me know if you want to walk through it.'

Generate the email.
"""
    },
    {
        "id": 231,
        "style": "The PAUSE Framework (Coaching)",
        "text": """
Act as a Sales Director. You are writing to a Sales Rep on your team.
Context: You need to schedule a coaching session for an upcoming high-stakes meeting with {Key_Account}.
Rule from Book: Apply the 'PAUSE' framework (Preparation, Affirm, Understand, Specify, Embed). Don't ask 'What's the status?' Ask 'What is your teaching objective?'
Strict Tone: Supportive, rigorous, development-focused.
Structure:

Subject line: Strategy session for {Key_Account}.

Opening: 'Let's prep for the upcoming meeting.'

Core: 'I want to focus specifically on the 'Teaching' phase. Come prepared to articulate the specific commercial insight you plan to deliver and how you will tailor it to {Stakeholder_Name}'s role.'

CTA: 'Please send your hypothesis 24 hours in advance.'

Generate the email.
"""
    },
    {
        "id": 232,
        "style": "SCAMMPERR Framework (Sales Innovation)",
        "text": """
Act as a VP of Sales. You are writing to a Sales Rep who is stuck on a deal.
Context: The rep wants to offer a discount to close {company}.
Rule from Book: Use 'Sales Innovation'. Do not approve the discount. Challenge the rep to 'Expand the Pie' using the SCAMMPERR framework to change the deal structure (terms, scope, timing) instead.
Strict Tone: Challenging, mentoring.
Structure:

Subject line: Structuring the {company} agreement.

Opening: Acknowledge the customer's pushback on price.

Core: 'Before we erode our margins, let's look at the deal structure. Can we Modify the contract length? Can we Substitute payment terms for price? Can we Eliminate a low-value service to hit their budget number?'

CTA: 'Come back to me with two non-price options.'

Generate the email.
"""
    },
    {
        "id": 233,
        "style": "The 'Deb Oler' Question (Hard Differentiation)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The customer says, 'You and [Competitor] look exactly the same.'
Rule from Book: Answer the question: 'Why should I buy from you over anyone else?' Do not use words like 'Innovative' or 'Customer-Centric.' Point to a specific, hard capability that minimizes their risk.
Strict Tone: Confident, distinct.
Structure:

Subject line: The difference between us and {Competitor}.

Opening: 'It is fair to say we share similar features.'

Core: 'However, the reason clients choose us is {Unique_Hard_Capability}. Without this specific mechanism, you remain exposed to {Specific_Risk}. No one else can cover that gap.'

CTA: 'Is mitigating that risk a priority for you?'

Generate the email.
"""
    },
    {
        "id": 234,
        "style": "The Commodity Reframe ('Unbranded Axle Grease')",
        "text": """
Act as a Senior Sales Executive. You are writing to a Procurement Manager at {company}.
Context: We sell a commodity. They want the lowest price.
Rule from Book: Differentiate on how they use the product, not the product itself. Teach them that their consumption process is inefficient.
Strict Tone: Analytical, efficiency-focused.
Structure:

Subject line: Efficiency gains in {Category_Spend}.

Opening: 'I understand you are looking for the lowest unit price.'

Core: 'However, unit price is only 20% of your total cost. Our data shows you are over-ordering/stockpiling because of inefficient supply chain triggers. We can lower your total spend by 15% even at our current price point by optimizing your usage.'

CTA: Ask to audit their usage patterns.

Generate the email.
"""
    },
    {
        "id": 235,
        "style": "'Respectful' Challenging (Cultural Adaptation)",
        "text": """
Act as a Senior Sales Executive. You are writing to a Conservative Client in {Region/Industry}.
Context: We need to challenge their thinking without offending their hierarchy.
Rule from Book: Add the word 'Respectfully' to the challenge. Frame the insight as a 'Market Observation' rather than a direct correction of their strategy.
Strict Tone: Deferential but firm on the facts.
Structure:

Subject line: Observations regarding {value}.

Opening: Acknowledge their experience and authority.

Core: 'With all due respect to your current process, the market data suggests that this approach may expose you to {pain}. May I respectfully suggest we look at [Alternative_Perspective] to ensure you are protected?'

CTA: Ask for permission to explore this view.

Generate the email.
"""
    },
    {
        "id": 236,
        "style": "The 'Call Center' Translation (Speaking Their Language)",
        "text": """
Act as a Senior Sales Executive. You are writing to a Line-of-Business Leader at {company}.
Context: We are selling a technical solution (e.g., IT security), but writing to a non-technical buyer (e.g., CFO).
Rule from Book: Remove all technical jargon. Translate features immediately into financial impact or risk probability.
Strict Tone: Commercial, plain English.
Structure:

Subject line: Financial exposure related to {System_Name}.

Opening: 'I'm writing to you because this isn't just an IT issue; it's a balance sheet issue.'

Core: 'We usually talk about this in terms of {Technical_Metric}, but for your P&L, this actually means {Financial_Impact}. Implementing this solution protects {Revenue_Stream}.'

CTA: Ask for 10 minutes to review the business case.

Generate the email.
"""
    },
    {
        "id": 237,
        "style": "Verifying the 'Reframe' (The Litmus Test)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: We just had a meeting where we presented an insight. We need to verify if they bought the problem before we sell the solution.
Rule from Book: Don't sell the solution yet. Verify the Reframe. Ask them to confirm the magnitude of the problem we uncovered.
Strict Tone: Inquisitive, verifying.
Structure:

Subject line: Follow up on our discussion regarding {pain}.

Opening: 'In our last meeting, we discussed how {Current_Behavior} is costing you {Loss_Metric}.'

Core: 'Before we move to solution design, I want to confirm: Does your team agree that fixing this root cause is a strategic priority for Q3? If we don't agree on the problem magnitude, the solution won't make sense.'

CTA: Ask for confirmation of the problem statement.

Generate the email.
"""
    },
    {
        "id": 238,
        "style": "Competitor Depositioning (Landmines)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: We know they are talking to {Competitor_Name}. {Competitor_Name} is weak in {Specific_Capability}.
Rule from Book: Lead to our strengths. Teach the customer that {Specific_Capability} is the only thing that matters, rendering the competitor irrelevant without mentioning them.
Strict Tone: Educational, objective.
Structure:

Subject line: Critical criteria for {value}.

Opening: 'As you evaluate partners for this initiative...'

Core: 'Make sure you verify that your partner can handle {Specific_Capability}. In our experience, vendors who lack this specific mechanism often fail to deliver ROI because [Reason]. It is the single most predictive factor of success.'

CTA: 'Here is a checklist to use when evaluating vendors.'

Generate the email.
"""
    },
    {
        "id": 239,
        "style": "The Executive 'Gate' (Protecting the Demo)",
        "text": """
Act as a Senior Sales Executive. You are writing to a Junior Evaluator at {company}.
Context: They asked for a full product demo for their team.
Rule from Book: Take Control. Explain that a demo is a custom resource that requires executive alignment to be effective.
Strict Tone: Professional, high-standard.
Structure:

Subject line: Demo request for {value}.

Opening: 'We would be happy to showcase the solution.'

Core: 'Because our solution is comprehensive, we tailor every demo to the strategic goals of the leadership team. We find these sessions are not effective without {Decision_Maker_Title} present to steer the use cases.'

CTA: 'Can we schedule this when {Decision_Maker_Name} is available?'

Generate the email.
"""
    },
    {
        "id": 240,
        "style": "The Post-Mortem (Learning from Failure)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: We lost the deal.
Rule from Book: Analyze the 'Teaching' failure. Don't ask 'Why didn't you buy?' Ask 'Did we fail to make the problem seem urgent?'
Strict Tone: Humble, learning-oriented.
Structure:

Subject line: Closing the loop on {value}.

Opening: Thank them for the consideration and wish them well.

Core: 'I'm not looking to change your mind, but I want to improve my approach. Did we fail to demonstrate that the cost of {pain} was high enough to warrant action? I suspect I may not have articulated the risk of the status quo clearly enough.'

CTA: Ask for a one-sentence reply on that specific point.

Generate the email.
"""
    },
    {
        "id": 241,
        "style": "Tactical Deafness (The Strategic Pivot)",
        "text": """
Act as a Senior Sales Executive. You are writing to a Tactical Buyer at {company}.
Context: The buyer asked for a small, specific tactical execution (e.g., a single feature or small order) that misses the bigger picture.
Rule from Book: Apply 'Tactical Deafness'. Do not confirm the order yet. Ask what strategic goal prompted this request to see if a broader solution is actually needed.
Strict Tone: Curious, strategic, pausing the action.
Structure:

Subject line: Context regarding your request for {value}.

Opening: Acknowledge the request.

Core: 'Typically, when companies ask for {value}, they are trying to achieve {value}. If that is the case here, executing this single tactic might not get you there. Are you trying to fix {pain}?'

CTA: Ask to clarify the strategy before executing the tactic.

Generate the email.
"""
    },
    {
        "id": 242,
        "style": "The 'Why Now?' (Catalyzing Action)",
        "text": """
Act as a Senior Sales Executive. You are writing to a Hesitant Prospect at {company}.
Context: The customer wants to delay the decision until next quarter/year.
Rule from Book: Catalyze Action. Do not accept the delay. Present data showing the specific financial loss they will incur by waiting 90 days.
Strict Tone: Urgent, factual.
Structure:

Subject line: Cost analysis of a Q3 vs. Q4 start.

Opening: 'I understand the desire to wait.'

Core: 'However, based on the burn rate of {pain} we identified, delaying 90 days will cost {company} an additional {value}. This expense is unrecoverable. It makes financial sense to stop the bleeding now rather than budget for it later.'

CTA: 'Is this cost acceptable to the board?'

Generate the email.
"""
    },
    {
        "id": 243,
        "style": "The Hypothesis-Based Referral",
        "text": """
Act as a Senior Sales Executive. You are writing to a Champion at {company}.
Context: We need access to the VP of Operations/Finance to lock in the deal.
Rule from Book: Don't ask for a generic referral. State a hypothesis about how the problem affects the other department to justify the intro.
Strict Tone: Professional, explanatory.
Structure:

Subject line: Implications for {title}.

Opening: 'We've defined the value for your team.'

Core: 'However, usually when {pain} exists in your department, it causes {pain} for {title}. We need to verify this hypothesis with them to ensure our solution doesn't create friction there.'

CTA: 'Can you connect me with {title} to verify this?'

Generate the email.
"""
    },
    {
        "id": 244,
        "style": "Resource Allocation (Killing the Deal)",
        "text": """
Act as a Senior Sales Executive. You are writing to a Prospect at {company}.
Context: The prospect is too small or not ready for a complex solution, but keeps asking questions.
Rule from Book: Allocate Resources efficiently. Disqualify the lead politely but firmly to focus on high-potential accounts.
Strict Tone: Final, helpful but distant.
Structure:

Subject line: {company} and {value} fit.

Opening: 'I've reviewed your requirements against our ideal deployment profile.'

Core: 'At this stage, our solution is over-engineered for your current volume. Implementing us now would likely yield a negative ROI for you. I recommend looking at [Competitor/Alternative] which is better suited for this stage.'

CTA: 'I'm going to close this file on my end. Best of luck.'

Generate the email.
"""
    },
    {
        "id": 245,
        "style": "The 'Consensus Check' (Widespread Support)",
        "text": """
Act as a Senior Sales Executive. You are writing to the Decision Maker at {company}.
Context: We are expecting a signature, but we need to be sure no 'silent objectors' will blow it up last minute.
Rule from Book: Prioritize 'Widespread Support'. Ask the Decision Maker if their team is aligned, subtly reminding them of the risk of signing without consensus.
Strict Tone: Prudent, experienced.
Structure:

Subject line: Final alignment check.

Opening: 'We are ready to move to signature.'

Core: 'Before you sign, I want to ensure {title} and {title} are fully aligned. In my experience, if Operations isn't 100% on board, implementation stalls. Have they given you their full confidence in this plan?'

CTA: 'If not, let's address their concerns before finalizing.'

Generate the email.
"""
    },
    {
        "id": 246,
        "style": "The 'Shared Risk' Proposal (Sales Innovation)",
        "text": """
Act as a Senior Sales Executive. You are writing to the CFO at {company}.
Context: The CFO is blocking the deal due to financial risk/uncertainty of ROI.
Rule from Book: Use 'Sales Innovation'. Propose a non-standard, risk-sharing agreement to remove the objection.
Strict Tone: Confident, 'skin-in-the-game'.
Structure:

Subject line: Proposal for shared risk model.

Opening: Acknowledge the hesitation on ROI certainty.

Core: 'We are confident in the outcome. To prove it, I'd like to propose a performance-based tier. We will defer {value}% of the fees, payable only upon hitting the {value} milestones we discussed.'

CTA: 'Does this structure alleviate your risk concern?'

Generate the email.
"""
    },
    {
        "id": 247,
        "style": "Validating the Insight (Marketing to Sales)",
        "text": """
Act as the Head of Marketing. You are writing to the Sales Team.
Context: Marketing launched a new deck based on a specific 'Insight'. We need to know if it's landing.
Rule from Book: Calibrate the 'Reframe'. Ask if customers are reacting with 'I never thought of it that way' (Success) or 'I agree' (Failure).
Strict Tone: Internal, inquisitive, data-driven.
Structure:

Subject line: Field feedback on the {value} pitch.

Opening: 'We need a reality check on the new messaging.'

Core: 'When you present the {value} slide, are customers acting surprised/disturbed, or are they just agreeing with you? If they are just agreeing, we haven't found the true Reframe yet.'

CTA: 'Send me your honest anecdotal feedback by Friday.'

Generate the email.
"""
    },
    {
        "id": 248,
        "style": "The Personal Risk Mitigation",
        "text": """
Act as a Senior Sales Executive. You are writing to a Champion at {company}.
Context: The Champion is nervous about recommending a change because if it fails, it's on them.
Rule from Book: Address Personal Risk. Acknowledge that this is a career-stakes decision and explain how you will protect their reputation.
Strict Tone: Personal, reassuring, partner-focused.
Structure:

Subject line: Reducing the execution risk for you.

Opening: 'I know recommending a shift this size puts your political capital on the line.'

Core: 'We have built a dedicated post-sales support team specifically to ensure your first 90 days are a win. I will personally oversee the Q1 metrics so you can report a quick win to the board.'

CTA: 'Let's review the 90-day protection plan.'

Generate the email.
"""
    },
    {
        "id": 249,
        "style": "The 'Un-Teaching' (Correcting Misconceptions)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: A competitor has convinced them that {value} is the most important thing. We know {value} is irrelevant.
Rule from Book: Challenge customers' assumptions. dismantle the competitor's teaching without naming them, by proving that criteria is flawed.
Strict Tone: Corrective, expert.
Structure:

Subject line: The hidden downside of prioritizing {value}.

Opening: 'I see that {value} is a high priority in your evaluation.'

Core: 'While that sounds logical, our data suggests that companies who optimize for {value} actually see a decrease in performance because it forces them to sacrifice {value}. The market is moving away from that metric.'

CTA: Ask to share the case study on this specific trade-off.

Generate the email.
"""
    },
    {
        "id": 250,
        "style": "The Final Push (Constructive Tension)",
        "text": """
Act as a Senior Sales Executive. You are writing to the Decision Maker at {company}.
Context: We have negotiated, agreed on value, and handled objections. The customer is still hesitating at the signature line.
Rule from Book: Take Control. Press the customer to honor their commitment or release the resources.
Strict Tone: Firm, final.
Structure:

Subject line: Decision timeline for {value}.

Opening: 'We have agreed that {pain} is costing you $X/day.'

Core: 'We have mobilized our team to solve this, but I cannot hold these implementation slots past Friday. We need a final decision to proceed or we will need to re-allocate these resources to other partners.'

CTA: 'Please let me know by EOD if we are proceeding.'

Generate the email.
"""
    },
    {
        "id": 251,
        "style": "The 'Have You Given Up?' Email (The Magic Email)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect has gone silent (ghosted) after an initial positive interaction regarding {value}.
Rule from Book: Apply the 'Email Magic' concept from Chapter 4. Do not use a subject line. Do not use a salutation. The body must be a single sentence designed to trigger a 'No' response that actually means 'I am still interested.'
Strict Tone: Brief, direct, and surgical.
Structure:

Subject line: {value}

Opening: None.

Core: Ask strictly: 'Have you given up on {value}?' (or a variation tailored to the specific value prop).

CTA: None.

Generate the email.
"""
    },
    {
        "id": 252,
        "style": "The Accusation Audit (Cold Outreach)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: This is a cold email. You know they receive hundreds of sales pitches and likely view them as a nuisance.
Rule from Book: Use an 'Accusation Audit' to diffuse negative dynamics immediately. List the negatives (e.g., that you are an outsider, pestering them, or interrupting their day) right at the start.
Strict Tone: Self-effacing but confident.
Structure:

Subject line: A honest label like 'A terrible idea' or 'Apology in advance'.

Opening: Acknowledge that this email probably looks like a waste of their time or an annoyance.

Core: Briefly state that you don't want to be 'that salesperson,' but you noticed {pain} at {company}.

CTA: A 'No'-oriented question like 'Is it a bad time to chat for 3 minutes?'

Generate the email.
"""
    },
    {
        "id": 253,
        "style": "The 'No'-Oriented Opener",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You are trying to secure a discovery call regarding {value}, but they are busy.
Rule from Book: Avoid seeking a 'Yes'. Rephrase the ask to invite a 'No' response that signals safety.
Strict Tone: Deferential but professional.
Structure:

Subject line: {pain}

Opening: A brief context sentence about {industry} trend.

Core: Do not ask for a meeting directly. Ask if it is a bad time or if they are against a specific improvement.

CTA: 'Is it a bad time to talk about {value}?' or 'Are you against seeing how we solved {pain}?'

Generate the email.
"""
    },
    {
        "id": 254,
        "style": "The Calibrated 'How' (Objection Handling)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect has replied saying they need your solution, but their budget has been cut to zero or is locked until next year.
Rule from Book: Use a 'Calibrated Question' (Chapter 7). Do not accept the 'No,' but do not argue. Ask them to explain how you can proceed given the constraint.
Strict Tone: Collaborative and puzzled (not accusatory).
Structure:

Subject line: Re: Budget constraints

Opening: Acknowledge the difficulty of their situation (Labeling).

Core: Use a specific Calibrated Question starting with 'How'. Example: 'How are we supposed to address {pain} if we delay until next year?'

CTA: Leave the question hanging for them to answer.

Generate the email.
"""
    },
    {
        "id": 255,
        "style": "Summary for 'That's Right'",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You have just completed a discovery call. You need to confirm alignment before moving to a demo/proposal.
Rule from Book: Summarize the known facts and emotions (Tactical Empathy). Paraphrase their situation regarding {pain} back to them to trigger a 'That's Right' response.
Strict Tone: Empathetic and precise. No fluff.
Structure:

Subject line: Summary of our conversation

Opening: 'I want to make sure I understood your position correctly.'

Core: List the specific pressures and technical challenges they mentioned regarding {value}. Do not offer your solution yet.

CTA: 'Did I miss anything?' or 'Does that sound right?'

Generate the email.
"""
    },
    {
        "id": 256,
        "style": "The Label (Uncovering the Unknown)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect is stalling on a deal for {value} and giving vague reasons. You suspect there is an internal blocker or hidden objection.
Rule from Book: Use a 'Label' to call out the unexpressed negative emotion or dynamic.
Strict Tone: Observant and calm.
Structure:

Subject line: Thoughts on {value}

Opening: Go straight to the observation.

Core: Use a label structure: 'It seems like there is hesitation regarding {value}.' or 'It sounds like there is an internal voice that hasn't been heard yet.'

CTA: A calibrated question: 'What is the biggest challenge you face in getting this approved?'

Generate the email.
"""
    },
    {
        "id": 257,
        "style": "Finding the Black Swan (Leverage)",
        "text": """
Act as a Senior Sales Executive. You are writing to a procurement manager at {company}.
Context: Negotiations on {value} have stalled over price. You suspect price isn't the real issue; it's likely fear of implementation failure or reputation damage.
Rule from Book: Probe for the 'Black Swan' (the hidden motivator). Use leverage by identifying what they have to lose (Loss Aversion).
Strict Tone: Serious and protective of their interests.
Structure:

Subject line: Implementation concerns

Opening: Acknowledge the price gap briefly.

Core: Pivot to 'Negative Leverage' (Loss Aversion). 'It seems like your biggest concern isn't the price, but the risk of {pain}.'

CTA: 'How does this affect your personal reputation if {value} fails again?'

Generate the email.
"""
    },
    {
        "id": 258,
        "style": "The Ackerman Offer (Price Negotiation)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You are in the final stages of negotiation for {value}. They are demanding a discount you cannot give.
Rule from Book: Apply the 'Ackerman Model' logic. Use a specific, non-round number to give the number credibility and weight. Pivot to non-monetary terms.
Strict Tone: Final but polite.
Structure:

Subject line: Finalizing {value}

Opening: 'I’m afraid I just can’t do that price.' (Direct 'No' delivered gently).

Core: Offer a very specific, calculated number (e.g., {value}). Mention a non-monetary value-add you can include instead of a discount.

CTA: 'Does that work for you?'

Generate the email.
"""
    },
    {
        "id": 259,
        "style": "Depersonalizing the 'No'",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect has requested a feature or term for {value} that your company simply cannot provide.
Rule from Book: Eliminate the word 'I'. Do not say 'I can't do that.' Use 'How' or object-focused sentences to remove your ego from the refusal.
Strict Tone: Objective and constrained.
Structure:

Subject line: Regarding {value}

Opening: Acknowledge the request generosity ('It is a generous request...').

Core: 'How am I supposed to do that?' or 'That just doesn't work for this specific package.'

CTA: 'What is the best way to proceed without that element?'

Generate the email.
"""
    },
    {
        "id": 260,
        "style": "The Rule of Three (Closing)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect agreed to sign the contract for {value} by Friday, but you want to ensure they don't flake.
Rule from Book: Use the 'Rule of Three' logic. You have the first 'Yes'. Now extract the second and third confirmation by labeling the implementation and asking a 'How' question about potential failure.
Strict Tone: Diligent and forward-thinking.
Structure:

Subject line: Implementation timeline

Opening: 'It sounds like we are all set for Friday.' (Confirmation #1).

Core: 'It seems like {title} is fully on board with this timeline.' (Seeking Confirmation #2). 'What do we do if {pain} happens before signature?' (Seeking Confirmation #3 via solution).

CTA: 'Are we 100% ready to go?'

Generate the email.
"""
    },
    {
        "id": 261,
        "style": "The Mirror (Discovery/Deepening)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect sent a short, vague reply declining a meeting (e.g., 'We are focused on other priorities right now' or 'It's too expensive').
Rule from Book: Apply the 'Mirror' technique. Do not counter their objection. Simply repeat their key keywords back to them as a question to force them to explain the 'Why'.
Strict Tone: Inquisitive and calm (Late Night FM DJ Voice).
Structure:

Subject line: Re: [Their last subject line]

Opening: Acknowledge receipt.

Core: Mirror the key phrase from their objection with a question mark. Example: 'Other priorities?' or 'Too expensive?'

CTA: Silence (implied). Just sign off.

Generate the email.
"""
    },
    {
        "id": 262,
        "style": "The 'Fair' Defense (Negotiation)",
        "text": """
Act as a Senior Sales Executive. You are writing to a procurement lead at {company}.
Context: The prospect has accused your pricing for {value} of being unfair or stated, 'We just want what's fair.'
Rule from Book: Defend against the 'F-Bomb' (Fairness). Do not get defensive. Pivot immediately to asking how you have mistreated them or asking for the evidence behind their definition of 'fair.'
Strict Tone: Composed and open.
Structure:

Subject line: Regarding the proposal terms

Opening: State clearly: 'It is my goal to treat you fairly.'

Core: Ask them to stop the negotiation if they feel you aren't being fair. Then ask: 'It seems like you have evidence that supports a lower price?' or 'How have I treated you unfairly?'

CTA: 'Please let me know so I can address it.'

Generate the email.
"""
    },
    {
        "id": 263,
        "style": "The Deadline Test (Stalled Deals)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect is rushing you to sign a contract for {value} by an arbitrary date, demanding concessions to meet that date.
Rule from Book: Test the deadline. Deadlines make people do impulsive things. Calm the situation by asking about the consequences of missing the date.
Strict Tone: Unhurried and analytical.
Structure:

Subject line: Timeline for {value}

Opening: Acknowledge the date they provided.

Core: Use a Calibrated Question to test the reality of the deadline. 'What happens if we don't reach an agreement by {Date}?' or 'How does missing this date affect the larger initiative?'

CTA: 'Let's ensure we get this right, rather than just done.'

Generate the email.
"""
    },
    {
        "id": 264,
        "style": "The Non-Monetary Pivot (Price Negotiation)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: They are demanding a 20% discount on {value} which you cannot approve.
Rule from Book: Pivot to non-monetary terms. Do not say 'No' to the discount directly yet. Ask what else they can offer to make the deal work at your price (e.g., case studies, full upfront payment, longer term).
Strict Tone: Collaborative but firm on value.
Structure:

Subject line: Options for {value}

Opening: 'Let's put price aside for a moment.'

Core: 'What else would you be able to offer to make this a good deal for us at the current price?' Mention specific items like {value} or {value}.

CTA: 'How does that sound?'

Generate the email.
"""
    },
    {
        "id": 265,
        "style": "Identifying the Deal Killers (Multi-Threading)",
        "text": """
Act as a Senior Sales Executive. You are writing to your Champion at {company}.
Context: You have a good relationship with this contact, but you need to uncover the hidden committee members who could kill the deal for {value}.
Rule from Book: Use Calibrated Questions to identify the 'Behind the Table' players. Ask how the deal affects others.
Strict Tone: Strategic and thoughtful.
Structure:

Subject line: internal alignment

Opening: 'It seems like we have a solid path forward.'

Core: Ask: 'How does this project affect the rest of your team?' and 'What do your colleagues see as the main challenges here?'

CTA: 'How on board are the people not on this email chain?'

Generate the email.
"""
    },
    {
        "id": 266,
        "style": "The 'Time-Out' (De-escalation)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The email chain has become aggressive or passive-aggressive regarding contract terms for {value}.
Rule from Book: De-escalate. Do not counter-attack. Suggest a brief pause to reset the dynamic so they regain a sense of agency.
Strict Tone: calm, adult, and poised.
Structure:

Subject line: Pausing for a moment

Opening: 'It seems like we are frustrated with the current progress.' (Labeling).

Core: Suggest taking a step back to ensure we are solving the right problem. 'I want to ensure we aren't losing sight of {value}.'

CTA: 'Shall we reconnect next week once we've reviewed the terms again?'

Generate the email.
"""
    },
    {
        "id": 267,
        "style": "Forced Empathy (Bad News)",
        "text": """
Act as a Senior Sales Executive. You are writing to a long-term client at {company}.
Context: You have to inform them of a price increase for {value} due to inflation/market costs.
Rule from Book: Use 'Forced Empathy' and the 'Chris Discount' concept (humanizing yourself). Make them see you as a person, not a vendor. Use the 'I' message.
Strict Tone: Apologetic but resolute.
Structure:

Subject line: Update on {value} pricing

Opening: 'I’m sorry, but I have some difficult news regarding our renewal.'

Core: Explain the situation using 'I' statements. 'I wish I could keep the rates flat, but I simply can't do that given {value}.'

CTA: 'How can I help you sell this adjustment internally?'

Generate the email.
"""
    },
    {
        "id": 268,
        "style": "The 'No' Setup (Re-engagement)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You are reaching out to a lead from 6 months ago who didn't buy. You want to see if they are ready to reconsider {value}.
Rule from Book: Do not ask 'Do you have time?' Ask a question where the answer 'No' allows the conversation to start.
Strict Tone: Brief and detachment-oriented.
Structure:

Subject line: {pain}

Opening: None.

Core: 'Are you opposed to revisiting the conversation around {value}?'

CTA: None.

Generate the email.
"""
    },
    {
        "id": 269,
        "style": "Spotting the Counterfeit 'Yes' (Qualification)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect said 'Yes' to the proposal very quickly without asking questions. You suspect they might be using you for a price check against a competitor.
Rule from Book: Test the 'Yes'. Ask a 'How' question about implementation to see if they have actually thought about the next steps.
Strict Tone: Skeptical but helpful.
Structure:

Subject line: Implementation of {value}

Opening: 'It's great that we are agreed on the price.'

Core: 'How will we address {pain} once we start?' (Testing if they have a plan).

CTA: 'How does this fit into your current quarterly budget cycle?'

Generate the email.
"""
    },
    {
        "id": 270,
        "style": "Loss Aversion Anchoring (Closing)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The deal for {value} is approved but unsigned. They are dragging their feet.
Rule from Book: Leverage 'Loss Aversion.' Don't talk about benefits. Talk about the concrete cost of inaction/status quo.
Strict Tone: Urgent and protective.
Structure:

Subject line: Cost of delay

Opening: 'I want to ensure we don't lose the ground we've gained.'

Core: 'It seems like every day we delay implementation is costing {company} roughly {value} in inefficiencies.'

CTA: 'Are you willing to risk leaving that on the table for another week?'

Generate the email.
"""
    },
    {
        "id": 271,
        "style": "Proof of Life (Reverse Qualification)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect has asked for a proposal/quote but you suspect they are just using you to drive down the price of their incumbent vendor.
Rule from Book: Use the 'Proof of Life' concept. Ask 'Why us?' questions to see if there is a real deal here. If they can't answer, there is no deal.
Strict Tone: Skeptical and detached.
Structure:

Subject line: Regarding your request

Opening: 'I’m frankly surprised you are considering a switch from {Current_Vendor}.'

Core: Ask a 'Why' question that favors you (the only time 'Why' is allowed). 'Why would you ever consider changing to us given the risk of switching?'

CTA: 'Does it make sense to put this much effort into a switch?'

Generate the email.
"""
    },
    {
        "id": 272,
        "style": "The Mislabel (Information Extraction)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect has gone dark or is giving vague answers about their budget cycle. You need the truth.
Rule from Book: Intentionally 'Mislabel' the situation. State something you suspect is wrong to provoke a correction.
Strict Tone: Casual and slightly confused.
Structure:

Subject line: Budget clarity

Opening: 'I haven't heard back, so I am assuming the worst.'

Core: Drop the Mislabel: 'It seems like {value} has been completely deprioritized and funding has been pulled for the year.'

CTA: None (Silence invites the correction).

Generate the email.
"""
    },
    {
        "id": 273,
        "style": "Strategic Umbrage (Lowball Defense)",
        "text": """
Act as a Senior Sales Executive. You are writing to a procurement officer at {company}.
Context: They just sent a counter-offer for {value} that is 50% below your price and unreasonable.
Rule from Book: Use 'Strategic Umbrage.' Do not attack them personally, but attack the offer with 'I' statements expressing confusion and inability to perform.
Strict Tone: Shocked but professional.
Structure:

Subject line: The proposal terms

Opening: 'I reviewed your counter-offer.'

Core: 'I’m sorry, but I just don’t see how that would ever work.' (Do not offer a counter-number).

CTA: 'How am I supposed to accept that without cutting the core deliverables that solve {pain}?'

Generate the email.
"""
    },
    {
        "id": 274,
        "style": "Normative Leverage (Consistency Trap)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect previously stated that {value} was their #1 priority, but they are now delaying the deal over a minor cost difference.
Rule from Book: Apply 'Normative Leverage.' Quote their own words back to them to highlight the hypocrisy/inconsistency gently.
Strict Tone: Direct and factual.
Structure:

Subject line: Your goal regarding {value}

Opening: 'In our last conversation, you stated that {value} was the single most important metric for Q3.'

Core: 'It seems like we are now prioritizing a marginal cost saving over that primary goal.'

CTA: 'Did I misunderstand your objective?'

Generate the email.
"""
    },
    {
        "id": 275,
        "style": "The Authority Label (Gatekeeper Bypass)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The contact is deferring the decision for {value} to a superior, stalling the deal.
Rule from Book: Use a specific Label to challenge their status without being rude.
Strict Tone: Deferential but challenging.
Structure:

Subject line: Approval process

Opening: Acknowledge the need for internal buy-in.

Core: 'It seems like you don’t have the latitude to make this decision on your own.' OR 'It seems like {title} is the only one who understands the strategic value here.'

CTA: 'How should we proceed?'

Generate the email.
"""
    },
    {
        "id": 276,
        "style": "The 'I'm an Asshole' (Mistake Recovery)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You missed a scheduled call or your team dropped the ball on a deliverable. The client is angry.
Rule from Book: Use the 'Bless me father for I have sinned' approach. Call yourself out immediately.
Strict Tone: Humble and direct.
Structure:

Subject line: I messed up

Opening: 'I am going to be the first to say it—I dropped the ball.'

Core: 'I know you are frustrated, and you have every right to be. It seems like I didn't respect your time.'

CTA: 'How would you like to proceed from here?'

Generate the email.
"""
    },
    {
        "id": 277,
        "style": "The 'In-House' Challenge (Competitor Pivot)",
        "text": """
Act as a Senior Sales Executive. You are writing to a VP of Operations at {company}.
Context: The prospect wants to build a solution for {pain} internally rather than buying your {value}.
Rule from Book: Do not argue facts. Use 'How' questions to make them visualize the difficulty of execution.
Strict Tone: Concerned and helpful.
Structure:

Subject line: Internal build vs. {value}

Opening: 'It sounds like you have a talented team.'

Core: 'How will you handle the maintenance debt three months from now when your engineers need to focus on {value}?'

CTA: 'Does it make sense to allocate resources to a non-core competency?'

Generate the email.
"""
    },
    {
        "id": 278,
        "style": "Closing the Loophole (Commitment Test)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect replied to your timeline request with 'We'll try to get that signed by Friday.' This is a red flag.
Rule from Book: Recognize that 'I'll try' usually means 'I plan to fail.' Dive back in with a Calibrated Question.
Strict Tone: Vigilant.
Structure:

Subject line: Friday timeline

Opening: 'I noticed you said you’ll "try" to get it done.'

Core: 'How do we address things if we find we are off track on Thursday?'

CTA: 'What happens if we miss this deadline?'

Generate the email.
"""
    },
    {
        "id": 279,
        "style": "The 'Why' Pivot (Selling the Change)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You are in early discovery. You want them to pitch you on why they need to solve {pain}.
Rule from Book: Ask 'Why' to trigger them to defend your position.
Strict Tone: Curious and challenging.
Structure:

Subject line: Context on {value}

Opening: 'I know {value} has worked for you for years.'

Core: 'Why change now? Why not just stay with the current system and save the budget?'

CTA: 'Is this really a priority?'

Generate the email.
"""
    },
    {
        "id": 280,
        "style": "The 7-38-55 Text/Tone Check",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect's latest email was one word ('Fine' or 'Ok') or very terse, which contradicts their previous enthusiasm.
Rule from Book: Apply the '7-38-55' rule logic to text. Label the shift in 'digital tone.'
Strict Tone: Tentative and concerned.
Structure:

Subject line: Checking in

Opening: 'I read your last note.'

Core: 'It seems like there is some hesitation or frustration on your end regarding the latest terms.'

CTA: 'Am I reading that right?'

Generate the email.
"""
    },
    {
        "id": 281,
        "style": "The Price Anchor (Accusation Audit)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You are about to send a proposal for {value} that is significantly more expensive than their budget or the competition.
Rule from Book: Use an 'Accusation Audit' to anchor emotions before they see the number. Predict their negative reaction to soften the blow.
Strict Tone: Confident but self-effacing.
Structure:

Subject line: Proposal for {value}

Opening: 'Before you open the attached, I want to warn you.'

Core: 'You are going to think this is expensive. You might even think I am out of my mind regarding the budget for {value}.'

CTA: 'After you review the value breakdown, let me know if I am actually crazy.'

Generate the email.
"""
    },
    {
        "id": 282,
        "style": "'What Are We Up Against?' (Competition)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You know they are evaluating other vendors for {value}, but you don't know who or what the criteria are.
Rule from Book: Do not ask 'Who else are you talking to?' Use a 'What' question to identify the hurdles or competitive landscape.
Strict Tone: Strategic and curious.
Structure:

Subject line: Evaluation criteria

Opening: 'I want to ensure we are addressing the right variables.'

Core: 'What are we up against in terms of other approaches to {value}?' OR 'What keeps you from simply staying with {Current_Vendor}?'

CTA: 'How does our approach compare to the field so far?'

Generate the email.
"""
    },
    {
        "id": 283,
        "style": "The Scope Defense (Calibrated 'How')",
        "text": """
Act as a Senior Sales Executive. You are writing to a Client Manager at {company}.
Context: The client has requested an add-on or extra service for {value} but expects it to be included in the original fee.
Rule from Book: Use the classic 'How am I supposed to do that?' defense. Do not get angry. Ask them to solve the resource problem.
Strict Tone: Deferential but firm.
Structure:

Subject line: Request for {value}

Opening: 'I would love to include that feature.'

Core: 'But if we add that scope without adjusting the budget, how am I supposed to maintain the quality of the core deliverables we agreed upon?'

CTA: 'How would you like me to prioritize the resources?'

Generate the email.
"""
    },
    {
        "id": 284,
        "style": "The 'Bad Faith' Label (Negotiation Reset)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You had a verbal agreement on terms for {value}, but legal/procurement has just redlined the document and changed the deal significantly.
Rule from Book: Label the dynamic. Do not accuse them of lying. Label the appearance of the situation.
Strict Tone: Cold and confused.
Structure:

Subject line: Contract redlines

Opening: 'I reviewed the latest changes.'

Core: 'It seems like we are moving the goalposts regarding {value}.' OR 'It seems like the terms we agreed upon verbally are no longer valid.'

CTA: 'How do we get back to the original agreement?'

Generate the email.
"""
    },
    {
        "id": 285,
        "style": "The 'Ridiculous Idea' (Pattern Interrupt)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You want to suggest a meeting, a demo, or a specific next step that is slightly bold or out of the ordinary process.
Rule from Book: Frame the request to trigger a 'No' answer. Use the phrase 'Is it a ridiculous idea...'
Strict Tone: Casual and low stakes.
Structure:

Subject line: Idea for {value}

Opening: 'I was thinking about how to solve {pain}.'

Core: 'Is it a ridiculous idea to skip the formal RFP process and do a paid pilot for {value} instead?'

CTA: Just the question above.

Generate the email.
"""
    },
    {
        "id": 286,
        "style": "The Implementation Audit (Post-Sale)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The contract for {value} is signed. You are handing off to Customer Success but want to prevent churn.
Rule from Book: Use Calibrated Questions to define success and failure modes (Pre-Mortem).
Strict Tone: Forward-looking and protective.
Structure:

Subject line: Defining success for {value}

Opening: 'We are excited to get started.'

Core: 'What will happen if we are not fully live by {Date}?' AND 'How will we know we are off track before it becomes a critical issue?'

CTA: 'Does it make sense to map those risks now?'

Generate the email.
"""
    },
    {
        "id": 287,
        "style": "The 'Stalled' Label",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You have had three good meetings regarding {value}, but they haven't replied to your last two emails.
Rule from Book: Label the silence/negative status. Do not ask 'Just checking in.'
Strict Tone: Direct and devoid of neediness.
Structure:

Subject line: {value} status

Opening: None.

Core: 'It seems like I've lost you.' OR 'It seems like you've decided to go in a different direction.'

CTA: None.

Generate the email.
"""
    },
    {
        "id": 288,
        "style": "The Internal Sell (Coaching the Champion)",
        "text": """
Act as a Senior Sales Executive. You are writing to your Champion at {company}.
Context: Your Champion loves {value} but has to present it to the CFO for budget approval. You worry they will fail.
Rule from Book: Use Calibrated Questions to make them simulate the internal conversation.
Strict Tone: Collaborative/Coaching.
Structure:

Subject line: Presentation to {title}

Opening: 'I want to make sure you are armed for the meeting.'

Core: 'How will you handle it if {title} asks why this budget can't be delayed to next year?'

CTA: 'What is the best way for me to support you in that conversation?'

Generate the email.
"""
    },
    {
        "id": 289,
        "style": "The 'Vision' Pivot (Upsell)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You are trying to upsell them from the Basic Plan to the Enterprise Plan. They are stuck on the price difference.
Rule from Book: Pivot to their aspirations/religion (worldview). Sell the 'Ideal Future' using a summary.
Strict Tone: Visionary.
Structure:

Subject line: Long-term goals for {title}

Opening: 'It seems like your goal is not just to fix {pain}, but to transform the way {company} handles {value}.'

Core: 'The Enterprise tier is built specifically for that transformation. Sticking with Basic seems like it keeps you in "fix-it" mode rather than "growth" mode.'

CTA: 'Does that sound right?'

Generate the email.
"""
    },
    {
        "id": 290,
        "style": "The '65%' Response (Handling Procurement)",
        "text": """
Act as a Senior Sales Executive. You are writing to Procurement at {company}.
Context: Procurement has demanded a 15% cut on the final contract value of {value}.
Rule from Book: Use the logic of the Ackerman Model (Step 2/3). Suggest you have already cut to the bone. Use a precise, non-round number to suggest calculation.
Strict Tone: Constrained and final.
Structure:

Subject line: Final adjustments

Opening: 'I appreciate you trying to get the best value for {company}.'

Core: 'I have crunched the numbers to their absolute limit. The best I can do is {value} (e.g., $84,965).'

CTA: 'I’m afraid I just can’t do a penny less. Does that number work for you?'

Generate the email.
"""
    },
    {
        "id": 291,
        "style": "The Name Pivot (Humanizing/Discount)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You are asking for a favor—either a faster signature or a testimonial—but you have run out of leverage. You need to rely on the relationship.
Rule from Book: Use your name. Introduce yourself in the third person to break the pattern and create a moment of human connection.
Strict Tone: Friendly but expectant.
Structure:

Subject line: A favor for {My_First_Name}

Opening: 'I was hoping I could ask for a personal favor.'

Core: 'What is the {My_First_Name} discount on getting this signature processed by Friday?' (Or similar construction using your name).

CTA: 'Is that feasible?'

Generate the email.
"""
    },
    {
        "id": 292,
        "style": "The 'Paradox of Power' (Walking Away)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect is demanding unreasonable terms or endless free consulting for {value}. You need to regain control.
Rule from Book: Apply the 'Paradox of Power.' Withdraw the proposal gently to show you are not needy (Neediness is a deal killer).
Strict Tone: Professional and detached.
Structure:

Subject line: Withdrawal of proposal

Opening: 'I’ve been thinking about our last conversation.'

Core: 'It seems like we are not the right fit for {company} at this stage. I don't want to force a fit where there isn't one.'

CTA: 'I am going to pull our proposal for now to save us both time. I wish you the best.'

Generate the email.
"""
    },
    {
        "id": 293,
        "style": "Labeling the Saboteur (Ghost-Busting)",
        "text": """
Act as a Senior Sales Executive. You are writing to a Champion at {company}.
Context: The deal was progressing, but now there is silence. You suspect an internal detractor (perhaps IT or Legal) is blocking it.
Rule from Book: Label the hidden dynamic. Suggest that someone else is the problem.
Strict Tone: Intuitive and direct.
Structure:

Subject line: Internal roadblocks

Opening: None.

Core: 'It seems like there is a voice in the room that we haven't addressed yet.' OR 'It seems like someone on the team is uncomfortable with this change.'

CTA: 'Who is it?'

Generate the email.
"""
    },
    {
        "id": 294,
        "style": "The 'Yesterday' Label (Relationship Repair)",
        "text": """
Act as a Senior Sales Executive. You are writing to a Client Lead at {company}.
Context: A long-time client is suddenly making unreasonable demands or threatening to churn over a minor issue with {value}.
Rule from Book: Use a 'Past Label.' Remind them of the previous relationship standard to diffuse the current negativity.
Strict Tone: Confused and disappointed.
Structure:

Subject line: Our partnership

Opening: 'We have worked together for {Duration}.'

Core: 'You have always been fair and logical in the past. It seems like something has changed drastically on your end to cause this reaction.'

CTA: 'What is the real issue here?'

Generate the email.
"""
    },
    {
        "id": 295,
        "style": "Labeling the Fear (Risk Mitigation)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: The prospect has the budget and the need, but still won't pull the trigger on {value}. They are paralyzed.
Rule from Book: Label the fear. Do not sell benefits. Call out the anxiety of the decision.
Strict Tone: Empathetic and low-pressure.
Structure:

Subject line: Hesitation regarding {value}

Opening: 'I sense some hesitation.'

Core: 'It seems like you are worried that this implementation might fail and reflect poorly on you.'

CTA: 'What is the worst-case scenario you are envisioning?'

Generate the email.
"""
    },
    {
        "id": 296,
        "style": "The 'What' Definition (Scope Control)",
        "text": """
Act as a Senior Sales Executive. You are writing to a Project Lead at {company}.
Context: The client is getting bogged down in minor details or feature requests that don't matter for the main goal of {value}.
Rule from Book: Use a Calibrated 'What' question to refocus the lens on the objective.
Strict Tone: Big-picture focused.
Structure:

Subject line: Project objectives

Opening: 'I want to ensure we aren't getting lost in the weeds.'

Core: 'What is the core objective we are trying to accomplish with {value}?'

CTA: 'Does this current request help us get there?'

Generate the email.
"""
    },
    {
        "id": 297,
        "style": "The 'No' Exit (Pipeline Cleaning)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: This prospect has been in your pipeline for 6 months with no movement. You want to close the file.
Rule from Book: Go for the 'No.' Give them permission to reject you so you can stop wasting time.
Strict Tone: Final.
Structure:

Subject line: Closing file on {value}

Opening: 'I am writing to cross this off my list.'

Core: 'It seems like {value} is not a priority for 2024. I’m going to assume the answer is no and close this file.'

CTA: None.

Generate the email.
"""
    },
    {
        "id": 298,
        "style": "The Authority Test (Signing Power)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You are unsure if this person can actually sign the contract for {value} or if they need to ask a board/boss.
Rule from Book: Don't ask if they are the decision maker. Ask 'How' the decision is made.
Strict Tone: Process-oriented.
Structure:

Subject line: Execution process

Opening: 'We are ready to move to paperwork.'

Core: 'How does the signing process work at {company} for a deal of this size?' AND 'Who else needs to touch the document before it is valid?'

CTA: Just the questions above.

Generate the email.
"""
    },
    {
        "id": 299,
        "style": "The 'Unknown Unknown' Probe (Discovery)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You are in deep discovery. You feel like you are missing a piece of the puzzle regarding their timeline for {value}.
Rule from Book: Ask a question that invites them to reveal hidden constraints.
Strict Tone: Curious.
Structure:

Subject line: Context for {value}

Opening: 'I feel like I'm missing a piece of the puzzle.'

Core: 'What is it that we don't know about the internal pressures you are facing?'

CTA: 'How does that impact our timeline?'

Generate the email.
"""
    },
    {
        "id": 300,
        "style": "The Final 'That's Right' (Contract Confirmation)",
        "text": """
Act as a Senior Sales Executive. You are writing to a {title} at {company}.
Context: You are about to send the final contract for signature. You want to ensure zero friction.
Rule from Book: Summarize the entire value proposition and terms to trigger a 'That's Right' confirmation.
Strict Tone: Summary/Recap.
Structure:

Subject line: Summary of agreement

Opening: 'Before I send the docusign, I want to ensure I have this perfect.'

Core: Summarize the pain, the solution ({value}), the price, and the timeline in 3 bullet points.

CTA: 'Does that sound right?' (Do not send contract until they confirm).

Generate the email.
"""
    }
]
