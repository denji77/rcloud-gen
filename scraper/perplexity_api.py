import requests
import re

class PerplexityAPI:
    def __init__(self, api_key, base_url="https://api.perplexity.ai/chat/completions"):
        self.api_key = api_key
        self.base_url = base_url

    def _call_perplexity(self, prompt, model="sonar"):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant that provides concise, accurate responses."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 400,
            "temperature": 0.2
        }
        try:
            r = requests.post(self.base_url, headers=headers, json=payload, timeout=20)
            r.raise_for_status()
            j = r.json()
            text = None
            if isinstance(j, dict):
                if 'choices' in j and len(j['choices']) > 0:
                    c0 = j['choices'][0]
                    if isinstance(c0, dict):
                        msg = c0.get('message') or c0.get('text') or {}
                        if isinstance(msg, dict) and 'content' in msg:
                            text = msg['content']
                        elif isinstance(c0.get('text'), str):
                            text = c0.get('text')
                if not text:
                    text = j.get('text') or j.get('answer') or None
            if not text:
                text = r.text
            return text
        except Exception as e:
            print("Perplexity API error:", e)
            return None

    def generate_topic_stopwords(self, subreddit_name, sample_text=""):
        prompt = f"""
I'm analyzing text from r/{subreddit_name}. Provide a comma-separated list (lowercase, no quotes)
of common noise words, subreddit-specific jargon, abbreviations, and filler terms
that should be excluded from topic analysis. Example output: word1, word2, word3

Sample text (first 500 chars): {sample_text[:500] if sample_text else 'N/A'}
"""
        response = self._call_perplexity(prompt)
        if not response:
            return []
        candidates = []
        lines = [ln.strip() for ln in response.splitlines() if ln.strip()]
        if lines:
            comma_line = next((ln for ln in lines if ',' in ln), lines[0])
        else:
            comma_line = response
        for token in comma_line.split(','):
            w = re.sub(r"[^a-zA-Z0-9_-]", "", token).strip().lower()
            if len(w) > 1:
                candidates.append(w)
        return list(dict.fromkeys(candidates))

    def get_subreddit_symbol(self, subreddit_name):
        prompt = f"""
        Give me one single lowercase word (object, animal, or symbol)
        that best represents the subreddit r/{subreddit_name}.
        Output only the word, nothing else.
        """
        resp = self._call_perplexity(prompt)
        if not resp:
            return "circle"
        word = re.findall(r"[a-z]+", resp.lower())
        return word[0] if word else "python"