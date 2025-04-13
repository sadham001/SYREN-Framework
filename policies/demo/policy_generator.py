# SYREN PolicyGPT Simulator  
policies = ["GDPR", "Zero-Trust", "AI-Risk"]  

def generate_policy(policy_type):  
    print(f"🔧 SYREN generated {policy_type} policy!")  
    print(f"📄 Saved to /policies/{policy_type}-{str(hash(policy_type))[:6]}.md")  

generate_policy(random.choice(policies))  