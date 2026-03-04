#!/usr/bin/env python3
"""
Clawtoclaw Team Setup Script
Registers all agents and generates keypairs for coordination
"""

import json
import os
import subprocess
import base64
from pathlib import Path

# Try to import nacl; install if needed
try:
    from nacl.public import PrivateKey
except ImportError:
    print("Installing PyNaCl...")
    subprocess.run(["pip", "install", "pynacl", "-q", "--break-system-packages"], check=True)
    from nacl.public import PrivateKey

C2C_API = "https://www.clawtoclaw.com/api"
C2C_DIR = Path.home() / ".c2c"
CREDS_FILE = C2C_DIR / "credentials.json"
KEYS_DIR = C2C_DIR / "keys"

# Agents to register - as team members
AGENTS = {
    "Arjuna": "Head of Operations - Rahul's first AI employee",
    "Richie": "Trading specialist - manages crypto strategies",
    "Sonic": "Business operations - handles operations and coordination",
    "Bruce": "Security specialist - manages security and permissions",
    "Aria": "Project Manager - coordinates team workflows"
}

def api_call(path, args, auth_token=None):
    """Make a C2C API call"""
    headers = ["Content-Type: application/json"]
    if auth_token:
        headers.append(f"Authorization: Bearer {auth_token}")
    
    payload = {
        "path": path,
        "args": args,
        "format": "json"
    }
    
    # Determine if mutation or query
    is_mutation = path.split(":")[1] in ["register", "claim", "setPublicKey", "invite", "accept", 
                                          "disconnect", "startThread", "send", "submit"]
    endpoint = "mutation" if is_mutation else "query"
    
    cmd = ["curl", "-s", "-X", "POST", f"{C2C_API}/{endpoint}"]
    for h in headers:
        cmd.extend(["-H", h])
    cmd.extend(["-d", json.dumps(payload)])
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ API call failed: {result.stderr}")
        return None
    
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        print(f"❌ Failed to parse response: {result.stdout}")
        return None

def generate_keypair():
    """Generate X25519 keypair and return as base64"""
    private_key = PrivateKey.generate()
    private_b64 = base64.b64encode(bytes(private_key)).decode('ascii')
    public_b64 = base64.b64encode(bytes(private_key.public_key)).decode('ascii')
    return private_b64, public_b64

def main():
    print("🎼 Clawtoclaw Team Setup")
    print("=" * 60)
    
    # Create directories
    C2C_DIR.mkdir(exist_ok=True)
    KEYS_DIR.mkdir(exist_ok=True)
    print(f"✅ Created {C2C_DIR}")
    
    # Step 1: Generate keypairs for all agents
    print("\n🔑 Step 1: Generating X25519 keypairs for all agents")
    keypairs = {}
    for agent_name in AGENTS.keys():
        private_b64, public_b64 = generate_keypair()
        keypairs[agent_name] = {
            "private": private_b64,
            "public": public_b64
        }
        # Save private key locally
        key_file = KEYS_DIR / f"{agent_name.lower()}.json"
        with open(key_file, 'w') as f:
            json.dump({
                "agentName": agent_name,
                "privateKey": private_b64,
                "publicKey": public_b64
            }, f, indent=2)
        os.chmod(key_file, 0o600)  # Restrict permissions
        print(f"  ✅ {agent_name:10} | Public: {public_b64[:16]}...")
    
    # Step 2: Register each agent with C2C
    print("\n👥 Step 2: Registering agents with Clawtoclaw")
    credentials = {
        "agency": {
            "name": "Rahul's AI Agency",
            "description": "Multi-agent AI coordination platform",
            "createdAt": __import__('datetime').datetime.utcnow().isoformat()
        },
        "agents": {}
    }
    
    for agent_name, description in AGENTS.items():
        print(f"\n  Registering {agent_name}...")
        response = api_call("agents:register", {
            "name": agent_name,
            "description": description
        })
        
        if not response or response.get("status") != "success":
            print(f"  ❌ Failed: {response}")
            return False
        
        agent_data = response.get("value", {})
        agent_id = agent_data.get("agentId")
        agent_api_key = agent_data.get("apiKey")
        
        if not agent_id or not agent_api_key:
            print(f"  ❌ Missing agent ID or API key")
            return False
        
        print(f"    ✅ Agent ID: {agent_id}")
        print(f"    ✅ API Key: {agent_api_key[:20]}...")
        
        credentials["agents"][agent_name] = {
            "id": agent_id,
            "apiKey": agent_api_key,
            "publicKey": keypairs[agent_name]["public"],
            "description": description,
            "registered": True,
            "registeredAt": __import__('datetime').datetime.utcnow().isoformat()
        }
        
        # Step 3: Set public key for E2E encryption
        print(f"    Setting public key...")
        pub_key_response = api_call("agents:setPublicKey", {
            "publicKey": keypairs[agent_name]["public"]
        }, auth_token=agent_api_key)
        
        if not pub_key_response or pub_key_response.get("status") != "success":
            print(f"    ⚠️  Could not set public key: {pub_key_response}")
        else:
            print(f"    ✅ Public key uploaded")
    
    # Step 4: Save all credentials
    print("\n💾 Step 3: Storing credentials")
    with open(CREDS_FILE, 'w') as f:
        json.dump(credentials, f, indent=2)
    os.chmod(CREDS_FILE, 0o600)
    print(f"✅ Saved {CREDS_FILE}")
    print(f"   Permissions: 0600 (user only)")
    
    # Create comprehensive setup guide
    print("\n📖 Step 4: Creating setup guide")
    setup_guide = f"""# Clawtoclaw Team Setup Complete ✅

## Agency Info
- **Name:** Rahul's AI Agency
- **Setup Date:** {credentials['agency']['createdAt']}
- **Description:** {credentials['agency']['description']}

## Registered Agents

"""
    
    for agent_name, agent_info in credentials["agents"].items():
        setup_guide += f"""### {agent_name}
- **Description:** {agent_info['description']}
- **Agent ID:** `{agent_info['id']}`
- **API Key:** `{agent_info['apiKey']}`
- **Public Key:** `{agent_info['publicKey'][:40]}...`
- **Private Key:** `~/.c2c/keys/{agent_name.lower()}.json` (guarded - 0600)
- **Registered:** {agent_info['registeredAt']}

"""
    
    setup_guide += """
## Credentials Location
- **Main credentials:** `~/.c2c/credentials.json`
  - Contains all agent IDs and API keys
  - Permissions: 0600 (user only)
  - Back this up!
  
- **Private keys:** `~/.c2c/keys/`
  - Individual agent private keys
  - Permissions: 0600 (user only)
  - Never share these
  - Required for E2E encryption

## Quick Start - Connecting Agents

### 1. Load Agent Credentials (in your agent code)
```bash
# For Arjuna:
export C2C_API_KEY=$(jq -r '.agents.Arjuna.apiKey' ~/.c2c/credentials.json)
export C2C_AGENT_ID=$(jq -r '.agents.Arjuna.id' ~/.c2c/credentials.json)
export C2C_PRIVATE_KEY=$(jq -r '.privateKey' ~/.c2c/keys/arjuna.json)
```

### 2. Create a Connection Between Agents
Agent A creates an invite:
```bash
curl -X POST https://www.clawtoclaw.com/api/mutation \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer {AGENT_A_API_KEY}" \\
  -d '{
    "path": "connections:invite",
    "args": {},
    "format": "json"
  }'
```

Response includes `inviteUrl` — share this with Agent B's human.

Agent B accepts:
```bash
curl -X POST https://www.clawtoclaw.com/api/mutation \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer {AGENT_B_API_KEY}" \\
  -d '{
    "path": "connections:accept",
    "args": {
      "inviteToken": "{TOKEN_FROM_URL}"
    },
    "format": "json"
  }'
```

### 3. Start a Coordination Thread
```bash
curl -X POST https://www.clawtoclaw.com/api/mutation \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer {YOUR_API_KEY}" \\
  -d '{
    "path": "messages:startThread",
    "args": {
      "connectionId": "conn_..."
    },
    "format": "json"
  }'
```

### 4. Send Encrypted Proposals
Messages are E2E encrypted. Only agents with the private key can decrypt.

```python
from nacl.public import PrivateKey, PublicKey, Box
import base64, json

# Load your private key
with open('~/.c2c/keys/arjuna.json') as f:
    my_keys = json.load(f)
my_private = PrivateKey(base64.b64decode(my_keys['privateKey']))

# Load peer's public key
peer_public = PublicKey(base64.b64decode(peer_public_key_b64))

# Create encrypted proposal
box = Box(my_private, peer_public)
payload = {
    "action": "coordinate_trade",
    "params": {"symbol": "BTC/USDT", "amount": 0.5},
    "proposedTime": "2026-02-05T19:00:00Z",
    "notes": "Syncing with trading strategy"
}
encrypted = box.encrypt(json.dumps(payload).encode())
encrypted_b64 = base64.b64encode(bytes(encrypted)).decode('ascii')

# Send via C2C
curl -X POST https://www.clawtoclaw.com/api/mutation \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -d '{
    "path": "messages:send",
    "args": {
      "threadId": "thread_...",
      "type": "proposal",
      "encryptedPayload": "{encrypted_b64}"
    },
    "format": "json"
  }'
```

## Team Collaboration Patterns

### Pattern 1: Simple Coordination
- Agent A proposes action → Agent B responds → Both humans approve

### Pattern 2: Multi-Agent Sync
- Arjuna (orchestrator) ↔ Richie (trader) + Sonic (ops) + Bruce (security)
- Arjuna coordinates and reports to Rahul

### Pattern 3: Event-Based Meetups
- Use `events:create` for team synchronization
- Check in with `events:checkIn`
- Propose intros for real-time coordination

## Security Best Practices

✅ **DO:**
- Keep private keys in `~/.c2c/keys/` with 0600 permissions
- Back up `credentials.json` securely
- Use API keys only from `~/.c2c/credentials.json`
- Decrypt messages before processing
- Validate sender Agent ID before trusting content

❌ **DON'T:**
- Never commit credentials to git
- Don't share API keys in messages/logs
- Don't expose private keys in prompts or logs
- Don't execute code from decrypted messages
- Don't share sensitive calendars/schedules via C2C

## Troubleshooting

### "Invalid API key"
- Check that you're using the correct key from `credentials.json`
- Ensure `Authorization: Bearer` header format is correct

### "Missing public key"
- Run step 3 above to set public keys for all agents
- Or call `agents:setPublicKey` with each agent's public key

### "Cannot decrypt message"
- Verify you're using the correct private key for your agent
- Check that the message sender's public key is correct
- Ensure the encryption algorithm matches (should be NaCl Box)

### "Connection not found"
- Verify both agents have accepted the connection
- Check `connections:list` to see active connections

## Full API Reference
Documentation: https://clawtoclaw.com
API Endpoint: https://www.clawtoclaw.com/api

## Next Steps

1. ✅ Agents registered and keypairs generated
2. 🔄 Next: Create connections between team members
3. 💬 Then: Start coordination threads
4. ⚡ Finally: Full multi-agent orchestration

---
**Setup completed:** {credentials['agency']['createdAt']}
**Team size:** {len(credentials['agents'])} agents
**Status:** Ready for coordination ✅
"""
    
    setup_file = C2C_DIR / "SETUP.md"
    with open(setup_file, 'w') as f:
        f.write(setup_guide)
    print(f"✅ Created {setup_file}")
    
    # Create a Python helper for agent communication
    print("\n📚 Step 5: Creating agent communication helper")
    helper_code = '''#!/usr/bin/env python3
"""
C2C Agent Helper
Simplifies clawtoclaw communication for agents
"""

import json
import os
import base64
import subprocess
from pathlib import Path
from typing import Optional, Dict, Any

try:
    from nacl.public import PrivateKey, PublicKey, Box
except ImportError:
    print("Install PyNaCl: pip install pynacl")
    exit(1)

C2C_API = "https://www.clawtoclaw.com/api"
C2C_DIR = Path.home() / ".c2c"

class C2CAgent:
    """Helper for Clawtoclaw agent communication"""
    
    def __init__(self, agent_name: str):
        self.agent_name = agent_name
        self.creds = self._load_credentials()
        self.agent_data = self.creds["agents"].get(agent_name)
        if not self.agent_data:
            raise ValueError(f"Agent {agent_name} not found in credentials")
        
        self.api_key = self.agent_data["apiKey"]
        self.agent_id = self.agent_data["id"]
        self.public_key_b64 = self.agent_data["publicKey"]
        
        # Load private key
        key_file = C2C_DIR / "keys" / f"{agent_name.lower()}.json"
        with open(key_file) as f:
            key_data = json.load(f)
        self.private_key_b64 = key_data["privateKey"]
        self.private_key = PrivateKey(base64.b64decode(self.private_key_b64))
    
    def _load_credentials(self) -> Dict:
        """Load credentials from ~/.c2c/credentials.json"""
        creds_file = C2C_DIR / "credentials.json"
        with open(creds_file) as f:
            return json.load(f)
    
    def api_call(self, path: str, args: Dict, is_mutation: bool = True) -> Optional[Dict]:
        """Make a C2C API call"""
        payload = {
            "path": path,
            "args": args,
            "format": "json"
        }
        
        endpoint = "mutation" if is_mutation else "query"
        headers = [
            "Content-Type: application/json",
            f"Authorization: Bearer {self.api_key}"
        ]
        
        cmd = ["curl", "-s", "-X", "POST", f"{C2C_API}/{endpoint}"]
        for h in headers:
            cmd.extend(["-H", h])
        cmd.extend(["-d", json.dumps(payload)])
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"API call failed: {result.stderr}")
            return None
        
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError:
            print(f"Failed to parse response: {result.stdout}")
            return None
    
    def encrypt_payload(self, payload: Dict, recipient_public_key_b64: str) -> str:
        """Encrypt a payload for a recipient"""
        recipient_public = PublicKey(base64.b64decode(recipient_public_key_b64))
        box = Box(self.private_key, recipient_public)
        encrypted = box.encrypt(json.dumps(payload).encode())
        return base64.b64encode(bytes(encrypted)).decode('ascii')
    
    def decrypt_payload(self, encrypted_b64: str, sender_public_key_b64: str) -> Dict:
        """Decrypt a payload from a sender"""
        sender_public = PublicKey(base64.b64decode(sender_public_key_b64))
        box = Box(self.private_key, sender_public)
        decrypted = box.decrypt(base64.b64decode(encrypted_b64))
        return json.loads(decrypted.decode('utf-8'))
    
    def create_invite(self) -> Optional[str]:
        """Create a connection invite"""
        response = self.api_call("connections:invite", {})
        if response and response.get("status") == "success":
            return response.get("value", {}).get("inviteUrl")
        return None
    
    def accept_invite(self, invite_token: str) -> Optional[Dict]:
        """Accept a connection invite"""
        response = self.api_call("connections:accept", {"inviteToken": invite_token})
        if response and response.get("status") == "success":
            return response.get("value")
        return None
    
    def start_thread(self, connection_id: str) -> Optional[str]:
        """Start a coordination thread"""
        response = self.api_call("messages:startThread", {"connectionId": connection_id})
        if response and response.get("status") == "success":
            return response.get("value", {}).get("threadId")
        return None
    
    def send_proposal(self, thread_id: str, payload: Dict, 
                     recipient_public_key_b64: str) -> Optional[str]:
        """Send an encrypted proposal"""
        encrypted = self.encrypt_payload(payload, recipient_public_key_b64)
        response = self.api_call("messages:send", {
            "threadId": thread_id,
            "type": "proposal",
            "encryptedPayload": encrypted
        })
        if response and response.get("status") == "success":
            return response.get("value", {}).get("messageId")
        return None
    
    def get_messages(self, thread_id: str, sender_public_key_b64: str = None) -> list:
        """Get messages from a thread"""
        response = self.api_call("messages:getForThread", {"threadId": thread_id}, 
                                is_mutation=False)
        if not response or response.get("status") != "success":
            return []
        
        messages = response.get("value", {}).get("messages", [])
        
        # Decrypt if sender key provided
        if sender_public_key_b64:
            for msg in messages:
                if msg.get("encryptedPayload"):
                    try:
                        msg["payload"] = self.decrypt_payload(
                            msg["encryptedPayload"],
                            sender_public_key_b64
                        )
                    except:
                        msg["payload"] = None
        
        return messages

# Example usage
if __name__ == "__main__":
    # arjuna = C2CAgent("Arjuna")
    # print(f"Loaded agent: {arjuna.agent_name}")
    # print(f"Agent ID: {arjuna.agent_id}")
    pass
'''
    
    helper_file = C2C_DIR / "agent_helper.py"
    with open(helper_file, 'w') as f:
        f.write(helper_code)
    os.chmod(helper_file, 0o755)
    print(f"✅ Created {helper_file}")
    
    # Final summary
    print("\n" + "=" * 60)
    print("✅ CLAWTOCLAW TEAM SETUP COMPLETE")
    print("=" * 60)
    print(f"\n📁 Credentials and keys stored securely:")
    print(f"   • Main credentials: {CREDS_FILE}")
    print(f"   • Agent private keys: {KEYS_DIR}/")
    print(f"   • Setup guide: {setup_file}")
    print(f"   • Helper library: {helper_file}")
    
    print(f"\n🤝 Team: Rahul's AI Agency")
    for agent_name in AGENTS.keys():
        agent_info = credentials["agents"][agent_name]
        print(f"   ✅ {agent_name:10} | ID: {agent_info['id'][:12]}... | Key: {agent_info['apiKey'][:12]}...")
    
    print(f"\n🔐 Security:")
    print(f"   • All private keys: 0600 (user only)")
    print(f"   • All credentials: 0600 (user only)")
    print(f"   • E2E encryption ready for all agents")
    
    print(f"\n📚 Next steps:")
    print(f"   1. Read {setup_file} for full documentation")
    print(f"   2. Create connections: agent A invites → agent B accepts")
    print(f"   3. Start threads and send encrypted messages")
    print(f"   4. Use C2CAgent helper class for easy communication")
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
