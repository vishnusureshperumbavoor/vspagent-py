"""VSP Agent - CLI Interface"""

import sys
from .agent import VSPAgent


def main():
    """Main CLI entry point"""
    print("╔════════════════════════════════════════════════════════════╗")
    print("║          🤖  VSP Agent - Interactive Chat Mode            ║")
    print("║              Powered by Qwen2.5-0.5B AI                   ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print()
    
    agent = VSPAgent()
    
    try:
        agent.init_ai()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Try: pip install transformers torch")
        return
    
    print("\n✅ VSP Agent is ready to chat!\n")
    print("Commands: 'exit' to quit, 'github' to check GitHub stats\n")
    
    conversation_history = []
    
    while True:
        try:
            user_input = input("💬 You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['exit', 'quit']:
                print("\n👋 Thanks for chatting with VSP Agent! Goodbye! 🚀\n")
                break
            
            if user_input.lower() == 'github':
                print("\n🔍 Checking GitHub...")
                stats = agent.check_github()
                if 'error' in stats:
                    print(f"❌ Error: {stats['error']}")
                else:
                    print(f"\n📊 GitHub Stats:")
                    print(f"   Total Repos: {stats['total_repos']}")
                    print(f"   Total Stars: {stats['total_stars']}\n")
                continue
            
            # Get response
            response = agent.chat(user_input, conversation_history)
            
            # Update history
            conversation_history.append({"role": "user", "content": user_input})
            conversation_history.append({"role": "assistant", "content": response})
            
            print(f"\n🤖 VSP Agent: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!\n")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    main()

