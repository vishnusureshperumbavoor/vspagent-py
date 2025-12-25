"""VSP Agent - Core functionality"""

import requests
from typing import Dict, List, Optional

# Biodata
biodata = {
    "name": "VSP Agent",
    "creator": "Vishnu Suresh Perumbavoor",
    "founder_of": ["VSP Enterprises", "VSP Intelligence"],
    "created_on": "28 April 2023",
    "marital_status": "Single (Not married)",
    "political_affiliation": "None",
    "education": "Not a graduate (No degree)",
    "roles": ["SWE", "Singer", "YouTuber"],
    "interests": ["startups", "engineering", "geopolitics", "history"],
    "corporate": ["Trenser"],
    "technologies": [
        "React", "Node.js", "FastAPI", "Express", "MongoDB", 
        "Docker", "OHIF", "Cornerstone3D", "VTKjs", "DICOM"
    ],
    "accomplishments": [
        "Won 3rd prize in Vaiga Agrihack 2023",
        "Participated in Rajasthan IT Hackathon 2023",
        "Won 1st prize in startup idea presentation at Palakkad"
    ],
    "socials": {
        "linkedin": "https://www.linkedin.com/in/vishnu-suresh-perumbavoor/",
        "twitter": "https://twitter.com/vspeeeeee",
        "github": "https://github.com/vishnusureshperumbavoor",
        "youtube": "https://www.youtube.com/@vishnusureshperumbavoor9721/videos",
        "instagram": "https://www.instagram.com/vishnusureshperumbavoor/",
    }
}


class VSPAgent:
    """AI-powered agent for VSP information"""
    
    def __init__(self):
        self.biodata = biodata
        self.model = None
        self.tokenizer = None
    
    def init_ai(self):
        """Initialize AI model (Qwen2.5-0.5B)"""
        try:
            from transformers import AutoTokenizer, AutoModelForCausalLM
            import torch
            
            print("🚀 Initializing VSP Agent...")
            print("   🧠 Loading AI brain with Qwen2.5-0.5B...")
            
            model_name = "Qwen/Qwen2.5-0.5B-Instruct"
            
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                device_map="auto"
            )
            
            print("✅ VSP Agent is ready!")
            print(f"   🤖 Device: {'GPU' if torch.cuda.is_available() else 'CPU'}")
            
        except Exception as e:
            print(f"❌ Error initializing AI: {e}")
            print("💡 Install required packages: pip install transformers torch")
    
    def chat(self, message: str, conversation_history: Optional[List] = None) -> str:
        """Chat with the AI agent"""
        if self.model is None:
            return "Please initialize AI first using init_ai()"
        
        system_context = f"""You are VSP Agent, an AI assistant about {self.biodata['creator']}.

IMPORTANT: VSP = The PERSON (Vishnu Suresh Perumbavoor), VSP Agent = YOU (the AI)

VSP's Information:
- Name: {self.biodata['creator']}
- Founded: {', '.join(self.biodata['founder_of'])}
- Roles: {', '.join(self.biodata['roles'])}
- Technologies: {', '.join(self.biodata['technologies'])}
- Accomplishments: {'; '.join(self.biodata['accomplishments'])}
- LinkedIn: {self.biodata['socials']['linkedin']}
- GitHub: {self.biodata['socials']['github']}

RULES:
1. NEVER say "I am..." for VSP's details
2. ALWAYS say "He is...", "VSP is..."
3. DO NOT make up information"""

        messages = [{"role": "system", "content": system_context}]
        
        if conversation_history:
            messages.extend(conversation_history)
        
        messages.append({"role": "user", "content": message})
        
        try:
            # Generate response
            inputs = self.tokenizer.apply_chat_template(
                messages, 
                return_tensors="pt"
            ).to(self.model.device)
            
            outputs = self.model.generate(
                inputs,
                max_new_tokens=512,
                temperature=0.7,
                do_sample=False
            )
            
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Extract just the assistant's response
            response = response.split("assistant")[-1].strip()
            
            return response
            
        except Exception as e:
            return f"Error generating response: {e}"
    
    def check_github(self, username: str = "vishnusureshperumbavoor") -> Dict:
        """Check GitHub activity"""
        try:
            url = f"https://api.github.com/users/{username}/repos"
            headers = {"Accept": "application/vnd.github.v3+json"}
            
            response = requests.get(url, headers=headers)
            repos = response.json()
            
            total_stars = sum(repo.get('stargazers_count', 0) for repo in repos)
            
            return {
                "username": username,
                "total_repos": len(repos),
                "total_stars": total_stars,
                "recent_repos": [
                    {
                        "name": repo['name'],
                        "stars": repo['stargazers_count'],
                        "url": repo['html_url']
                    }
                    for repo in repos[:5]
                ]
            }
        except Exception as e:
            return {"error": str(e)}
    
    def search_jobs(self, role: str, location: str) -> Dict:
        """Search LinkedIn jobs"""
        from urllib.parse import urlencode
        
        params = {
            "keywords": role,
            "location": location,
            "sortBy": "DD"
        }
        
        search_url = f"https://www.linkedin.com/jobs/search?{urlencode(params)}"
        
        return {
            "search_url": search_url,
            "role": role,
            "location": location,
            "message": f"Visit {search_url} to see real job listings"
        }
    
    def generate_cover_letter(self, job_title: str, company: str) -> str:
        """Generate cover letter"""
        return f"""Dear Hiring Manager at {company},

I am writing to express my strong interest in the {job_title} position at {company}.

With my background in {', '.join(self.biodata['technologies'][:5])}, I believe I would be a valuable addition to your team.

Key qualifications:
{chr(10).join(f'- {acc}' for acc in self.biodata['accomplishments'])}

I am particularly drawn to {company}'s work and would welcome the opportunity to contribute.

Thank you for considering my application.

Best regards,
{self.biodata['creator']}
LinkedIn: {self.biodata['socials']['linkedin']}
GitHub: {self.biodata['socials']['github']}"""

