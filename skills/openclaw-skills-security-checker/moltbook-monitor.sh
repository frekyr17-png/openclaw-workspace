#!/bin/bash
# Moltbook Security Monitor (Standalone)
# Fetches security posts from Moltbook and reports findings

MOLTBOOK_API_KEY="${MOLTBOOK_API_KEY:-moltbook_sk_kB_hoyxPlRXnrsNW6NE2Mhr6ENT2VIzX}"
OUTPUT_DIR="/root/clawd/skills/security-skill-scanner/data"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M UTC')

mkdir -p "$OUTPUT_DIR"

echo "[$TIMESTAMP] Moltbook Security Monitor starting..."

# Fetch latest posts
POSTS=$(curl -s "https://www.moltbook.com/api/v1/posts?sort=new&limit=50" \
    -H "Authorization: Bearer $MOLTBOOK_API_KEY")

# Search for security-related posts
echo "$POSTS" | python3 -c "
import sys, json
from datetime import datetime

data = json.load(sys.stdin)
posts = data.get('posts', [])

SECURITY_KEYWORDS = ['skill.md', 'credential', 'stealer', 'scam', 'vulnerability', 'security', 'attack', 'exploit']
TRUSTED_AUTHORS = ['eudaemon_0', 'SentientDawn', 'SelfOrigin', 'Rufio']

security_posts = []
for post in posts:
    title = (post.get('title', '') or '').lower()
    content = (post.get('content', '') or '').lower()
    combined = title + ' ' + content
    
    for keyword in SECURITY_KEYWORDS:
        if keyword in combined:
            security_posts.append({
                'id': post.get('id'),
                'title': post.get('title'),
                'author': post.get('author', {}).get('name'),
                'upvotes': post.get('upvotes', 0),
                'is_trusted': post.get('author', {}).get('name') in TRUSTED_AUTHORS
            })
            break

print(json.dumps(security_posts))
" > "${OUTPUT_DIR}/moltbook-security-posts.json"

COUNT=$(python3 -c "import json; posts = json.load(open('${OUTPUT_DIR}/moltbook-security-posts.json')); print(len(posts))")
echo "[$TIMESTAMP] Found $COUNT security-related posts"

# Save to history
echo "[$TIMESTAMP] Security scan: $COUNT posts found" >> "${OUTPUT_DIR}/moltbook-history.log"

# Output summary
echo ""
echo "=== Moltbook Security Feed ==="
echo "Timestamp: $TIMESTAMP"
echo "Posts found: $COUNT"
echo ""

python3 -c "
import json

posts = json.load(open('${OUTPUT_DIR}/moltbook-security-posts.json'))

# Sort by upvotes (most important first)
posts.sort(key=lambda x: x.get('upvotes', 0), reverse=True)

for i, post in enumerate(posts[:10], 1):
    trusted = '✅' if post.get('is_trusted') else '⚪'
    print(f'{i}. {trusted} {post[\"title\"][:60]}...')
    print(f'   Author: {post[\"author\"]} | Upvotes: {post[\"upvotes\"]}')
    print()
"

echo "✅ Monitor complete"
