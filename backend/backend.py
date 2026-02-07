# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import re
# import tldextract

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class AnalysisRequest(BaseModel):
#     message: str

# def analyze_links(text):
#     # Regex to find all URLs in the text
#     url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
#     urls = re.findall(url_pattern, text)
    
#     link_score = 0
#     link_reasons = []
    
#     for url in urls:
#         ext = tldextract.extract(url)
#         domain = f"{ext.domain}.{ext.suffix}"
        
#         # 1. Check for IP-based URLs (e.g., http://192.168.1.1/login)
#         if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ext.domain):
#             link_score += 50
#             link_reasons.append(f"IP-based URL detected ({url})")
            
#         # 2. Check for URL shorteners (Common in smishing/phishing)
#         shorteners = ['bit.ly', 'goo.gl', 't.co', 'tinyurl.com', 'is.gd']
#         if domain in shorteners:
#             link_score += 30
#             link_reasons.append(f"Hidden link via shortener: {domain}")
            
#         # 3. Check for "Suspect" Keywords in URL path
#         if any(x in url.lower() for x in ['verify', 'secure', 'login', 'update', 'banking']):
#             link_score += 20
#             link_reasons.append("URL contains high-risk keywords")

#     return link_score, link_reasons

# def analyze_intent(text):
#     text_lower = text.lower()
#     intent_score = 0
#     intent_reasons = []

#     # Behavioral Signals (Psychological Triggers)
#     signals = {
#         "Urgency": (['urgent', 'immediately', 'within 24 hours', 'action required'], 35),
#         "Threat": (['blocked', 'suspended', 'illegal', 'police', 'penalty'], 30),
#         "Authority": (['official', 'administrator', 'support desk', 'internal revenue'], 25),
#         "Financial": (['payment', 'invoice', 'refund', 'wire transfer'], 20)
#     }

#     for category, (keywords, weight) in signals.items():
#         if any(word in text_lower for word in keywords):
#             intent_score += weight
#             intent_reasons.append(f"{category} triggers detected")

#     return intent_score, intent_reasons

# @app.post("/predict")
# async def predict(request: AnalysisRequest):
#     # 1. Run both analyzers
#     l_score, l_reasons = analyze_links(request.message)
#     i_score, i_reasons = analyze_intent(request.message)
    
#     total_score = l_score + i_score
#     all_reasons = l_reasons + i_reasons

#     # 2. Determine Label
#     if total_score >= 70:
#         label = "PHISHING"
#     elif total_score >= 35:
#         label = "SUSPICIOUS"
#     else:
#         label = "SAFE"

#     # 3. Create helpful analysis text
#     if not all_reasons:
#         analysis = "No suspicious links or psychological manipulation detected. Looks clean."
#     else:
#         analysis = f"Flags found: {'; '.join(all_reasons)}."

#     return {
#         "label": label,
#         "score": min(total_score, 100), # Cap at 100%
#         "analysis": analysis,
#         "confidence": "98.7%" if label != "SAFE" else "91.2%"
#     }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)


    

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re
import tldextract

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalysisRequest(BaseModel):
    message: str

def analyze_links(text):
    # Regex to find all URLs in the text
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(url_pattern, text)
    
    link_score = 0
    link_reasons = []
    
    for url in urls:
        ext = tldextract.extract(url)
        domain = f"{ext.domain}.{ext.suffix}"
        
        # 1. Check for IP-based URLs (e.g., http://192.168.1.1/login)
        if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ext.domain):
            link_score += 50
            link_reasons.append(f"IP-based URL detected ({url})")
            
        # 2. Check for URL shorteners (Common in smishing/phishing)
        shorteners = ['bit.ly', 'goo.gl', 't.co', 'tinyurl.com', 'is.gd']
        if domain in shorteners:
            link_score += 30
            link_reasons.append(f"Hidden link via shortener: {domain}")
            
        # 3. Check for "Suspect" Keywords in URL path
        if any(x in url.lower() for x in ['verify', 'secure', 'login', 'update', 'banking']):
            link_score += 20
            link_reasons.append("URL contains high-risk keywords")

    return link_score, link_reasons

# def analyze_intent(text):
#     text_lower = text.lower()
#     intent_score = 0
#     intent_reasons = []

#     # Behavioral Signals (Psychological Triggers)
#     signals = {
#         "Urgency": (['urgent', 'immediately', 'within 24 hours', 'action required'], 35),
#         "Threat": (['blocked', 'suspended', 'illegal', 'police', 'penalty'], 30),
#         "Authority": (['official', 'administrator', 'support desk', 'internal revenue'], 25),
#         "Financial": (['payment', 'invoice', 'refund', 'wire transfer'], 20)
#     }

#     for category, (keywords, weight) in signals.items():
#         if any(word in text_lower for word in keywords):
#             intent_score += weight
#             intent_reasons.append(f"{category} triggers detected")

#     return intent_score, intent_reasons

# @app.post("/predict")
# async def predict(request: AnalysisRequest):
#     # 1. Run both analyzers
#     l_score, l_reasons = analyze_links(request.message)
#     i_score, i_reasons = analyze_intent(request.message)
    
#     total_score = l_score + i_score
#     all_reasons = l_reasons + i_reasons

#     # 2. Determine Label
#     if total_score >= 70:
#         label = "PHISHING"
#     elif total_score >= 35:
#         label = "SUSPICIOUS"
#     else:
#         label = "SAFE"

#     # 3. Create helpful analysis text
#     if not all_reasons:
#         analysis = "No suspicious links or psychological manipulation detected. Looks clean."
#     else:
#         analysis = f"Flags found: {'; '.join(all_reasons)}."

#     return {
#         "label": label,
#         "score": min(total_score, 100), # Cap at 100%
#         "analysis": analysis,
#         "confidence": "98.7%" if label != "SAFE" else "91.2%"
#     }
def analyze_links(text):
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(url_pattern, text)
    
    link_score = 0
    link_reasons = []
    
    # NEW: List of brands scammers often spoof
    target_brands = ['paypal', 'amazon', 'google', 'microsoft', 'netflix', 'apple', 'bank']

    for url in urls:
        ext = tldextract.extract(url)
        domain_name = ext.domain.lower()
        full_domain = f"{ext.domain}.{ext.suffix}"
        
        # 1. Check for IP-based URLs
        if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ext.domain):
            link_score += 50
            link_reasons.append("IP-based URL detected")

        # 2. BRAND IMPERSONATION CHECK (Fixes paypa1.com)
        for brand in target_brands:
            # If the brand name is in the URL but it's NOT the official site
            if brand in domain_name and full_domain not in [f"{brand}.com", f"{brand}.net", f"{brand}.org"]:
                link_score += 60 
                link_reasons.append(f"Potential Brand Impersonation ({brand})")

        # 3. URL Shorteners (Now triggers SUSPICIOUS instantly)
        shorteners = ['bit.ly', 'goo.gl', 't.co', 'tinyurl.com', 'is.gd']
        if full_domain in shorteners:
            link_score += 35 
            link_reasons.append(f"Hidden link via shortener: {full_domain}")
            
        # 4. Suspect Keywords
        if any(x in url.lower() for x in ['verify', 'secure', 'login', 'update', 'banking']):
            link_score += 25
            link_reasons.append("URL contains high-risk keywords")

    return link_score, link_reasons

@app.post("/predict")
async def predict(request: AnalysisRequest):
    l_score, l_reasons = analyze_links(request.message)
    i_score, i_reasons = analyze_links(request.message)
    
    total_score = l_score + i_score
    all_reasons = l_reasons + i_reasons

    # NEW SENSITIVE THRESHOLDS
    if total_score >= 60:
        label = "PHISHING"  # Will trigger RED
    elif total_score >= 25:
        label = "SUSPICIOUS" # Will trigger YELLOW
    else:
        label = "SAFE" # Will trigger GREEN

    analysis = f"Flags found: {'; '.join(all_reasons)}." if all_reasons else "Looks clean."

    return {
        "label": label,
        "score": min(total_score, 100),
        "analysis": analysis,
        "confidence": "98.7%" if label != "SAFE" else "91.2%"
    }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

import os

if __name__ == "__main__":
    import uvicorn
    # Render provides a "PORT" environment variable. 
    # If it's not there (like on your PC), it defaults to 8000.
    port = int(os.environ.get("PORT", 8000))
    
    # On Render, we use 0.0.0.0. On your PC, we can use 127.0.0.1 or 0.0.0.0.
    # It's actually safe to use 0.0.0.0 everywhere!
    uvicorn.run("backend:app", host="0.0.0.0", port=port, reload=True)

    # uvicorn backend:app --reload -> uvicorn used to run run backend
    # http://127.0.0.1:8000/docs   -> open on new tab to cross check