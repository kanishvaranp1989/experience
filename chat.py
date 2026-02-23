def chat_handle(message, id_token=None):
    """Smart chat handler that answers questions based on user's experience.

    Parameters:
    - message: str message from user
    - id_token: optional authentication token

    Returns a string reply with information about Kanish's experience.
    """
    message = (message or '').strip().lower()
    if not message:
        return "I didn't receive any message. Please ask me something!"

    # Greetings
    if any(word in message for word in ['hello', 'hi', 'hey', 'greetings']):
        return 'Hi there! 👋 I\'m here to tell you about Kanish\'s experience and skills. What would you like to know?'

    # Experience & Role
    if any(word in message for word in ['role', 'position', 'job', 'work', 'sre', 'reliability engineer']):
        return 'Kanish is a Site Reliability Engineer (SRE) focused on infrastructure automation and production systems. He specializes in debugging complex production incidents and automating operational runbooks to improve system reliability.'

    # Skills & Expertise
    if any(word in message for word in ['skill', 'expertise', 'experience', 'know', 'technology', 'tech']):
        return 'Kanish has extensive experience with: Azure cloud, Confluent Kafka, Terraform, Kubernetes, and Linux-based systems. He can work on any equivalent cloud environment, including AWS (which powers this site). He\'s skilled in automation, infrastructure-as-code, and production system management.'

    # Achievements
    if any(word in message for word in ['achieve', 'accomplishment', 'success', 'done', 'result', 'impact']):
        return 'Key achievements: (1) Built a Python Flask tool to streamline workflows, reducing manual effort by 40%. (2) Automated critical tasks after vendor upgrade, eliminating 100% of manual intervention. (3) Authored Python automation scripts saving ~20 hours/week of manual work. His focus is on reducing human error through smart automation.'

    # Resume
    if any(word in message for word in ['resume', 'download', 'pdf', 'cv','years of experience','years']):
        return 'You can download Kanish\'s resume by clicking the "Generate resume link" button in the Welcome section. The link will be valid for 45 minutes.'

    # Onboarding / First days
    if any(word in message for word in ['onboarding', 'first', 'days', 'plan', '30 days']):
        return 'Kanish\'s 42-day onboarding plan: Days 1-7 (paperwork & setup), 7-14 (team & workflows), 14-21 (cross-functional teams), 21-28 (org processes), 28-35 (end-to-end workflows), 35-42 (team goals), 42+ (continuous improvement). See the Onboarding section for more details.'

    # AWS Services
    if any(word in message for word in ['aws', 'amazon', 'cloud', 'ec2', 'lambda', 's3', 'cognito', 'api gateway']):
        return 'This site leverages AWS services: Cognito (auth), EC2 (compute), API Gateway (entrypoint), Lambda (backend logic), S3 (storage), CloudWatch (monitoring). Kanish has worked with all these and can adapt to any cloud environment.'

    # Contact / Message
    if any(word in message for word in ['contact', 'message', 'email', 'reach', 'connect']):
        return 'You can reach out using the Contact form in the Contact section. Just provide your email and message (max 100 words). Your message will be processed via AWS Lambda and AWS SES will send confirmations.'

    # Default: provide helpful suggestion
    return f"That\'s an interesting question! I can help you learn about Kanish\'s experience, skills, achievements, resume, or onboarding plan. Feel free to ask about any of these topics!"
