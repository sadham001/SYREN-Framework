# SYREN PolicyGPT Simulator
import random

# Define available policy types
policies = [
    "GDPR-AI-Compliance",
    "Zero-Trust-AI-Adapter",
    "AI-Risk-Management-Policy"
]

# Function to generate policies
def generate_policy(policy_type):
    print(f"🔧 SYREN generated {policy_type} policy!")
    # Generate policy file name based on the policy type and unique hash
    file_name = f"/policies/{policy_type}-{str(hash(policy_type))[:6]}.md"
    print(f"📄 Saved to {file_name}")

# Simulate policy generation based on random selection from the list
if __name__ == "__main__":
    selected_policy = random.choice(policies)  # Randomly select a policy
    generate_policy(selected_policy)  # Generate and save the policy
